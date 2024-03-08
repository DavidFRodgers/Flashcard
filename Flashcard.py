#!/usr/bin/python3

import sys
import random
import os
import keyboard

#Program Setup


def import_file(file_path):
    try:
        data = []
        file_data = open(file_path, 'r')
        for line in file_data.readlines():
            data.append(line)
        return(data)

    except:
        print("Invalid Input File")
        exit(1)

reverse = False
outputfile = False

loopint = 0

while loopint < len(sys.argv):
    print(loopint)
    loopint = loopint +1




if len(sys.argv) > 3:
    print("Too many arguements")
    exit(1)

elif len(sys.argv) == 1:
    print("No Input File")
    exit(1)

elif len(sys.argv) == 2:
    data = import_file(sys.argv[1])
    data_file = sys.argv[1]

elif len(sys.argv) == 3:
    data = import_file(sys.argv[2])
    data_file = sys.argv[2]

    if sys.argv[1] == '-r':
        reverse = True
    elif sys.argv[1] == '-o':
        outputfile = True
    elif sys.argv[1] == '-ro':
        reverse = True
        outputfile = True
    else:
        print("Invalid Arguements")
        exit(1)

#Make a list of cards. This list will be a list of line numbers
#indicating flash cards which have yet to be solved


if os.path.exists(data_file + ".save") == True:
    print("yes")
 

incomplete_cards = []

for line_number, line in enumerate(data):
    incomplete_cards.append(line_number)

#Main program loop

while len(incomplete_cards) > 0:
    card_number = random.randrange(0,len(incomplete_cards))
    current_line = data[incomplete_cards[card_number]]
    delim_position = current_line.find("$$$")
    if delim_position < 0: 
        print("Line " + str(incomplete_cards[card_number] + 1)  + " incompatable")
        incomplete_cards.pop(card_number)
    else:   
        if outputfile == True:
            command = 'echo ' + current_line[:delim_position] + " - " + current_line[delim_position+3:].rstrip() + " >> outputfile"
            os.system(command)

        os.system('clear')
        print(current_line[:delim_position])
        #print("Hit enter to continue:")
        input()
        os.system('clear')
        print(current_line.rstrip())
        print("correct? y/n")
        answer = input()
        if answer == 'y':
            incomplete_cards.pop(card_number)
