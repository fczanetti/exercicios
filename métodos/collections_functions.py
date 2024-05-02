from collections import Counter, defaultdict, namedtuple

# Creates a dictionary containing number of occurrences of each element.
ls = [1, 2, 3, 3, 3, 4, 4, 5, 5]
c = Counter(ls)
print(c)

print('-'*30)
print('Defaultdict')
dd = defaultdict(list)
print(dd)
dd['key1'].append('valor1')
dd['key1'].append('valor2')
dd['key2'].append('valor3')
print(dd)

print('-'*30)
print('Namedtuple')
car = namedtuple('car', 'price, year, color')
car_01 = car(22000, 2010, 'Blue')
print(car_01)
