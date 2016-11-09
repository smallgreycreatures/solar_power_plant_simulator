# Solar Power Plant Simulator
##Challenges:
If this program were written for a command line interface it would almost write itself. Estimated time spent on the actual calculation methods will be around one working day. The challenge for this application instead lies in providing usability. 
In order to provide usability a Graphical User Interface(GUI) will be provided in order to create a good overview over the data. Writing such can be painstaking, however for this project the utilization of open source libraries will minimize the work and hence the cost.

The amount of time put into this project will be low and the program will be held simple which makes it easy to maintain. It will be written in a general way which will enable future extensions to be included easily.

##Use Cases:
Tom wants to see how much energy a solar power plant of the size 200m^2 outside of Stockholm would generate. Tom starts the program, chooses to simulate a solar power plant and inputs the latitude of Stockholm in the console. He also inputs the power plants area and the material constant. The program responds and asks if Tom want to see the data as a bar chart, a table or save the data to a file. Tom chooses to save the data in a file and then quits the program. He later visualizes the data in MatLab and compares it with data generated from other sessions.

Linda wants to see how the energy production for a solar plant outside of Tokyo would vary during a years time. She starts the program and choose to simulate a solar power plant. She inputs the material constans, the area of the cells and the latitude of Tokyo in the terminal. The program reponds and asks if she wants to see the data as a bar chart, in a table or save it to a file. Linda chooses to see the data as a bar chart. A bar chart is presented and Linda sees that during March the production is very low. She has to investigate why and therefore quits the program.

##Model:

```
class Power_Plant(object):
	"""Super class for power plants."""



class Solar_Power_Plant(object):

	def __init__(self, area, material_constant, latitude_list):
		"""Constructor that sets the class variables"""
	
	def get_area(self):
		"""Returns the area"""

	def get_material_constant(self):
		"""Returns the material constant"""

	def energy_caluclator():
		"""Iterates over the latitudes in the list latitude_list and then iterates over all days per year and for each day the energy generated is calculated through the calling of help methods. The function returns dictionary where each element is a latitude. Each latitude holds a list of days where each day list contains a tuple per day on the form (time, energy_produced, area, material_constant, sun_factor, latitude, latitude_time function value)

	def solar_energy_calculator(sun_factor, time, latitude):
		"""Help method for energy_calculator that calculates 
			the formula W(t) = area·material_constant·sun_factor·latitude_time(t, latitude)."""

	def latitude_time(time, latitude):
		"""Calculates v = ((23.5)·sin((pi(time-80))/180)+90-latitude)/90 for latitudes 0 < latitude < 90"""

class Wind_Power_Plant(object):

	def __init__(self, rotor_diameter):
		"""Constructor that sets the class variables"""

	def get_rotor_diameter(self):
		"""Returns rotor diameter"""

    def wind_variation(self, time):
        """Function that defines how the wind varies during the year. More wind in spring and autumn."""

	def energy_calculator(self):
		"""Iterates over all days per year and calculates how much energy the wind power plant produces. The prodcution is season dependent because of stronger winds in spring and autumn. The function returns dictionary containing one element with key 0. This element is a list of all days where each day is represented as a tuple of the form(time, energy_produced,wind_variation, rotor_diameter)


def main_menu():
	"""Function that handles the user interaction when the user is in the main menu. The user here chooses wind or solar and is asked to input the required data. A power plant object is then created."""

def power_calculation(power_plant):
	"""The energy_calculator() method is called and the result is stored in a variable. The user is asked what to do with the data (Table, Bar chart, save to file, discard)."""

def save_to_file(power_plant_dict, power_plant, file_name):
	"""Saves the generated data to a file"""

def display_bar_graph(energy_produced_per_month):
	"""Generates a bar graph through tkinter"""

def generate_table(energy_produced_per_month):
	"""Generate tables"""

def user_input_cleaner(prompt):
	"""Checks the user inputs for error."""

def calculate_mean_value(energy_production_list):
"""Calculates the mean value of energy produced during a given time. The number of items in the list is considered to give the time."""

def calculate_standard_deviation(energy_production_list):
"""Calculates the standard deviation of the energy produced during a period of time. The number of items in the list is considered to give the time."""

def quit():
	"""Exits the program"""
```

##Program flow and data flow
The program starts in the ```main_menu()``` function where the wind_power_plant or solar_power_plant object is created. This object is sent to ```power_calculation(power_plant)``` where the objects ```calculate_energy()``` is called. This returns a data dictionary containing one element for wind power and n for solar where n is the number of latitudes. Each element in the dictionary contains a list of all days, for each day there is a tuple containing all useful information. Depending on which objects method is called different help methods are called to calculate how much sun or wind power is collected. If the user choose to diplay the data as a bar graph or in a table the function ```energy_produced_per_month(power_plant, energy_production_list)``` is called which calls  ```calculate_mean_value(energy_production_list)``` and ```calculate_standard_deviation(energy_production_list)``` and produces a tuple of (max, min, mean, standard deviaton) lists for each month. A bar graph or table is then created through the calling of ```display_bar_graph(energy_tuple)```or ```display_table(energy_tuple)```. If the user chooses save file the function ```save_file(power_plant_dict, power_plant, file_name)``` is called which saves a file with the data for each day in a file with the name file_name.