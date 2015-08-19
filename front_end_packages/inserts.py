import os

def insert_data(cursor, cnx):
  os.system('clear')
  print("""Would you like to do?
  1) Insert a bridge
  2) Insert a house
  3) Insert a room into an existing house
  4) Back""")

  while True:
    c = int(raw_input("> "))
    if c  == 1:
      cost_to_build = int(raw_input("Cost to build: "))
      year_built = int(raw_input("Year built: "))
      bridge_name = raw_input("Bridge name: ")
      bridge_type = raw_input("Bridge type: ")
      insert_bridge(cursor, cnx, cost_to_build, year_built,
          bridge_name, bridge_type)
      break
    if c == 2:
      cost_to_build = int(raw_input("Cost to build: "))
      year_built = int(raw_input("Year built: "))
      house_type = raw_input("House type: ")
      insert_house(cursor, cnx, cost_to_build, year_built,
          house_type)
      break
    if c == 3:
      room_house_id = int(raw_input("House id: "))
      room_type = raw_input("Room type: ")
      insert_room(cursor, cnx, room_house_id, room_type)
      break
    if c == 4:
      break

def __insert_structure(cursor, cost_to_build, year_built):
  add_structure = ("""INSERT INTO `project`.`Structures`
           (cost_to_build, year_built)
           VALUES
           (%s, %s)""")
  structure_data = (cost_to_build, year_built)
  cursor.execute(add_structure, structure_data)

def insert_bridge(cursor, cnx, cost_to_build, year_built, bridge_name,
    bridge_type):

  __insert_structure(cursor, cost_to_build, year_built)
  structure_id = cursor.lastrowid

  add_bridge = ("""INSERT INTO `project`.`Bridges`
           (bridge_id, bridge_name, bridge_type)
           VALUES
           (%s, %s, %s)""")
  bridge_data = (structure_id, bridge_name, bridge_type)
  cursor.execute(add_bridge, bridge_data)
  cnx.commit()

def insert_house(cursor, cnx, cost_to_build, year_built,
    house_type):

  __insert_structure(cursor, cost_to_build, year_built)
  structure_id = cursor.lastrowid

  add_house = ("""INSERT INTO `project`.`Houses`
           (house_id, house_type)
           VALUES
           (%s, %s)""")
  house_data = (structure_id, house_type)
  cursor.execute(add_house, house_data)
  cnx.commit()

def insert_room(cursor, cnx, room_house_id, room_type):

  add_room = ("""INSERT INTO `project`.`Rooms`
           (room_house_id, room_type)
           VALUES
           (%s, %s)""")
  room_data = (room_house_id, room_type)
  cursor.execute(add_room, room_data)
  cnx.commit()
