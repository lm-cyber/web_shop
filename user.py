# import psycopg2
 # conn = psycopg2.connect(dbname='docker', user='docker', password='docker', host='localhost')
#
# def test_db():
# 	cursor = conn.cursor()
# 	cursor.execute("SELECT * FROM accounts")
# 	s = ''
# 	for i in cursor:
# 		s += str(i)
# 	cursor.close()
# 	return s


# @app.route("/db/")
# def db_rest():
# 	return test_db()
