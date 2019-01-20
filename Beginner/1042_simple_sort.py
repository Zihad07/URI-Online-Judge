
a, b, c = map(int, input().split())

read_element = [a,b,c]
sorting_element = read_element[:]
sorting_element.sort()

for item in sorting_element:
    print(item)
print()

for item in read_element:
    print(item)
