def gunction(lname,fname='waqar'):
    print("my name is "+fname+ " " +lname)
gunction('jahanzeb')

#8.3
def get_tshirt(size,messege):
    print(f'your t shirt size is {size}')

get_tshirt(23,'hello')

# 8.5
def cities(city,country):
    print(f'{city} is in {country}')

cities('karachi','Pakistan')

# return vaues
def name(fname,lname):
    fullname=fname+lname
    return fullname

# ahmed contain the return value of function
ahmed=name('mark',' honda')
print(ahmed)


# function with id and else statement
def name(fname,lname,mname=''):
    if mname:
        fullname=fname+mname+lname
        return fullname
    else:
        fullname=fname+lname
        return fullname
ahmed=name('mark',' honda')
print(ahmed)


# dictionary in function
def name(fname,lname):
    person={'first_name':fname,'last_name':lname}
    return person

ahmed=name('mark',' honda')
print(ahmed)

# user input programe using while in function
def get_formatted_name():

    while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")

        f_name = input("First name: ")
        if f_name == 'q':
            break

        l_name = input("Last name: ")
        if l_name == 'q':
            break
    
        print('hello '+f_name+ ' '+l_name)


get_formatted_name()

# 8.6
def city(city,country):
    # print('"'+city+','+country+'"')
    return'"'+city+','+country+'"'

q=city('karachi','Pakistan')
print(q)
# city('New yORK','America')
# city('Tehran','Iran')

# 8.7
from typing import ItemsView


def veiw_album(arname,musictittle,track=0):
    album={'artis_name':arname,'musictittle':musictittle,'track':track}
    # return album

    if track:
        album['track']=track
        return album
    else:
        album={'artis_name':arname,'musictittle':musictittle,'track':track}
        return album
      

music=veiw_album('atif','hamsafar')
print(music)
music=veiw_album('atif','hamsafar',4)
print(music)
music=veiw_album('atif','hamsafar')
print(music)


# passing list in function
def bag(names):
    for name in names:
        msg= "hello " + name
        print(msg)

first=['jahanzeb','ali','zia']

bag(first)


# coping a list from one to another using function
def uncomp(uncomplete,completed):
    while uncomplete:
        currentdesign=uncomplete.pop()
        print('Folowing design are in process :'+currentdesign)
        completed.append(currentdesign)

def showcomp(completed):
    print('Folowing list is completed')
    for show in completed:
        print('completed ='+ show)

uncomplete=['iphone','watch','calculator']
completed=[]

uncomp(uncomplete,completed)
showcomp(completed)


# 8.9
def show_magician(magician):
    for show in magician:
        print(show)

magician=['Altaf','Hussain','Hussain']

show_magician(magician)

