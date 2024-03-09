#!/usr/bin/python3

#import sys
import random
import os
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
    file_data.close()
    return(data)

def save_file(file_path, save_data):
    os.system("> " + file_path + ".save")
    for line in save_data:
        output_line = line.front + "$$$" + line.back + ":::" + str(int(line.complete))
        os.system("echo '" + output_line + "' >> " + file_path + ".save")

    return()




#Parse commandline arguements using argparse
parser = argparse.ArgumentParser()
parser.add_argument("InputFile")
parser.add_argument("-o", action='store_true', help="create file that shows full cards")
parser.add_argument("-r", action='store_true', help="reverse flashcards")
args = parser.parse_args() 



reverse = args.r 
outputfile = args.o

data = import_file(args.InputFile)



#Make a list of cards. This list will be a list of line numbers
#indicating flash cards which have yet to be solved



incomplete_cards = []

for line_number, line in enumerate(data):
    if line.complete == False:
        incomplete_cards.append(line_number)

os.system('clear')
print("Welcome to Flashcard")
print("")

#Main program loop

while len(incomplete_cards) > 0:
    card_number = random.randrange(0,len(incomplete_cards))
    current_line = data[incomplete_cards[card_number]]

    #The following if statement will output the full card to a file called "outputfile" if the -o flag was given. This allows a second person to follow along who can see the full contents of the flashcard while the primary user only sees one side of it
    if outputfile == True:
        command = 'echo ' + current_line.front + " - " + current_line.back + " >> outputfile"
        os.system(command)

    print(current_line.front)
    ctrl_bool = False
    while ctrl_bool == False:
        print("[Hit enter to continue] ", end='')
        answer = input()
        if answer == "":
            ctrl_bool = True
    os.system('clear')
    print(current_line.front + " - " + current_line.back )
    
    ctrl_bool = False
    while ctrl_bool == False:
        print("[Correct? y/n] ", end='')
        answer = input()
        match answer:
            case "y":
                data[incomplete_cards[card_number]].complete = True
                incomplete_cards.pop(card_number)
                ctrl_bool = True
            case "n":
                ctrl_bool = True
            case "save":
                save_file(args.InputFile, data)
            case "exit":
                exit()
            case other:
                print("Invalid Command")
                print("Valid Commands: y, n, save, exit")

    os.system('clear')



