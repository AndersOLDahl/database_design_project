import os

def delete_data(cursor, cnx):
  os.system('clear')
  print("""Would you like to do?
  1) Delete a structure
  2) Delete a room
  3) Back""")

  while True:
    c = int(raw_input("> "))
    if c  == 1:
      print("Note this will delete any rooms, houses, and bridges associated"
          " with the structure.")
      struct_id = int(raw_input("Structure id: "))
      delete_structure(cursor, cnx, struct_id)
      break
    if c == 2:
      room_id = int(raw_input("Room id: "))
      delete_room(cursor, cnx, room_id)
      break
    if c == 3:
      break

def delete_structure(cursor, cnx, structure_id):
  delete = ("DELETE FROM `project`.`Structures` WHERE structure_id=%s" % structure_id)
  cursor.execute(delete)
  cnx.commit()

def delete_room(cursor, cnx, room_id):
  delete = ("DELETE FROM `project`.`Rooms` WHERE room_id=%s" %
      room_id)
  cursor.execute(delete)
  cnx.commit()
