import psycopg2


def send_to_base(tbt):
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()

	# cur.execute("""
	# 	CREATE TABLE times (date_of_check DATE, 
	# 		time_of_hours REAL);
	# 	""")


	cur.execute("""
		INSERT INTO times (date_of_check, time_of_hours)
		VALUES (CURRENT_DATE, %s);
		""",
		([tbt]))

	conn.commit()

	cur.close()
	conn.close()

def open_DB():
	conn = psycopg2.connect(host="localhost", port="5432", database="timekeeper",
		user="postgres", password="b7o5k3e1r9")
	cur = conn.cursor()

	cur.close()
	conn.close()