# message = "Hello Python !"
# print(message)

# Name = "Eric"
# print(f"\n\tHello {Name.upper()}, would you like to learn some Python Today?")
# print(f"\n\tHello {Name.lower()}, would you like to learn some Python Today?")
# print(f"\nHello {Name.title()}, would you like to learn some Python Today?")

# Quote = "is not that which you see while sleeping, it is something that does not let you sleep."
# Author = "abdul kalam"
# print(f'{Author.title()} once said, "Dream {Quote.lower()}."')

# Quote = "is not that which you see while sleeping, it is something that does not let you sleep."
# famous_person = "abdul kalam"
# message = f'{famous_person.title()} once said, "Dream {Quote.lower()}."'
# print(message)

# Name = "   Bhavishya.  " ## strip used to remove whitespace around the string .
# print(Name.lstrip().rstrip())
# print(Name.strip())

# filename= "python_notes.txt"
# print(filename.removesuffix(".txt").removeprefix("python_"))

# print(4+4)
# print(10-2)
# print(4*2)
# print(32/4)

# we can only use int on numbers not on words.
# favourite_no = int(67.90)
# message = favourite_no
# print(message)

# names = ['Chulbul','krishna','Bhavesh','Yash','Ankit']
# print(f"Hi, aur kya ho rah he {names[1].title()}.") # We first mention the name of list then we put the value of element.
# print(f"Hi, aur kya ho rah he {names[3].upper()}.")
# print(f"Hi, aur kya ho rah he {names[0].lower()}.")
# print(f"Hi, aur kya ho rah he {names[2]}.")
# print(f"Hi, aur kya ho rah he {names[4]}.")

# modes = ['Toyota','Mercedes','Maruti Suzuki','Audi','BMW']
# print(f"I would like to have {modes[0]} and {modes[1]} in my real life.")


##########################################


# motorcycles = ["Honda","BMW","Ducati","Royal Enfield"]
# print(motorcycles)

# # here we change the element of list by providing new value to its position.
# motorcycles[3] = "Yamaha"
# print(motorcycles)
# # we can also add the element in list by (append) it will add element in last of list.
# motorcycles.append("Kawasaki")
# print(motorcycles)
# # we can insert any element in list at any index with insert() method.
# motorcycles.insert(3,"Suzuki")
# print(motorcycles)
# # we can del any element in a list by using del statement.
# del motorcycles[3]
# print(motorcycles)
# #The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
# # You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses
# # Remember that each time you use pop(), the item you work with is no longer stored in the list.
# first = motorcycles.pop(2)
# print(f"\nThe first motorcycle I owned was a {first}.")
# second = motorcycles.pop(2)
# print(f"\nThe second motorcycle I owned was a {second}.")
# # we can remove the element with (remove method) if we do not know the index of an element but we know the element name .
# cheaper = "BMW"
# motorcycles.remove(cheaper)
# print(motorcycles)
# print(f"\nA {cheaper.title()} is too cheaper for me.")


#try it yourself.
# guests=["Vinee","Ankit","Simran","Yash","Krishna","Bhavish"]
# print("\nSorry to say but",guests[0],"will not be able to come to our party. ")
# guests[0]="Djwala"
# print("\nBut",guests[0],"is coming in place of Vinee will come")
# guests.insert(0,"DJwala")
# print(guests[2],"you have to come to otherwise  .")
# print(guests[3],"you have to come to otherwise  .")
# print(guests[4],"you have to come to otherwise  .")
# print("\nI found a bigger table.")
# guests.insert(0,"Golu")
# guests.insert(3,"Khusi")
# guests.append("Madhu")
# print(guests,"\n now all these members have to come.")
# print("\n",guests[0],"you have to come to otherwise .")
# print("\n",guests[1],"you have to come to otherwise .")
# print("\n",guests[2],"you have to come to otherwise .")
# print("\n",guests[3],"you have to come to otherwise .")
# print("\n",guests[4],"you have to come to otherwise .")
# print("\n",guests[5],"you have to come to otherwise .")
# print("\n",guests[6],"you have to come to otherwise .")
# print("\n",guests[7],"you have to come to otherwise .")
# print("\n",guests[8],"you have to come to otherwise .")
# print("\n",guests[9],"you have to come to otherwise .")
# print(guests[0],",Sorry i can not invite you to dinner.")
# guests.pop(0)
# print(guests[1],",Sorry i can not invite you to dinner.")
# guests.pop(1)
# print(guests[2],",Sorry i can not invite you to dinner.")
# guests.pop(2)
# print(guests[3],",Sorry i can not invite you to dinner.")
# guests.pop(3)
# print(guests[4],",Sorry i can not invite you to dinner.")
# guests.pop(4)
# print(guests[0],",Sorry i can not invite you to dinner.")
# guests.pop(0)
# print(guests[1],",Sorry i can not invite you to dinner.")
# guests.pop(1)
# print(guests[1],",Sorry i can not invite you to dinner.")
# guests.pop(1)
# print(guests)
# del guests[0]
# print(guests)
# del guests[0]
# print(guests)

