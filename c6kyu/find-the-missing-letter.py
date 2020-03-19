from string import ascii_lowercase, ascii_uppercase


def find_missing_letter(chars):
    start_pos = ascii_lowercase.index(chars[0].lower())
    for i, letter in enumerate(chars):
        if letter.lower() != ascii_lowercase[start_pos + i]:
            return ascii_lowercase[start_pos + i] if chars[0] in ascii_lowercase \
                else ascii_uppercase[start_pos + i]

if __name__ == "__main__":
    print(find_missing_letter(find_missing_letter(['a','b','c','d','f'])))