import os
import shutil
from datetime import datetime


def main_menu():
    print("Welcome to the main menu. "
          "Please make a choice\n"
          "1. Sort files by extensions\n"        #Main menu screen
          "2. Sort files by date\n" 
          "3. Move files to the directory\n"
          "4. Quit")

    try:
        menu_choice = int(input("\n"))   #Asks users choice
        if menu_choice == 1:
            file_extension_sorter() #Sorts files by extensions
        elif menu_choice ==2:
            file_date_sorter() #Sorts files by dates
        elif menu_choice ==3:
            undo() #Moves all files to the directory
        elif menu_choice ==4:
            print("Quitting...") #Ends task
            return 1
        else:
            print("Please try again with a valid number")  #Warns user if invalid number is entered
            main_menu()
    except: #Prevents errors
        print("Please try again with numbers\n")
        main_menu()

def file_extension_sorter(): #It sorts all files by extensions
    try:

        directory = input("Please enter the directory to sort the files\n"      #This variable gets the directory to sort the files
                          "To go back to main menu type quit\n")
        if directory.lower() == 'quit':
            main_menu()
            return 0
        os.chdir(directory) #Sets the directory
        folderlist = [] #Holds all folders
        filelist = [] #Holds all files
        all = os.listdir() #Holds everything
        for extensionfolder in os.listdir():
            if os.path.isdir(extensionfolder) == True: #Checks every index if it's a folder
                all.remove(extensionfolder)            #If it's a folder it removes it from "all" so when it comes to creating files, it won't be a problem

        for files in all:
            all_extensions=(files.split(".")[-1]) #Extracts each files extension
            if os.path.isdir(all_extensions) == False: #Checks if there is any folder with the same name as extension
                os.mkdir(all_extensions)               #If not, it will create a new folder with the extensions name

        for everything in os.listdir():
            isfile = os.path.isfile(everything)     #The variable that identifies every file
            if isfile == False:               #If "everything" isn't a file,
                folderlist.append(everything) #It adds "everything" to folderlist
            elif isfile == True:              #If it is,
                 filelist.append(everything)  #It adds "everything" to filelist

        for files in filelist:
            filesplit = (files.split(".")[-1])      #Extracts each files extension
            if filesplit in folderlist:       #If files extension in "folderlist",
                shutil.move(files, filesplit) #It moves the file to the folder which has the files extension name

        print("All files are successfully sorted by extensions\n"
              "Going back to main menu...")
        main_menu()
    except:
        print(f"The directory '{directory}' is incorrect try again")
        file_extension_sorter()

def file_date_sorter():
    try:
        directory = input("Please enter the directory to sort the files\n"      #This variable gets the directory to sort the files
                          "To go back to main menu type quit\n")
        if directory.lower() == 'quit':
            main_menu()
            return 0
        os.chdir(directory) #Sets the directory
        folderlist = [] #Holds all folders
        filelist = [] #Holds all files
        all = os.listdir() #Holds everything

        for extensionfolder in os.listdir():
            if os.path.isdir(extensionfolder) == True: #Checks every index if it's a folder
                all.remove(extensionfolder)            #If it's a folder it removes it from "all" so when it comes to creating files, it won't be a problem

        for files in all:
            creation_date = str(datetime.fromtimestamp(os.path.getmtime(files)))
            creationsplit = creation_date.split(" ")[0] #Extracts each files creation dates
            if os.path.isdir(files) == False and creationsplit not in os.listdir(): #Checks if there is any folder with the same name as the date
                    os.mkdir(creationsplit)                                         #If not it creates a new folder with which will be named as the date

        for files in os.listdir():
            creation_date = str(datetime.fromtimestamp(os.path.getmtime(files)))
            creationsplit = creation_date.split(" ")[0]
            if os.path.isdir(files) == True: #If "files" is a file
                folderlist.append(files)     #It adds "files" to "folderlist"
            else:                            #If it is not
                filelist.append(files)       #Then it will add "files" to "filelist"

        for files in filelist:
            creation_date = str(datetime.fromtimestamp(os.path.getmtime(files)))
            creationsplit = creation_date.split(" ")[0]
            if creationsplit in folderlist: #Makes sure that the file will go to the right folder
                shutil.move(files,creationsplit) #It moves file to the folder

        print("All files are successfully sorted by date\n"
              "Going back to main menu...")
        main_menu()
    except:  # Prevents errors
        print(f"The directory '{directory}' is incorrect try again")
        file_date_sorter()

def undo():  # It moves all files to the directory,
    try:
        directory = input("Please enter the directory to move back the files\n"      #This variable gets the directory to move the files to the directory
                          "To go back to main menu type quit\n")
        if directory.lower() == 'quit':
            main_menu()
            return 0
        os.chdir(directory)#Sets the directory
        try:
            for currentfolder, insidefolders, insidefiles in os.walk(os.getcwd()):  #Displays everything
                for files in insidefiles:
                    shutil.move(f"{currentfolder}\\{files}", os.getcwd())  #It moves all files to the directory
            for deleted in os.listdir():
                if os.path.isdir(deleted) == True: #If it detects a file,
                    os.removedirs(deleted)         #It deletes the file
            print("All files went back to the directory\n"
                  "Going back to main menu...")
            main_menu()
        except: #Prevents errors
            print("All files are in the directory\n"
                  "Going back to main menu...")
            main_menu()
    except:  # Prevents errors
        print(f"The directory '{directory}' is incorrect try again")
        undo()
main_menu()























