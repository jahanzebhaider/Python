names=['jahanzeb','haider','ali']
print(names[1].upper())
print(names[0].title())
print(names[2].lower())
# will return the last element in thw list
print(names[-1])

#concatinatiojn in lists
print("My name is " + names[0].title() + names[1].title())


# changing data in list
cars=['honda','suzuki','mazada','bmw']
print(cars)
cars[0]='toyota'
print(cars)

# inserting data into list at the end o list
cars.append(45)
print(cars)

# inserting data in starting  of a list 
cars.insert(2,45)
print(cars)

#deleting ele,ent in list using del statement
cars=['honda','suzuki','mazada','bmw']
del cars[1]
print(cars)



# removing an item from the list using pop method it help us to store the remove value
cars=['honda','suzuki','mazada','bmw']
print(cars)
rev_car=cars.pop(1)
print(cars)
print("the removed element was " + rev_car.title())

#excersice 
guest=['mustafa','warda','irfan']
print("hello " + guest[0] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[1] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[2] + " you are invited for dinner tommorow at half past 5" )
guest[1]="maha"
print("hello " + guest[0] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[1] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[2] + " you are invited for dinner tommorow at half past 5" )
guest.insert(0,'ali')
guest.insert(0,'talha')
guest.insert(0,'umair')
print(guest)
print("hello " + guest[0] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[1] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[2] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[3] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[4] + " you are invited for dinner tommorow at half past 5 \n" + "hello " + guest[5] + " you are invited for dinner tommorow at half past 5" )
print("You can only invite 2 person for dinner ")
one_rev=guest.pop()
print("SORRY " + one_rev + " you are not invited")
sec_rev=guest.pop()
print("SORRY " + sec_rev + " you are not invited")
thd_rev=guest.pop()
print("SORRY " + thd_rev + " you are not invited")
for_rev=guest.pop()
print("SORRY " + for_rev + " you are not invited")
print(guest)
print("hy " + guest[0] + " you are still invited " +"hy " + guest[1] + " you are still invited ")
del guest[0]
print(guest)
del guest[0]
print(guest)

# string sorting alphabaticly
laptop=['dell','hp','accer','intel']
laptop.sort()
print(laptop)