# 📱 WhatsApp Sender

Projeto em Python para envio automatizado de mensagens via WhatsApp utilizando a Z-API, com leitura de contatos armazenados no Supabase.

## Descrição

O sistema busca contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp por meio da Z-API.

Exemplo de mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Funcionalidades

- Envio automatizado de mensagens via WhatsApp
- Integração com Supabase para leitura de contatos
- Configuração por variáveis de ambiente
- Registro de logs das operações realizadas
- Tratamento básico de erros e exceções

## Tecnologias

- Python 3.8+
- Supabase
- Z-API
- python-dotenv

## Estrutura do projeto

```text
whatsapp-sender/
├── config/
│   └── .env.example
├── docs/
│   └── README.md
├── src/
│   └── main.py
├── .gitignore
└── requirements.txt
```

### Organização

- `src/main.py`: ponto de entrada da aplicação
- `config/.env.example`: modelo das variáveis de ambiente
- `docs/README.md`: documentação principal do projeto
- `.gitignore`: arquivos e pastas ignorados pelo Git
- `requirements.txt`: dependências necessárias para execução

## Estrutura da tabela no Supabase

Tabela utilizada: `contatos`

| Campo | Tipo | Descrição |
|---|---|---|
| id | bigint | Identificador único |
| nome | text | Nome do contato |
| telefone | text | Número com DDD |

Exemplo de dados:

| id | nome | telefone |
|---|---|---|
| 1 | Clara Silva | 11999999999 |
| 2 | Maria Souza | 11988888888 |
| 3 | Carlos Lima | 11977777777 |

## Pré-requisitos

Antes de executar o projeto, é necessário ter:

- Python 3.8 ou superior
- pip
- Conta no Supabase
- Conta na Z-API
- Número conectado à Z-API

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/mariaeduardafigueiredo-tech/whatsapp-sender.git
cd whatsapp-sender
```

### 2. Crie e ative o ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com base no arquivo `config/.env.example`.

Exemplo:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-supabase
ZAPI_INSTANCE_ID=sua-instancia
ZAPI_TOKEN=seu-token
```

## Execução

Execute o projeto com:

```bash
python src/main.py
```

## Observações

- O arquivo `.env` não é versionado por conter informações sensíveis.
- A pasta `.venv` não é enviada ao GitHub, pois contém apenas dependências locais do ambiente.
- O arquivo `config/.env.example` serve como modelo para configuração do ambiente.
