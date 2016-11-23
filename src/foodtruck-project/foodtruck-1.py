"""
this is a food truck project that will let the user know where a food truck 
is in san francisco on a specific day. 

we need to filter food truck by day.

add on's: filter by cuisine

"""

# import data from sf open data

# load data 

# loop through data and set parameters to search for 

from urllib2 import urlopen
from json import load
from testtruck import kettlecorn

FOODTRUCK_ENDPOINT = "https://data.sfgov.org/resource/6a9r-agq8.json"



def call_sfdataapi(endpoint):
	response = urlopen(endpoint)
	return response

def load_sfdata(response):
	json_obj = load(response)
	return json_obj
	
# lots of conditionals and parsing!! parse days and hours, make sure it is searchable
# normalize data

# screen for location, expired permits 
# another idea - creating an object based on user preferences, ask questions
# ahead of time. given user preferences, provide suggestions 

def search_by_day(foodtruck_list):
	# return foodtruck_list[0]
	for truck in foodtruck_list:
	# truck = kettlecorn
		truck_name = truck['applicant']
		if 'dayshours' in truck:
			truck_avail_list = truck['dayshours'].split(':')
			# truck_days, truck_hours = truck['dayshours'].split(':')
			# print truck_name
			# print truck_days, truck_hours
		# 	if truck_days == 'Mo-Su':
		# 		truck_days = {'Monday': truck_hours,'Tuesday': truck_hours, 
		# 					'Wednesday': truck_hours, 'Thursday': truck_hours,
		# 					'Friday': truck_hours, 'Saturday': truck_hours, 
		# 					'Sunday': truck_hours}
		# # else:
			print truck_name, truck_avail_list
			# print truck_name, truck_days
		else:
			print truck_name	

# search off  clean data

def main():
	response = call_sfdataapi(FOODTRUCK_ENDPOINT)
	foodtruck_list = load_sfdata(response)
	print search_by_day(foodtruck_list)




if __name__ == '__main__':
	main()