
import random
import math
from tkinter import *
import plotly
class Power_Plant(object):
	def calculate_mean_value(self, energy_production_list):

		return sum(energy_production_list)/len(energy_production_list)

	def calculate_standard_deviation(self, energy_production_list):
		total = 0
		for i in energy_production_list:
			total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
		return math.sqrt((1/(len(energy_production_list)-1))*total)
	
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

	def __init__(self, area, sun_number):
		self.area = area
		self.sun_number = sun_number
	
	def get_area(self):
		return self.area

	def get_sun_number(self):
		return self.sun_number
	def solar_energy_calculator(self, sun_factor, time, latitude):

		return (self.get_area()*self.get_sun_number()*sun_factor*self.latitude_time(time, latitude))

	def latitude_time(self, time, latitude):
		#0<latitude<90
		v = (23.5*math.sin((math.pi*(time-80))/180) + 90 - latitude)/90
		
		return v

	def energy_caluclator(self, latitude):
		
		energy_production_list = []
		month_mean_value_list =[]
		month_standard_deviation_list = []
		
		max_value = 0
		min_value = 0
		#Index identifies month, value identifies actual value.
		max_list = []
		min_list = []

		for time in range(360):
			sun_factor = random.random()


			energy_produced = self.solar_energy_calculator(sun_factor, time, latitude)
			energy_production_list.append(energy_produced)

			if energy_produced >= max_value:
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
		standard_deviation = super().calculate_standard_deviation(energy_production_list)
		return (mean_value, standard_deviation, month_mean_value_list, month_standard_deviation_list)

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

		return ()
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

	#Main Buttons
	#solar_button = Button(top_frame, "Solar Calculator")
	#root.mainloop()
	#solar_power_plant_calculation()
	wind_power_plant_calculation()
def wind_power_plant_calculation():
	wind_power_plant = Wind_Power_Plant(25)
	print(wind_power_plant.wind_power_plant_calculator())





def solar_power_plant_calculation():
	solar_plant = Solar_Power_Plant(100, 2)
	#x = Solar_Power_Plant(100, 2)
	lat_1 = 80
	#lat_2 = 70
	latitude_list = []
	latitude_list.append(lat_1)
	#latitude_list.append(lat_2)
	for latitude in latitude_list:
		print (solar_plant.energy_caluclator(latitude))




main_function()