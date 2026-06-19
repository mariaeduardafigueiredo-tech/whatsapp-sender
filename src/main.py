import os
import logging
from supabase import create_client, Client
import httpx
from dotenv import load_dotenv

# Load env
load_dotenv()

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise EnvironmentError("SUPABASE_URL e SUPABASE_KEY devem estar definidos no .env")
    return create_client(url, key)


def fetch_contacts(client: Client, limit: int = 3) -> list[dict]:
    logger.info("Buscando contatos no Supabase...")
    response = (
        client.table("contacts")
        .select("name, phone")
        .limit(limit)
        .execute()
    )
    contacts = response.data
    logger.info(f"{len(contacts)} contato(s) encontrado(s).")
    return contacts


def send_whatsapp_message(phone: str, message: str) -> bool:
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    client_token = os.getenv("ZAPI_CLIENT_TOKEN")

    if not instance_id or not token or not client_token:
        raise EnvironmentError(
            "ZAPI_INSTANCE_ID, ZAPI_TOKEN e ZAPI_CLIENT_TOKEN devem estar definidos no .env"
        )

    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": client_token,
    }
    payload = {
        "phone": phone,
        "message": message,
    }

    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=15)
        response.raise_for_status()
        logger.info(f"  ✅ Mensagem enviada para {phone}")
        return True
    except httpx.HTTPStatusError as e:
        logger.error(f"  ❌ Erro HTTP ao enviar para {phone}: {e.response.status_code} - {e.response.text}")
        return False
    except httpx.RequestError as e:
        logger.error(f"  ❌ Erro de conexão ao enviar para {phone}: {e}")
        return False


def main():
    logger.info("=== Iniciando envio de mensagens WhatsApp ===")

    try:
        supabase = get_supabase_client()
        contacts = fetch_contacts(supabase, limit=3)
    except EnvironmentError as e:
        logger.error(f"Configuração inválida: {e}")
        return
    except Exception as e:
        logger.error(f"Erro ao buscar contatos no Supabase: {e}")
        return

    if not contacts:
        logger.warning("Nenhum contato encontrado. Encerrando.")
        return

    success_count = 0
    fail_count = 0

    for contact in contacts:
        name = contact.get("name", "").strip()
        phone = contact.get("phone", "").strip()

        if not name or not phone:
            logger.warning(f"Contato inválido (nome/telefone vazio): {contact}")
            fail_count += 1
            continue

        message = f"Olá, {name} tudo bem com você?"
        logger.info(f"Enviando para {name} ({phone})...")

        if send_whatsapp_message(phone, message):
            success_count += 1
        else:
            fail_count += 1

    logger.info("=== Resumo ===")
    logger.info(f"  Enviados com sucesso : {success_count}")
    logger.info(f"  Falhas               : {fail_count}")
    logger.info("=== Concluído ===")


if __name__ == "__main__":
    main()
