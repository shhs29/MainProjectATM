from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'users'

cnx = mysql.connector.connect(user='root', password='kizhakkaneth',
                              database='users')
cursor = cnx.cursor()
cursor1 = cnx.cursor()
#query_createtable = "create table table2(User_id int(4),Frequency int(4),Image_path varchar(30));"
#cursor.execute(query_createtable);

query_insert = "insert into userdata VALUES('s3','img2.jpg',3);"
cursor.execute(query_insert)
cnx.commit()


cnx.close()
