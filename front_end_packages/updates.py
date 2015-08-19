import os

def update_data(cursor, cnx):
  os.system('clear')
  print("""Would you like to do?
  1) Update the cost to build a structure
  2) Update the year built for a structure
  3) Update a bridge's name
  4) Update a bridge's type
  5) Update a house's type
  6) Update a room's type
  7) Back""")

  while True:
    c = int(raw_input("> "))
    if c  == 1:
      struct_id = int(raw_input("Structure id: "))
      cost_to_build = int(raw_input("Cost to build: "))
      update_cost_to_build(cursor, cnx, struct_id, cost_to_build)
      break
    if c == 2:
      struct_id = int(raw_input("Structure id: "))
      year_built = int(raw_input("Year built: "))
      update_year_built(cursor, cnx, struct_id, year_built)
      break
    if c == 3:
      struct_id = int(raw_input("Structure id/bridge id: "))
      bridge_name = raw_input("Bridge name: ")
      update_bridge_name(cursor, cnx, struct_id, bridge_name)
      cnx.commit()
      break
    if c == 4:
      struct_id = int(raw_input("Structure id/bridge id: "))
      bridge_type = raw_input("Bridge type: ")
      update_bridge_type(cursor, cnx, struct_id, bridge_type)
      break
    if c == 5:
      struct_id = int(raw_input("Structure id/house id: "))
      house_type = raw_input("House type: ")
      update_house_type(cursor, cnx, struct_id, house_type)
      break
    if c == 6:
      room_id = int(raw_input("Room id: "))
      room_type = raw_input("Room type: ")
      update_room_type(cursor, cnx, room_id, room_type)
      break
    if c == 7:
      break

def update_cost_to_build(cursor, cnx, structure_id, cost_to_build):
  cursor.execute ("""
  UPDATE `project`.`Structures` S
  SET cost_to_build=%s
  WHERE S.structure_id=%s
  """, (cost_to_build, structure_id))
  cnx.commit()

def update_year_built(cursor, cnx, structure_id, year_built):
  cursor.execute ("""
  UPDATE `project`.`Structures` S
  SET year_built=%s
  WHERE S.structure_id=%s
  """, (year_built, structure_id))
  cnx.commit()

def update_bridge_name(cursor, cnx, structure_id, bridge_name):
  cursor.execute ("""
  UPDATE `project`.`Bridges` B
  SET bridge_name=%s
  WHERE B.bridge_id=%s
  """, (bridge_name, structure_id))
  cnx.commit()

def update_bridge_type(cursor, cnx, structure_id, bridge_type):
  cursor.execute ("""
  UPDATE `project`.`Bridges` B
  SET bridge_type=%s
  WHERE B.bridge_id=%s
  """, (bridge_type, structure_id))
  cnx.commit()

def update_house_type(cursor, cnx, structure_id, house_type):
  cursor.execute ("""
  UPDATE `project`.`Houses` H
  SET house_type=%s
  WHERE H.house_id=%s
  """, (house_type, structure_id))
  cnx.commit()

def update_room_type(cursor, cnx, room_id, room_type):
  cursor.execute ("""
  UPDATE `project`.`Rooms` R
  SET room_type=%s
  WHERE R.room_id=%s
  """, (room_type, room_id))
  cnx.commit()
