smallest = None
print('Before')
for value in [9,41,23,45,63,1,7]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest =value
    print(smallest, value)
print('After', smallest)
