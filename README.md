# Envio de Mensagens via Z-API e Supabase

## Descrição

Este projeto lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp utilizando a Z-API.

A mensagem enviada segue o formato:

Olá, <nome_contato> tudo bem com você?

O sistema busca até 3 contatos da tabela e realiza o envio automaticamente.

## Estrutura da Tabela no Supabase

Tabela: contatos

Campos:

| Campo    | Tipo   |
| -------- | ------ |
| id       | bigint |
| nome     | text   |
| telefone | text   |

Exemplo:

| id | nome  | telefone      |
| -- | ----- | ------------- |
| 1  | Clara Silva | XXXXXXXXXXXXX|
| 2  | Maria Souza  | XXXXXXXXXXXXX|
| 3  | Carlos Lima  | XXXXXXXXXXXXX|

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-supabase

ZAPI_INSTANCE_ID=sua-instancia
ZAPI_TOKEN=seu-token
```

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute o projeto:

```bash
python main.py
```

## Funcionamento

1. Conecta ao Supabase.
2. Busca até 3 contatos da tabela `contatos`.
3. Monta a mensagem personalizada utilizando o nome do contato.
4. Envia a mensagem através da Z-API.
5. Exibe logs de sucesso ou erro no terminal.

## Tecnologias Utilizadas

* Python
* Supabase
* Z-API
* Requests
* Python-dotenv