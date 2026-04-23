# task 4 emmail slicer

email= input('Enter email:')
slice_point= email.find('@')
name= email[0:slice_point]
domain= email[slice_point+1:]

print('Name: ', name)
print('Domain', domain)
