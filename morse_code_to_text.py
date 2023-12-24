char_dict = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    " ":" "
}

x = input("Enter a morse coode that you want to translate into text. Enter a space between each letter.")

word_in_morse = [i for i in x.split(" ") if i in char_dict.values()]
print(word_in_morse)
indexes =  [list(char_dict.values()).index(i) for i in word_in_morse]
print(indexes)
plain_text = [list(char_dict.keys())[i] for i in indexes] 
print(plain_text)