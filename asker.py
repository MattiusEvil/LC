import PySimpleGUI as sg
from broker import send_to_base


def ask_about():
	time_by_trash = None


	# Window's content
	layout = [
	[sg.Text("What time do you waste today, my friend?")],
	[sg.Input(size=(40,50)),sg.Text("(0.0)h")],
	[sg.Button("Send")],
	[[sg.Button(i) for i in range(13)]]
	]

	# Create the window
	window = sg.Window('Life Checker', layout)

	# Display window
	event, values = window.read()

	if event=="Send":
		time_by_trash = test_for_adequacy(values[0])
	else:
		time_by_trash = test_for_adequacy(event)
	send_to_base(time_by_trash)
	print(time_by_trash)

	window.close() 


def test_for_adequacy(number_of_waste) -> float:
	if number_of_waste=="": return 0
	try:
		number_of_waste = float(number_of_waste)
	except:
		raise("Written number is not right!")
	return number_of_waste


