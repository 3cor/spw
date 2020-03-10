# refer to: https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password

import secrets
from base64 import urlsafe_b64decode as b64d
from base64 import urlsafe_b64encode as b64e

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()
iterations = 100_000

def _derive_key(password: bytes, salt: bytes, iterations: int = iterations) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    return b64e(kdf.derive(password))

def password_encrypt(message: bytes, password: str, iterations: int = iterations) -> bytes:
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt, iterations)
    return b64e(
        b'%b%b%b' % (
            salt,
            iterations.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )

def password_decrypt(token: bytes, password: str) -> bytes:
    decoded = b64d(token)
    salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iterations = int.from_bytes(iter, 'big')
    key = _derive_key(password.encode(), salt, iterations)
    return Fernet(key).decrypt(token)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Commands available: encrypt and decrypt")
    parser.add_argument("password", help="Password or passphrase to be used")
    parser.add_argument("message", help="Message to be encrypt")
    args = parser.parse_args()
    command = args.command
    password = args.password
    message = args.message

    if command == 'e' or command == 'encrypt':
        output = password_encrypt(message.encode(), password).decode('utf-8')
    elif command == 'd' or command == 'decrypt':
        output = password_decrypt(bytes(message, 'utf-8'), password).decode('utf-8')
    else:
        output == 'Wrong command'

    print(output)
