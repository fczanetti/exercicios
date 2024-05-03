# You have a list of  items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

from collections import OrderedDict

od = OrderedDict()
N = int(input())
for _ in range(N):
    pi = input().rsplit(' ', maxsplit=1)
    if not pi[0] in od:
        od[pi[0]] = int(pi[1])
    else:
        od[pi[0]] += int(pi[1])
for k, i in od.items():
    print(k, i)
