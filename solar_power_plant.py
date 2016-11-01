
import random
import math
class Solar_Power_Plant(object):

	def __init__(self, area, sun_number):
		self.area = area
		self.sun_number = sun_number
	
	def get_area(self):
		return self.area

	def get_sun_number(self):
		return self.sun_number

	def get_latitude(self):
		return self.latitude


class Wind_Power_Plant(object):

	def __init__(self, rotor_diameter):
		self.rotor_diameter = rotor_diameter

	def get_rotor_diameter(self):
		return self.rotor_diameter

def main_function():
	solar_power_plant_calculation()

def wind_power_plant_calculation():
	
	for time in range(360):	
		energy_production_list = []
		energy_production_list.append(wind_power_plant_calculator(wind_power_plant, time))

	mean_value(energy_production_list)
	standard_deviation(energy_production_list)

def wind_power_plant_calculator(wind_power_plant, time):
	big_wind_factor = 20
	small_wind_factor = 10
	if time < 60:
		return small_wind_factor *wind_power_plant.get_rotor_diameter()
	elif time < 150:
		return big_wind_factor*wind_power_plant.get_rotor_diameter()
	elif time < 270:
		return small_wind_factor*wind_power_plant.get_rotor_diameter()
	elif time < 330:
		return big_wind_factor*wind_power_plant.get_rotor_diameter()
	else:
		return small_wind_factor*wind_power_plant.get_rotor_diameter()

def solar_power_plant_calculation():
	solar_plant = Solar_Power_Plant(100, 2)
	#x = Solar_Power_Plant(100, 2)
	lat_1 = 80
	lat_2 = 70
	latitude_list = []
	latitude_list.append(lat_1)
	latitude_list.append(lat_2)
	for latitude in latitude_list:
		energy_production_list = []
		for time in range(360):
			sun_factor = random.randrange(0,1)
			energy_production_list.append(solar_energy_calculator(solar_plant, sun_factor, time, latitude))
		mean_value(energy_production_list)
		standard_deviation(energy_production_list)
def mean_value(energy_production_list):

	return sum(energy_production_list)/len(energy_production_list)

def standard_deviation(energy_production_list):
	total = 0
	for i in energy_production_list:
		total += math.pow((i - (sum(energy_production_list) / len(energy_production_list))), 2)
	return math.sqrt((1/(len(energy_production_list)-1))*total)

def solar_energy_calculator(solar_plant, sun_factor, time, latitude):

	return (solar_plant.get_area()*solar_plant.get_sun_number()*sun_factor*latitude_time(time, latitude))

def latitude_time(time, latitude):
	v = (23.5*math.sin((math.pi*(time-80))/180) + 90 - latitude)/90
	return v

main_function()