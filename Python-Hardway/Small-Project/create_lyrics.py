# import os to use exists(path)
import os

# Class to Create File, Write, and Read Songs


class Song(object):

    # * init function
    def __init__(self, title):
        self.title = title
        # ? filepath with filename to create our file
        self.filepath = os.path.join(
            r'C:\Users\Kael\Documents\GitHub\PythonRep\Python-Hardway\Small-Project\File_Lyrics', f'{title}.txt')
        self.file, self.bool = self.createFile(self.filepath)

    # function to create file if the title didnt exist in filePath

    def createFile(self, title):
        isExisting = os.path.exists(title)
        if not isExisting:
            print("File Created!")
            return open(self.filepath, 'w+'), False
        else:
            print("File Already Existing")
            return open(self.filepath, 'r+'), True

    # Function to write lyrics on the file

    def writeLyrics(self, lyrics):
        file = open(self.filepath, 'w+')
        for line in lyrics:
            file.write(line)
            file.write("\n")

    # Function to Display the lyrics inside the file

    def displayLyrics(self):
        songLyrics = open(self.filepath).read()
        print(songLyrics)


# Main function
def introduction():
    # Introduction
    # ask your name first, gender, honorifics, greetings.
    greetings()
    # - - - - -- -- - - - - - -- -


def askName():
    print("Please input your name")
    return input("Here -> ")


def askGender():
    print("Are you a Male or Female?")
    return input("M or F: ")


def honorifics():
    name = askName()  # receive inputted name
    gender = askGender()  # receive inputted gender

    global honorifics
    if gender == 'M' or gender == 'm':
        return f'Mr. {name}'  # return honorifics
    elif gender == 'F' or gender == 'f':
        return f'Miss {name}'
    else:
        return f'Non Binary: {name}'


def greetings():
    genderName = honorifics()  # received the honorifics
    print(f"Hello there {genderName}")  # print
    welcome()


def welcome():
    print("""
                Welcome to Create Lyrics Program
        You can Create a File and Write a Lyrics From that File
                        Please Enjoy!!!
    """)


def askUser():
    return input('>Do you want me to Display the Lyrics? Y/N: ')


def inputLyrics():
    print("\tType S to stop if you are done")
    print("And what is the Lyrics for this song?")
    count = 1
    lyrics_arr = []
    while True:
        lyrics = input(f"L{count} Lyrics>")
        count = count + 1

        if lyrics == 'S' or lyrics == 's':
            break
        else:
            lyrics_arr.append(lyrics)
            continue

    return lyrics_arr  # todo: return arr[] for writingLyrics in Song classs


# Main Process and Loop for asking
introduction()  # intro
while True:
    print("What is the song title")
    title = input("> ")
    song = Song(title)

    if song.bool == True:
        answer = askUser()
        if answer == 'Y' or answer == 'y':
            song.displayLyrics()
    elif song.bool == False:
        song.writeLyrics(inputLyrics())
        # ? return the inputLyrics array and pass it into the writeLyrics
    else:
        print("ERROR")

    # If still want to input a song
    question = input("> Do you still want to input a song? Y/N: ")
    if question == 'Y' or question == 'y':
        welcome()
        continue
    else:
        break
