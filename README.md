### Vendas de Produtos com Kaggle | Python

### Objetivo

Desenvolver uma apresentação técnica para os diretores, com foco na análise e interpretação das principais métricas de desempenho da empresa.

Utilizei um dataset público do Kaggle como base para criar um modelo de análise direcionado ao setor de vendas. O template foi estruturado e aplicado em uma apresentação em PowerPoint utilizando dados reais da corporação. Contudo, neste projeto, para fins de compartilhamento e compliance, os dados reais foram substituídos exclusivamente por dados públicos.

### Organização do projeto 

```

├── .gitignore    <- Arquivos e diretórios a serem ignorados pelo Git  
├── LICENSE       <- Licença de código aberto (MIT)  
├── README.md     <- README principal para desenvolvedores que utilizam este projeto  
├── notebooks     <- Cadernos Jupyter contendo análises e experimentos.
       ├── 01_JV_Criando uma apresentação executiva.ipynb
       ├── Funções.py

├── images       <- Imagens usadas no README.
       ├── Clusterizado meses.png
       ├── Vendas 2018 meses.png
       ├── Vendas por ano.png
       ├── Vendas por categoria.png
       ├── Vendas por meses.png
       ├── Categoria.png
       ├── Clusterizado Categoria.png
       ├── Top N.png


```

### Detalhes das métricas utilizadas 

O Kaggle é uma plataforma online voltada para ciência de dados e machine learning, oferecendo desafios competitivos com premiações, um vasto repositório de datasets, 
notebooks em nuvem para desenvolvimento de projetos, cursos gratuitos para aprendizado e uma comunidade ativa para colaboração e troca de conhecimento, 
sendo ideal para aprendizado, prática e networking na área. 

Base de dados : https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

Este dataset foi previamente tratado utilizando a biblioteca pandas. 
Durante o processo de preparação, os dados foram segmentados e estruturados para atender às necessidades específicas das análises a serem realizadas, incluindo:

 - Vendas por Período: Estruturado para análise temporal, permitindo identificar tendências sazonais e padrões de vendas em diferentes intervalos de tempo (mensal e anual).
 - Categoria Mais Vendida: Segmentado por categorias de produtos, possibilitando a identificação de quais categorias geraram maior receita ou volume de vendas.
 - Itens Mais Vendidos: Filtrado para destacar os produtos com maior receita gerada, ajudando a determinar os itens de melhor desempenho.
   
Caso seja necessário expandir as análises ou adaptar o tratamento, os dados podem ser facilmente ajustados.

### Discussão dos resultados

A primeira métrica é acompanhar, de forma agrupada, as vendas nos últimos anos.

![image](https://github.com/user-attachments/assets/0ec376eb-b8e6-41fd-86f8-8827ff8f9f8d)


No último ano analisado (2018), a empresa registrou um aumento de 17% em relação ao ano anterior. 
O objetivo é destacar o desempenho das vendas desse último ano de forma mais abrangente, para assim, chegar nas causas do aumento.

A segunda métrica foca em um nível abaixo da hierarquia anual: os meses.

![image](https://github.com/user-attachments/assets/864991c8-dc0f-4c41-b5e0-4e9567e1847e)


Conforme mostrado no gráfico de barras clusterizado, os últimos trimestres do ano apresentam um aumento consistente, pegando os últimos 4 anos.

Mas o que nos iteressa de fato é o ano com mais vendas, 2018.

![image](https://github.com/user-attachments/assets/3b9f3228-e038-40fa-869f-5e415351e918)

A terceira métrica, é relacionada as categorias dos nossos produtos.

![image](https://github.com/user-attachments/assets/a211a281-0324-46e4-85c5-2364135b3812)


O destaque fica com a categoria tecnologia olhando os valores agrupados.

![image](https://github.com/user-attachments/assets/72e159f8-896a-46d4-9a19-1cd1d2ad5cad)


Com a visão das vendas por categoria ao longo dos anos, a categoria tecnologia apresentou um aumento somente nos últimos dos anos. 

Por fim, o cerne do projeto é saber quais são os Top N produtos terão um aumento no estoque, conforme seu número de vendas. 

![image](https://github.com/user-attachments/assets/b4af4a8e-f341-4734-b58e-3e9a233ef7bb)

Essa visão é clusterizada por ano, com ela temos uma ideia dos comportamentos do produtos nos últimos períodos. 

### Principais Ferramentas

 - As ferramentas de visualização: Matplotlib
 - Construção e Cálculos: Pandas e Numpy. 

### Como Reproduzir o Projeto

 - Baixar o arquivo ipynb no repositório.
 - Acessar a base no Kaggle.
      
