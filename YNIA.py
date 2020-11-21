
# Array For Replacing to Arabic letters
arabic = ["ا", "ب" , "س", "د", "ي", "ف", "ج", "ه", "ي", "چ", "ك", "ل", "م", "ن", "و", "ب", "ك", "ر", "س", "ت", "يو", "ف", "و", "ك", "ي", "ز"]


def eTA(name):
    in_Arabic = ""
    counter = -1
    count = -1
    arr = []
    mname = name

    #To Stop The Game
    if name == "exit" or name == "Exit":
        return -1

    #loop to remove repeatitive letters that may cause problem in arabic
    for letter in name:
        count += 1
        if count == 0:
            arr.append(letter)
        elif letter == arr[-1]:
            mname = name.replace(name[count], "", 1)
        else:
            arr.append(letter)
    
    #Replacing English letters by Arabic letters
    for letter in mname:
        counter += 1
        
        #from line 32 to 94 for special pronunciation of english letters
        if letter in "ACcEeIHhSsuXxTt":
            if  letter == "A":
                in_Arabic += "أ"
            elif letter in "Cc":
                if mname[counter + 1] == "h":
                    in_Arabic += "ش"
                elif mname[counter + 1] in "eiy":
                    in_Arabic += "س"
                elif mname[counter + 1] == "k":
                    in_Arabic += ""
                else:
                    in_Arabic += "ك"
            elif letter in "EI":
                in_Arabic += "إ"
            elif letter in "Tt":
                in_Arabic += "ت"
                if mname.endswith("t"):
                    continue
                elif mname[counter + 1] == "h":
                    in_Arabic += "ث"
            elif letter == "e":
                if mname[counter - 1] in "aeiouXx":
                    in_Arabic += "ي"
                elif mname[counter -2] in "aeiou":
                    continue
            elif letter in "Hh":
                if mname[counter - 1] in "Ccst":
                    continue
                else:
                    in_Arabic += "ه"
            elif letter in "Ss":
                if mname.endswith("s"):
                    in_Arabic += "س"
                    continue
                if mname[counter + 1] == "h":
                    in_Arabic += "ش"
                else:
                    in_Arabic += "س"
            elif letter == "u":
                if mname[counter - 1] in "lrjntdszh":
                    if mname[counter -1] == "h" and mname[counter - 2] in "sct":
                        in_Arabic += "و"
                elif mname[counter -1] in "aeiou":
                    in_Arabic += ""
                elif mname.endswith("e"):
                    in_Arabic += "ي"
                    continue
                elif mname[counter + 1] and mname[counter + 2] not in "aeiou":
                    in_Arabic += "ي"
                else:
                    in_Arabic += "يو"
            elif letter in "x":
                if mname[counter - 1] in "aeiou":
                    in_Arabic += "كس"
                elif mname.endswith("x"):
                    continue
                elif mname[counter + 1] in "aeiouh":
                    in_Arabic += "كز"
                
                else:
                    in_Arabic += "ك"
            elif letter in "ZzX":
                in_Arabic += "ز"
        
        #For replacing letter by letter depending on the Ascci number & the Arabic array.
        elif ord(letter) in range(65, 90):
            letter_index = ord(letter) - 65
            in_Arabic += arabic[letter_index]
        elif ord(letter) in range(97, 122):
            letter_index = ord(letter) - 97
            in_Arabic += arabic[letter_index]
        
        #For any sympols or digits other than the normal letters
        else:
            in_Arabic += letter
            
    return in_Arabic

#Infinity loop to keep running the game
while True:
    print("Please Enter your name in english letters (Type exit to stop the game)",
    "\n **************************************")

    #Loop breaked if (exit) was typed
    result = eTA(input("Enter Your Name: "))
    if result == -1 :
        print("Thanks For playing with me ^_^")
        break

    else:
        print("Your Name In Arabic is: ", result, "\n ###################################### \n")