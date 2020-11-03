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
