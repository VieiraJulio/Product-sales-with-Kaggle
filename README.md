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

A primeira métrica é identificar, de forma agrupada, o acompanhamento das vendas nos últimos anos.

![image](https://github.com/user-attachments/assets/b8c92847-1760-4479-973b-27d7ae548a4c)

No último ano analisado (2018), a empresa registrou um aumento de 17% em relação ao ano anterior. No visual, o objetivo é destacar o desempenho desse último ano de forma mais abrangente, para assim, chegar
nas causas do aumento.

A segunda métrica foca em um nível abaixo da hierarquia anual: os meses.

![image](https://github.com/user-attachments/assets/864991c8-dc0f-4c41-b5e0-4e9567e1847e)


Conforme mostrado no gráfico de barras clusterizado, os últimos trimestres do ano apresentam um aumento consistente, pegando os últimos 4 anos.

Mas o que nos iteressa de fato é o ano com mais vendas, 2018.

![image](https://github.com/user-attachments/assets/3b9f3228-e038-40fa-869f-5e415351e918)



![image](https://github.com/user-attachments/assets/5cd739a4-d355-4538-ae3b-9c6cfe07bd53)















### Como Reproduzir o Projeto

 - Baixar o arquivo ipynb no repositório.
 - Acessar a base no Kaggle.
      
