#Sriharsha Devulapalli
#31st May 2016
#Homework3

countries = ['Mexico', 'USA', 'Peru', 'India', 'France', 'South Africa', 'Indonesia']
print ""
print ""
print "This is the set of countries:"
print ""
for country in countries:
    print country

countries=sorted(countries)
n=len(countries)
print ""
print "The first country in the list after being permanently sorted is", countries[0]
print ""
print "The last but one country in the list is ", countries[n-2]
print ""
countries.remove("Indonesia") #Removing a country
print "The new list of countries after one has been removed is"
for country in countries:
    print country


#===========DICTIONARIES===========
print ""
print "======================================================================="
print "Now, we move on to the trees."
trees= [
{'name': 'Great Banyan', 'species':'Ficus Benghalensis', 'age':250, 'location_name': 'Kolkata,India', 'latitude': 22.5608, 'longitude':88.2866}
]

for tree in trees:
    print "The",tree['name'],"is a",tree['age'],"years old tree that is in",tree['location_name']

newyorklatitude=40.7128
newyorklongitude=-74.0059

if newyorklatitude > tree['latitude']:
    print "The",tree['name'],"in",tree['location_name'],"is south of New York City"
else:
    print "The",tree['name'],"in",tree['location_name'],"is north of New York City"

ageofuser=input("Let us check how your age compares to the tree. What's your age?")
yearofbirth=2016-int(ageofuser)


if tree['age'] < ageofuser:
    print ("You are",ageofuser-tree['age'],"years older than",tree['name'])
else:
    dummy=tree['age']-ageofuser
    print "The",tree['name'],"was",dummy,"years old when you were born"

print ""
print "======================================================================="
#===========LISTS OF DICTIONARIES===========

cities= [
{'name': 'Moscow', 'latitude':55.7558, 'longitude':37.6173},
{'name': 'Tehran', 'latitude':35.6892, 'longitude':51.3890},
{'name': 'Falkland Islands', 'latitude':-51.7963, 'longitude':-59.5236},
{'name': 'Seoul', 'latitude':37.5665, 'longitude':126.9780},
{'name': 'Santiago', 'latitude':-33.4489, 'longitude':-70.6893},
]

print ""
print("We are now going to check if the cities in our list are above or below the equator.")
print ""
for city in cities:
    if city['latitude'] > 0:
        print city['name'],"is above equator"
        print ""
    if city['latitude'] < 0:
        print city['name'],"is below equator"
        print ""
    if city['name'] == 'Falkland Islands':
        print "The Falkland Islands are a biogeographical part of the mild Antarctic zone."
print ""
print ""
print "======================================================================="
print ""
print("We are now going to check if the cities in our list are above or below the tree.")
for city in cities:
    if city['latitude'] > tree['latitude']:
        print city['name'],"is above the",tree['name'], "in",tree['location_name']
        print ""
    if city['latitude'] < tree['latitude']:
        print city['name'],"is below the",tree['name'], "in",tree['location_name']
        print ""
    if city['name'] == 'Falkland Islands':
        print "The Falkland Islands are a biogeographical part of the mild Antarctic zone."
        print ""
