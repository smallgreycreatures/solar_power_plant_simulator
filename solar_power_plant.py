
import random
import math
from tkinter import *
import plotly
class Power_Plant(object):
	def calculate_mean_value(energy_production_list):

		return sum(energy_production_list)/len(energy_production_list)

	def calculate_standard_deviation(energy_production_list):
		total = 0
		for i in energy_production_list:
			total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
		return math.sqrt((1/(len(energy_production_list)-1))*total)

class Solar_Power_Plant(Power_Plant):

	def __init__(self, area, sun_number):
		self.area = area
		self.sun_number = sun_number
	
	def get_area(self):
		return self.area

	def get_sun_number(self):
		return self.sun_number
	def solar_energy_calculator(sun_factor, time, latitude):

		return (get_area()*get_sun_number()*sun_factor*latitude_time(time, latitude))

	def latitude_time(time, latitude):
			v = (23.5*math.sin((math.pi*(time-80))/180) + 90 - latitude)/90
		return v

	def energy_caluclator(latitude):
		
		energy_production_list = []
		month_mean_value_list =[]
		month_standard_deviation_list = []
		
		max_value = 0
		min_value = 0

		for time in range(360):
			sun_factor = random.randrange(0,1)
			energy_produced = solar_energy_calculator(sun_factor, time, latitude)
			energy_production_list.append(energy_produced)

			if energy_produced >= max_value:
				max_value = energy_produced

			elif energy_produced <= min_value:
				min_value = energy_produced

			if (time%30)==0 and time != 0:
				month_mean_value_list.append(mean_value(energy_production_list[(time-30,time)]))
				month_standard_deviation_list.append(standard_deviation(energy_production_list[time-30,time]))
				##implement dict to save day and man,min values
				max_value = 0
				min_value = 0

		mean_value = mean_value(energy_production_list)
		standard_deviation = standard_deviation(energy_production_list)
	return (mean_value, standard_deviation, month_mean_value_list, month_standard_deviation_list)

class Wind_Power_Plant(Power_Plant):

	def __init__(self, rotor_diameter):
		self.rotor_diameter = rotor_diameter

	def get_rotor_diameter(self):
		return self.rotor_diameter

	def wind_power_plant_calculator(wind_power_plant, time):
		big_wind_factor = 20
		small_wind_factor = 10
		if time < 60:
			return small_wind_factor *get_rotor_diameter()
		elif time < 150:
			return big_wind_factor*get_rotor_diameter()
		elif time < 270:
			return small_wind_factor*get_rotor_diameter()
		elif time < 330:
			return big_wind_factor*get_rotor_diameter()
		else:
			return small_wind_factor*get_rotor_diameter()

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
	header = Label(top_frame, text="Power Plant Simulator",command = solar_power_plant_calculation())
	header.pack(side = LEFT)

	#Main Buttons
	solar_button = Button(top_frame, "Solar Calculator")
	root.mainloop()
	solar_power_plant_calculation()

def wind_power_plant_calculation():
	
	for time in range(360):	
		energy_production_list = []
		energy_production_list.append(wind_power_plant_calculator(wind_power_plant, time))

	mean_value(energy_production_list)
	standard_deviation(energy_production_list)



def solar_power_plant_calculation():
	solar_plant = Solar_Power_Plant(100, 2)
	#x = Solar_Power_Plant(100, 2)
	lat_1 = 80
	lat_2 = 70
	latitude_list = []
	latitude_list.append(lat_1)
	latitude_list.append(lat_2)
	for latitude in latitude_list:
		solar_plant.energy_caluclator(latitude)




main_function()