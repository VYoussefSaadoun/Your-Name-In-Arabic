
def ETA(name):
    in_Arabic = ""
    counter = -1
    count = -1
    arr = []
    print(name)
    for letter in name:
        count = count + 1
        if count == 0:
            arr.append(letter)
        elif letter == arr[-1]:
            mname = name.replace(name[count], "", 1)
        else:
            arr.append(letter)
    print(mname)
    for letter in mname:
        counter = counter + 1
        if  letter == "A":
            in_Arabic += "أ"
        elif letter == "a":
            in_Arabic += "ا"
        elif letter in "BbPp":
            in_Arabic += "ب"
        elif letter in "Cc":
            if name[counter + 1] == "h":
                in_Arabic += "ش"
            elif name[counter + 1] in "eiy":
                in_Arabic += "س"
            else:
                in_Arabic += "ك"
        elif letter in "Dd":
            in_Arabic += "د"
        elif letter in "EI":
            in_Arabic += "إ"
        elif letter == "e":
            if name[counter - 1] in "aeiou":
                in_Arabic += "ي"
            elif name[counter -2] in "aeiou":
                continue
        elif letter in "Ff":
            in_Arabic += "ف"
        elif letter in "GgJj":
            in_Arabic += "ج"
        elif letter in "Hh":
            if name[counter - 1] in "Ccst":
                continue
            else:
                in_Arabic += "ه"
        elif letter == "i":
            in_Arabic += "ي"
        elif letter in "Kk":
            in_Arabic += "ك"
        elif letter in "Ll":
            in_Arabic += "ل"
        elif letter in "Mm":
            in_Arabic += "م"
        elif letter in "Nn":
            in_Arabic += "ن"
        elif letter == "O":
            in_Arabic += "أ"
        elif letter == "o":
            in_Arabic += "و"
        elif letter in "Qq":
            in_Arabic += "ك"
        elif letter in "Rr":
            in_Arabic += "ر"
        elif letter in "Ss":
            if name[counter + 1] in "h":
                in_Arabic += "ش"
            else:
                in_Arabic += "س"
        elif letter in "Tt":
            in_Arabic += "ت"
        elif letter == "U":
            in_Arabic += "أ"
        elif letter == "u":
            if name[counter - 1] in "lrjntdszh":
                if name[counter -1] == "h" and name[counter - 2] in "sct":
                    in_Arabic += "و"
            elif name[counter -1] in "aeiou":
                in_Arabic += ""
            elif name[counter + 1] and name[counter + 2] not in "aeiou":
                in_Arabic += "ي"
            
            else:
                in_Arabic += "يو"
        elif letter in "Vv":
            in_Arabic += "ف"
        elif letter in "Ww":
            in_Arabic += "و"
        elif letter in "x":
            if name[counter + 1] in "aeiouh":
                in_Arabic += "كز"
            elif name[counter - 1] in "aeiou":
                in_Arabic += "كس"
            else:
                in_Arabic += "ك"
        elif letter in "Yy":
            in_Arabic += "ي"
        elif letter in "ZzX":
            in_Arabic += "ز"
        
    return in_Arabic

print(ETA(input("Enter Your Name: ")))