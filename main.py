import matplotlib.pyplot as plt

# Reading the csv file and storing the data in a dictionary

data = {}
new_string = ""
curr_string = ""
flag = 1

with open("Emissions.csv") as file:
	f = file.read()
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

	file.close()

data[curr_string].append(new_string)


# User Input

print("All data from Emissions.csv has been read into a dictionary.\n")
year = input("Select a year to find statistics (1997 to 2010): ")
print()


# Finding the index of the year

index = data['CO2 per capita'].index(year)


# Finding Min and Max and Average CO2 Emission Levels (CEL)

cel_list = {}

for key in data:
	if key == 'CO2 per capita':
		continue
	cel_list[key] = float(data[key][index])

min_cel = 1000000007.00
max_cel = 0.00
min_country = ""
max_country = ""
total = 0.00
avg_cel = 0.00

for item in cel_list:
	if cel_list[item] < min_cel:
		min_cel = cel_list[item]
		min_country = item
	if cel_list[item] > max_cel:
		max_cel = cel_list[item]
		max_country = item
	total = total + cel_list[item]

avg_cel = total/len(cel_list)


# Displaying Information

print(f"In {year}, countries with minimum and maximum CO2 emission levels were: \
	{min_country} and {max_country} respectively.")
print(f"Average CO2 emissions in {year} were {avg_cel}\n")


# Visualizing Data

print("Here's the list of countries: \n")
num = 1
for item in data:
	if item == 'CO2 per capita':
		continue
	print(f"{num}. {item}", end="    ")
	num += 1
print("\n")

country = input("Select the country to visualize: ")

x = data['CO2 per capita']
y = data[country]

plt.plot(x, y, color='green', marker='o', linestyle='solid',linewidth=2, markersize=12)
plt.xlabel("Year")
plt.ylabel(f"Emissions in {country}")
plt.title("Year vs Emissions in Capita")
plt.show()