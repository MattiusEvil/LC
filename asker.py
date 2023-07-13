import PySimpleGUI as sg
from broker import send_to_base, take_row, drop_table, drop_row
from config import BUT_NUMBER_SSS, HEADINGS


def test_ask_about():
	sg.theme('SystemDefaultForReal')
	time_by_trash = None


	# Window's content
	layout = [
	[sg.Text("What time do you waste today, my friend?")],
	[sg.InputText(size=5),sg.Text("(00:00) hours:minutes")],
	[sg.Button("Send")],
	[*[sg.Button(i) for i in BUT_NUMBER_SSS],sg.Button("Check DB")]
	]

	# Create the window
	window = sg.Window('Life Checker', layout)

	# Display window
	

	while True:
		event, values = window.read()
		if event==sg.WINDOW_CLOSED :
			print("Programm was closed.")
			return 0    									#В таблицу ничего не уходит
		elif event=="Send":
			time_by_trash = test_for_adequacy(values[0])
			send_to_base(time_by_trash)
			# break
		elif event=="Check DB":
			open_DB()
		elif event in [i for i in BUT_NUMBER_SSS]:
			time_by_trash = test_for_adequacy(event)
			send_to_base(time_by_trash)
			# break

	# send_to_base(time_by_trash)

	window.close() 

def ask_about():
	sg.theme('SystemDefaultForReal')
	time_by_trash = None


	# Window's content
	layout = [
	[sg.Text("What time do you waste today, my friend?")],
	[sg.InputText(size=5),sg.Text("(00:00) hours:minutes")],
	[sg.Button("Send")],
	[*[sg.Button(i) for i in BUT_NUMBER_SSS],sg.Button("Check DB")]
	]

	# Create the window
	window = sg.Window('Life Checker', layout)

	# Display window
	

	while True:
		event, values = window.read()
		if event==sg.WINDOW_CLOSED :
			print("Programm was closed.")
			return 0    									#В таблицу ничего не уходит
		elif event=="Send":
			time_by_trash = test_for_adequacy(values[0])
			break
		elif event=="Check DB":
			open_DB()
		elif event in [i for i in BUT_NUMBER_SSS]:
			time_by_trash = test_for_adequacy(event)
			break

	send_to_base(time_by_trash)

	window.close() 


def open_DB():
	if take_row():
		list_of_rows = make_format_rows(take_row())
		l_i_g = []
		for i in range(len(list_of_rows)):
			if (test_for_adequacy(list_of_rows[i][1])) <= 0.3: l_i_g.append(i)
		stg1 = [
		[sg.Table(list_of_rows,
			row_colors=[tuple([i,"#00ff00"]) for i in l_i_g], 
			headings=HEADINGS,
			key='-CLICK-',
			enable_events=True
			)]
		
		]
		stg2 = [
		[sg.Button("Reset table", s = (10, 5))],
		[sg.Button("Delete line", disabled=True)]
		]
	else:
		sg.popup("Table is empty")
		return 0
	layout = [
	[sg.Frame('',stg1,s=(900,600)),sg.Frame('',stg2,s=(200,300))]
	]

	# Create the window
	window = sg.Window('Life Checker', layout)

	# Display window
	while True:
		event, values = window.read()
		if event==sg.WINDOW_CLOSED :
			return 0
		elif event=="Reset table":
			drop_table()
			sg.popup("Table was cleared")
			break
		elif event=="-CLICK-":
			spec_row = take_row()[values["-CLICK-"][0]]
			window['Delete line'].update(disabled=False)
			pass
		elif event=="Delete line":
			drop_row(spec_row)
			sg.popup("Row was cleared")
			break


	window.close() 



def test_for_adequacy(number_of_waste) -> float:
	if number_of_waste=="": return 0

	try:
		number_of_waste = number_of_waste.replace(",",".").replace(":",".")
		for i in range(10):
			if number_of_waste == f"0.{i}": number_of_waste = f"0.0{i}"
		number_of_waste = float(number_of_waste)
	except:
		raise("Written number is not right! ERROR n1")

	if number_of_waste > 24.0 or number_of_waste < 0:
		raise("Written number is not right! ERROR n2")
	return number_of_waste

def make_format_rows(rows):
	new_list = []
	for i in rows:
		datec = str(i[0])
		timec = str(i[1])
		for i in range(10):
			if timec == f"0.{i}": timec = f"0.{i}0"
		timec = timec.replace('.',':')
		new_list.append([datec, timec])
	return new_list
