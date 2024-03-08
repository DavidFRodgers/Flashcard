#!/usr/bin/python3

import sys
import random
import os
import keyboard
import argparse

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

#Parse commandline arguements using argparse
parser = argparse.ArgumentParser()
parser.add_argument("InputFile")
parser.add_argument("-o", action='store_true', help="create file that shows full cards")
parser.add_argument("-r", action='store_true', help="reverse flashcards")
args = parser.parse_args() 



reverse = args.r 
outputfile = args.o

data = import_file(args.InputFile)
data_file = (args.InputFile)


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
