# Solar Power Plant Simulator
##Challenges:
If this program were written for a command line interface it would almost write itself. Estimated time spent on the actual calculation methods will be around one working day. The challenge for this application instead lies in providing usability. 
In order to provide usability a Graphical User Interface(GUI) will be provided. Writing such can be painstakin, however for this project the utilization of open source libraries will minimize the work and hence the cost.

The amount of time put into this project will be low and the program will be held simple which makes it easy to maintain. It will be written in a general way which will enable future extensions to be included easily.

##Use Cases:
Tom wants to see how much energy a solar power plant of the size 200m^2 outside of Stockholm would generate. Tom starts the program, chooses to simulate a solar power plant and inputs the latitude of Stockholm in a text box. He also inputs the power plants area and the material constant in simliar textboxes. The program responds with a dialog window which asks if Tom want to see the data as a bar chart, a table or save the data to a file. Tom chooses to save the data in a file and then quits the program through pressing the x button in the corner. He later visualizes the data in MatLab and compares it with data generated from other sessions.

Linda wants to see how the energy production for a solar plant outside of Tokyo would vary during a years time. She starts the program and choose to simulate a solar power plant. She inputs the material constans, the area of the cells and the latitude of Tokyo in the text boxes. The program reponds with a dialog window which asks if she wants to see the data as a bar chart, in a table or save it to a file. Linda chooses to see the data as a diagram. A bar chart is presented and Linda sees that during March the production is very low outside of Tokyo. She has to investigate why and therefore quits the program through a keyboard command.

##Model:

```
class Power_Plant(object):
	"""Super class for power plants."""
	def mean_value(energy_production_list):
		"""Calculates the mean value of energy produced during a given time. The number of items in the list is considered to give the time."""

	def standard_deviation(energy_production_list):
	"""Calculates the standard deviation of the energy produced during a period of time. The number of items in the list is considered to give the time."""

class Solar_Power_Plant(object):

	def __init__(self, area, material_constant):
		"""Constructor that sets the class variables"""
	
	def get_area(self):
		"""Returns the area"""

	def get_material_constant(self):
		"""Returns the material constant"""

	def energy_caluclator(latitude):
		"""Iterates over all days per year and for each day the energy generated is calculated through the calling of help methods. The function returns a tuple with the standard deviation, mean value and two lists. One with the standard deviation for all months and the other with the mean value for all months."""

	def solar_energy_calculator(sun_factor, time, latitude):
		"""Help method for energy_calculator that calculates 
			the formula W(t) =area·material_constant·sun_factor·latitude_time(t, latitude)."""
	def latitude_time(time, latitude):
		"""Calculates v = ((23.5)·sin((pi(time-80))/180)+90-latitude)/90 for latitudes 0 < latitude < 90"""

class Wind_Power_Plant(object):

	def __init__(self, rotor_diameter):
		"""Constructor that sets the class variables"""

	def get_rotor_diameter(self):
		"""Returns rotor diameter"""
	def wind_power_plant_calculator(wind_power_plant, time):
		"""Iterates over all days per year and calculates how much energy the wind power plant produces. The prodcution is season dependent because of stronger winds in spring and autumn. The function returns a tuple with the standard deviation, mean value and two lists. One with the standard deviation for all months and the other with the mean value for all months."""


def main_menu():
	"""Function that handles the user interaction when the user is in the main menu. It can here choose to calculate wind or solar."""

def calculate_solar_power():
	"""User interaction function which asks for input data. Latitudes, area, material constant and presents the generated data."""

def calculate_wind_power():
	"""Ask for the rotor diameter and presents the generated wind data."""

def save_to_file():
	"""Saves the generated data to a file"""

def generate_bar_chart():
	"""Generates a bar chart through plotpy"""

def generate_table():
	"""Generate tables"""

def user_input_cleaner():
	"""Checks the user inputs for error."""

def quit():
	"""Exits the program"""
```

##Program flow and data flow
The program starts in the ```main_menu()``` function. The user calls either ```calculate_solar_power()``` or ```calculate_wind_power()``` where a solar or wind power plant object with class variables as input to their constructors are created. If the user created a solar power plant latitudes are collected from the user and for each latitude the solar power plants function energy_calculator(latitude) is called. This function iterates over all days of a year and calls the functions solar_energy_calculator, mean_value_calculator and standard_deviation_calculator. A tuple is returned to the main calculate_solar_power function and depending on the user save_to_file(), generate_bar_chart() or generate_table() is called. Pressing the x-button in the left corner calls the quit() function which exits the program.