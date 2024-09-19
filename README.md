#Análise de Acidentes em Rodovias Federais Brasileiras (2019-2023)

Este projeto foi desenvolvido com o objetivo de analisar dados sobre acidentes em rodovias federais no Brasil, utilizando técnicas estatísticas como a distribuição binomial e o teste qui-quadrado para comparar dados reais com dados simulados. A proposta original foi elaborada pela Profª Drª Adriana Barbosa, focando em uma análise probabilística de sucessos e fracassos no contexto de acidentes, utilizando um dataset público disponível no Kaggle.

Dataset
O dataset utilizado para esta análise contém dados de acidentes em rodovias federais brasileiras entre os anos de 2019 e 2023. Ele inclui informações sobre o número de acidentes, mortos, feridos (leves e graves), ilesos e registros ignorados. O dataset pode ser encontrado no Kaggle: Link para o dataset.

Objetivo
O principal objetivo deste projeto é comparar a proporção de acidentes sem mortes e com mortes, realizando simulações probabilísticas e verificando se há diferenças estatisticamente significativas entre os dados reais e simulados. Para isso, utilizamos a distribuição binomial para modelar o comportamento de sucessos (acidentes sem mortes) e fracassos (acidentes com mortes) e o teste qui-quadrado para validar os resultados.

Critérios de Sucesso e Fracasso
Sucesso: Acidentes onde não houve mortos e feridos.
Fracasso: Acidentes que resultaram em mortes ou feridos.

Metodologia
1. Importação e Preparação dos Dados
Os dados foram importados utilizando a biblioteca pandas, e a análise inicial focou no total de acidentes registrados e na contagem de sucessos e fracassos.

2. Cálculo das Proporções Reais
A partir dos dados reais, calculamos as proporções de sucessos e fracassos, onde:

Sucesso: Acidentes sem mortos e feridos.
Fracasso: Acidentes com mortos ou feridos.

3. Simulação com Distribuição Binomial
Com base na proporção de sucessos reais, realizamos uma simulação de novos dados utilizando a distribuição binomial.

4. Teste Qui-Quadrado
Para verificar se há diferenças significativas entre os dados reais e simulados, aplicamos o teste qui-quadrado.

5. Visualização dos Resultados
Foi gerado um gráfico comparativo entre os dados reais e simulados para ilustrar a diferença entre os eventos de sucesso (sem mortes) e fracasso (com mortes).

