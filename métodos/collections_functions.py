from collections import Counter, defaultdict, namedtuple, OrderedDict

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

print('-'*30)
print('OrderedDict')
od = OrderedDict()  # OrderedDict saves the order that its elements were input.
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