######################################################

# cars = ["Suzuki","Audi","BWW","Land Rover"]
# cars.sort()# it will form list in alphabetical order.But after using this we can not revert the order of list.
# print(cars)

# cars = ["Suzuki","Audi","BWW","Land Rover"]
# cars.sort(reverse=True)#to reverse the output of ([sort method ]output) in list.
# print(cars)

# cars = ["Suzuki","Audi","BWW","Land Rover"]
# cars.reverse()# we can use reverse method directly on list .
# print(cars)



# # to not change the order of list permanently after alphabetical order we use sorted() method instead of sort() method.
# cars = ["Suzuki","Audi","BWW","Land Rover"]
# print("here is the original list.")
# print(cars)

# cars = ["Suzuki","Audi","BWW","Land Rover"]
# print("\nhere is the original list.")
# print(sorted(cars))

# cars = ["Suzuki","Audi","BWW","Land Rover"]
# print("\nhere is the original list again:")
# print(cars)

# cars =["bmw","audi","toyota","supra"]
# print(len(cars))#to find the length of the list we use len() function.


###################################
#page 45 try yourself
# places = ['Kedarnath','Gangotri','Moscow','Scotland','Newzealand','Chardham']
# print(places)
# print(sorted(places))
# reversed_ =sorted(places,reverse=True)#### to reverse the order of list alphabetically by using revere and sorted method of instead sort method because after using we can not make any change in the list afterwards.
# print(reversed_)
# reversed_.reverse()
# print(reversed_)
# reversed_.sort
# print(reversed_)
# reversed_.sort(reverse=True)
# print(reversed_)
# print(len(reversed_))## to find the number of elements in list.
# print(reversed_[4])

##########################################
# for loop start
# for loop provide same action with every item in a list.
# magicians=["Alice","David","Carolina"]
# for magician in magicians: #we commonly give list name in pulral just to make the code easier to read ,when we give its name in ( for loop ).
#     #print(magician)
#     print(f"{magician.title()},that was a great trick.")
#     print(f"I can not wait to see your next trick,{magician.title()}.\n")
# print(f"Thank you everyone for your performance.")# if we put this print under others print then this message will repeat for every element in the list.because of the identation mistake.

# try yourself 56
# sweets = ["rasgulla","sonpapdi","kajukatli","malpuri","ghewar"]
# for sweet in sweets:
#     print(f"I like {sweet}.")
# print(f"I really like sweets but i try to control my self to eat more sweets becuse too much sweet is harmful for health it can several diseases.\nbut i really love sweets.")

# animals = ["Dog","Cat","Horse","Cow","Eagle","Parrots"]
# for animal in animals :
#     print(f"A {animal} would make a great pet.\n")
# print(f"Anyone of those can make a great pet.")

##### range function 
# for value in range(1,5):
#     print(value)


# for value in range (6):#this range argument  will start the sequence of number at 0.
#     print(value)

# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,2))# here first 2 means the value will start with 2 and second 2 tell to add 2 to each number and 11 is the range last number means list will stop before 11.
# print(even_numbers)

# squares=[]
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

# #or

# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

#########################################
# digits=[1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
###########################################list comprehensions ( A list comprehension combines the 
#for loop and the creation of new elements into one line, and automatically 
#appends each new element)
# squares =[value**2 for value in range(1,11)]
# print(squares)

# try it yourself page60
# for i in range(1,21):
#     print(i,end=" ")

# for i in range(1,1000001):
#     print(i,end=" ")

# numbers = list(range(1,1000001))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# for i in range (1,21,2):
#     print(i,end=" ")

# multiples=list(range(1,11))
# multiple = multiples**3
# print(multiples)

# list = []
# for i in range(1,11):
#     list.append(i**3)
# print(list)

# list=[cubes**3 for cubes in range(1,11)]#list comprehension for the above code
# print(list)

##############################################slicing of a list(it helps to work with individual element of a list )
# players=["ujwal","kunal","jitesh","bhavishya","rudra","argh","raghav"]
# print(players[0:3])
# print(players[1:3])
# print(players[0:])
# print(players[:3])
# print(players[3:])
# print(players[0:3])
# print(players[1:5:2])#third value indicate how many items(1 minus the given value)  to skip between items in the specified range.
# print(players[3:8:3])
# print("Here are the first four players on my team:")
# for player in players[:4]:
#     print(player.title())

#############################
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]#this is use to make separate copy list of another person now if we add anything in myfood it wil not include in myfriend food automatically .

my_foods.append("canoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)