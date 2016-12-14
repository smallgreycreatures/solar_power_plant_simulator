"""Author=Frans Nordén, Date=2016-12-14"""

from power_plant import Solar_Power_Plant, Wind_Power_Plant
import math
import types
import sys
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk

""" The main data structure is the power_plant_dict. This is a dictionary where each element (for solar power plants) is a latitude. 
		Each latitude holds a list of days where each day list contains a tuple per day on 
		the form (time, energy_produced, area, material_constant, sun_factor, latitude, latitude_time function value)

		For wind power plants the dictionary just contains one entry with key 0.
		This element is a list of all days where each day is represented as a tuple of
		the form(time, energy_produced,wind_variation, rotor_diameter)
		"""

def get_month_by_day_number(day_number):
	"""Connects a day number to a day. Simplified to 30 days per month"""
	month_day_dict = {0: "January", 30: "February", 60: "Mars", 90: "April", 120:"May", 150: "June",
					180: "July", 210:"August", 240:"September", 270:"October", 300:"November", 330:"December"}
	return month_day_dict[day_number]

def get_month_by_number(month_number):
	"""Connects the month number to the month name"""
	month_number_dict = {0: "January", 1: "February", 2: "Mars", 3: "April", 4:"May", 5: "June",
					6: "July", 7:"August", 8:"September", 9:"October", 10:"November", 11:"December"}
	return month_number_dict[month_number]

def calculate_mean_value(energy_production_list):
	"""Calculates mean value. sum of the list / lenght of list"""
	return sum(energy_production_list)/len(energy_production_list)

def calculate_standard_deviation(energy_production_list):
	"""Calculates standard deviation of the energy in energy production list"""
	total = 0
	for i in energy_production_list:
		total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
	return math.sqrt((1/(len(energy_production_list)-1))*total)

def main_menu():
	"""Program main menu with a while loop that asks the user for input"""
	running = True
	while(running):
		print("Welcome to Solar and Wind power plant simulator, what would you like to simulate?")

		arg = user_input_int_handler("1. Solar Power Plant \n2. Wind Power Plant\n3. Quit", 1,3)

		if arg == 1: #Solar plant is choosen
			number_of_latitudes = user_input_int_handler("How many latitudes do you want to calculate?", 0, sys.maxsize)
			
			#stores inputed latitudes
			latitude_list = []
			for latitudes in range(number_of_latitudes):
				latitude = user_input_float_handler("Enter a latitude (0<latitude<90): ", 0, 90, False)
				latitude_list.append(latitude)

			area = user_input_float_handler("Enter the area (0<area<1000) in square meter: ", 0, 1000, False) #max 1000m^2
			material_constant = user_input_float_handler("Enter material constant (0<constant<10): ", 0, 10, False) #max 10kWh/m^2
			solar_plant = Solar_Power_Plant(area, material_constant, latitude_list)
			power_calculation(solar_plant)

		elif arg == 2: #Wind power plant choosen
			rotor_diameter = user_input_float_handler("Enter rotor diameter(25<=diameter<=50): ", 25, 50, True) #min 25, max 50
			wind_power_plant = Wind_Power_Plant(rotor_diameter)
			power_calculation(wind_power_plant)

		elif arg == 3: #Exit application
			running = False

def extract_energy_production_list(power_plant_dict, latitude):
	"""Extracts the energy production list from the power plant dict for
		a given latitude (latitude 0 for wind plants)
		Returns a list of the energy produced per day where the day is the index"""
	energy_production_list = []

	#extracting the energy produced per day from the dict. First step is extracting a list
	day_data_list = power_plant_dict[latitude]
	for day_data_tuple in day_data_list:
		#For each tuple in the list (per day) there are produced energy stored at [1]
		energy_production_list.append(day_data_tuple[1])

	return energy_production_list

def selectionSort(alist, b):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]<alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		temp2 = b[fillslot]
		alist[fillslot] = alist[positionOfMax]
		b[fillslot] = b[positionOfMax]
		alist[positionOfMax] = temp
		b[positionOfMax] = temp2
	print(alist)
	print(b)

def bubblesort_for_two_lists(A, B):
	"""Simple sorting algorithm for two lists. Takes List A and B as input
	and sorts decreasing order list A and keeps track of the elements of B so that the
	elements on index i in both lists gets index j in both lists when sorted.
	http://www.geekviewpoint.com/python/sorting/bubblesort""" 
	for i in range( len( A ) ):
		for k in range( len( A ) - 1, i, -1 ):
			if ( A[k] > A[k - 1] ):
				swap( A, B, k, k - 1 )
 
def swap( A, B, x, y ):
	"""Help function for bubblesort, swaps numbers at index x, y in lists A and B"""
	tmp = A[x]
	tmp2 = B[x]
	A[x] = A[y]
	B[x] = B[y]
	A[y] = tmp
	B[y] = tmp2	

