#Sriharsha Devulapalli
#23rd May 2016
#Homework 1

#This part of the program takes the input from the user
year = input("Which year were you born in?  ")
humanage= 2016-int(year)

#This part of the program checks if the user has entered a wrong date and quits, if he has.
if humanage < 0:
    print ("You have either entered a wrong year or are from the future. Please run program again.")
    quit()

#This part of the program makes the required calculations and returns the answers.

print("")
print("")
print "The following figures are approximated based on your age."
print "Please contact the coder for citations on these numbers."
print("")
print("")
print "You are",humanage,"years old"
print("")
print("")
ageofcoder=25
humanheart=72*60*24*365
print "=====HEARTBEAT====="
print("")
print "Your heart has beaten",humanheart,"times."
print("")
whaleheart=6*60*24*365*humanage
print "In the same period a blue whale's heart would have beaten",whaleheart,"times."
print("")
rabbitheart=205*60*24*365*humanage
if rabbitheart >= 1000000000:
    print "In the same period a rabbit's heart would have beaten",rabbitheart/float(1000000000),"billion times."
else:
    print "In the same period a rabbit's heart would have beaten",rabbitheart,"billion times"
print("")
print("")
print "===== COSMOS ====="
print("")
venusyear=0.62*humanage
print "In Venus Years you are",venusyear, "years old."
print("")
neptuneyear=humanage/165.0
print "In Neptune Years you are",neptuneyear, "years old."
print("")
print("")
print "===== RANDOM FACTS ABOUT YOUR AGE ====="
print("")
if humanage > 25:
    print "You are older than the coder by",humanage-ageofcoder,"years"
elif humanage < 25:
    print "You are younger than the coder by",ageofcoder-humanage,"years"
elif humanage==25:
    print "You are as old as the coder is, but you will never be as awesome as he is."
print("")
print("")
if year%2==0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")
print("")
print("")
if year <= 1975:
    print("The Pittsburgh Steelers have won 6 times since you were born.")
elif year <= 1976 and year >= 1975:
    print("The Pittsburgh Steelers have won 5 times since you were born.")
elif year <= 1979 and year >= 1976:
    print("The Pittsburgh Steelers have won 4 times since you were born.")
elif year <= 1980 and year >= 1979:
    print("The Pittsburgh Steelers have won 3 times since you were born.")
elif year <= 2006 and year >= 1980:
    print("The Pittsburgh Steelers have won 2 times since you were born.")
elif year <= 2009 and year >= 2006:
    print("The Pittsburgh Steelers have won 1 time since you were born.")

print("")
print("")

if year < 1933:
    print("You are too old. We cannot help you.")
elif year <= 1945 and year >= 1933:
    print("FDR was president when you were born(pretty likely).")
elif year <= 1953 and year >= 1945:
    print("Harry S Truman was president when you were born(pretty likely).")
elif year <= 1961 and year >= 1953:
    print("Dwight D Eisenhower was president when you were born(pretty likely).")
elif year <= 1963 and year >= 1961:
    print("JFK was president when you were born(pretty likely).")
elif year <= 1969 and year >= 1963:
    print("Lyndon B Johnson was president when you were born(pretty likely).")
elif year <= 1974 and year >= 1969:
    print("Richard Nixon was president when you were born(pretty likely).")
elif year <= 1977 and year >= 1974:
    print("Gerald Ford was president when you were born(pretty likely).")
elif year <= 1981 and year >= 1977:
    print("Jimmy Carter was president when you were born(pretty likely).")
elif year <= 1989 and year >= 1981:
    print("Ronald Reagan was president when you were born(pretty likely).")
elif year <= 1993 and year >= 1989:
    print("George Bush Sr was president when you were born(pretty likely).")
elif year <= 2001 and year >= 1993:
    print("Bill Clinton was president when you were born(pretty likely).")
elif year <= 2009 and year >= 2001:
    print("George Bush Jr was president when you were born(pretty likely). Jet fuels dont melt steel beams.")
elif year <= 2016 and year >= 2009:
    print("Barrack Obama was president when you were born(pretty likely).")
print("")
print("")
print "Do play around and Have a good day!"
