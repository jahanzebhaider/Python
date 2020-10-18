#THIS CODE WILL PRINT THR HONDA CAR WITH UPPER CASE AND REST WITH LOWER CASE ALPHABETS
cars=['audi','bmw','honda','toyota','suzuki']
for car in cars:
    if car =='Honda':
        print(car.upper())
    else:
        print(car.lower())

# checking nother of checking in list
if 'ponks'  in cars:
    print("it's not their")
elif 'bmw' not in cars:
    print('it is their')


names=['ali','ahmed','muetaza']
if names !='ali':
    print('their is no  ali present in list')

#checking if for numerical value
no=17
if no ==17:
    print('no is present')
else:
    print('no is not present')

marks=80
if marks>70 and marks<100:
    print('A')
else:
    print('Fail')        


#price for diff student
age=input('Enter your age')
age=int(age)
if age<5:
    print("YOU ARE NOT ELIGIBLE")
elif age<10:
    price=10
    print('your age is ' + str(age) +".Your admission fees is"+ str(price))
elif age<18:
    price=0
    print('your age is ' + str(age) +".Your admission fees is"+ str(price))

#using in statement in if condition
pizza=['mashroom','cheese']
if 'mashroom' in pizza:
    print('pizza is ready')
elif 'pepproni' in pizza:
    print('pizza will take time')
else:
    print('pizza')

#alien game 0.1
alien_colour=['red','yellow','green']
if 'green' in alien_colour:
    print('You Earned 5 points')
    
elif 'yellow'  in alien_colour:
    print('Your earned 10 points')
elif 'red' in alien_colour:
    print('you earned 15 ponts')

#stages of life
age=89
if age<2:
    print('you are a baby')
elif age >=2 and age<4:
    print('toddller')
elif age >=4 and age<13:
    print('kid')
elif age >=13 and age<20:
    print('teenager')
elif age >=20 and age<65:
    print('addult')
else:
    print('Elder')

#favorite food
favorite_food=['banana','apple','mango']
for favorite_food in favorite_food:
    if favorite_food=='BANANA':
        print('Sorry we ran out of '+favorite_food)
    else:
        print('Adding' + favorite_food)
print('THNAK YOU')   

#checking a list is not empty
requested_topping=[]
if requested_topping:
    for requested_topping in requested_topping:
         print('Adding'+requested_topping)
    print('Pizza is finished')
else:
    print('yopu want pizza with no topping')

#using multiples list in python
avl_topping=['mashroom','olives','green peepers','pepporni','pineapple','extra cheese']
requested_topping=['mashrooms','french fries','extra cheese']
for requested_topping in requested_topping:
    if requested_topping in avl_topping:
        print(requested_topping+ 'added to your pizza')
    else:
        print('Sorry we dont have '+requested_topping)
print('Thank you for choosing piza hut pakistan')

#5.8
user_name=['jahanzeb','admin','waqas','hassan','mustafa']
for user_name in user_name:
    if user_name == 'admin':
        print('Hello' +user_name+'would you like to see a status report')
    else:
        print('Hello ' +user_name+' ging and ging')
if user_name:
    for user_name in user_name:
        print('Hello' +user_name+'ging and ging')
else:
    print('no user is present in list')

# 5.9
current_users=['jahanzeb','admin','waqas','hassan','mustafa']
new_user=['moni','hassan','hani','moazam','admin']
for new_user in new_user:
    if new_user in current_users:
        print(new_user + 'is already takken please take another one')
    else:
        print(' user name available')

# 5.10
uni=[1,2,3,4,5,6,7,8,9]
for uni in uni:
    print(str(uni) + 'th')

