import sqlite3



DB_response = ""

def get(DB_request):
    if DB_request == "MAIN":
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT * FROM product WHERE Product_ID == 123")
        DB_response = c.fetchmany(1)
        conn.commit()
        conn.close()
        return DB_response
