[![Standard](https://github.com/ZyamHunter/pytest-rpaframework-json/actions/workflows/standard.yaml/badge.svg)](https://github.com/ZyamHunter/pytest-rpaframework-json/actions/workflows/standard.yaml)

# pytest-rpaframework-json
Repositório de testes dedicados ao uso da biblioteca rpaframework-json utilizando pytest

# robot template
> Repositório de testes dedicados ao uso da bibliotecas rpaframework com json 

# Configuração do Ambiente

## 1. Instalar Python 3.10

Certifique-se de ter o Python 3.10 instalado em seu sistema. Você pode baixá-lo no [site oficial do Python](https://www.python.org/).

## 2. Instalar Pytest
Acesse o site e para o seu entender mais sobre o pytest: https://docs.pytest.org/en/7.4.x/getting-started.html#get-started
> Rode no terminal: 
- pip install -U pytest
> Verifique a versão:
- pytest --version

## 3. Criar um ambiente virtual:
- python -m venv venv

## 4. Se você estiver usando o PowerShell e encontrar problemas para executar scripts, talvez precise alterar a política de execução temporariamente para permitir a execução de scripts:
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## 5. Ativar o ambiente virtual:
- .\venv\Scripts\activate

## 6. Remover cache do pip
- pip cache remove *

## 7. Rodar os testes
- coverage run -m pytest
- coverage report -m
- coverage html


## 8. Desativar ambiente virtual
- deactivate

## 9. Instalar dependências
> Primeiro ative o ambiente virtual para evitar erros de versão com outras bibliotecas instaladas
- pip install -r requirements.txt

<br/>

### ---- Diferenciais no projeto ----
<br/>

- Page Object
- RPA Framework
- Pytest
- Massa de Dados
- Cobertura dos testes
- Report dos testes personalizado

<br/>
