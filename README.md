# Projeto de Integração com SQL Server

## Índice

1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Como Executar o Aplicativo](#como-executar-o-aplicativo)
7. [Funcionalidades](#funcionalidades)
8. [Exemplo de Uso](#exemplo-de-uso)
9. [Considerações Finais](#considerações-finais)

## Introdução

Este projeto tem como objetivo integrar um aplicativo desenvolvido em Python com um banco de dados SQL Server. A interface do usuário é criada utilizando a biblioteca Streamlit, permitindo a inserção e recuperação de dados em uma tabela SQL.

## Pré-requisitos

Certifique-se de que você tem os seguintes pré-requisitos instalados:

- Python 3.x
- Bibliotecas:
  - Streamlit
  - pyodbc
  - python-dotenv

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install streamlit pyodbc python-dotenv

Configuração do Ambiente
Criar um Ambiente Virtual:

É recomendado criar um ambiente virtual para o projeto. Use o seguinte comando:
bash
Copiar código
python -m venv .venv
Ativar o Ambiente Virtual:

No Windows:
bash
Copiar código
.venv\Scripts\activate
No macOS/Linux:
bash
Copiar código
source .venv/bin/activate
Instalar as Dependências:

Após ativar o ambiente virtual, instale as dependências com o comando mencionado anteriormente.
Configuração do Banco de Dados
Criar um Banco de Dados:

No SQL Server, crie um banco de dados chamado TesteDB.
Criar a Tabela CADASTRO:

Execute o seguinte comando SQL para criar a tabela onde os dados serão armazenados:
sql
Copiar código
CREATE TABLE CADASTRO (
    NOME NVARCHAR(100),
    EMAIL NVARCHAR(100),
    TELEFONE NVARCHAR(15),
    ENDERECO NVARCHAR(255),
    CPF NVARCHAR(11) PRIMARY KEY
);
Configuração do Arquivo .env:

Crie um arquivo chamado .env na raiz do projeto e insira as seguintes informações:
plaintext
Copiar código
DB_SERVER=edson\MSSQLSERVER1
DB_NAME=TesteDB
DB_USER=sa
DB_PASSWORD=sua_senha_aqui
Estrutura do Projeto
A estrutura básica do projeto é a seguinte:

bash
Copiar código
projeto/
│
├── .venv/               # Ambiente virtual
├── .env                 # Arquivo de configuração do ambiente
├── main.py              # Script principal do aplicativo
└── database.py          # Módulo de conexão com o banco de dados
main.py
Contém a lógica principal do aplicativo, incluindo a interface do Streamlit.

database.py
Contém a classe Database, responsável pela conexão com o banco de dados e operações de inserção e recuperação de dados.

Como Executar o Aplicativo
Ativar o Ambiente Virtual (se ainda não estiver ativo).
Executar o aplicativo Streamlit:
bash
Copiar código
streamlit run main.py
Acessar a Interface:
O aplicativo estará disponível em um navegador web, geralmente em http://localhost:8501.
Funcionalidades
Inserir Dados: Permite que o usuário insira um nome, e-mail, telefone, endereço e CPF na tabela CADASTRO.
Buscar Dados: Exibe os dados já armazenados na tabela.
Exemplo de Uso
Após executar o aplicativo:

Insira os dados nos campos fornecidos.
Clique no botão para enviar os dados.
Verifique se os dados foram armazenados corretamente no banco de dados.


