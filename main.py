# Reading the csv file and storing the data in a dictionary

with open("Emissions.csv") as file:
	f = file.read()
	data = {}
	temp = ""
	curr = ""
	flag = 1
	for element in f:
		if element == ",":
			if flag:
				data[temp] = []
				curr = temp
				flag = 0
			else:
				data[curr].append(temp)
			temp = ""
			continue
		if element == "\n":
			flag = 1
			data[curr].append(temp)
			temp = ""
			continue
		temp = temp + element

	print(data["Albania"])

	file.close()