# -*- encoding: utf-8 -*-

"""
this is a food truck project that will let the user know where a food truck 
is in san francisco on a specific day. 

we need to filter food truck by day, cuisine, and truck name. 
"""

from urllib2 import urlopen
from json import load

from foodtruckuser import * 
from testtruck import kettlecorn

FOODTRUCK_ENDPOINT = "https://data.sfgov.org/resource/6a9r-agq8.json"

def call_sfdataapi(endpoint):
	"""import data from sf open data"""

	response = urlopen(endpoint)
	return response

def load_sfdata(response):
	""" load data """

	json_obj = load(response)
	return json_obj

def clean_data(json_obj):
	""" parsing data in json_obj and returns a dictionary of cleaned up data """

	clean_data = {}

	for truck in json_obj:
		truck_name = truck['applicant'].lower()
		if 'fooditems' in truck:
			truck_cuisine = truck['fooditems'].lower()
		else:
			truck_cuisine = None
		if 'dayshours' in truck:
			truck_days = truck['dayshours'].lower()
		else:
			truck_days = None
		if 'locationdescription' in truck:
			truck_location = truck['locationdescription'].lower()
		else: 
			truck_location = None

		clean_data[truck_name] = truck_cuisine, truck_days, truck_location
	return clean_data 

def search_by_day(cleaned_data, username, user_day_pref=1):
	""" loop through data and searches by day """

	if user_day_pref == 1:
		truck_days = ['mo-su', 'mo-fri', 'm', 'mo-sat']
	# FINISH THIS! 

	display_recommendations(username)
	# this iterates over every single truck in cleaned data 
	for truck, info in cleaned_data.items():
		# this iterates over every day in truck days 
		for day in truck_days:
			if info[1] and day in info[1]:
				print truck, "is at ", info[2], "\n"

		
def search_by_cuisine(cleaned_data, user_food_pref, username):
	""" loop through data and searches by cuisine """

	display_recommendations(username)

	for truck,info in cleaned_data.items():
		if info[0] and user_food_pref in info[0]:			
			print truck, "is at ", info[2]

def main():
	# this is loading data
	response = call_sfdataapi(FOODTRUCK_ENDPOINT)
	foodtruck_list = load_sfdata(response)
	cleaned_data = clean_data(foodtruck_list)
	
	# this is where we prompt user for preferences
	
	username = prompt_user_for_username()
	# while (True):
	# TODO: write search by truck function, test while loop
	display_menu()
	user_menu_choice = prompt_user_menu_choice()

	if user_menu_choice == "A":
		user_food_pref = prompt_user_for_cuisine()
		search_by_cuisine(cleaned_data, user_food_pref, username)

	if user_menu_choice == "B":

		print day_choices
		user_day_pref = int(raw_input("Select your choice between 1-7. "))
		search_by_day(cleaned_data, username, user_day_pref)

	# if C:
		# search_by_truck_name()
	if user_menu_choice == "X":
		pass
		# break




if __name__ == '__main__':
	main()