def power_calculation(power_plant):
	"""Calls the energy_calculator function for the parameter power plant and asks the user if it want to save data, generate a bar graph, a table or quit"""
	#stores all lists generated by energy calculator.
	power_plant_dict= {}
	power_plant_dict = power_plant.energy_calculator()

	running = True
	while running:
		print("What do you want to do with the simulated data?")
		arg = user_input_int_handler("1. Create a table \n2. Create a bar chart \n3. Save to file \n4. Go to main menu (data will be lost)", 1,4)

		if type(power_plant).__name__ == "Solar_Power_Plant" and (arg == 1 or arg == 2):
			if arg == 1:
				row_list = []
				mean_value_of_energy_over_a_year_list = []
				for latitude in power_plant_dict:
					energy_production_list = extract_energy_production_list(power_plant_dict, latitude)
					mean_value_of_energy_over_a_year = calculate_mean_value(energy_production_list)
					row_list.append(latitude)
					mean_value_of_energy_over_a_year_list.append(mean_value_of_energy_over_a_year)
				list_of_column_headers = ["Latitude", "Mean value"]
				bubblesort_for_two_lists(mean_value_of_energy_over_a_year_list, row_list)
				energy_matrix = []
				energy_matrix.append(mean_value_of_energy_over_a_year_list)
				display_table(energy_matrix, len(list_of_column_headers), len(row_list)+1, list_of_column_headers, row_list, "Energy Comparision Table")
				continue

			elif arg == 2:
				print ("Latitudes: ")
				index = 1
				#store the index number connected to latitude
				dict_keys = []
				for key in power_plant_dict:
					print(index, ". ", key)
					dict_keys.append(key)
					index +=1

				latitude = dict_keys[user_input_int_handler("Which latitude do you want to display? ", 1, index)-1]

				#Energy produced from the power plant dict for given latitude
				energy_production_list = extract_energy_production_list(power_plant_dict, latitude)

				#Tuple with monthly data (max,min,mean,normal deviation)
				energy_tuple = energy_produced_per_month(power_plant, energy_production_list)


				display_bar_graph(energy_tuple)

		elif arg == 1 or arg == 2: #if not solar power plant and bar chart or table
			#Energy produced from the power plant dict.
			energy_production_list = extract_energy_production_list(power_plant_dict, 0)

			#Tuple with monthly data (max,min,mean,normal deviation)
			energy_matrix = energy_produced_per_month(power_plant, energy_production_list)

			if arg == 2:
				display_bar_graph(energy_matrix)

			elif arg == 1:
				list_of_column_headers = ["Month", "Max value", "Min value", "Mean Value", "Standard deviation"]
				list_of_row_headers = []
				for i in range(0,12):
					list_of_row_headers.append(get_month_by_number(i))

				display_table(energy_matrix, len(list_of_column_headers), len(list_of_row_headers)+1, list_of_column_headers, list_of_row_headers, "Energy Produced Per Month Table")


		elif arg == 3:#save to file
			file_name = input("Enter a file name: ")
			save_file(power_plant_dict, power_plant, file_name)
		elif arg == 4:
			return

def display_bar_graph(energy_tuple):
	"""Generates a bar graph with tkinter through a number of rectangels dependent of the number of months.
	Takes an tuple of the form (power_plant object, list of energy produced per month)"""

	#Gets the mean values
	data = energy_tuple[2]

	root = tk.Tk()
	root.title("Power Production Bar Graph")
	canvas_width = 600
	canvas_height = 350
	canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg = 'white')
	canvas.pack()

	y_stretch = 0.1
	y_gap = 10
	x_stretch = 10
	x_width = 20
	x_gap = 100
	for x, y in enumerate(data): #Calculates the rectangle coordinates for each bar
		x0 = x*x_stretch + x*x_width + x_gap #Bottom left
		y0 = canvas_height - (y * y_stretch + y_gap) # top left
		x1 = x * x_stretch + x*x_width + x_width + x_gap # bottom right
		y1 = canvas_height - y_gap #top right
		canvas.create_rectangle(x0, y0, x1, y1, fill="red")
		canvas.create_text(x0-10, y0, anchor=tk.SW, text=str("%.1f" % round(y,1)))
		canvas.create_text(x1-20, y1+15, anchor=tk.SW, text=get_month_by_number(x)[0:3])
	root.mainloop()

def display_table(data_matrix, columns, rows, list_of_column_headers, list_of_row_headers, table_name):
	"""Displays an ColumnXrows table. data_matrix is a list of list containing the content of the table.
	columns is number of columns, rows, nr of rows, list_of_column_headers are a list of col headers,
	list_of_row_headers a list of row headers and table_name the name of the table"""

	root = tk.Tk()
	root.title(table_name)
	table = Table(root, rows, columns)
	table.pack(side ="top", fill="x")
	#Sets the col headers 
	for index, header in enumerate(list_of_column_headers):
		table.set(0,index, header)

	#Sets the row headers 
	for row, header in enumerate(list_of_row_headers):
		table.set(row+1, 0, header)
		for col_num, list_in_matrix in enumerate(data_matrix):
			table.set(row+1, col_num+1, str("%.4f" %round(list_in_matrix[row],4)))	

