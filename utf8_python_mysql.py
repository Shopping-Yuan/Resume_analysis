'''
# Connect to mysql.
dbc = MySQLdb.connect(host='###', user='###', passwd='###', db='###', use_unicode=True)

# Create a cursor.
cursor = dbc.cursor()

# Enforce UTF-8 for the connection.
cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")

# Do database stuff.

# Commit data.
dbc.commit()

# Close cursor and connection.
cursor.close()
dbc.close()
'''