#first method
N = int(input())
a = tuple([int(x) for x in input().split(maxsplit=N)])
print(hash(a))
#second method
N = int(input())
t = tuple(map(int, tuple(input().split(maxsplit=N))))
print(hash(t))