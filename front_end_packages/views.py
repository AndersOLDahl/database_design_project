import os

def view_data(cursor):
  os.system('clear')
  print("""Would you like to do?
  1) Query all data
  2) Query all structures
  3) Query all bridges
  4) Query all houses
  5) Query all rooms
  6) Back""")

  while True:
    c = int(raw_input("> "))
    if c  == 1:
      query_all(cursor)
      raw_input("Press enter to continue...")
      break
    if c == 2:
      query_structures(cursor)
      raw_input("Press enter to continue...")
      break
    if c == 3:
      query_bridges(cursor)
      raw_input("Press enter to continue...")
      break
    if c == 4:
      query_houses(cursor)
      raw_input("Press enter to continue...")
      break
    if c == 5:
      query_rooms(cursor)
      raw_input("Press enter to continue...")
      break
    if c == 6:
      break

def query_all(cursor):
  query_bridges(cursor)
  print('-----')
  query_houses(cursor)
  print('-----')
  query_rooms(cursor)

def query_structures(cursor):
  query_bridges(cursor)
  print('-----')
  query_houses(cursor)

def query_bridges(cursor):
  query = ("""
  SELECT  S.structure_id,
          S.cost_to_build,
          S.year_built,
          B.bridge_name,
          B.bridge_type
  FROM    `project`.`Structures` S
          INNER JOIN `project`.`Bridges` B
              ON  S.structure_id = B.bridge_id
  """)
  cursor.execute(query)

  print("BRIDGES: \n")
  for (structure_id, cost_to_build, year_built, bridge_name,
      bridge_type) in cursor:
    print("""Structure Id: {}
Cost To Build: {}
Year Built: {}
Bridge Name: {}
Bridge Type: {}
    """).format(structure_id, cost_to_build, year_built, bridge_name,
    bridge_type)

def query_houses(cursor):
  query = ("""
  SELECT  S.structure_id,
          S.cost_to_build,
          S.year_built,
          H.house_type
  FROM    `project`.`Structures` S
          INNER JOIN `project`.`Houses` H
              ON  S.structure_id = H.house_id
  """)
  cursor.execute(query)

  print("HOUSES: \n")
  for (structure_id, cost_to_build, year_built, house_type) in cursor:
    print("""Structure Id: {}
Cost To Build: {}
Year Built: {}
House Type: {}
    """).format(structure_id, cost_to_build, year_built, house_type)

def query_rooms(cursor):
  query = ("""
  SELECT  H.house_id,
          R.room_type
  FROM    `project`.`Houses` H
          LEFT JOIN `project`.`Rooms` R
              ON  H.house_id = R.room_house_id
  """)
  cursor.execute(query)

  print("ROOMS: \n")
  for (house_id, room_type) in cursor:
    print("House Id: {} \n"
    "Room Type: {} \n".format(house_id, room_type))
