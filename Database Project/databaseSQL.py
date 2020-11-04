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


c.execute("""CREATE TABLE product(
            Product_ID integer,
            Address text,
           Manufacturer text,
            Price real,
            Image text,
            Description text,
            Condition text,
           Grade text,
            Title text,
            CartID integer
    )""")

#this command will save the above code , but must be ran once per insertion
conn.commit()


c.execute("INSERT INTO product VALUES (123456, '123 hill dr', 'apple',100.00, './ip2.jpg', 'Very good deal', 'new' , 'new' ,'Iphone 6' , 6785)")
c.execute("INSERT INTO product VALUES (987654, '123 hill dr', 'apple',80.00, './ip1.jpg', 'trying to sell small crack on screen', 'used' , 'decent' ,'Iphone 8' , 6785)")
c.execute("INSERT INTO product VALUES (654321, '123 hill dr', 'apple',150.00, './ip2.jpg', 'Good condition. I never took it out of the case, now I want to upgrade ', 'used' , 'Great' ,'Iphone 6' , 6785)")
c.execute("INSERT INTO product VALUES (654398, '123 hill dr', 'apple',300.00, './ip1.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' , 6785)")
c.execute("INSERT INTO product VALUES (000001, '123 hill dr', 'apple',9999.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' , 6785)")




#c.execute("SELECT * FROM product WHERE Manufacturer == 'apple'")
#fetchone()    -- this will only get one that matches
#fetchmany(#)  -- this will get the # of matches
#fetchall() -- this will get all of the matches

#print(c.fetchmany(1))
conn.commit()
conn.close()
