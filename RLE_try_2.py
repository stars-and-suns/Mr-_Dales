def RLE(string:str, compress_ones:bool = False) -> str:
    letters = [' ']
    repeats = [0]
    output = ''

    for i in string:
        if i != letters[-1]:
            letters.append(i)
            repeats.append(1)
        else:
            repeats[-1] += 1

    letters.pop(0)
    repeats.pop(0)

    for i in range(len(letters)):
        if compress_ones == True:
            if repeats[i] == 1:
                output += letters[i]

            else:
                output += letters[i] + str(repeats[i])
        else:
            output += letters[i] + str(repeats[i])

    return output
