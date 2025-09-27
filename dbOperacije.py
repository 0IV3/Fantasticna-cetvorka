import mysql.connector
from datetime import datetime
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="skladiste",
        auth_plugin='mysql_native_password')
    print("DB Connected.")
except:
    print("Unable to connect to the databse.")

cursor = connection.cursor()
datenow = datetime.now()

def dodajProizvod(pname,pprice,pamount):
   sql="select * FROM Proizvodi where name='"+ pname +"';"
   cursor.execute(sql)
   row = cursor.fetchone()
   if cursor.rowcount == 0:
       cursor.execute("INSERT INTO Proizvodi(name,price,amount,created_at,updated_at) VALUES (%s,%s,%s,%s,%s)", (pname,pprice,pamount,datenow,datenow))
       connection.commit()
       return 1
   else:
        return -1
   
def dodajKupca(cfirstname,clastname,cstreet,cpostcode,cage):
    sql = "SELECT * FROM Kupci where first_name = '"+ cfirstname +"' AND last_name='"+ clastname +"';"
    cursor.execute(sql)
    row = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.execute("INSERT INTO Kupci (first_name,last_name,street,post_code,age,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)", (cfirstname,clastname,cstreet,cpostcode,cage,datenow,datenow))
        connection.commit()
        return 1
    else:
        return -1

def dodajOsoblje(sfirstname,slastname,ssempsins,sage):
    sql = "SELECT * FROM Osoblje where first_name = '"+ sfirstname +"' AND last_name='"+ slastname +"';"
    cursor.execute(sql)
    row = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.execute("INSERT INTO Osoblje (first_name,last_name,employee_since,age,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s)", (sfirstname,slastname,ssempsins,sage,datenow,datenow))
        connection.commit()
        return 1
    else:
        return -1
    
def dodajPorudzbinu (opid,ocid,osid,ocount):
    cursor.execute("INSERT INTO Orders(product_id,customer_id,staff_id,count,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s)", (opid,ocid,osid,ocount,datenow,datenow))
    connection.commit()
    return 1

def prikaziProizvod():
    cursor.execute("SELECT * FROM Proizvodi")
    rows = cursor.fetchall()
    return rows

def prikaziKupca():
    cursor.execute("SELECT * FROM Kupci")
    rows = cursor.fetchall()
    return rows

def prikaziOsoblje():
    cursor.execute("SELECT * FROM Osoblje")
    rows = cursor.fetchall()
    return rows

def prikaziPorudzbinu():
    cursor.execute("SELECT o.id,\
                  p.name as product_name,\
                   Concat(c.first_name,' ',s.last_name) as customer_name, \
                   Concat(s.first_name, ' ',s.last_name) as staff_name, \
                   o.count,p.price, \
                   round(o.count*p.price,2) as total_price \
                   FROM Porudzbine as o inner join Proizvodi as P,Kupci as c,Osoblje as s \
                    where o.product_id=p.id and o.customer_id=c.id and o.staff_id=s.id;")
    rows = cursor.fetchall()
    return rows

def prikaziTacanProizvod(pid):
    sql="select * from Proizvodi where id=%s ; " % pid
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def IzbrisiTacanProizvod(pid):
    sql="delete from Proizvodi where id=%s ; " % pid
    cursor.execute(sql)
    connection.commit()
    return 1

def PrikaziTacnogKupca(cid):
    sql="select * from Kupci where id=%s ; " % cid
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def IzbrisiTacnogKupca(cid):
    sql="delete from Kupci where id=%s ; " % cid
    cursor.execute(sql)
    connection.commit()
    return 1

def prikaziTacnoOsoblje(sid):
    sql="select * from Osoblje where id=%s ; " % sid
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def IzbrisiTacnogOsoblje(sid):
    sql="delete from Osoblje where id=%s ; " % sid
    cursor.execute(sql)
    connection.commit()
    return 1

def prikaziTacnuPorudzbinu(oid):
    sql="SELECT o.id,\
                  p.name as product_name,\
                   Concat(c.first_name,' ',s.last_name) as customer_name, \
                   Concat(s.first_name, ' ',s.last_name) as staff_name, \
                   o.count,p.price, \
                   round(o.count*p.price,2) as total_price, p.id, c.id, s.id \
                   FROM Porudzbine as o inner join Proizvodi as P,Kupci as c,Osoblje as s \
                    where o.product_id=p.id and o.customer_id=c.id and o.staff_id=s.id \
                        and o.id = %s; " % oid
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def IzbrisiTacnuPorudzbinu(oid):
    sql="delete from Porudzbine where id=%s ; " % oid
    cursor.execute(sql)
    connection.commit()
    return 1

def urediProizvod(pID,pName,pPrice,pAmount):
    sql="select * from Proizvodi where name='" + pName + "' ; "
    cursor.execute(sql)
    row = cursor.fetchone()
    if cursor.rowcount == 0:
        cursor.execute("update Proizvodi set name= %s ,price=%s,amount=%s,updated_at=%s where id=%s", (pName,pPrice,pAmount,datenow,pID))
        connection.commit()
        return 1
    else:
        return -1

def urediKupca(cID,fName,lName,cStreet,cPostCode,cAge):
    sql="SELECT * from Kupci where first_name='" + fName + "' and last_name'" + lName + "' ; "
    cursor.execute(sql)
    row = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.execute("update Kupci set first_name= %s ,last_name=%s, street=%s, post_code=%s,age=%s,updated_at=%s where id=%s", (fName,lName,cPostCode,cAge,datenow,cID))
        connection.commit()
        return 1
    else:
        return -1
    
def urediOsoblje(sID,fName,lName,sEmployeeSince,sAge):
    sql="SELECT * FROM Osoblje where first_name='" + fName + "' and last_name'" + lName + "' ; "
    cursor.execute(sql)
    row = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.execute("update Osoblje set first_name= %s ,last_name=%s, employee_since=%s,age=%s,updated_at=%s where id=%s", (fName,lName,sEmployeeSince,sAge,datenow,sID))
        connection.commit()
        return 1
    else:
        return -1
    
def urediPorudzbinu(oid,productid,customerid,staffid,ocount):
    cursor.execute("update Orders set product_id=%s, customer_id=%s,staff_id=%s,count=%s,updated_at=%s where id=%s", (productid,customerid,staffid,ocount,datenow,oid))
    connection.commit()
    return 1