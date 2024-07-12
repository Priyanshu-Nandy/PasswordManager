from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def pad(s):
    return s + (AES.block_size - len(s)%AES.block_size) * chr(AES.block_size - len(s)%AES.block_size)
def unpad(s):
    return s[:-ord(s[len(s)-1:])]
def encrypt(password,key):
    # Generates a random initialization vector for AES encryption
    iv=get_random_bytes(AES.block_size)
    # Create AES cipher object
    cipher=AES.new(key,AES.MODE_CBC,iv)
    padded_password=pad(password).encode()
    # Encrypt the padded password
    combined_data=iv + cipher.encrypt(padded_password)
    return combined_data
def decrypt(combined_data,key):
    iv=combined_data[:AES.block_size]
    cipher_text=combined_data[AES.block_size:]
    cipher=AES.new(key,AES.MODE_CBC,iv)
    decrpyted_padded = cipher.decrypt(cipher_text)
    decrypted_data=unpad(decrpyted_padded.decode())
    return decrypted_data
# key=get_random_bytes(16)
# # data="HA AHAA"
# # combined_data= encrypt(data,key)
# # print(combined_data)
# # decrypted_data=decrypt(combined_data,key)
# # print(decrypted_data)