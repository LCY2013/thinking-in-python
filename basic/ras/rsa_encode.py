import rsa
import base64

PUBLIC_KEY="""
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEA0oLocXzyiu3qn6MoWB31FPWI1AFuikuDEsSCsIoDEvXOXvh0NOG1
ByIiScPWuFLNSbCwGyYm+vV5qnHE/C95/Yn6qZf1dZXbndxZoNp4zuPoRYVnHZ8V
Jra0IuX7eWU4UdntIB/QnNOsUdKTX3ZiWymqbTVZIBA2Ugktnw2Y3KxuFU/994GB
TTw9xKfvl9eZoX7S15zIuEP77eN6BZW4XQQDeaZg6T/0cMxPWMsFuZSZMpSW7c7Q
gj8+UX1k0r3uiQKgc+HwnAGo0iQ/bAj96W0LrUS5OvtrWiVTjuyOJ4SSaNEDfcoP
jd8JPqb102/Ay+xfox/BVTkyxTvoZ05O0wIDAQAB
-----END RSA PUBLIC KEY-----
"""

# rsa encrypt text to base64
def rsa_encrypt(plaintext: str) -> str:
    public_key = rsa.PublicKey.load_pkcs1(PUBLIC_KEY.encode())
    ciphertext = rsa.encrypt(plaintext.encode('utf-8'), public_key)
    return base64.b64encode(ciphertext).decode('utf-8')

print(rsa_encrypt("mZjNjYWE0MDBiZjMxYmQ1M2E0YTI3NzM0OWFhZTVmNzFhNTUxM2MwYzA1MzJiN2ViYjM4OTAyNmEyMDgxMzcyMmY"))