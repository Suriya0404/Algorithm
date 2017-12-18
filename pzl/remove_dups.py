

def remove_dups(string1):
    seen = set()
    final_string = []
    for letter in string1:
        if letter not in seen:
            seen.add(letter)
            final_string.append(letter)

    return ''.join(final_string)

if __name__ == '__main__':
    print(remove_dups('tree traversal'))