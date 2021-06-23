
import sys, getopt
import time
from pygame import mixer

mixer.init()
dit = mixer.Sound('dit.wav')
dah = mixer.Sound('dah.wav')
B = mixer.Sound('B.wav')

def playdit():
    dit.play()
    #time.sleep(delay * 0.18)

def playb():
    B.play()

def playdah():
    dah.play()
    #time.sleep(delay * 0.35)


def main(file):


    # read textfile into string 
    with open(file, 'r') as txtfile:
        mytextstring = txtfile.read()

   
    # change text into a binary array
    a_byte_array = bytearray(mytextstring, "utf8")


    byte_list = []

    for byte in a_byte_array:

        binary_representation = bin(byte)
        byte_list.append(binary_representation)


    byte_string = ' '.join(str(e) for e in byte_list )


    print(byte_string)
    for b in byte_string:
        if b == "b": 
            playb()
            time.sleep(0.5)
        #plays 0 
        elif b == "0": 
            playdah()
            time.sleep(0.5)
        #Plays 1
        elif b == "1":
            playdit()
            time.sleep(0.5)
        elif b == " ":
            time.sleep(1)
        else:
            print(b)
            print("Character not recognised")

        
# Executes the main function
if __name__ == '__main__':
    main(sys.argv[1])