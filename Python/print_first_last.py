def print_full_name(first, last):
    sentence = f"Hello {first} {last}! You just delved into python."
    print(sentence)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)