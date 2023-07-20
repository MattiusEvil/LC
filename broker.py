import psycopg2
from psycopg2 import Error


def send_to_base(tbt, chosed_date):
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	make_db()


	cur.execute("""
	INSERT INTO times (date_of_check, time_of_hours)
	VALUES (%(bibiDate)s, %(bubuTime)s);
	""",
	({"bubuTime":tbt, "bibiDate":chosed_date}))

	conn.commit()

	cur.close()
	conn.close()
			
def take_row():
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	make_db()
	cur.execute("""
		SELECT date_of_check, time_of_hours FROM times
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

def drop_row(s_row):
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	try:
		cur.execute("""
			DELETE FROM times
			WHERE date_of_check=%(date)s and time_of_hours>%(time1)s and time_of_hours<%(time2)s
			""",
			({"date":s_row[0],"time1":s_row[1]-0.001,"time2":s_row[1]+0.001})
			)

		conn.commit()
	except (Exception, Error) as error:
		# print ("Trouble with the database work", error, sep="\n")
		pass
	finally:
		cur.close()
		conn.close()

def take_one_row(interval_from_now: int):
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()
	make_db()
	cur.execute("""
		SELECT date_of_check FROM times
		WHERE date_of_check=CURRENT_DATE - interval'%(days)s day'
		""",
		({"days":interval_from_now})
		)
	row_of_dots=cur.fetchone()
	cur.close()
	conn.close()
	return row_of_dots