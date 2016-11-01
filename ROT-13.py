def encode(code):
    import string
    code = code.upper()
    alpa_biet = (list(string.ascii_uppercase))
    new_code = []
    for i in range(len(code)):
        letter = code[i]
        if letter.isalpha():
            letter_index = alpa_biet.index(letter)
            new_letter = alpa_biet[(letter_index+13)%len(alpa_biet)]
        else:
            new_letter = letter
        new_code.append(new_letter)
    return ''.join(new_code)

def decode(code):
    import string
    code = code.upper()
    alpa_biet = (list(string.ascii_uppercase))
    new_code = []
    for i in range(len(code)):
        letter = code[i]
        if letter.isalpha():
            letter_index = alpa_biet.index(letter)
            new_letter = alpa_biet[(letter_index-13)%len(alpa_biet)]
        else:
            new_letter = letter
        new_code.append(new_letter)
    return ''.join(new_code)



print(encode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))
print(decode('I AM LEARNING PYTHON WITH SHE CODES ACADEMY!'))




