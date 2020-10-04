#print tuples
a=('ali','waqar','saad')
print(a)


#printing tuple through for loop
for y in a:
    print(y)

#print through indexes
print(a[2])

#4.13
basics=('rotti','daal','chawal','chai')
for basics in basics:
    print(basics)

#rejecting yhe change in python this will generate error
# basics[0]='chicken'
# print(basics)
a="overwritng"
print(a.upper())
basics=('rotti','chicken','karhai','chai')
for basics in basics:
    print(basics)