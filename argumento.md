# Argumento central do artigo

*Ponto de partida*:

Este artigo foi desenvolvido partindo do problema de que em geral, as pesquisas em ensino de biologia negligenciam (ou dão pouco enfoque) os debates sobre questões socioculturais e políticas, temas fundamentais e urgentes na educação básica. A ausência desses debates nos processos educativos tem grande impacto social, uma vez que ao não ser discutido e problematizado, corrobora indiretamente para a manutenção de comportamentos opressivos em nossa sociedade, como por exemplo as opressões de gênero e raça.

De acordo com Kelly Fenandes (2015), no âmbito das pesquisas sobre o ensino de biologia, tanto no ensino fundamental quanto no superior, ainda são poucos os estudos que abordam a questão da educação das relações étnico-raciais ou mesmo demais aspectos sociais, políticos e culturais, por exemplo. Isso reflete, de certo modo, o silêncio existente na academia e nos cursos de formação de professores(as) de ciências biológicas sobre as temáticas desta natureza. Como consequência, tem-se números irrisórios de publicações científicas relevantes sobre o tema, bem como uma formação de docentes não preparados ou não engajados criticamente com as questões sociopolíticas que nos atravessam.

A questão da formação docente em biologia e as ausências ou lacunas curriculares no que concerne a abordagem de temas socialmente relevantes também foi analisada por Marco Barzano (2016). Esse autor nos explica que consta nas diretrizes curriculares do curso de ciências biológicas uma parte relacionada as habilidades e competências deste(a) profissional, na qual, dentre outros aspectos, devem 

>“Reconhecer formas de discriminação racial, social, de gênero, etc. que se fundem inclusive em alegados pressupostos biológicos, posicionando-se diante delas de forma crítica, com respaldo em pressupostos epistemológicos coerentes e na bibliografia de referência” (BRASIL, 2001, p. 3).

Apesar disso, argumenta o autor, há uma completa ausência nos conteúdos específicos desta disciplina das temáticas gênero, sexualidade, raça/etnia na formação inicial docente, por exemplo. Essa ausência impacta fortemente no ensino da biologia escolar, pois, nos pergunta o autor, como poderiam os(a) professores(as) abordar em suas aulas essas temáticas se essas questões não foram discutidas nas disciplinas ao longo de sua formação? (BARZANO, 2016). No entanto, é importante salientar que uma formação considerada adequada (para estes fins) não garante, necessariamente, um exercício de docência socialmente comprometido.

Nesse aspecto, consideramos as ciências biológicas como um campo privilegiado, pois, enxergarmos que essa ciência guarda, em seus mais diversos campos do conhecimento, um enorme potencial em endereçar questões sociopolíticas e culturais importantes para o nosso tempo, uma vez que um ensino de ciências acrítico e descontextualizado pode contribuir para a manutenção de pressupostos que fundamentam estereótipos, reforçam as desigualdades e oprimem grupos de seres humanos, como é o caso das opressões de raça e gênero, que tem muitos de seus fundamentos ancorados em uma leitura equivocada, datada, ultrapassada dos conhecimentos produzidos pela biologia. Assim como Sandra Selles (2014, p. 22), acreditamos que é possível (e urgente) abrir janelas no âmbito das pesquisas em ensino de biologia, uma vez que “pensar nas janelas que o ensino de biologia permite abrir é também trazer outras representações culturais e outros sujeitos para dialogar”, o que, ao nosso ver, contribui para que alcancemos uma educação transformadora e transgressora.

Nesse sentido, este artigo busca contribuir para o diálogo acerca das pesquisas em ensino de biologia alinhadas à questões sociopolíticas importantes de nosso tempo, especificamente as opressões de gênero e raça. Para isso, temos como objetivo principal mapear as publicações sobre o ensino de biologia, das últimas décadas, em algumas das principais revistas científicas brasileiras da área da educação. Argumentamos que é preciso que cada vez mais pesquisas sobre essa temática sejam desenvolvidas, a fim de contribuir a politização do ensino de biologia e seu consequente impacto positivo no desenvolvimento de pensamento crítico às dinâmicas de opressões em nossa sociedade pelos(as) discentes nas salas de aula do ensino básico.

## Filtros testados

No *dataframe* gerado a partir dos dados do Scielo, foram aplicados os seguintes filtros à coluna "abstract":

- filters = ['biologia','ciências biológicas','bióloga*','biólogo*']
   - Shape: (63, 20)
- f_antr = ['antropologia','antropólog*']
   - Shape: (40, 20)
- f_cien_soc = ['cientista* socia*','ciência social','ciências sociais']
   - Shape: (57, 20) 
- f_hist = ['história','historiador*']
   - Shape: (702, 20) 
- f_soci = ['sociologia','sociólog*']
   - Shape: (198, 20) 

Acredito que seja válido rodar os filtros de segundo nível na coluna "keywords".

## Estratégias futuras

- Comparar com os resultados obtidos com o *dataframe* da revista **Renbio**.
### Análise de conteúdo com Spacy

- Contar palavras e *ngrams* para identificar os temas mais recorrentes nas 63 publicações filtradas com os termos ligados à biologia na coluna "abstract".
- Aplicar mesma estratégia para os artigos da revista **Renbio**.
- Rodar NER para identificar pessoas na lista de Referências.

### Visualização de dados com Plotly

- Gerar gráficos de barras para visualizar a distribuição das publicações por ano.
- Gerar gráficos de porcentagem para visualizar a distribuição das publicações por revista e ano.
- Gerar gráficos com ngrams para visualizar os temas mais recorrentes nas publicações.
