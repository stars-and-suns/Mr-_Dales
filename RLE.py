def RLE(string:str, compress_ones:bool = False) -> str:
    compressed = ''
    # creating a dictionary
    sections = {}

    # checking if the length is 1 as otherwise it would not enter the for loop
    if len(string) == 1:
        compressed = f'{string}1'

    else:
        for char in range(len(string)-1):
            # if the letter is not in the dictionary, it is added
            if string[char] not in sections:
                sections[f"{string[char]}"] = 1

            # if the letter is already in the dictionary, the value is incremented
            if string[char] == string[char + 1]:
                sections[f'{string[char]}'] += 1

        # for loop doesnt go to last letter, so if it is different, it is added
        if string[-1] not in sections:
            sections[f"{string[-1]}"] = 1

        # goes through dictionary, joins the key and value and then adds it to the final string
        for key,value in sections.items():
            line = ''.join(str(key) + str(value))
            compressed += line

        # in one line:
        # compressed = "".join(str(key) + str(value) for key, value in sections.items())

    # if removal of 1s was requested, they are removed
    if compress_ones == True:
        compressed = compressed.replace('1', '')

    return compressed

print(RLE('ABA'))