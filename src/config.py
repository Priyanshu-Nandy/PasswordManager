import sqlite3
from getpass import getpass
import hashlib
import random
import string
def generateDeviceSecret(length=10):
    characters=string.ascii_uppercase+string.digits
    secret_key=''.join(random.choice(characters) for _ in range(length))
    return secret_key
def config():
    db = sqlite3.connect('pm.db')
    cursor=db.cursor()
    query='''CREATE TABLE IF NOT EXISTS secrets(
    masterkey_hash TEXT NOT NULL,
    device_secret TEXT NOT NULL
    )'''
    res=cursor.execute(query)
    query='''CREATE TABLE IF NOT EXISTS entries(
    sitename TEXT NOT NULL,
    siteurl TEXT NOT NULL,
    email TEXT,
    username TEXT,
    password TEXT NOT NULL
    )'''
    res=cursor.execute(query)
    while 1:
        mp=getpass('Choose a MASTER PASSWORD: ')
        if(mp==getpass('Re-type: ') and mp!=""):
            break
        print("Try again")
    hashed_mp =  hashlib.sha256(mp.encode()).hexdigest()
    print("Generated hash of master password")
    ds = generateDeviceSecret()
    print("Device secret generated")
    cursor.execute('''
    INSERT INTO secrets(masterkey_hash,device_secret) VALUES (?,?)''', (hashed_mp,ds)
    )
    print('Secret data has been added')
    # cursor.execute('SELECT * FROM secrets')
    # rows=cursor.fetchall()
    # for row in rows:
    #     print(rows)
    db.commit()
    db.close()

config()