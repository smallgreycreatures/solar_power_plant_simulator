import random
import math
class Solar_Power_Plant(object):

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

	def energy_calculator(self):
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

		return latitude_dict

	def capabilities(self):
		return "Area, Sun factor, Latitude ,Day ,Sun factor ,f(t,latitude), W(t)"

class Wind_Power_Plant(object):

	def __init__(self, rotor_diameter):
		#Rotor diameter can be 	25-50m
		self.rotor_diameter = rotor_diameter

	def get_rotor_diameter(self):
		return self.rotor_diameter

	def wind_variation(self, time):
			big_wind_factor = 20
			small_wind_factor = 10
			rand_factor = random.random()
			if time < 60:
				return small_wind_factor*rand_factor
			elif time < 150:
				return big_wind_factor *rand_factor
				
			elif time < 270:
				return small_wind_factor *rand_factor
				
			elif time < 330:
				return big_wind_factor *rand_factor
			else:
				return small_wind_factor*rand_factor

	def energy_calculator(self):
		wind_power_dict = {}
		day_list = []
		for time in range(360):
			wind_variation = self.wind_variation(time)
			energy_produced = wind_variation*self.get_rotor_diameter()
			day_list.append((time, energy_produced, wind_variation, self.get_rotor_diameter()))

		
		wind_power_dict[0] = day_list
		return wind_power_dict

	def capabilities(self):
		return "Rotor diameter, Day, W(t), Wind variation"