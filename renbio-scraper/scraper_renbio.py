#Scraper to get article information and PDF files of Renbio's journal
#It uses BeautifulSoup to parse the HTML and requests to get the HTML
#It uses wget to download the PDF files
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import re
import wget
import os
from urllib.error import HTTPError

# function to get all issue links from the journal
def get_issues(base_url):
    '''Get all issue links from the journal homepage'''
    issues = []
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    issue_list = soup.find_all('div', class_="media-body")
    for issue in issue_list:
        issue_link = issue.find('a')['href']
        issues.append(issue_link)
    return issues

# function to rename the pdfs
def rename_pdf(folder_path):
    '''Rename the downloaded pdfs to the article number'''
    # change the directory to save the pdfs
    os.chdir(folder_path)
    # get all pdfs from the folder
    pdf_list = os.listdir()
    for pdf in pdf_list:
        # get the number from the pdf name
        pdf_number = re.search(r"Artigo-(\d+-\d+-\d+-\d+-\d+)\.pdf", pdf)
        if pdf_number:
            # rename the pdf
            os.rename(pdf, pdf_number.group(1) + ".pdf")
        else:
            print("PDF not found")

# function to get the pdf using wget
def get_pdf(pdf_link):
    '''Get the pdf from the article page'''
    # path to save the pdfs: current directory + "renbio_pdfs"
    folder_path = os.getcwd() + "/renbio_pdfs"
    try:
        # if pdf exists in tbe folder, skip
        if os.path.exists(folder_path + "/" + pdf_link.split("/")[-1]):
            print("PDF already exists")
            return "PDF already exists"
        else:
            # use wget to download the pdf, pass folder_path to save the pdfs
            wget.download(pdf_link, folder_path)
    except HTTPError:
        print("HTTP Error 404: Not Found")
        return "Not Found"

# function to get all articles from the issue
def get_articles(issue_link):
    '''Get all links to all articles from the issue page'''
    articles = []
    page = requests.get(issue_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_list = soup.find_all('div', class_="media-body")
    for article in article_list:
        article_link = article.find('a')['href']
        articles.append(article_link)
    return articles

# function to get infos from each article
def article_infos(article_link):
    '''Get all infos from the article page'''
    page = requests.get(article_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', class_='page-header')
    #main title is text, sub title is in small tag
    title_text = title.text.strip()
    #remove /n and /t from the title
    title_text = title_text.replace("\n", " ")
    title_text = title_text.replace("\t", "")
    print(title_text)
    try:
        doi_item = soup.find('div', class_="list-group-item doi")
        doi = doi_item.find('a')['href']
    except:
        doi = "DOI not found"
    try:
        pub_date = soup.find('div', class_="list-group-item date-published").text
        # use regex to get last 4 digits
        pub_date = re.findall(r'\d{4}', pub_date)[0]
    except:
        pub_date = "Publication date not found"
    authors = soup.find('div', class_="authors")
    authors_list = authors.find_all('div', class_="author")
    try:
        authors_names = []
        aff_names = []
        for author in authors_list:
            #author_name is only the text in tag "strong"
            author_name = author.find('strong').text
            author_name = author_name.strip()
            authors_names.append(author_name)
            authors_affiliations = author.find('div', class_="article-author-affilitation")
            #strip the authors' affiliations
            authors_affiliations = authors_affiliations.text.strip()
            aff_names.append(authors_affiliations)
        authors = ", ".join(authors_names)
        authors_affiliations = ", ".join(aff_names)
    except:
        authors = "Authors not found"
        authors_affiliations = "Authors' affiliations not found"
    try:
        abstract = soup.find('div', class_="article-abstract").text
        #strip the abstract
        abstract = abstract.strip()
    except:
        abstract = "Abstract not found"
    try:
        keywords_list = soup.find('div', class_="list-group-item keywords")
        keywords = keywords_list.find('span').text
        #strip the keywords
        keywords = keywords.strip()
        # replace /n with ""
        keywords = keywords.replace("\n", "")
        # replace one /t with ", " and replace all other /t with ""
        keywords = keywords.replace("\t", ",")
    except:
        keywords = "Keywords not found"
    # use regex to substitute multiple commas with one comma
    for i in range(len(keywords)):
        keywords = keywords.replace(",,", ",")
    keywords = keywords.replace(";", ",")
    # create a list with all 'p,text' in class 'article-references-content'
    references = soup.find_all('div', class_="article-references-content")
    references_list = []
    for reference in references:
        references_list.append(reference.text)
    pdf_view = soup.find('div', class_ = "download").find('a')['href']
    article_info = {
        'authors': authors,
        'authors_affiliation': authors_affiliations,
        'article_title': title_text,
        'journal_title': "Revista de Ensino de Biologia",
        'journal_issn': "2763-8898",
        'journal_publisher': "Associação Brasileira de Ensino de Biologia",
        'pub_date': pub_date,
        'abstract': abstract,
        'key_words': keywords,
        'doi': doi,
        'refs': references_list,
        'pdf_link': pdf_view
    }
    # replace "view" with "download" in the link
    pdf_link = pdf_view.replace("view", "download")
    #call the function to get the pdf
    #get_pdf(pdf_link)
    return article_info

# call the functions
base_url = "https://renbio.org.br/index.php/sbenbio/issue/archive"
# create a folder to save the pdfs
if not os.path.exists('renbio_pdfs'):
    os.makedirs('renbio_pdfs')
issues = get_issues(base_url)
all_art_issues_info = []
for issue in issues:
    articles = get_articles(issue)
    articles_info_list = []
    for article in articles:
        article_info = article_infos(article)
        articles_info_list.append(article_info)
        print("\nNext article:\n")
    all_art_issues_info.append(articles_info_list)
    print("Next issue")

# save all_art_issues_info in a csv file
# get the current date and time
now = datetime.now()
# format the date and time
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
with open(f'renbio-articles_{date_time}.csv', 'w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['authors', 'authors_affiliation', 'article_title', 'journal_title', 'journal_issn', 'journal_publisher',
                  'pub_date',  'abstract', 'key_words', 'doi', 'refs', 'pdf_link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for issue in all_art_issues_info:
        for article in issue:
            writer.writerow(article)

#call function to rename the pdf files
#rename_pdf("/home/ebn/Documentos/Github/artigo-ensino-de-biologia/renbio_pdfs")