import sqlite3


conn = sqlite3.connect('webDatabase.db')

c = conn.cursor()


"""
NULL - EMPTY
INTEGER - INT
REAL - FLOAT POINT
TEXT - STRING
BLOB - DATA

"""



c.execute("""CREATE TABLE PartsAccessories(
            Product_ID integer,
            Title text,
            Address text,
            Manufacturer text,
            Price real,
            Image text,
            Description text,
            Condition text,
            type text
    )""")


#this command will save the above code , but must be ran once per insertion
conn.commit()

c.execute("""CREATE TABLE Computers(
            Product_ID integer,
            Title text,
            Address text,
            Manufacturer text,
            Price real,
            Image text,
            Description text,
            Condition text,
            type text,
            Processor text,
            Memory text,
            HardDrive text

    )""")

conn.commit()

c.execute("""CREATE TABLE NetServ(
            Product_ID integer,
            Title text,
            Address text,
            Manufacturer text,
            Price real,
            Image text,
            Description text,
            Condition text,
            type text,
            Processor text,
            Memory text
    )""")

conn.commit()


c.execute("""CREATE TABLE Other(
            Product_ID integer,
            Title text,
            Address text,
            Manufacturer text,
            Price real,
            Image text,
            Description text,
            Condition text,
            type text,

    )""")

conn.commit()


c.execute("""CREATE TABLE users(
        Name text,
        Username text,
        Password text,
        Address text,
        CartID integer
    )""")
conn.commit()

c.execute("""CREATE TABLE admin(
        Name text,
        Username text,
        Password text,
        Role text
    )""")

conn.commit()

c.execute("INSERT INTO admin VALUES('Mario','Mario5648','password','Owner')")
c.execute("INSERT INTO users VALUES('Mario','Mario5648','password','1234 sunset drive',123456)")

c.execute("INSERT INTO product VALUES (123456, '123 hill dr', 'apple',1.00, './ip2.jpg', 'Very good deal', 'new' , 'new' ,'Iphone 6')")
c.execute("INSERT INTO product VALUES (987654, '123 hill dr', 'apple',2.00, './ip1.jpg', 'trying to sell small crack on screen', 'used' , 'decent' ,'Iphone 8' )")
c.execute("INSERT INTO product VALUES (654321, '123 hill dr', 'apple',3.00, './ip2.jpg', 'Good condition. I never took it out of the case, now I want to upgrade ', 'used' , 'Great' ,'Iphone 6' )")
c.execute("INSERT INTO product VALUES (654398, '123 hill dr', 'apple',4.00, './ip1.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000001, '123 hill dr', 'apple',5.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000002, '123 hill dr', 'apple',6.00, './ip2.jpg', 'Very good deal', 'new' , 'new' ,'Iphone 6' )")
c.execute("INSERT INTO product VALUES (000003, '123 hill dr', 'apple',7.00, './ip2.jpg', 'trying to sell small crack on screen', 'used' , 'decent' ,'Iphone 8' )")
c.execute("INSERT INTO product VALUES (000004, '123 hill dr', 'apple',8.00, './ip1.jpg', 'Good condition. I never took it out of the case, now I want to upgrade ', 'used' , 'Great' ,'Iphone 6' )")

c.execute("INSERT INTO product VALUES (000005, '123 hill dr', 'apple',9.00, './ip1.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000006, '123 hill dr', 'apple',10.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000007, '123 hill dr', 'apple',11.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000008, '123 hill dr', 'apple',12.00, './ip2.jpg', 'Very good deal', 'new' , 'new' ,'Iphone 6' )")
c.execute("INSERT INTO product VALUES (000009, '123 hill dr', 'apple',13.00, './ip2.jpg', 'trying to sell small crack on screen', 'used' , 'decent' ,'Iphone 8' )")
c.execute("INSERT INTO product VALUES (000010, '123 hill dr', 'apple',14.00, './ip1.jpg', 'Good condition. I never took it out of the case, now I want to upgrade ', 'used' , 'Great' ,'Iphone 6' )")
c.execute("INSERT INTO product VALUES (000011, '123 hill dr', 'apple',15.00, './ip1.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")

c.execute("INSERT INTO product VALUES (000012, '123 hill dr', 'apple',16.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")
c.execute("INSERT INTO product VALUES (000012, '123 hill dr', 'apple',17.00, './ip2.jpg', 'Great condition hardly used', 'used' , 'decent' ,'Iphone 11' )")


#c.execute("SELECT * FROM product WHERE Manufacturer == 'apple'")
#fetchone()    -- this will only get one that matches
#fetchmany(#)  -- this will get the # of matches
#fetchall() -- this will get all of the matches

#print(c.fetchmany(1))
conn.commit()
conn.close()
