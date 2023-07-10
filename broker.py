import psycopg2
from psycopg2 import Error


def send_to_base(tbt):
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	make_db()

	cur.execute("""
	INSERT INTO times (date_of_check, time_of_hours)
	VALUES (CURRENT_DATE, %s);
	""",
	(tbt,))

	conn.commit()

	cur.close()
	conn.close()
			
def take_row():
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	make_db()

	cur.execute("""
		SELECT to_char(date_of_check,'YYYY/MM/DD'), to_char(time_of_hours,'99') FROM times
		""")
	row_of_dots=cur.fetchall()

	cur.close()
	conn.close()
	return row_of_dots


def make_db():
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	try:
		cur.execute("""
			CREATE TABLE times (
				index BIGSERIAL PRIMARY KEY,
				date_of_check DATE, 
				time_of_hours REAL);
			""")

		conn.commit()
	except (Exception, Error) as error:
		# print ("Trouble with the database work", error, sep="\n")
		pass
	finally:
		cur.close()
		conn.close()

def drop_table():
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	try:
		cur.execute("""
			DROP TABLE times;
			""")

		conn.commit()
	except (Exception, Error) as error:
		# print ("Trouble with the database work", error, sep="\n")
		pass
	finally:
		cur.close()
		conn.close()