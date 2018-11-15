from subprocess import check_call
from sys import platform, argv
from random import randint
from os import path

def copy_to_clip(string):
    if(platform == 'darwin'):
        cmd='echo \"' + string.strip()+'\" | pbcopy'
    else:
        cmd='echo \"' + string.strip()+'\" | clip'
    return check_call(cmd, shell=True)

def convert_to_spongecase(text):
    userInput = text.lower()
    spongeString = ""
    for i in range(0,len(userInput)):
        if not userInput[i].isalpha():
            spongeString = spongeString + userInput[i]
            continue
        if(randint(0,100) > 50):
            spongeString = spongeString + userInput[i].upper()
        else:
            spongeString = spongeString + userInput[i]
    return spongeString

firstLoop = False
while(1):
    userInput = ""
    if(len(argv) == 2 and not firstLoop):
        userInput = argv[1]
        firstLoop = True
    else:
        userInput = input('Enter the string or file name to switch to sponge case. Ctrl + C or "!exit!" to quit program.\n')
    spongeString = ""
    if(userInput == '!exit!'):
        exit()
    if(path.isfile(userInput)):
        inputFile = open(userInput, "r")
        spongeString = convert_to_spongecase(inputFile.read())
        inputFile.close()
        newFile = open(path.splitext(userInput)[0] + '_spongeCase.txt', "w+")
        newFile.write(spongeString)
        newFile.close()        
    else:
        spongeString = convert_to_spongecase(userInput)

    
    print(spongeString)
    try:
        copy_to_clip(spongeString)
        print("*Sponge case (probably) copied to clipboard.*")
    except:
        continue
        #do nothing

    