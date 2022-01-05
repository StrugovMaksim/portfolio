from __future__ import print_function

import mysql.connector

cnx = mysql.connector.connect(user='root', password="12345",database='myusers' )
cursor = cnx.cursor()
def create_account(name, password):
    add_to_table = ("INSERT INTO accounts "
              "(id, name, password) "
              "VALUES (DEFAULT, %(name)s, %(password)s)")
    keys = {
  'name': name,
  'password': password
  }
    cursor.execute(add_to_table, keys)
    print('done')
    cnx.commit()

    cursor.close()
    cnx.close()

def check_account(name, password):
  find_in_table = ("SELECT * FROM accounts WHERE %(name)s = name")
  keys = {
    'name': name
  }
  cursor.execute(find_in_table,keys)
  for i in cursor:
      if i[2] == password:
        print('done') #here i can use function to join 
        continue
      else:
        print('try again')
  cnx.commit()
  cursor.close()
  cnx.close()

def delete_account(name, password):
  find_acc = ("SELECT * FROM accounts WHERE %(name)s = name")
  dell_acc = ('DELETE FROM accounts WHERE %(name)s = name ')
  keys = {
    'name': name
  }
  cursor.execute(find_acc,keys)
  for i in cursor:
      if i[2] == password:
        cursor.execute(dell_acc,keys)
        print("done")
        continue
      else:
        print('wrong password')
  cnx.commit()
  cursor.close()
  cnx.close()




answer = input('what do you wnat\n\
  1)Login\n\
  2)Register\n\
  3)Delete your log\n\
  Enter: ')
if answer == '1':
  name = input('your nane: ')
  password = input("your password: ")
  check_account(name,password)
elif answer == '2':
  name = input('your nane: ')
  password = input("your password: ")
  create_account(name, password)
elif answer == '3':
  name = input('your nane: ')
  password = input("your password: ")
  delete_account(name,password)
else:
  print('something was wrong')