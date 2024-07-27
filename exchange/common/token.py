import secrets


async def generate_token(length=20) -> str:
    return secrets.token_hex(nbytes=length)
