from power_plant import Solar_Power_Plant, Wind_Power_Plant
import math
import types
import sys
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk

class CustomDialog:

    def __init__(self, parent, message_box_title_list):

        top = self.top = Toplevel(parent)
        for title in message_box_title_list:

        	Label(top, text=title).pack()

        	self.e = Entry(top)
        	self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print ("value is", self.e.get())
        self.top.destroy()

month_day_dict = {0: "January", 30: "February", 60: "Mars", 90: "April", 120:"May", 150: "June",
					180: "July", 210:"August", 240:"September", 270:"October", 300:"November", 330:"December"}
month_number_dict = {0: "January", 1: "February", 2: "Mars", 3: "April", 4:"May", 5: "June",
					6: "July", 7:"August", 8:"September", 9:"October", 10:"November", 11:"December"}
def calculate_mean_value(energy_production_list):

	return sum(energy_production_list)/len(energy_production_list)

def calculate_standard_deviation(energy_production_list):
	total = 0
	for i in energy_production_list:
		total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
	return math.sqrt((1/(len(energy_production_list)-1))*total)

def main_menu():
	#root = Tk()
	#solar_button = Button(root, text="Solar")
	#wind_button = Button(root, text="Wind")
	#solar_button.grid(row =0, column=0)
	#wind_button.grid(row=1, column=1)

	#solar or wind 0 or 1
	#solar_button.configure(command=lambda: button_pressed(2, root))
	#wind_button.configure(command=lambda: button_pressed(3))

	#solar_button.pack()
	#wind_button.pack()

	#root.mainloop()

	#wind_power_plant_calculation()
	running = True
	while(running):
		print("Welcome to Solar and Wind power plant simulator, what would you like to simulate?")

		arg = user_input_int_handler("1. Solar Power Plant \n2. Wind Power Plant\n3. Quit", 1,3)

		if arg == 1:
			number_of_latitudes = user_input_int_handler("How many latitudes do you want to calculate?", 0, sys.maxsize)
			latitude_list = []
			for latitudes in range(number_of_latitudes):
				latitude = user_input_float_handler("Enter a latitude: ", 0, 90)
				latitude_list.append(latitude)
			area = user_input_float_handler("Enter the area: ", 0, 1000) #max 1000m^2
			material_constant = user_input_float_handler("Enter material constant: ", 0, 10) #max 10kWh/m^2
			solar_plant = Solar_Power_Plant(area, material_constant, latitude_list)
			power_calculation(solar_plant)
		elif arg == 2:
			rotor_diameter = user_input_float_handler("Enter rotor diameter: ", 25, 50) #min 25, max 50
			wind_power_plant = Wind_Power_Plant(rotor_diameter)
			power_calculation(wind_power_plant)
		elif arg == 3:
			running = False
#def button_pressed(arg, root):
#	print (arg)
#	d = CustomDialog(root, ["stuff", "more stuff"])



def power_calculation(power_plant):
	power_plant_dict= {}
	power_plant_dict = power_plant.energy_calculator()
	energy_production_list = []
	for key in power_plant_dict:
		day_data_list = power_plant_dict[key]
		for day_data_tuple in day_data_list:
			energy_production_list.append(day_data_tuple[1])

	running = True
	while running:
		print("What do you want to do with the simulated data?")
		arg = user_input_int_handler("1. Create a table \n2. Create a bar chart \n3. Save to file \n4. Go to main menu (data will be lost)", 1,4)
		print (type(power_plant).__name__)
		if type(power_plant).__name__ == "Solar_Power_Plant" and (arg == 1 or arg == 2):
			print ("Latitudes: ")
			index = 1
			for key in power_plant_dict:
				print(index, ". ", key)

			latitude = user_input_int_handler("Which latitude do you want to display? ", 1, index)
			
			#Tuple with monthly data (max,min,mean,normal deviation)
			energy_tuple = energy_produced_per_month(power_plant, energy_production_list)

			if arg == 2:
				display_bar_graph(energy_tuple)

			elif arg == 1:
				display_table(energy_tuple)
		elif arg == 1 or arg == 2:
			#Tuple with monthly data (max,min,mean,normal deviation)
			energy_tuple = energy_produced_per_month(power_plant, energy_production_list)

			if arg == 2:
				display_bar_graph(energy_tuple)

			elif arg == 1:
				display_table(energy_tuple)
		elif arg == 3:
			file_name = input("Enter a file name: ")
			save_file(power_plant_dict, power_plant, file_name)
		elif arg == 4:
			return

