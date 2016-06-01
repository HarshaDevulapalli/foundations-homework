#Sriharsha Devulapalli
#25th May 2016
#Homework2

number = [22,90,0,-10,3,22,48]
print("This is the list")
print(number) #displaying the list
n= len(number) #calculating the length of the list
print("")
print "The length of the list is",n
print("")
print "The fourth element in the list is", number[3] #displaying the fourth element.
print("")
print "The sum of fourth and second element is", ((number[3])+(number[1])) #displaying the sum of the 4th and 2nd element.
print("")
sortednumber = sorted(number) #sorting the list to find out the second largest number
print "The second largest element is ", sortednumber[n-2] #printing the second largest element
print("")
print "The last element of the original unsorted list is", (number[n-1]) #printing the last element of the original unsorted list.
print("")
print("This is the start of the sixth question")
result=0
for n in number:
    if n < 10 and n%2==0:
        new=n*30+6
    else:
        new= n*30
    if n > 50:
        new=n-10
    if n == -10:
        new = n
    else:
        new = n-1
    print(new)
    result=result+new
print("")
print "The sum of all the numbers after the math is",result

#DICTIONARIES PART
#Multiple aspects of a single object.
print("")
print "=====MOVIES====="
print("")
movies =[
{'title': 'The Wizard of Oz', 'year':'1939', 'director':'King Vidor', 'budget': 200000, 'revenue': 5000000},
{'title': 'The Terminator', 'year':'1984', 'director':'James Cameron', 'budget': 783838888, 'revenue': 1212121212},
{'title': 'Boyhood', 'year':'2014', 'director':'Richard Linklater', 'budget': 50000000, 'revenue': 10000000},
{'title': 'Hurt Locker', 'year':'2010', 'director':'Kathyryn Bigelow', 'budget': 70000000, 'revenue': 75000000}
]

for movie in movies:
    print "My Favourite Movie", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director']
    if (movie['revenue']-movie['budget']) < 0:
        print "It was a flop."
    if (movie['revenue'] >= 5*movie['budget']):
        print "That film was a good investment."
    print("")

#Same aspects of Multiple Objects
print("")
print "=====NEW YORK BOROUGHS====="
print("")
populations = [1600000,2600000,1400000,2300000,470000]
boroughs = ["Manhattan","Brooklyn","Bronx","Queens","Staten Island"]
for borough in boroughs:
    if(borough=='Brooklyn'):
        print "The borough of",borough,"has a population of", populations[2]
print("")
print "The total population of the Boroughs is",sum(populations)
print("")
for borough in boroughs:
    if(borough=='Manhattan'):
        dummy=sum(populations)
        Manhattanpercentage=(float(populations[1])/float(dummy)*100)
        print "The percentage of NYC's population that lives in",borough,"is",Manhattanpercentage,"percent"
