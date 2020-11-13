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
        user_cartid = str(int(randint(1,20000)))
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
    elif DB_info[0] == "PRODPA":
        #create variables aand convert them to string with the info
        prod_ID = str(int(randint(1,20000)))
        prod_title = str(DB_info[1])
        prod_address = str(DB_info[2])
        prod_manufacturer = str(DB_info[3])
        prod_price = str(DB_info[4])
        prod_image = str(DB_info[5])
        prod_description = str(DB_info[6])
        prod_condition = str(DB_info[7])
        prod_type = str(DB_info[8])

        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()
        c.execute("INSERT INTO PartsAccessories VALUES ("+prod_ID+",'"+prod_title+"','"+prod_address+"','"+prod_manufacturer+"', '"+prod_price+"', '"+prod_image+"', '"+prod_description+"', '"+prod_condition+"', '"+prod_type+"')")
        conn.commit()
        conn.close()
        print("[+] Successfully Added Product "+prod_title+" To The Database")
    elif DB_info[0] == "PRODCOMP":

        #create variables aand convert them to string with the info
        prod_ID = str(int(randint(1,20000)))
        prod_title = str(DB_info[1])
        prod_address = str(DB_info[2])
        prod_manufacturer = str(DB_info[3])
        prod_price = str(DB_info[4])
        prod_image = str(DB_info[5])
        prod_description = str(DB_info[6])
        prod_condition = str(DB_info[7])
        prod_type = str(DB_info[8])
        prod_processor = str(DB_info[9])
        prod_memory = str(DB_info[10])
        prod_harddrive = str(DB_info[11])
        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()
        c.execute("INSERT INTO Computers VALUES ("+prod_ID+",'"+prod_title+"','"+prod_address+"','"+prod_manufacturer+"', '"+prod_price+"', '"+prod_image+"', '"+prod_description+"', '"+prod_condition+"', '"+prod_type+"', '"+prod_processor+"', '"+prod_memory+"', '"+prod_harddrive+"')")
        conn.commit()
        conn.close()
        print("[+] Successfully Added Product "+prod_title+" To The Database")

    elif DB_info[0] == "PRODNS":

        #create variables aand convert them to string with the info
        prod_ID = str(int(randint(1,20000)))
        prod_title = str(DB_info[1])
        prod_address = str(DB_info[2])
        prod_manufacturer = str(DB_info[3])
        prod_price = str(DB_info[4])
        prod_image = str(DB_info[5])
        prod_description = str(DB_info[6])
        prod_condition = str(DB_info[7])
        prod_type = str(DB_info[8])
        prod_processor = str(DB_info[9])
        prod_memory = str(DB_info[10])
        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()
        c.execute("INSERT INTO NetServ VALUES ("+prod_ID+",'"+prod_title+"','"+prod_address+"','"+prod_manufacturer+"', '"+prod_price+"', '"+prod_image+"', '"+prod_description+"', '"+prod_condition+"', '"+prod_type+"', '"+prod_processor+"', '"+prod_memory+"')")
        conn.commit()
        conn.close()
        print("[+] Successfully Added Product "+prod_title+" To The Database")
    elif DB_info[0] == "PRODO":

        #create variables aand convert them to string with the info
        prod_ID = str(int(randint(1,20000)))
        prod_title = str(DB_info[1])
        prod_address = str(DB_info[2])
        prod_manufacturer = str(DB_info[3])
        prod_price = str(DB_info[4])
        prod_image = str(DB_info[5])
        prod_description = str(DB_info[6])
        prod_condition = str(DB_info[7])
        prod_type = str(DB_info[8])

        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()
        c.execute("INSERT INTO Other VALUES ("+prod_ID+",'"+prod_title+"','"+prod_address+"','"+prod_manufacturer+"', '"+prod_price+"', '"+prod_image+"', '"+prod_description+"', '"+prod_condition+"', '"+prod_type+"')")
        conn.commit()
        conn.close()
        print("[+] Successfully Added Product "+prod_title+" To The Database")
