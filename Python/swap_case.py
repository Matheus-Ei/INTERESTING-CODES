def swap_case(s):
    s = list(s)
    swapped = ""

    for e in s:
        if e == e.lower():
            swapped = swapped + str(e.upper())
        elif e == e.upper():
            swapped = swapped + str(e.lower())

    return swapped

if __name__ == '__main__':
    sentence = str(input())
    print(swap_case(sentence))