def display_bar_graph(energy_tuple):
	
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
		canvas.create_text(x1-20, y1+15, anchor=tk.SW, text=month_number_dict[x][0:3])
	root.mainloop()

def display_table(energy_tuple):
	root = tk.Tk()
	root.title("Power Production Table")
	table = Table(root, 13, 5)
	table.pack(side ="top", fill="x")
	table.set(0,0, "Month")
	table.set(0,1, "Mean Value")
	table.set(0,2, "Standard deviation")
	table.set(0,3, "Min value")
	table.set(0,4, "Max value")
	
	
	for index in range(12):
		table.set(index+1, 0, month_number_dict[index])
		table.set(index+1, 1, str("%.4f" % round(energy_tuple[2][index],4)))
		table.set(index+1, 2, str("%.4f" % round(energy_tuple[3][index], 4)))
		table.set(index+1, 3, str("%.4f" % round(energy_tuple[1][index], 4)))
		table.set(index+1, 4, str("%.4f" % round(energy_tuple[0][index], 4)))

def energy_produced_per_month(power_plant, energy_production_list):
	max_list = []
	min_list = []
	month_mean_value_list = []
	month_standard_deviation_list = []
	max_value = 0
	min_value = 0
	time = 1
	for energy_produced in energy_production_list:

		if energy_produced >= max_value:
			max_value = energy_produced
	
		elif energy_produced <= min_value:
			min_value = energy_produced

		if (time%30)==0 and time != 0:
			month_mean_value_list.append(calculate_mean_value(energy_production_list[time-30:time]))
			month_standard_deviation_list.append(calculate_standard_deviation(energy_production_list[time-30:time]))
				
			min_list.append(min_value)
			max_list.append(max_value)
			max_value = 0
			min_value = 0	
		time +=1
	return (max_list, min_list, month_mean_value_list, month_standard_deviation_list)

def save_file(power_plant_dict, power_plant, file_name):
	column_headers = power_plant.capabilities()
	data = column_headers + "\n"
	for identifier in power_plant_dict: #for solar this is latitude
		day_data_list = power_plant_dict[identifier]
		for day_data_tuple in day_data_list:
			
			day = day_data_tuple[0]
			energy_produced = day_data_tuple[1]

			if (day% 30) == 0:
				data += (month_day_dict[day]+"\n")

			if len(day_data_tuple) == 4:
				wind_variation = day_data_tuple[2]
				rotor_diameter = day_data_tuple[3]
				data += (str(rotor_diameter) + "\t" + str(day) + "\t" + str(energy_produced) + "\t" + str(wind_variation) + "\n")

			elif len(day_data_tuple) == 6:	
				area = day_data_tuple[2]
				material_constant = day_data_tuple[3]
				sun_factor = day_data_tuple[4]
				latitude = day_data_tuple[5]
				energy_function = day_data_tuple[6]

				data += (str(area) +"\t" + str(material_constant) +"\t" + str(latitude) +"\t" + str(sun_factor) +"\t" + str(energy_produced) +"\t" + str(energy_function) + "\n")
	file = open(file_name, "w")

	file.write(data)
	file.close()
			

def user_input_int_handler(prompt, lower_lim, upper_lim):
	while True:
		try:
			user_input = int(input(prompt))
			if user_input > upper_lim or user_input < lower_lim:
				print("Wrong choice: try again")
				continue
			return user_input
		except:
			print("This is no interger, try again: ")

def user_input_float_handler(prompt, lower_lim, upper_lim):
	while True:
		try:
			user_input = float(input(prompt))
			if user_input > upper_lim or user_input < lower_lim:
				print("Wrong choice: try again")
				continue

			return user_input
		except:
			print("This is no float, try again: ")

class Table(tk.Frame):
	def __init__(self, parent, rows=12, columns=5):
		tk.Frame.__init__(self, parent, background="black")
		self._widgets = []
		#self.bind_all("<control-q>", self.quit)
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
		widget = self._widgets[row][column]
		widget.configure(text=value)

main_menu()





		
