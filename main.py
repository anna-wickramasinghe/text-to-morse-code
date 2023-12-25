from converter import Converter
#imptr

converter = Converter()

flag =True 

while flag:
    
    choice = input("Choose 'E' to encode a plain text into Morse or choose 'D' to decode a Morse code or 'Q' to quit': ").upper()
    
    if choice == 'E':
        
        text_to_convert = input("Input the text that you wish to convert into Morse code: ")
        morse_code_result = converter.text_to_morse(text_to_convert)
        print("Morse Code:", morse_code_result)
    
    elif choice == 'D':
        morse_to_decode = input("Enter a Morse code that you want to translate into text. Enter a space between each letter: ")
        decoded_text_result = converter.morse_to_text(morse_to_decode)
        print("Decoded Text:", decoded_text_result)
        
    elif choice == 'Q':
        flag = False
    
    else:
        print("Invalid Entry")
    



