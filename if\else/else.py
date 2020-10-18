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