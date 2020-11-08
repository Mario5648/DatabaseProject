import sqlite3
from random import randint

"""
This python file is reponsible for adding to
the databse accordingly.

**Add a User
    -Assign a cart ID

**Add a product

"""

#Codes:
#    SIGNUP   -- Add a user
#    ADDPROD  -- Add a product

def add(DB_request):
    exists_flag = []
    DB_info = DB_request.split("|")

    #Username,Name,Address,Password
    if DB_info[0] == "SIGNUP":
        #create variables aand convert them to string with the info
        user_username = str(DB_info[1])
        user_name = str(DB_info[2])
        user_address = str(DB_info[3])
        user_password = str(DB_info[4])
        user_cartid = str(int(randint(1,5000)))
        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()

        #Check if the user name exists
        c.execute("SELECT * FROM users WHERE Username = '"+user_username+"'")
        exists_flag = c.fetchall()

        if exists_flag == []:
            c.execute("INSERT INTO users VALUES ('"+user_name+"','"+user_username+"','"+user_password+"','"+user_address+"', "+user_cartid+")")
            conn.commit()
            conn.close()
            print("[+] Successfully Added User "+user_username+" To The Database")
            return 0
        else:
            conn.commit()
            conn.close()
            print("[!] ERROR: Username "+user_username+" Already Exists")
            return 1
