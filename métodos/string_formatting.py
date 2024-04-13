s = 'Texto'
print(s.rjust(15, '-'))
print(s.ljust(15, ' '))
print(s.center(15, '~'))
print('-'*30)

n = 25
print(f'{n:d}')  # Decimal format
print(f'{n:o}')  # Octal format
print(f'{n:x}')  # Hex format (lower case)
print(f'{n:X}')  # Hex format (upper case)
print(f'{n:b}')  # Binary format
print('-'*30)

n2 = 5
print(f'{n2:^10.2f}')  # Center, 10 spaces, float format and 2 decimal places
print(f'{n2:<10.2f}')  # Left aligned, 10 spaces, float format and 2 decimal places
print(f'{n2:>10.2f}')  # Right aligned, 10 spaces, float format and 2 decimal places
print('-'*30)
