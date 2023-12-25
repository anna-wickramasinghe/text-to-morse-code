class Converter:
    def __init__(self):
        self.char_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            " ": " "
        }

    def text_to_morse(self, text):
        return " ".join([self.char_dict[i] for i in text.upper() if i in self.char_dict])
    
    def morse_to_text(self, morse_code):
        word_in_morse = [i for i in morse_code.split(" ") if i in self.char_dict.values()]
        indexes = [list(self.char_dict.values()).index(i) for i in word_in_morse]
        plain_text = [list(self.char_dict.keys())[i] for i in indexes]
        return "".join(plain_text)

