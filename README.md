Consulta Clima com Python

Projeto desenvolvido em Python para consulta de condições climáticas em tempo real utilizando a API OpenWeatherMap.

Objetivos do Projeto

Este projeto foi criado com foco em aprendizado e prática dos seguintes conceitos:

Consumo de APIs REST
Manipulação de JSON
Variáveis de ambiente (.env)
Tratamento de erros HTTP
Organização de projetos Python em módulos
Leitura e escrita de arquivos CSV
Manipulação de datas e horários
Testes automatizados com Pytest
Boas práticas para projetos Python

Funcionalidades
Consultar clima por cidade
Exibir:
Temperatura
Sensação térmica
Umidade
Condição climática
Salvar histórico das consultas em CSV
Visualizar histórico de consultas
Validação de entrada
Tratamento de erros de cidade não encontrada
🛠️ Tecnologias Utilizadas
Python 3.12
Requests
Python Dotenv
Pytest
CSV (biblioteca padrão)
Datetime (biblioteca padrão)
OpenWeatherMap API

Estrutura do Projeto
consulta-clima/
│
├── services/
│   ├── clima.py
│   └── validacoes.py
│
├── utils/
│   └── csv_handler.py
│
├── tests/
│   └── test_validacoes.py
│
├── .env
├── .gitignore
├── historico_clima.csv
├── main.py
├── requirements.txt
└── README.md

Instalação

Clone o repositório:

git clone https://github.com/SEU_USUARIO/consulta-clima-python.git

Entre na pasta:

cd consulta-clima-python

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

Windows:

venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Configuração da API

Crie um arquivo .env na raiz do projeto:

API_KEY=SUA_CHAVE_OPENWEATHER

Você pode obter uma chave gratuita em:

https://openweathermap.org/api

Executando o Projeto
python main.py
Executando os Testes
python -m pytest

Exemplo de Uso
===== CONSULTA CLIMA =====

1 - Consultar clima
2 - Ver histórico
3 - Sair

Escolha uma opção: 1

Digite o nome da cidade: Rio de Janeiro

Cidade: Rio de Janeiro
Temperatura: 25.3°C
Sensação térmica: 25.4°C
Umidade: 61%
Condição: céu limpo

Consulta salva com sucesso!

Próximos Passos
Análise dos dados climáticos com Pandas
Geração de relatórios
Criação de gráficos com Matplotlib
Dashboard com Streamlit
Deploy da aplicação

Autor: Yves Siruffo

Projeto desenvolvido como parte da trilha de estudos em Python, Dados e Inteligência Artificial.