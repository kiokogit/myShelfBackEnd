# try tuples and dicts

dict1 = {'one':1, 'two':2, 'tree':('model','serializer'), 'four':4}

print(dict1['one'])

for keys in dict1:
    print(keys)
    if keys=='two':
        print('FOUND ONE')
        
for keys in dict1:
    if keys=='tree':
        print(dict1[keys])
    
        
for keys in dict1:
    if keys=='tree':
        print(dict1[keys][0])

props=dict1['tree'][0]
propsSecond=dict1['tree'][1]
props1, props2=dict1['tree'][0], dict1['tree'][1],

print(props)
print(propsSecond)
print(props1)
print(props2)

new = {'show':'Breaking Bad'}
dict1.__setitem__('Show',new)
print(dict1)
