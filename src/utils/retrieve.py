import sqlite3
from utils.encdec import decrypt 
def retrieveEntries(mp,ds,search,decryptPassword=False):
    db = sqlite3.connect('pm.db')
    cursor=db.cursor()
    
    query=""
    # iF user does not specify something then return all the entries
    if(len(search)==0):
        query="SELECT * FROM entries"
    else:
        query="SELECT * FROM entries WHERE 1=1"
        for i in search:
            query+=f"{i} = {search[i]}' AND"
        query=query[:-5]#removing the last and
    
    cursor.execute(query)
    results=cursor.fetchall()

    if(len(results)==0):
        return
    # if(decryptPassword and len(results)>1 or (not decryptPassword)):
        
    