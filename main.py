from broker import take_one_row
from asker import ask_about, is_acheck 
from config import DAYS_BEFORE
import schedule as sh
import datetime as dt
import time as tt


def _main():
	# ask_about()
	date_list = []
	example = []

	for i in range(1,DAYS_BEFORE):
		example.append(dt.date.today()-dt.timedelta(days=i))

	info = is_acheck(DAYS_BEFORE)

	for j in range(DAYS_BEFORE-1):
		if example[j] not in info: date_list.append(example[j])

	date_list.reverse()

	for chosed_date in date_list:
		ask_about(chosed_date)

	if (dt.timedelta(hours=dt.datetime.today().time().hour) > dt.timedelta(hours=17)) and not take_one_row(0):
		ask_about()


	sh.every().day.at("18:00").do(ask_about)

	while True:
		sh.run_pending()


if __name__ == "__main__":
	_main()