Repositório criado com o intuito de explorar a utilidade do API do Harmony Endpoint.

Requisitos:
Python 3.8+

## Instalar o Software Development Kit (SDK):
```bash 
pip install chkp-harmony-endpoint-management-sdk
```
## Preparar o ambiente Python
```bash 
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```
## Gerar credenciais para acesso à API
1. Acesse o portal Infinity pela visão de contrato "actarlab"
2. Clique na engrenagem que simboliza "configurações"
3. Selecione API Keys e clique no botão "new"
4. No campo "Service" selecione "Endpoint" e no campo "Roles" selecione "Admin"
5. Clique em "Create"
## Altere as variáveis de ambiente
No arquivo .env do projeto, altere as variáveis API_URL, CLIENT_ID e API_SECRET para as credenciais criadas no Portal Infinity.
