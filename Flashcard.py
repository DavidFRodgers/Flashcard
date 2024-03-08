#!/usr/bin/python3

import sys
import random
import os
#import keyboard
import argparse

#Program Setup

class flashcard:
    front = ''
    back = ''
    complete = None

def import_file(file_path):

    data = []
    try:
        file_data = open(file_path, 'r')
    except:
        print("Invalid Input File")
        exit(1)
        
    for line in file_data.readlines():
        trans_line = flashcard()
        delim1 = line.find("$$$")
        delim2 = line.find(":::")
        trans_line.front = line[:delim1]
        trans_line.back = line[delim1 + 3:delim2]
        if int(line[delim2 + 3:]) == 0:
            trans_line.complete = False
        if int(line[delim2 + 3:]) == 1:
            trans_line.complete = True
        data.append(trans_line)
    return(data)




#Parse commandline arguements using argparse
parser = argparse.ArgumentParser()
parser.add_argument("InputFile")
parser.add_argument("-o", action='store_true', help="create file that shows full cards")
parser.add_argument("-r", action='store_true', help="reverse flashcards")
args = parser.parse_args() 



reverse = args.r 
outputfile = args.o

data = import_file(args.InputFile)

for line in data:
    print(line.front)
    print(line.back)
    print(line.complete)
    print("")

#     save_data = open(file_path, 'r')

#Make a list of cards. This list will be a list of line numbers
#indicating flash cards which have yet to be solved

'''


incomplete_cards = []

for line_number, line in enumerate(data):
    incomplete_cards.append(line_number)

#Main program loop

while len(incomplete_cards) > 0:
    print(incomplete_cards)
    card_number = random.randrange(0,len(incomplete_cards))
    current_line = data[incomplete_cards[card_number]]
    delim_position = current_line.find("$$$")
    if delim_position < 0: 
        print("Line " + str(incomplete_cards[card_number] + 1)  + " incompatable")
        incomplete_cards.pop(card_number)
    else:   
        #The following if statement will output the full card to a file called "outputfile" if the -o flag was given. This allows a second person to follow along who can see the full contents of the flashcard while the primary user only sees one side of it
        if outputfile == True:
            command = 'echo ' + current_line[:delim_position] + " - " + current_line[delim_position+3:].rstrip() + " >> outputfile"
            os.system(command)

        #os.system('clear')
        print(current_line[:delim_position])
        #print("Hit enter to continue:")
        input()
        os.system('clear')
        print(current_line.rstrip())
        print("correct? y/n")
        answer = input()
        if answer == 'y':
            incomplete_cards.pop(card_number) 

'''

