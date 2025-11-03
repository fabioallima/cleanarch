# CleanArch - Documentação do Projeto

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Arquitetura Clean Architecture](#arquitetura-clean-architecture)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Configuração e Instalação](#configuração-e-instalação)
- [Como Executar](#como-executar)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Testes](#testes)
- [API Endpoints](#api-endpoints)
- [Collection do Postman](#collection-do-postman)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)

---

## 🎯 Sobre o Projeto

O **CleanArch** é um projeto educacional que demonstra a implementação dos princípios da Clean Architecture (Arquitetura Limpa) em uma aplicação Python utilizando Flask. O projeto implementa um sistema básico de gerenciamento de usuários com operações de criação e busca.

### Objetivos

- Demonstrar a aplicação prática da Clean Architecture
- Separar responsabilidades em camadas bem definidas
- Facilitar a manutenibilidade e testabilidade do código
- Criar um código desacoplado e independente de frameworks

---

## 🏗️ Arquitetura Clean Architecture

O projeto segue os princípios da Clean Architecture, organizando o código em camadas concêntricas:

```
┌─────────────────────────────────────────────────┐
│           Presentation Layer (Controllers)      │
│  ┌───────────────────────────────────────────┐  │
│  │      Application Layer (Use Cases)        │  │
│  │  ┌─────────────────────────────────────┐  │  │
│  │  │   Domain Layer (Entities/Models)    │  │  │
│  │  │                                     │  │  │
│  │  └─────────────────────────────────────┘  │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
└─────────────────────────────────────────────────┘
         Infrastructure Layer (Database)
```

### Camadas da Arquitetura

1. **Domain (Domínio)**: Regras de negócio e entidades fundamentais
   - Models: Modelos de domínio
   - Use Cases Interfaces: Contratos dos casos de uso

2. **Data (Dados)**: Implementação das regras de negócio
   - Use Cases: Implementação dos casos de uso
   - Interfaces: Contratos dos repositórios
   - Factories: Criação de instâncias dos casos de uso

3. **Infra (Infraestrutura)**: Implementações de baixo nível
   - Database: Conexão e configuração do banco de dados
   - Entities: Mapeamento ORM (SQLAlchemy)
   - Repositories: Implementação dos repositórios

4. **Presentation (Apresentação)**: Interface com o mundo externo
   - Controllers: Controladores que processam requisições
   - HTTP Types: Tipos de request e response
   - Interfaces: Contratos dos controladores

5. **App (Aplicação)**: Configuração da aplicação
   - Routes: Definição das rotas
   - Composers: Composição de dependências
   - Adapters: Adaptadores de request
   - Server: Configuração do servidor Flask

6. **Validators (Validadores)**: Validação de entrada de dados

7. **Errors (Erros)**: Tratamento centralizado de erros

---

## 📁 Estrutura do Projeto

```
cleanarch/
├── docker/                         # Configurações Docker
│   └── docker-compose.yml         # Orquestração de containers
├── docs/                          # Documentação
│   ├── README.md                  # Este arquivo
│   └── CleanArch.postman_collection.json
├── init/                          # Scripts de inicialização
│   └── schema.sql                 # Schema do banco de dados
├── src/                           # Código fonte
│   ├── app/                       # Camada de aplicação
│   │   ├── adapters/              # Adaptadores de requisição
│   │   ├── composers/             # Composição de dependências
│   │   ├── routes/                # Definição de rotas
│   │   └── server/                # Configuração do servidor
│   ├── data/                      # Camada de dados
│   │   ├── factories/             # Factories dos casos de uso
│   │   ├── interfaces/            # Interfaces dos repositórios
│   │   └── use_cases/             # Implementação dos casos de uso
│   ├── domain/                    # Camada de domínio
│   │   ├── models/                # Modelos de domínio
│   │   └── use_cases/             # Interfaces dos casos de uso
│   ├── errors/                    # Tratamento de erros
│   │   └── types/                 # Tipos de erros HTTP
│   ├── infra/                     # Camada de infraestrutura
│   │   └── db/                    # Configuração do banco de dados
│   │       ├── entities/          # Entidades SQLAlchemy
│   │       ├── repositories/      # Implementação dos repositórios
│   │       └── settings/          # Configuração de conexão
│   ├── presentation/              # Camada de apresentação
│   │   ├── controllers/           # Controladores
│   │   ├── http_types/            # Tipos HTTP
│   │   └── interfaces/            # Interfaces dos controladores
│   └── validators/                # Validadores de entrada
├── conftest.py                    # Configuração do pytest
├── dockerfile                     # Dockerfile da aplicação
├── requirements.txt               # Dependências Python
└── run.py                         # Ponto de entrada da aplicação
```

---

## ⚙️ Pré-requisitos

### Opção 1: Executar com Docker (Recomendado)

- [Docker](https://www.docker.com/get-started) (versão 20.x ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão 2.x ou superior)

### Opção 2: Executar Localmente

- Python 3.13 ou superior
- MySQL 8.4 ou superior
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

---

## 🚀 Configuração e Instalação

### Opção 1: Usando Docker (Recomendado)

Esta é a maneira mais simples de executar o projeto, pois o Docker cuidará de todas as dependências.

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd cleanarch
```

2. **Configure as variáveis de ambiente (opcional)**:

Você pode criar um arquivo `.env` na raiz do projeto para customizar as configurações:

```env
# Configurações do MySQL
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=clean_database
MYSQL_USER=cleanarch_user
MYSQL_PASSWORD=123456
MYSQL_PORT=3307

# Porta do phpMyAdmin
PHPMYADMIN_PORT=8080
```

3. **Inicie os containers**:
```bash
cd docker
docker-compose up -d
```

Isso iniciará três serviços:
- **database**: MySQL 8.4 (porta 3307)
- **app**: Aplicação Flask (porta 5001)
- **phpmyadmin**: Interface web para gerenciar o banco (porta 8080)

4. **Verifique se os containers estão rodando**:
```bash
docker-compose ps
```

5. **Acesse a aplicação**:
- API: http://localhost:5001
- phpMyAdmin: http://localhost:8080

### Opção 2: Executar Localmente

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd cleanarch
```

2. **Crie um ambiente virtual**:
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. **Instale as dependências**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Configure o banco de dados MySQL**:

Execute o script SQL localizado em `init/schema.sql` no seu MySQL:

```bash
mysql -u root -p < init/schema.sql
```

5. **Configure as variáveis de ambiente**:

Crie as seguintes variáveis de ambiente ou edite o código de conexão:

```bash
export DB_DRIVER=mysql+pymysql
export DB_USER=cleanarch_user
export DB_PASSWORD=123456
export DB_HOST=localhost
export DB_PORT=3306
export DB_NAME=clean_database
```

6. **Execute a aplicação**:
```bash
python run.py
```

A aplicação estará disponível em: http://localhost:5001

---

## 🏃 Como Executar

### Iniciar a Aplicação (Docker)

```bash
cd docker
docker-compose up -d
```

### Parar a Aplicação (Docker)

```bash
docker-compose down
```

### Ver logs da aplicação (Docker)

```bash
docker-compose logs -f app
```

### Reiniciar a aplicação (Docker)

```bash
docker-compose restart app
```

### Executar localmente

```bash
python run.py
```

---

#### 🔧 Configurações Python

- **Interpretador**: Automaticamente configurado para `.venv/bin/python`
- **Linting**: Pylint habilitado com configurações do `.pylintrc`
- **Formatação**: Black configurado para formatar automaticamente ao salvar
- **Imports**: isort configurado para organizar imports automaticamente
- **Type Checking**: Pylance configurado em modo básico

#### 🧪 Configurações de Teste

- **Framework**: pytest habilitado
- **Auto-discovery**: Descobre testes automaticamente ao salvar
- **Debug**: Configurações de debug prontas para testes

#### 🐛 Configurações de Debug

O workspace inclui 4 configurações de debug:

1. **Python: Flask** - Inicia o servidor Flask em modo debug
2. **Python: Current File** - Executa o arquivo atual
3. **Python: Run Tests** - Executa testes em modo debug
4. **Docker: Attach to Python** - Conecta ao container Docker

Para usar, vá em **Run and Debug (F5)** e selecione a configuração desejada.

#### ⚙️ Tarefas Automatizadas

O workspace inclui 12 tarefas prontas para uso:

**Desenvolvimento:**
- `Run Flask App` - Inicia a aplicação Flask
- `Run Tests` - Executa todos os testes
- `Run Pylint` - Verifica o código com pylint
- `Format with Black` - Formata o código
- `Sort Imports` - Organiza imports com isort

**Docker:**
- `Docker: Build` - Constrói as imagens Docker
- `Docker: Up` - Inicia os containers
- `Docker: Down` - Para os containers
- `Docker: Logs` - Mostra os logs dos containers

**Ambiente:**
- `Install Requirements` - Instala dependências do requirements.txt
- `Install Pre-commit Hooks` - Instala os hooks de pre-commit
- `Run Pre-commit (All Files)` - Executa pre-commit em todos os arquivos

**Para executar uma tarefa:**
1. Pressione `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux)
2. Digite "Tasks: Run Task"
3. Selecione a tarefa desejada

Ou use o atalho: `Cmd+Shift+B` para executar a tarefa padrão (Run Flask App)

#### 🔌 Extensões Recomendadas

Ao abrir o workspace pela primeira vez, o Cursor recomendará instalar as seguintes extensões:

**Python:**
- Python
- Pylance
- Black Formatter
- isort

**Docker:**
- Docker

**Git:**
- GitLens

**Database:**
- SQLTools
- SQLTools MySQL Driver

**Outras:**
- REST Client
- YAML
- Markdown All in One
- TODO Highlight
- Better Comments
- Path Intellisense

### Configurações Importantes

#### Formatação Automática

O código será automaticamente formatado ao salvar:
- **Black** para formatação geral
- **isort** para organização de imports

#### Linting em Tempo Real

Erros e avisos do pylint aparecerão em tempo real enquanto você codifica.

#### IntelliSense Aprimorado

- Auto-completar imports
- Sugestões de código
- Type hints
- Documentação inline

#### Exclusões de Arquivos

Arquivos desnecessários são automaticamente excluídos:
- `__pycache__/`
- `*.pyc`
- `.pytest_cache/`
- `.mypy_cache/`
- `.venv/`

### Variáveis de Ambiente

Para o workspace funcionar corretamente, certifique-se de que:

1. O ambiente virtual está criado em `.venv/`:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. A variável `PYTHONPATH` está configurada (o workspace faz isso automaticamente)

### Configuração

O arquivo `.pre-commit-config.yaml` define dois hooks:

1. **pylint**: Analisa o código Python em busca de erros e problemas de estilo
2. **requirements**: Atualiza automaticamente o arquivo `requirements.txt` com as dependências atuais

### Como Instalar os Pre-commit Hooks

1. **Certifique-se de que o pre-commit está instalado**:
```bash
pip install pre-commit
```

2. **Instale os hooks no seu repositório local**:
```bash
pre-commit install
```

### Como Funciona

Após a instalação, os hooks serão executados automaticamente sempre que você executar `git commit`:

1. **pylint** irá verificar todos os arquivos Python alterados:
   - Mostra apenas mensagens (sem pontuação)
   - Usa as configurações do arquivo `.pylintrc`
   - Carrega extensões para validar docstrings

2. **requirements** irá:
   - Gerar automaticamente o `requirements.txt` baseado nos pacotes instalados
   - Adicionar o arquivo ao commit automaticamente

### Executar Manualmente

Você pode executar os hooks manualmente sem fazer commit:

```bash
# Executar em todos os arquivos
pre-commit run --all-files

# Executar apenas o pylint
pre-commit run pylint --all-files

# Executar apenas o hook de requirements
pre-commit run requirements --all-files
```

### Pular os Hooks (Não Recomendado)

Se necessário, você pode pular os hooks em um commit específico:

```bash
git commit --no-verify -m "Sua mensagem"
```

⚠️ **Importante**: Evite pular os hooks, pois eles garantem a qualidade do código!

### Desinstalar os Hooks

Se precisar remover os hooks:

```bash
pre-commit uninstall
```

---

## 🧪 Testes

O projeto inclui testes unitários usando **pytest**.

### Executar todos os testes

```bash
pytest
```

### Executar testes de um módulo específico

```bash
# Testes do UserFinder
pytest src/data/use_cases/user_finder_test.py

# Testes do UserRegister
pytest src/data/use_cases/user_register_test.py

# Testes do Repository
pytest src/infra/db/repositories/users_repository_test.py

# Testes dos Controllers
pytest src/presentation/controllers/user_finder_controller_test.py
pytest src/presentation/controllers/user_register_controller_test.py

# Testes dos Validators
pytest src/validators/user_finder_validator_test.py
pytest src/validators/user_register_validator_test.py
```

### Executar testes com cobertura

```bash
pytest --cov=src --cov-report=html
```

O relatório de cobertura será gerado em `htmlcov/index.html`.

---

## 🌐 API Endpoints

### Base URL

```
http://localhost:5001
```

### Endpoints Disponíveis

#### 1. Criar Usuário

**POST** `/user`

Cria um novo usuário no sistema.

**Request Body**:
```json
{
    "first_name": "Fabio",
    "last_name": "Lima",
    "age": 34
}
```

**Response Success (201)**:
```json
{
    "type": "users",
    "count": 1,
    "attributes": {
        "id": 1,
        "first_name": "Fabio",
        "last_name": "Lima",
        "age": 34
    }
}
```

**Response Error (400)**:
```json
{
    "errors": [
        {
            "title": "BadRequest",
            "detail": "Mensagem de erro"
        }
    ]
}
```

**Regras de Validação**:
- `first_name`: obrigatório, string
- `last_name`: obrigatório, string
- `age`: obrigatório, número inteiro

---

#### 2. Buscar Usuário

**GET** `/user/find?first_name={nome}`

Busca usuários pelo primeiro nome.

**Query Parameters**:
- `first_name` (string): Nome do usuário a ser buscado

**Request**:
```
GET /user/find?first_name=Fabio
```

**Response Success (200)**:
```json
{
    "type": "users",
    "count": 1,
    "attributes": [
        {
            "id": 1,
            "first_name": "Fabio",
            "last_name": "Lima",
            "age": 34
        }
    ]
}
```

**Response Not Found (404)**:
```json
{
    "errors": [
        {
            "title": "NotFound",
            "detail": "User not found"
        }
    ]
}
```

**Regras de Validação**:
- `first_name`: obrigatório, string, deve ser passado como query parameter

---

## 📮 Collection do Postman

O projeto inclui uma collection do Postman para facilitar o teste da API.

### Arquivo da Collection

A collection está disponível em:
```
docs/CleanArch.postman_collection.json
```

### Conteúdo da Collection

A collection inclui os seguintes requests:

#### 1. **Create User** (POST /user)
- Método: POST
- URL: `{{host}}/user`
- Headers:
  - Content-Type: application/json
- Body:
```json
{
    "first_name": "Fabio",
    "last_name": "Lima",
    "age": 34
}
```

#### 2. **Get User** (GET /user/find)
- Método: GET
- URL: `{{host}}/user/find?first_name=Fabio9`
- Headers:
  - Content-Type: application/json
- Query Parameters:
  - `first_name`: Fabio9

### Como Importar a Collection no Postman

1. Abra o Postman
2. Clique em "Import" no canto superior esquerdo
3. Selecione o arquivo `docs/CleanArch.postman_collection.json`
4. A collection "CleanArch" será adicionada ao seu workspace

### Configurar Variável de Ambiente

Para usar a collection, configure a variável `{{host}}`:

1. No Postman, clique em "Environments"
2. Crie um novo ambiente chamado "CleanArch Local"
3. Adicione a variável:
   - Variable: `host`
   - Initial Value: `http://localhost:5001`
   - Current Value: `http://localhost:5001`
4. Salve e selecione o ambiente

### Exemplos de Uso

**Criar um usuário**:
1. Selecione o request "Create User"
2. Ajuste o body JSON conforme necessário
3. Clique em "Send"

**Buscar um usuário**:
1. Selecione o request "Get User"
2. Modifique o query parameter `first_name` na URL
3. Clique em "Send"

### Conteúdo Completo da Collection

```json
{
	"info": {
		"_postman_id": "17a8bd1b-5d42-4b42-a89c-4c596b4165bf",
		"name": "CleanArch",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "7045704"
	},
	"item": [
		{
			"name": "User",
			"item": [
				{
					"name": "Create User",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"first_name\": \"Fabio\",\n    \"last_name\": \"Lima\",\n    \"age\": 34\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{host}}/user",
							"host": [
								"{{host}}"
							],
							"path": [
								"user"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get User",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json",
								"type": "text"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"first_name\": \"Fabio\",\n    \"last_name\": \"Lima\",\n    \"age\": 34\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{host}}/user/find?first_name=Fabio9",
							"host": [
								"{{host}}"
							],
							"path": [
								"user",
								"find"
							],
							"query": [
								{
									"key": "first_name",
									"value": "Fabio9"
								}
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
```

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.13**: Linguagem de programação
- **Flask 3.1.2**: Framework web minimalista
- **SQLAlchemy 2.0.44**: ORM (Object-Relational Mapping)
- **PyMySQL 1.1.2**: Driver Python para MySQL

### Banco de Dados
- **MySQL 8.4**: Sistema de gerenciamento de banco de dados

### Validação e Qualidade de Código
- **Cerberus 1.3.7**: Validação de dados
- **Pylint 3.3.9**: Análise estática de código
- **Black 25.9.0**: Formatador de código
- **isort 6.1.0**: Organizador de imports
- **pre-commit 4.3.0**: Framework de hooks de pre-commit

### Testes
- **pytest 8.4.2**: Framework de testes

### DevOps
- **Docker**: Containerização
- **Docker Compose**: Orquestração de containers
- **phpMyAdmin 5.2**: Interface web para gerenciar MySQL

### Outros
- **python-dotenv 1.2.1**: Gerenciamento de variáveis de ambiente
- **GitPython 3.1.45**: Interface Python para Git

---

## 📝 Notas Adicionais

### Estrutura do Banco de Dados

O banco de dados `clean_database` contém uma tabela `users`:

```sql
CREATE TABLE users (
    id BIGINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age BIGINT NOT NULL,
    PRIMARY KEY (id)
);
```

### Healthcheck do MySQL

O Docker Compose inclui um healthcheck para garantir que o MySQL esteja pronto antes de iniciar a aplicação:

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
  timeout: 20s
  retries: 10
  interval: 10s
  start_period: 30s
```

### Desenvolvimento com Hot Reload

Ao usar Docker Compose, os arquivos em `src/` estão montados como volume, permitindo hot reload durante o desenvolvimento:

```yaml
volumes:
  - ../src:/app/src
```

### Acesso ao phpMyAdmin

O phpMyAdmin está disponível em http://localhost:8080 com as credenciais:
- **Servidor**: database
- **Usuário**: cleanarch_user
- **Senha**: 123456

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

**Lembre-se**: Os pre-commit hooks serão executados automaticamente. Certifique-se de que seu código passa em todas as verificações!

---

## 📄 Licença

Este é um projeto educacional desenvolvido para fins de aprendizado da Clean Architecture.

---

## 👤 Autor

Fabio Lima

---

## 📚 Referências

- [Clean Architecture - Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)
- [pre-commit Documentation](https://pre-commit.com/)

---

**Última atualização**: Novembro de 2025
