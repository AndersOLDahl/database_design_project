import mysql.connector, sys, os
from mysql.connector import errorcode
from front_end_packages import *

# Connection config
config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'Project',
  'raise_on_warnings': True,
}

# Connect to database
try:
  cnx = mysql.connector.connect(**config)

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:

  cursor = cnx.cursor();

  while True:
    os.system('clear')
    print("""Would you like to do?
    1) Delete data
    2) Insert data
    3) Update data
    4) View data
    5) Exit""")

    while True:
      c = int(raw_input("> "))
      if c  == 1:
        deletes.delete_data(cursor, cnx)
        break
      if c == 2:
        inserts.insert_data(cursor, cnx)
        break
      if c == 3:
        updates.update_data(cursor, cnx)
        break
      if c == 4:
        views.view_data(cursor)
        break
      if c == 5:
        sys.exit(1)

  cursor.close()
  cnx.close()
