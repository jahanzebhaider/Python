#coping list to another using while
unconfirmed_user=['ali','raza','haider']
confirmed_user=[]
print('List of uncomfirmed user:\n')
while unconfirmed_user:
    print(unconfirmed_user)
    current=unconfirmed_user.pop()
    print('Verifing...'+str(current))
    confirmed_user.append(current)

print('VERIFIRED USERS')
for confirmed_users in confirmed_user:
    print(confirmed_users)

#delete elemnt in list which end with d
# declare list
element_list = ['abc', 'def', 'dfv', 'acd', 'xyz']
print("List before deletion:", element_list)
# list index variable
index = 0
# iterate over the list
while index < len(element_list):
    # check if element begins with 'd'
    if element_list[index].endswith('d'):
        # remove it
        del(element_list[index])
    else:
        index += 1
# print list after deletion
print("List after deletion:", element_list)

#user input in dictionary
responses={}

start=True
while start:
    name=input('enter your name ')
    mountain=input('which mountain wiould you like to climb ')

    responses[name]=mountain
    play=input('would you like to play more YES/NO')

    if play=='NO'or play=='no':
        start=False

for names,mountains in responses.items():
    print(names+' world like to climb '+mountains)

    