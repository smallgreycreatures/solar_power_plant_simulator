import random
import math
class Solar_Power_Plant(object):

	def __init__(self, area, material_constant, latitude_list):
		self.area = area
		self.material_constant = material_constant
		self.latitude_list = latitude_list
	
	def get_area(self):
		"""return the area of the solar panels"""
		return self.area

	def get_material_constant(self):
		"""returns the material constant"""
		return self.material_constant

	
	def solar_energy_calculator(self, sun_factor, time, latitude):
		"""calculates energy produced with formula W(t) = 
		area·material_constant·sun_factor·latitude_time(t, latitude)
		return W(t) and the returned value from latitude_time in a tuple."""
		latitude_time = self.latitude_time(time, latitude)
		return (self.get_area()*self.get_material_constant()*sun_factor*latitude_time, latitude_time)

		
	def latitude_time(self, time, latitude):
		"""Decides what each latitude gives for solar value, help function to solar_energy_calculator"""
		
		#for 0<latitude<90: this is the formula mentioned in the f(x) section in the spec
		v = (23.5*math.sin((math.pi*(time-80))/180) + 90 - latitude)/90
		
		if v > 0 and v < 1:
			return v*v

		elif v >= 1:
			return 1

		else: #v < 0
			return 0

			
	def energy_calculator(self):
		"""Calculates energy produced each day for 360 days.
		Returns dictionary where each element is a latitude. 
		Each latitude holds a list of days where each day list contains a tuple per day on 
		the form (time, energy_produced, area, material_constant, sun_factor, latitude, latitude_time function value)"""
		
		#stores data from each latitude
		latitude_dict = {}

		for latitude in self.latitude_list:

			#stores data from each day. One tuple per index(day) (Area, material constant, sun factor, latitude, W, f(t,lat))
			day_list = []

			for time in range(360): #360 days per year
				sun_factor = random.random()

				#Stores energy produced that day as [0] and the value from latitude_time() as [1]
				energy_produced_tuple = self.solar_energy_calculator(sun_factor, time, latitude)
				energy_produced = energy_produced_tuple[0]
				day_list.append((time, energy_produced, self.get_area(), self.get_material_constant(), sun_factor, latitude, energy_produced_tuple[1]))
			latitude_dict[latitude] = day_list

		return latitude_dict

	def capabilities(self):
		"""returns a string with the data labels from the solar plant"""
		return "Area, Sun factor, Latitude ,Day ,Sun factor ,f(t,latitude), W(t)"

class Wind_Power_Plant(object):

	def __init__(self, rotor_diameter):
		#Rotor diameter can be 	25-50m
		self.rotor_diameter = rotor_diameter

	def get_rotor_diameter(self):
		"""returns rotot diameter"""
		return self.rotor_diameter

		
	def wind_variation(self, time):
		"""Decides how the wind varies. It's windier during autumn and spring (month 3-5 and 9-11)."""
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
		"""The function returns dictionary containing one element with key 0.
		This element is a list of all days where each day is represented as a tuple of
		the form(time, energy_produced,wind_variation, rotor_diameter) """
		
		#Stores a list of tuples. Only contains one element
		wind_power_dict = {}
		#Contains a tuple with the daily data from the wind power plant
		#on the form (time,energy produced,wind variation, rotor diameter)
		day_list = []
		for time in range(360):
			wind_variation = self.wind_variation(time)
			energy_produced = wind_variation*self.get_rotor_diameter()
			day_list.append((time, energy_produced, wind_variation, self.get_rotor_diameter()))

		
		wind_power_dict[0] = day_list
		return wind_power_dict

	def capabilities(self):
		"""returns a string with the data labels from the wind plant"""
		return "Rotor diameter, Day, W(t), Wind variation"