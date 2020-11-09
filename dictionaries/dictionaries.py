#defining dictionary
thisdic={
'brand':'toyota',
'model':2004,
'name':'revo'
}
#printing whole dictionary
print(thisdic)

#empty whole dictionary
thisdic.clear()
print(thisdic)
thisdic['model']=2004
thisdic['brand']='toyota'
thisdic['name']='revo'
print(thisdic)
print("i have a car which model is " +str(thisdic['model'])+'which gives me a good milage')


#this is a simple programe usinf dictionary and if and elif condition
alien={
    'x_position':0,
    'y_position':25,
    'speed':"medium"
}
print("Before programe "+str(alien['x_position']))
if alien['speed']=='slow':
    x_increment=5
elif alien['speed']=='medium':
    x_increment=10
else:
    x_increment=20
alien['x_position']=alien['x_position']+x_increment
print('Alien is moving with '+str(alien['x_position'] )+' on right')

#excercise 6.1
info={
    'firstname':"jahanzeb",
    'lastname':'haider',
    'age':20,
    'city':'karachi'
}
print(info)

#6.2
fno={
    'ali':3343363729,
    'walli':3343599020,
    'rakshi':3313560749
}
print(fno)


#printing dictionary using loop
user={
    'name':'jahanzeb',
    'lastn':'haider'
}
#this will print the key value only
for x in user:
    print(x)
#this will print the value only
for x in user:
    print(user[x])
#this will print the values using values function only
for x in user.values():
    print(x)
#this will print the values and keys using item function only
for x,y in user.items():
    print(x,y)
user['food']='biryani'
for x,y in user.items():
    print(x,y)
#this will remove item with specified name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict
)
thisdict.popitem()
print(thisdict)

#The del keyword can also delete the dictionary completely:
#del thisdict
#this will empty the string 
# thisdict.clear()

#copy of dictionary
mydic=user.copy()
print(mydic)

#nasted dictionaries
myfamily={
    'child1':{
        'name':'jahanzeb',
        'lname':'haider'
    },
    'child2':{
        'name':'waqar',
        'lname':'ahmed'
    },
    'child3':{
        'name':'mustafa',
        'lname':'qadri'
    }
}
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

favorite_lan={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'jen':'python'
}
for name in favorite_lan.keys():
    print(name.title()
    )

#print inorder through loop 
for name in sorted(favorite_lan):
    print(name.title()+' hello ')


#printing unique values
for language in set(favorite_lan.keys()):
    print(language.capitalize()+" All are unique keys value")


#6.5
river={
    'Egypt':'nile',
    'Pakistan':'Jhelum',
    'india':'ravi',
    'america':'sunset',
    'afganistan':'pathan'

}
for x,y in river.items():
    print(y.title()+' runs through'+ x.title())
for x in river.values():
    print(x)
for x in river.keys():
    print(x)

#a list of dictinary
# alien_1={'colour':'red','size':'big'}
# alien_2={'colour':'blue','size':'big'}
# alien_3={'colour':'pink','size':'small'}

# alien=[alien_1,alien_2,alien_3]

# print(alien)

alien=[]
for aliens in range(30):
    new_alein={'colour':'red','size':'medium'}
    alien.append(new_alein)

for y in alien[2:5]:
    if y['size']=='medium':
        y['colour']='black',
        y['size']='small'




for x in alien:
    print(x)
print('....')

print('Total no of alein :'+str(len(alien)))

pizza ={
    'crust':'thick',
    'topping':['mashrooms','chicken','cheese']
    
}
print('you orrdered pizza with ' + pizza['crust']+'with ')
for u in pizza['topping']:
    print(''+u)


favorite_lan={
'jen':['python','ruby'],
'sarah':['c'],
'edward':['ruby','go'],
'jen':['python','haskell']
}
for men,language in favorite_lan.items():
    print('\n'+men.capitalize() + 'favorite language :')
    for lan in language:
        print(lan)


users={

    'albert':{
        'name':'einstien',
        'location':'london'
    },
    'wassem':{
        'name':'badami',
        'location':'karachi'
    },
    'poja':{
        'name':'podina',
        'location':'Dehli'
    }

}
for u,i in users.items():
    print('Username'+u)
    fullname=i['name']+u
    location=i['location']
    print('Fullname:'+fullname.title())
    print('location:'+location
    )

for z in users.keys():
    print(z)

#6.8
dog={
    'owner':'waqar'

}
cat={
    'owner':'zakka'
}
pets=[dog,cat]
for i in pets:
    print(i)

#6.9
favorate_places={
    'ali':['new zeland','australia'],
    'maha':['turkey','karachi'],
    'jahanzeb':['northern areas']
}
for x,y in favorate_places.items():
    print('\n'+x.title()+'favorites places are :')
    for s in y:
        print(s.title())

#6.11
cities={
    'karachi':{
    'country':' pakistan ',
    "population": 34524555,
    'fact':" lovely"
    },
    'lahore':{
      'country':' pakistan ',
    "population": 20000,
    'fact':" donkey"
    },
    'islamabad':{
        'country':' pakistan ',
    "population": 10000,
    'fact':" burger"
    }

}
for x,y in cities.items():
    print('City:'+x+' details:')
    # details=y['country']+str(y['population'])+y['fact']
    # print(details)
    print(y['country'])
    print(str(y['population']))
    print(y['fact'])

