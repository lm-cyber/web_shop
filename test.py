from flask import Flask, render_template
import psycopg2
conn = psycopg2.connect(dbname='docker', user='docker', password='docker', host='localhost')

def test_db():
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM accounts")
	s = ''
	for i in cursor:
		s += str(i)
	cursor.close()
	return s

app = Flask(__name__)

@app.route("/db/")
def db_rest():
	return test_db()
@app.route("/")
def test():
    return render_template("index.html")

@app.route("/image/")
def image():
	return render_template("image.html")



if __name__ == "__main__":
    app.run(debug=True)
