# Reading the csv file and storing the data in a dictionary

with open("Emissions.csv") as file:
	f = file.read()
	data = {}
	new_string = ""
	curr_string = ""
	flag = 1
	for element in f:
		if element == ",":
			if flag:
				data[new_string] = []
				curr_string = new_string
				flag = 0
			else:
				data[curr_string].append(new_string)
			new_string = ""
			continue
		if element == "\n":
			flag = 1
			data[curr_string].append(new_string)
			new_string = ""
			continue
		new_string = new_string + element

	print(data)

	file.close()