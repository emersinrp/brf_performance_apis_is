# BRF Performance and tests APIs - IS

Este projeto contém testes de performance/carga para várias APIs utilizando a biblioteca Locust em Python. As APIs são testadas para verificar seu desempenho sob diferentes condições de carga.

## Estrutura do Projeto

```bash
BRF_PERFORMANCE_APIS_IS/
├── helpers/
│ ├── pycache/
│ ├── payloads.py
│ └── utils.py
├── locustfiles/
│ ├── pycache/
│ └── locustfile.py
├── venv_brf_performance_apis_is/
├── .env
├── .gitignore
├── locust_requests.log
└── README.md
```


## Pré-requisitos

- Python 3.6+
- `pip` instalado

## Instalação

1. Clone o repositório:

    ```bash
    git clone <url_do_repositorio>
    cd BRF_PERFORMANCE_APIS_IS
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv_brf_performance_apis_is
    source venv_brf_performance_apis_is/bin/activate  # Linux/Mac
    .\venv_brf_performance_apis_is\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install locust python-dotenv requests
    ```

4. Crie um arquivo `.env` com as seguintes variáveis de ambiente:

    ```env
    BASE_HOST=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com
    PERSON_ACCOUNT_SOUK_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/person_accounts_souk
    PERSON_CUSTOMER_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/person/customer
    PERSON_DELIVERY_WINDOW_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/person/delivery_window
    FINANCIAL_CREDIT_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/financial/credit
    FINANCIAL_MATERIAL_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/financial/material
    PRODUCT_STOCK_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/product/stock
    UTILS_DESCRIPTION_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/utils/description
    ORDER_URL=https://brf-sap-integration-suite-hml-l5ztmvm0.it-cpi008-rt.cfapps.br10.hana.ondemand.com/http/ygg/operation/order
    AUTHORIZATION_HEADER=Basic c2ItMTQ4NzNmZWEtMWI2Zi00ZmI4LWEzZmYtYzY0YmU2M2YwNjc2IWI0ODc5fGl0LXJ0LWJyZi1zYXAtaW50ZWdyYXRpb24tc3VpdGUtaG1sLWw1enRtdm0wIWIxMDY6Y2M3OTMxNWMtZGJjZi00ZjQ0LWFhZjctN2NhMmQyMjYzNDk4JC1fakxVNUo0Z3lmUmJvY0RUUmZxUVZWcXQzaFVJZ0I3b3RWZnh3RmllNWM9
    CONTENT_TYPE_HEADER=application/json
    ```

## Estrutura dos Arquivos

- **`locustfiles/locustfile.py`**: Arquivo principal que contém as tarefas de teste do Locust.
- **`helpers/payloads.py`**: Contém o payload utilizado na requisição `POST` da API "Person account Souk - IS".
- **`helpers/utils.py`**: Contém funções auxiliares, como geração de valores aleatórios para `top` e `skip`.

## Executando os Testes de Performance

1. Ative o ambiente virtual:

    ```bash
    source venv_brf_performance_apis_is/bin/activate  # Linux/Mac
    .\venv_brf_performance_apis_is\Scripts\activate  # Windows
    ```

2. Execute o Locust:

    ```bash
    locust -f locustfiles/locustfile.py
    ```

3. Abra um navegador e acesse `http://localhost:8089`.

4. Configure o número de usuários e a taxa de spawn para iniciar os testes de carga.

## Logs

Os logs das requisições são separados em dois arquivos diferentes:

- **`locust_success.log`**: Contém logs de requisições bem-sucedidas.
- **`locust_error.log`**: Contém logs de requisições que falharam.

## Executando Testes Automatizados

Para verificar a configuração do ambiente e a acessibilidade dos endpoints:

1. Instale o `pytest` se ainda não o fez:

    ```bash
    pip install pytest python-dotenv requests
    ```

2. Crie o arquivo `tests/test_environment.py` com o seguinte conteúdo:

    ```python
    import os
    from dotenv import load_dotenv
    import requests

    load_dotenv()

    def test_environment_variables():
        required_vars = [
            'BASE_HOST', 'PERSON_ACCOUNT_SOUK_URL', 'PERSON_CUSTOMER_URL', 
            'PERSON_DELIVERY_WINDOW_URL', 'FINANCIAL_CREDIT_URL', 
            'FINANCIAL_MATERIAL_URL', 'PRODUCT_STOCK_URL', 
            'UTILS_DESCRIPTION_URL', 'ORDER_URL', 
            'AUTHORIZATION_HEADER', 'CONTENT_TYPE_HEADER'
        ]
        for var in required_vars:
            assert os.getenv(var) is not None, f"Environment variable {var} is not set"

    def test_endpoints_accessibility():
        headers = {
            'Authorization': os.getenv('AUTHORIZATION_HEADER'),
            'Content-Type': os.getenv('CONTENT_TYPE_HEADER')
        }
        urls = [
            os.getenv('PERSON_ACCOUNT_SOUK_URL'), os.getenv('PERSON_CUSTOMER_URL'), 
            os.getenv('PERSON_DELIVERY_WINDOW_URL'), os.getenv('FINANCIAL_CREDIT_URL'), 
            os.getenv('FINANCIAL_MATERIAL_URL'), os.getenv('PRODUCT_STOCK_URL'), 
            os.getenv('UTILS_DESCRIPTION_URL'), os.getenv('ORDER_URL')
        ]
        for url in urls:
            response = requests.get(url, headers=headers)
            assert response.status_code == 200, f"Endpoint {url} is not accessible, status code: {response.status_code}"
    ```

3. Execute os testes:

    ```bash
    pytest tests/test_environment.py
    ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

```
Este arquivo README.md agora reflete corretamente a estrutura do projeto conforme fornecida na imagem, e fornece instruções detalhadas para instalação, configuração e execução dos testes de performance e testes automatizados.
```