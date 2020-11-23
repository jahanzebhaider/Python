print('Enter your name')
x=str(input())
print('hello MR '+x)

prompt='if tell uss'
prompt +='we are awsome'
print(prompt)

#7.1
print('which rental car do you want')
car=input()
print("i'm searching for "+ car)

#7.2
x=int(input('how many are their with you?'))
if x<=8:
    print('Table is ready')
else:
    print('WAIT table is getting ready')

#7.3
x=int(input('Enter any no'))
a=x%10
if a==0:
    print(f'{x} is MULTIPLES OF 10')
else:
    print(f'{x} is Ordinary no')

prompt="enter a city you want to visit"
prompt +="\n(Enter 'quit to exit the programe')"

while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print('I love to visit ' + city.title())
#print only not divisible by 2
curr_no=0
while curr_no <=10:
    curr_no +=1
    if curr_no%2==0:
        continue
    print(curr_no)

#7.4
messege='enter you pizza topping'
messege +="\n (enter quit to end the process)"
pixxa=''

while pixxa !='quit':
    pixxa=input(messege)

    if pixxa!='quit':
        print('yes we have mentioned '+pixxa.title()+' woluld you like to add something more')
print('please wait')
