from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from encdec import encrypt
import sqlite3
# from Crypto.Random import get_random_bytes
def computeMasterKey(mp,ds):
    password = mp.encode()
    salt=ds.encode()
    key=PBKDF2(password,salt,dkLen=32,count=1000000,hmac_hash_module=SHA256)
    return key
def addEntry(mp,ds,sitename,siteurl,email,username):
    # get the password
    password=getpass('Password: ')
    mk=computeMasterKey(mp,ds)
    encrypted=encrypt(password,mk)

    #Adding to the database
    db = sqlite3.connect('pm.db')
    cursor=db.cursor()
    cursor.execute('''
    INSERT INTO entries(sitename,siteurl,email,username,password) VALUES (?,?,?,?,?)''', (sitename,siteurl,email,username,encrypted)
    )
    db.commit()
    db.close()