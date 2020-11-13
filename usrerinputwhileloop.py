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