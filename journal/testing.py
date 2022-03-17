# try tuples and dicts
dict1 = {'one':'1', 'two':'2', 'tree':'58', 'four':'4'};

print(dict1['one']);

sum = '';

for keys in dict1:
    print(keys);
    sum += dict1[keys];
    print(sum);
    if keys=='two':
        print('FOUND ONE');

for keys in dict1:
    if keys=='tree':
        print(dict1[keys]);

for keys in dict1:
    if keys=='tree':
        print(dict1[keys][0]);

props=dict1['tree'][0];
propsSecond=dict1['tree'][1];
props1, props2=dict1['tree'][0], dict1['tree'][1];

print(props);
print(propsSecond);
print(props1);
print(props2);

dict1.__setitem__('show','Breaking Bad');
print(dict1);
print(dict1.__getitem__('show'));
print('Live as if you were not chased \nbecause you cannot stand being chased \n\nby a monkey')
