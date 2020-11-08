import sqlite3






def verify(DB_request):
    DB_info = DB_request.split("|")
    exists_flag = None
    if DB_info[0] == "LOGIN":
        user_username = str(DB_info[1])
        user_password = str(DB_info[2])

        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()

        #find user that has both the password and username
        c.execute("SELECT * FROM users WHERE Username = '"+user_username+"' AND Password = '"+user_password+"'")
        exists_flag = c.fetchone()

        if exists_flag != None:
            conn.commit()
            conn.close()
            print("[+] User "+user_username+" Found In Database, Logging In Now")
            return 0
        else:
            conn.commit()
            conn.close()
            print("[!] ERROR: User "+user_username+" Credentials Invalid")
            return 1
    elif DB_info[0] == "ALOGIN":
        user_username = str(DB_info[1])
        user_password = str(DB_info[2])

        conn = sqlite3.connect('webDatabase.db')
        c = conn.cursor()

        #find user that has both the password and username
        c.execute("SELECT * FROM admin WHERE Username = '"+user_username+"' AND Password = '"+user_password+"'")
        exists_flag = c.fetchone()
        print(exists_flag)
        if exists_flag != None:
            conn.commit()
            conn.close()
            print("[+] Admin "+user_username+" Found In Database, Logging In Now")
            return 0
        else:
            conn.commit()
            conn.close()
            print("[!] ERROR: User "+user_username+" Attempted to login, Credentials Invalid")
            return 1
