from cryptography.fernet import Fernet
from django.conf import settings
import base64
import hashlib

def get_cipher():
    """
    Generate a Fernet cipher from Django's SECRET_KEY.
    """
    key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key)
    return Fernet(fernet_key)

def encrypt_password(password):
    cipher = get_cipher()
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    cipher = get_cipher()
    return cipher.decrypt(encrypted_password.encode()).decode()