number_elements = int(input())
elements = tuple(map(int, (input()).split(maxsplit=number_elements)))
elements_hash = hash(elements)
print(elements_hash)