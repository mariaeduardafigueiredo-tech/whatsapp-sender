# 📱 WhatsApp Sender

Sistema para envio automatizado de mensagens via WhatsApp utilizando a API Z-API e integração com Supabase para gerenciamento de contatos.

## 📋 Descrição

Este projeto lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp utilizando a Z-API.

**Formato da mensagem:**

Olá, <nome_contato> tudo bem com você?


**Funcionamento:**
- Busca até 3 contatos por execução
- Envia mensagem personalizada para cada contato
- Registra logs de todas as operações

## 🗄️ Estrutura da Tabela no Supabase

**Tabela:** `contatos`

| Campo    | Tipo   | Descrição              |
| -------- | ------ | ---------------------- |
| id       | bigint | Identificador único    |
| nome     | text   | Nome do contato        |
| telefone | text   | Número com DDD (sem 9) |

**Exemplo de dados:**
| id | nome         | telefone      |
| -- | ------------ | ------------- |
| 1  | Clara Silva  | 11999999999   |
| 2  | Maria Souza  | 11988888888   |
| 3  | Carlos Lima  | 11977777777   |

## ✨ Funcionalidades

- ✅ Envio automatizado de mensagens via WhatsApp
- ✅ Integração com Supabase para armazenamento de dados
- ✅ Logs detalhados de operações
- ✅ Configuração via variáveis de ambiente
- ✅ Tratamento de erros e exceções

## 🚀 Tecnologias

- **Python 3.8+** - Linguagem principal
- **Supabase** - Banco de dados e autenticação
- **Z-API** - API para envio de mensagens WhatsApp
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter:

- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes Python)
- Conta no [Supabase](https://supabase.com/)
- Conta na [Z-API](https://z-api.com/)
- Número de WhatsApp conectado na Z-API

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/mariaeduardafigueiredo-tech/whatsapp-sender.git
cd whatsapp-sender
```

## 2. Variáveis de Ambiente

```env

SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-supabase

ZAPI_INSTANCE_ID=sua-instancia
ZAPI_TOKEN=seu-token
```
## Observações

O arquivo `.env` não está incluído no repositório por questões de segurança.

Utilize o arquivo `.env.example` como modelo para criar seu próprio arquivo `.env` com as credenciais do Supabase e da Z-API.

A pasta `.venv` não faz parte do projeto versionado, pois contém dependências locais do ambiente Python.

Crie um arquivo `.env` na raiz do projeto:

## 3. Crie o ambiente virtual
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 5. Execução

Execute o projeto:

```bash
python main.py
```
