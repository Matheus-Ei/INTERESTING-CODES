if __name__ == '__main__':
    elements = []
    for _ in range(int(input())):
        command, *numbers = input().split() # Splits the input between command and the rest in the numbers
        numbers = list(map(int, numbers)) # Transforms each element of the list to int

        match command:
            case "insert":
                elements.insert(numbers[0], numbers[1])
            case "remove":
                elements.remove(numbers[0])
            case "print":
                print(str(elements))
            case "append":
                elements.append(numbers[0])
            case "sort":
                elements.sort()
            case "pop":
                elements.pop()
            case "reverse":
                elements.reverse()