import time
import sys

MORSE_CODE_DICTIONARY = { ' ':' ',
                          'A':'.-',
                          'B':'-...',
                          'C':'-.-.',
                          'D':'-..',
                          'E':'.',
                          'F':'..-.',
                          'G':'--.',
                          'H':'....',
                          'I':'..',
                          'J':'.---',
                          'K':'-.-',
                          'L':'.-..',
                          'M':'--',
                          'N':'-.',
                          'O':'---',
                          'P':'.--.',
                          'Q':'--.-',
                          'R':'.-.',
                          'S':'...',
                          'T':'-',
                          'U':'..-',
                          'V':'...-',
                          'W':'.--',
                          'X':'-..-',
                          'Y':'-.--',
                          'Z':'--..',
                          '1':'.----',
                          '2':'..---',
                          '3':'...--',
                          '4':'....-',
                          '5':'.....',
                          '6':'-....',
                          '7':'--...',
                          '8':'---..',
                          '9':'----.',
                          '0':'-----',
                          ', ':'--..--',
                          '.':'.-.-.-',
                          '?':'..--..',
                          '/':'-..-.',
                          '-':'-....-',
                          '(':'-.--.',
                          ')':'-.--.-'}


FLASH_CODE_DICTIONARY = { 'G':'.',
                          'R':'-',
                          ' ':' '}



def Text_to_Morse():
    txt = input('Enter Text to Convert to Morse: ')
    Converted_code = [MORSE_CODE_DICTIONARY[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICTIONARY.keys()]
    morse_code = ''.join(Converted_code)
    print(morse_code)

def Text_FLash_Text():
    text = input('Enter Text to Convert to Morse: ')
    print("INPUT TEXT : ", text)
    code = [MORSE_CODE_DICTIONARY[i.upper()] + ' ' for i in text if i.upper() in MORSE_CODE_DICTIONARY.keys()]
    morse_code = ''.join(code)
    print("\n")
    print("-----------------------------------------------------------------------------")
    print("Encrypting in morse code")
    time.sleep(1)
    print("Encryption Completed, Converted Morse Code:", morse_code)
    print("-----------------------------------------------------------------------------")
    flashlight_list = []
    for m in morse_code:
        if m == '.':
            flashlight_list.append("G")
        elif m == '-':
            flashlight_list.append("R")
        else:
            time.sleep(0.9)
            flashlight_list.append(" ")
    string_version = "".join(flashlight_list)


    print("Blinking Flashlight with respective to Morse.")
    print("flash-toggling  reconversion into Morse")
    print("\n")
    def blink_once():
        sys.stdout.write('\rFLASHLIGHT BLINKING * ')
        time.sleep(1)
        time.sleep(0.5)
        b = ("Loading")
        sys.stdout.write('\r                      ')
        time.sleep(0.7)


    def blink(number):
      for x in range(0, number):
        blink_once()
    blink(len(flashlight_list))

    new_code = [FLASH_CODE_DICTIONARY[i.upper()] + '' for i in string_version if i.upper() in FLASH_CODE_DICTIONARY.keys()]
    fLash_morse = ''.join(new_code)
    print("\n")
    print("-----------------------------------------------------------------------------")
    print("Reconverted Morse Code", fLash_morse)
    print("-----------------------------------------------------------------------------")
    code = [k for i in fLash_morse.split() for k, v in MORSE_CODE_DICTIONARY.items() if i == v]
    new_text = ''.join(code)
    print("-----------------------------------------------------------------------------")
    print("Decrypting  morse code")
    time.sleep(1)
    print("Decryption Completed, Converted TEXT:", new_text)
    print("-----------------------------------------------------------------------------")
    print("Encryption and Decryption Completed")



def Morse_to_Txt():
    morse = input('Enter Morse to Convert to Text: ')
    text = [k for i in morse.split() for k,v in MORSE_CODE_DICTIONARY.items() if i==v]
    new_text = ''.join(text)
    print(new_text)










print(
    '''
------------------------------------------------------------------------------    
     *        *        *           *  * *         * *        * * * * *
     * *   *  *      *   *         *      *     *            *
     *  * *   *    *       *       *     *      *            *
     *   *    *   *         *      * * *         *           * * *
     *        *    *       *       *    *           *        *
     *        *      *   *         *      *          *       *
     *        *        *           *       *     * *         * * * * *
------------------------------------------------------------------------------
    '''
)
print("Encryption and Decryption between users in Morse Code using a Flashlight.")
print("1. Encryption of Morse_Code")
print("2. Decryption of Morse_Code to text")
print("3. Encryption of Morse, using flashlight and Decrypting again in text")
selection = int(input('Select Your Choice: '))




if selection == 1:
    print(Text_to_Morse())

elif selection == 2:
    print(Morse_to_Txt())

elif selection == 3:
    print(Text_FLash_Text())


else:
    print('Wrong Selection, enter again')





