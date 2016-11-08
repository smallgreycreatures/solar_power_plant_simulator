
import random
import math
from tkinter import *
import plotly
class Power_Plant(object):



	
	def collect_month_information(self, energy_produced, max_value, min_value, time, energy_production_list, month_mean_value_list, month_standard_deviation_list, min_list, max_list):
		if energy_produced >= max_value:
			max_value = energy_produced

		elif energy_produced <= min_value:
			min_value = energy_produced

		if (time%30)==0 and time != 0:
			month_mean_value_list.append(self.calculate_mean_value(energy_production_list[time-30:time]))
			month_standard_deviation_list.append(self.calculate_standard_deviation(energy_production_list[time-30:time]))
				
			min_list.append(min_value)
			max_list.append(max_value)
			max_value = 0
			min_value = 0


class Solar_Power_Plant(Power_Plant):

	def __init__(self, area, material_constant, latitude_list):
		self.area = area
		self.material_constant = material_constant
		self.latitude_list = latitude_list
	
	def get_area(self):
		return self.area

	def get_material_constant(self):
		return self.material_constant
	def solar_energy_calculator(self, sun_factor, time, latitude):
		latitude_time = self.latitude_time(time, latitude)
		return (self.get_area()*self.get_material_constant()*sun_factor*latitude_time, latitude_time)

	def latitude_time(self, time, latitude):
		#0<latitude<90
		v = (23.5*math.sin((math.pi*(time-80))/180) + 90 - latitude)/90
		if v > 0 and v < 1:
			return v*v
		elif v >= 1:
			return 1
		else: #v < 0
			return 0

	def energy_caluclator(self):
		latitude_dict = {}

	#latitude_list.append(lat_2)
		for latitude in self.latitude_list:
			
			energy_production_list = []
			month_mean_value_list =[]
			month_standard_deviation_list = []
			#stores data from each day. One tuple per index(day) (Area, material constant, sun factor, latitude, W, f(t,lat))
			day_list = []

			max_value = 0
			min_value = 0
			#Index identifies month, value identifies actual value.
			max_list = []
			min_list = []

			for time in range(360):
				sun_factor = random.random()


				energy_produced_tuple = self.solar_energy_calculator(sun_factor, time, latitude)
				energy_produced = energy_produced_tuple[0]
				energy_production_list.append(energy_produced)
				day_list.append((time, energy_produced, self.get_area(), self.get_material_constant(), sun_factor, latitude, energy_produced_tuple[1]))
			latitude_dict[latitude] = day_list
		'''	if energy_produced >= max_value:
				max_value = energy_produced

			elif energy_produced <= min_value:
				min_value = energy_produced

			if (time%30)==0 and time != 0:
				print (time)
				month_mean_value_list.append(super().calculate_mean_value(energy_production_list[time-30:time]))
				month_standard_deviation_list.append(super().calculate_standard_deviation(energy_production_list[time-30:time]))
				
				min_list.append(min_value)
				max_list.append(max_value)
				max_value = 0
				min_value = 0

		mean_value = super().calculate_mean_value(energy_production_list)
		standard_deviation = super().calculate_standard_deviation(energy_production_list)'''
		return latitude_dict

	def capabilities(self):
		return "Area,soltal,latitud,dag,solighetsfaktor,f(t,latitud),W(t)"

month_day_dict = {0: "Januari", 30: "Februari", 60: "Mars", 90: "April", 120:"Maj", 150: "Juni",
					180: "Juli", 210:"Augusti", 240:"September", 270:"Oktober", 300:"November", 330:"December"}
def calculate_mean_value(energy_production_list):

	return sum(energy_production_list)/len(energy_production_list)

def calculate_standard_deviation(energy_production_list):
	total = 0
	for i in energy_production_list:
		total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
	return math.sqrt((1/(len(energy_production_list)-1))*total)

