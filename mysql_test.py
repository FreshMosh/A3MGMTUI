import MySQLdb

db = MySQLdb.connect(           # Create an connection object from a database \
    host="localhost",           # which is used for actions on the db later on
    db="test_db",
    user="db_user", passwd="random"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `Adressen1` (`id` int(11) NOT NULL AUTO_INCREMENT, "  # Create Database \
               "`Name` varchar(28), `Strasse` varchar(40), `PLZ` int(5), "                      # and define columns
               "`Ort` varchar(35), primary key (`id`));")
cursor.executemany("""INSERT INTO Adressen1 (Name, Strasse, PLZ, Ort)
                  VALUES (%s, %s, %s, %s)""",                # The way to insert from a tuple, awesome!!
               [ ('Dr. Hans Mustermann', 'Musterstraße 13', 50823, 'Köln'),
                 ('Peter Lustig', 'Im Bauwagen 2', 50827, 'Porz'),
                 ('Edmund Stoiber', 'Spendensumpf 1', 47011, 'Bimbesdorf'),
                 ('Onkel Hotte', 'Im Siff 42', 57072, 'Siegen'),
                 ('Gerhard Schröder', 'Großmaulweg 2', 11901, 'Worthülsen') ]
              )
db.commit()     # Important as the data will not be written without
db.close()      # disconnect from server

