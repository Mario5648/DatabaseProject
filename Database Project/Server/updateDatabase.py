import sqlite3


# 0 : NetServ
# 1: Computers
# 2: PartsAccessories
# 3: Other

def update(DB_request):
    DB_info = DB_request.split("|")
    product = None

    prod_ID = str(DB_info[1])

    conn = sqlite3.connect('webDatabase.db')
    c = conn.cursor()

    #find user that has both the password and username
    c.execute("SELECT * FROM NetServ WHERE Product_ID = "+prod_ID)
    product = c.fetchone()

    if product != None:
        print("[+] Product ID Found!")
        conn.commit()
        conn.close()
        return [0,product]

    c.execute("SELECT * FROM Computers WHERE Product_ID = "+prod_ID)
    product = c.fetchone()

    if product != None:
        print("[+] Product ID Found!")
        conn.commit()
        conn.close()
        return [1,product]

    c.execute("SELECT * FROM PartsAccessories WHERE Product_ID = "+prod_ID)
    product = c.fetchone()

    if product != None:
        print("[+] Product ID Found!")
        conn.commit()
        conn.close()
        return [2,product]

    c.execute("SELECT * FROM Other WHERE Product_ID = "+prod_ID)
    product = c.fetchone()

    if product != None:
        print("[+] Product ID Found!")
        conn.commit()
        conn.close()
        return [3,product]
