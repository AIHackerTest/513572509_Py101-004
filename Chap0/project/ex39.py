# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': "MI"
}

#create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('_'*10)
print("Michigan's abbreviation is: ",state['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('_'*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#print every state abbreviation
print('_'*10)
for state,abbrev in states.items():
    print("%s is abbreviation %s"%(state,abbrev))

print('_'*10)
for abbrev,city in cities.items():
	print("%s has the city %s" %(abbrev,city))

#now do both at the same time
print('_'*10)
for state,abbrev in states.items():
	print("%s state is abbreviation %s and hsa city %s"%(state,abbrev,cities[abbrev]))


print('_'*10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX','Does Not Exit.')
print("The city for the state 'TX' is :%s" % city)
