# this file opens a connection to our hana db and inserts one row, 2 columns, with a key and a pdf as blob


import pyodbc
conn = pyodbc.connect('Driver={HDBODBC};SERVERNODE=<IP address:port>;SERVERDB=HDB;UID=SYSTEM;PWD=<password>') #Open connection to SAP HANA
cur = conn.cursor() # Open a cursor
file = open('c:/temp/python/Business_Objects_in_LRM.pdf', 'rb') #Open file in read-only and binary mode
content = file.read() #Save the content of the file in a variable

cur.execute("INSERT INTO \"HANA_WORKSHOP_01\".\"workshop.exercises.g01.data::mytable\" VALUES(?,?)", ('1',content)) #save the content to the table
cur.execute("COMMIT") #commit content to the table
file.close() # close the file
cur.close() # close the cursor
conn.close() # close the connection