def energy_produced_per_month(power_plant, energy_production_list):
	"""Returns a tuple with monthly data (max,min,mean,normal deviation) from the energy produced per day. 
	Takes the power plant object and a list of energy produced per day as parameters."""

	#List for monthly max value
	max_list = []
	#List for monthly min value
	min_list = []
	#List for monthly mean value
	month_mean_value_list = []
	#List for monthly standard deviation
	month_standard_deviation_list = []
	max_value = 0
	min_value = 0
	time = 1

	for energy_produced in energy_production_list:

		if energy_produced >= max_value:
			max_value = energy_produced
	
		elif energy_produced <= min_value:
			min_value = energy_produced

		if (time%30)==0 and time != 0: #Divide per month (30 days)
			month_mean_value_list.append(calculate_mean_value(energy_production_list[time-30:time]))
			month_standard_deviation_list.append(calculate_standard_deviation(energy_production_list[time-30:time]))
				
			min_list.append(min_value)
			max_list.append(max_value)
			max_value = 0
			min_value = 0	
		time +=1

	return (max_list, min_list, month_mean_value_list, month_standard_deviation_list)

def save_file(power_plant_dict, power_plant, file_name):
	"""Saves file with name as parameter file_name on the form defined in power_plant.capabilities().
	Takes the power_plant_dict dictionary and an power_plant object as input parameters."""

	column_headers = power_plant.capabilities()
	data = column_headers + "\n"
	for identifier in power_plant_dict: #for solar this is latitude, wind 0
		day_data_list = power_plant_dict[identifier]

		for day_data_tuple in day_data_list:
			day = day_data_tuple[0]
			energy_produced = day_data_tuple[1]

			if (day% 30) == 0:
				data += (get_month_by_day_number(day)+"\n")

			if len(day_data_tuple) == 4: #Customization for wind power plants
				wind_variation = day_data_tuple[2]
				rotor_diameter = day_data_tuple[3]
				data += (str(rotor_diameter) + "\t" + str(day) + "\t" + str(energy_produced) + "\t" + str(wind_variation) + "\n")

			elif len(day_data_tuple) == 7:	#Customization for solar plant
				area = day_data_tuple[2]
				material_constant = day_data_tuple[3]
				sun_factor = day_data_tuple[4]
				latitude = day_data_tuple[5]
				energy_function = day_data_tuple[6]
				#print("in like flynn")
				data += (str(area) +"\t" + str(material_constant) +"\t" + str(latitude) +"\t" + str(sun_factor) +"\t" + str(energy_produced) +"\t" + str(energy_function) + "\n")
			
	file = open(file_name, "w")
	file.write(data)
	file.close()
			
def user_input_int_handler(prompt, lower_lim, upper_lim):
	""" Cleans user input for ints. A upper limit and lower limit of numbers allowed are also set
	params are prompt with text to user, lower_lim: the lower limit of the number allowed, upper_lim: upper limit of numbers allowed"""
	while True:
		try:
			user_input = int(input(prompt))
			if user_input > upper_lim or user_input < lower_lim:
				print("Wrong choice: try again")
				continue
			return user_input
		except:
			print("This is no interger, try again: ")

def user_input_float_handler(prompt, lower_lim, upper_lim, greq):
	""" Cleans user input for floats. A upper limit and lower limit of numbers allowed are also set
	params are prompt with text to user, lower_lim: the lower limit of the number allowed, upper_lim: upper limit of numbers allowed
	and greq is true or false dependent on you want greater or equal or greater than on upper and lower lim."""
	while True:
		try:
			user_input = float(input(prompt))
			if (user_input >= upper_lim or user_input <= lower_lim) and not greq:
				print("Wrong choice: try again")
				continue

			elif (user_input > upper_lim or user_input < lower_lim) and greq:
				print("Wrong choice: try again")
				continue	

			return user_input
		except:
			print("This is no float, try again: ")


class Table(tk.Frame):
	"""Specialized class for tkinter to handle tables. Creates one row as a list of labels which enables change."""
	def __init__(self, parent, rows=12, columns=5):
		"""constructor for the tkinter table, generates rows and columns. takes
		the parent container, number of rows and number of columns as parameters"""
		tk.Frame.__init__(self, parent, background="black")
		self._widgets = []
		self.bind("<Control-q>", self.quit)

		for row in range(rows):
			current_row = []
			for column in range(columns):
				label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=15)
				label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
				current_row.append(label)

			self._widgets.append(current_row)
		for column in range(columns):
			self.grid_columnconfigure(column, weight=1)

	
	def set(self, row, column, value):
		"""Makes it possible to set values in the cells
		takes in tkinter widgets identified as row and column in the table and the 
		value you want to fill the [row][column] with."""
		widget = self._widgets[row][column]
		widget.configure(text=value)

main_menu()


		