def main_function():
	root = Tk()
	main_frame = Frame(root)
	
	#Lower part of GUI
	bottomframe = Frame(root)
	bottomframe.pack(side = BOTTOM)

	#Top part of GUI
	top_frame = Frame(root)
	top_frame.pack(side = TOP)
	main_frame.pack()
	#header = Label(top_frame, text="Power Plant Simulator",command = solar_power_plant_calculation())
	#header.pack(side = LEFT)
	choice = 0
	#Main Buttons
	#solar_button = Button(top_frame, "Solar Calculator")
	#root.mainloop()
	if choice == 0:
		latitude_list = []
		lat_1 = 80
		latitude_list.append(lat_1)
		solar_plant = Solar_Power_Plant(100,2,latitude_list)
		power_calculation(solar_plant)
	elif choice == 1:
		wind_power_plant = Wind_Power_Plant(25)
	#wind_power_plant_calculation()

def power_calculation(power_plant):
	energy_dict = {}
	energy_dict = power_plant.energy_caluclator()
	energy_produced_list = []
	for key in energy_dict:
		day_data_list = energy_dict[key]
		for day_data_tuple in day_data_list:
			energy_produced_list.append(day_data_tuple[1])

	print(calculate_mean_value(energy_produced_list))
	print(calculate_standard_deviation(energy_produced_list))

	save_file(energy_dict, power_plant, "name.txt")

def save_file(latitude_dict, power_plant, file_name):
	column_headers = power_plant.capabilities()
	data = column_headers
	for latitude in latitude_dict:
		day_data_list = latitude_dict[latitude]
		for day_data_tuple in day_data_list:
	#		print (day_data_tuple)
			
			day = day_data_tuple[0]
			if (day% 30) == 0:
				data += (month_day_dict[day]+"\n")
			energy_produced = day_data_tuple[1]
			area = day_data_tuple[2]
			material_constant = day_data_tuple[3]
			sun_factor = day_data_tuple[4]
			latitude = day_data_tuple[5]
			
			energy_function = day_data_tuple[6]
			data += (str(area) +"\t" + str(material_constant) +"\t" + str(latitude) +"\t" + str(sun_factor) +"\t" + str(energy_produced) +"\t" + str(energy_function) + "\n")
	file = open(file_name, "w")

	file.write(data)
	file.close()
			

def user_input_int_handler(prompt):
	while True:
		try:
			user_input = int(input(prompt))
			return user_input
		except:
			print("Detta är inget heltal, försök igen")
main_function()



class Wind_Power_Plant(Power_Plant):

	def __init__(self, rotor_diameter):
		#Rotor diameter can be 	25-50m
		self.rotor_diameter = rotor_diameter

	def get_rotor_diameter(self):
		return self.rotor_diameter

	def wind_power_plant_calculator(self):
		energy_production_list = []
		month_mean_value_list =[]
		month_standard_deviation_list = []
		
		energy_produced = 0

		max_value = 0	
		min_value = 0
		#Index identifies month, value identifies actual value.
		max_list = []
		min_list = []
		for time in range(360):	
			


			
			big_wind_factor = 20
			small_wind_factor = 10
			if time < 60:
				energy_produced = small_wind_factor*self.get_rotor_diameter()
			elif time < 150:
				energy_produced = big_wind_factor *self.get_rotor_diameter()
				
			elif time < 270:
				energy_produced = small_wind_factor *self.get_rotor_diameter()
				
			elif time < 330:
				energy_produced = big_wind_factor *self.get_rotor_diameter()

			energy_production_list.append(energy_produced)
			super().collect_month_information(energy_produced, max_value, min_value, time, energy_production_list, month_mean_value_list, month_standard_deviation_list, min_list, max_list)
			
			print (max_value)
		mean_value = super().calculate_mean_value(energy_production_list)
		standard_deviation = super().calculate_standard_deviation(energy_production_list)
		return (mean_value, standard_deviation, month_mean_value_list, month_standard_deviation_list)

		
