
import time
from pygame import mixer

mixer.init()
dit = mixer.Sound('dit.wav')
dah = mixer.Sound('dah.wav')
delay = 1
from funny_morse import *

MORSE_CODE_DICT = { 'B':'-...',
                    '1':'.',
                    '0':'-'}
  
# Function to encrypt the string
# according to the morse code chart

def playdit():
    dit.play()
    time.sleep(delay * 0.18)


def playdah():
    dah.play()
    time.sleep(delay * 0.35)

def encrypt(message):
    cipher = ''
    for letter in message:
         
        if letter != ' ':
  
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += '  '
  
    return cipher
  
# Function to decrypt the string
# from morse to english
def decrypt(message):
  
    # extra space added at the end to access the
    # last morse code
    message += ' '
  
    decipher = ''
    citext = ''
    for letter in message:
  
        # checks for space
        if (letter != ' '):
  
            # counter to keep track of space
            i = 0
  
            # storing morse code of a single character
            citext += letter
  
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
  
            # if i = 2 that indicates a new word
            if i == 2 :
  
                 # adding space to separate words
                decipher += ' '
            else:
  
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
  
    return decipher

def main():


    # read textfile into string 
    with open("sneaky_text.txt", 'r') as txtfile:
        mytextstring = txtfile.read()
   
    # change text into a binary array
    a_byte_array = bytearray(mytextstring, "utf8")


    byte_list = []

    for byte in a_byte_array:

        binary_representation = bin(byte)
        byte_list.append(binary_representation)


    byte_string = ' '.join(str(e) for e in byte_list )


    print(byte_list)

    message = byte_string
    result = encrypt(message.upper())
    f = open("sneakyMorse.txt", "a")
    f.write(result)
    f.close()

    for i in result:
        #plays 0 
        if i == "-": 
            playdah()
            time.sleep(0.1)
        #Plays 1
        elif i == ".":
            playdit()
            time.sleep(0.1)

        #Plays the B
        elif i == "-...": 
            playdah()
            playdit()
            playdit()
            playdit()
            time.sleep(0.1)
        
# Executes the main function
if __name__ == '__main__':
    main()