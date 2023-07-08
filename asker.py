import PySimpleGUI as sg
from broker import send_to_base, take_row, drop_table
from config import NUMBER_BUTTONS


def ask_about():
	sg.theme('SystemDefaultForReal')
	time_by_trash = None


	# Window's content
	layout = [
	[sg.Text("What time do you waste today, my friend?")],
	[sg.InputText(size=5),sg.Text("(0.0)h")],
	[sg.Button("Send")],
	[*[sg.Button(i) for i in range(NUMBER_BUTTONS)],sg.Button("Check DB")]
	]

	# Create the window
	window = sg.Window('Life Checker', layout)

	# Display window
	

	while True:
		event, values = window.read()
		# and sg.popup_yes_no("Are you sure?")=="Yes"
		if event==sg.WINDOW_CLOSED :
			print("Programm was closed.")
			return 0    									#В таблицу ничего не уходит
		elif event=="Send":
			time_by_trash = test_for_adequacy(values[0])
			break
		elif event=="Check DB":
			open_DB()
		elif event in [str(i) for i in range(NUMBER_BUTTONS)]:
			time_by_trash = test_for_adequacy(event)
			break

	send_to_base(time_by_trash)

	window.close() 


def test_for_adequacy(number_of_waste) -> float:
	if number_of_waste=="": return 0

	try:
		number_of_waste = number_of_waste.replace(",",".")
		number_of_waste = float(number_of_waste)
	except:
		raise("Written number is not right! ERROR n1")

	if number_of_waste > 24.0 or number_of_waste < 0:
		raise("Written number is not right! ERROR n2")
	return number_of_waste

def open_DB():
	if take_row():
		stg = [sg.Table(take_row()),sg.Button("Reset table")]
	else:
		sg.popup("Table is empty")
		return 0
	layout = [
	[sg.Frame('',[stg],s=(500,300))]
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


	window.close() 


