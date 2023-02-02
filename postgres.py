



import psycopg2
conn = psycopg2.connect(dbname='docker', user='docker', 
                        password='docker', host='localhost')
cursor = conn.cursor()


# cursor.execute("CREATE TABLE accounts (\
	# user_id serial PRIMARY KEY,\
	# username VARCHAR ( 50 ) UNIQUE NOT NULL,\
	# password VARCHAR ( 50 ) NOT NULL\
    # );")

# conn.commit()
# cursor.execute("INSERT INTO accounts (username, password)\
    # VALUES (\'1232132\', \'v1233alue3\');")

# conn.commit()


cursor.execute("SELECT * FROM accounts")


for i in cursor:
	print(i)


