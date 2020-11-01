import sqlite3


conn = sqlite3.connect('product.db')

c = conn.cursor()


"""
NULL - EMPTY
INTEGER - INT
REAL - FLOAT POINT
TEXT - STRING
BLOB - DATA

"""


#c.execute("""CREATE TABLE product(
#            Product_ID integer,
#            Address text,
#            Manufacturer text,
#            Price real,
#            Image text,
#            Description text,
#            Condition text,
#            Grade text,
#            CartID integer
#    )""")

#this command will save the above code , but must be ran once per insertion
#conn.commit()


#c.execute("INSERT INTO product VALUES (123, '123 hill dr', 'apple',100.00, 'shdfsd/sdfsdf/sdfsdf.png', 'Very good deal', 'new' , 'new' , 6785)")


c.execute("SELECT * FROM product WHERE Manufacturer == 'apple'")
#fetchone()    -- this will only get one that matches
#fetchmany(#)  -- this will get the # of matches
#fetchall() -- this will get all of the matches

print(c.fetchmany(1))
conn.commit()
conn.close()
