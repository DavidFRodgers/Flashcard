#!/usr/bin/python3

import random
import os
import argparse
from colorama import Fore, Back, Style

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
    output_file = open(file_path, "w")
    for line in save_data:
        output_line = line.front + "$$$" + line.back + ":::" + str(int(line.complete))+ "\n"
        output_file.write(output_line)
    output_file.close()
    return()

def input_parse(status):
    ctrl_bool = False
    while ctrl_bool == False:
        if status == 1:
            print("[Correct? y/n]  (command): ", end='')
        elif status == 0:
            print("[Hit enter to continue] (command): ", end='')
        answer = input()
        mod_answer = answer + ":" + str(status)
        match mod_answer:
            case "y:1":
                data[incomplete_cards[card_number]].complete = True
                incomplete_cards.pop(card_number)
                ctrl_bool = True
            case "n:1":
                ctrl_bool = True
            case "save:0" | "save:1":
                print("")
                print("Saving Card Completion Status")
                print("")
                save_file(args.InputFile, data)
            case "exit:0" | "exit:1":
                exit()
            case "stats:0" | "stats:1":
                print(str(len(data) - len(incomplete_cards)) + "/" + str(len(data)) + " cards complete")
            case "help:0" | "help:1":
                print("")
                print("Available Commands:")
                print("     help: See this help")
                print("     save: Save card completion status to file")
                print("     exit: Exit the program")
                print("     stats: View how many cards are complete")
                print("")
            case ":0":
                ctrl_bool = True
            case other:
                print("Invalid Command")

def clear_screen():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')



#Parse commandline arguements using argparse
parser = argparse.ArgumentParser()
parser.add_argument("InputFile")
parser.add_argument("-o", action='store_true', help="create file that shows full cards")
parser.add_argument("-r", action='store_true', help="reverse flashcards (non functioning)")
parser.add_argument("--clear", action='store_true', help="set all flashcards as unfinished")
args = parser.parse_args() 



reverse = args.r 
outputfile = args.o

data = import_file(args.InputFile)

#if the --clear arguement is passed, the following code, to set all Flashcards as unfinished will run, and the program will exit

if args.clear == True:
    print("Setting All Flashcards as Incomplete")
    ctrl_int = 0
    while ctrl_int < len(data):
        data[ctrl_int].complete = False
        ctrl_int = ctrl_int + 1
    save_file(args.InputFile, data)
    exit()

#Make a list of cards. This list will be a list of line numbers
#indicating flash cards which have yet to be solved



incomplete_cards = []

for line_number, line in enumerate(data):
    if line.complete == False:
        incomplete_cards.append(line_number)

clear_screen()
print("Welcome to Flashcard")
print("Type 'help' for a list of commands")
#print("")

#Main program loop

while len(incomplete_cards) > 0:
    card_number = random.randrange(0,len(incomplete_cards))
    current_line = data[incomplete_cards[card_number]]
    print(card_number)

    #The following if statement will output the full card to a file called "outputfile" if the -o flag was given. This allows a second person to follow along who can see the full contents of the flashcard while the primary user only sees one side of it
#    if outputfile == True:
#        command = 'echo ' + current_line.front + " - " + current_line.back + " >> outputfile"
#        os.system(command)

    print("")
    print("Front:")
    print(Fore.BLUE + current_line.front + Style.RESET_ALL)
    print("")
    input_parse(0)

    clear_screen()
    
    print("")
    print("Front:")
    print(Fore.BLUE + current_line.front + Style.RESET_ALL)
    print("")
    print("Back:")
    print(Fore.YELLOW + current_line.back + Style.RESET_ALL)
    print("")

    input_parse(1)
    
    clear_screen()

print("All Flashcards Complete!")
print("Saving Card Completetion Status")
save_file(args.InputFile, data)




