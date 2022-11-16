# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Carol Hubbard, 11/13/2022, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        lstTotal = len(lstTable)
        if lstTotal == 0:
            print("There are", lstTotal, "items on your To-Do List.\nTo add an item please select option #2 from the menu.")
        elif lstTotal > 1:
            print("There are", lstTotal, "items on your To-Do List. They are:")
            print("___" * 15)
            for i, item in enumerate(lstTable, 1):
                print(i,"Task:", item["Task"] + " | " + "Priority:", item["Priority"])
        elif lstTotal < 2:
            print("There is", lstTotal, "item on your ToDoList. It is: ")
            print("___" * 15)
            for i, item in enumerate(lstTable, 1):
                print(i,"Task:", item["Task"] + " | " + "Priority:", item["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a new task: ")
        strPriority = input("Please assign the task a priority: (Low, Medium, High) ")
        if strPriority.lower() == "high": #High priority tasks will appear in all caps
           lstTable.append({"Task": strTask.title(), "Priority": strPriority.upper()})
        else:
            lstTable.append({"Task": strTask.title(), "Priority": strPriority.title()})
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strExists = False
        rowNuke = input("Please enter an item to remove: ")
        for row in lstTable:
            if row["Task"].lower() == rowNuke.lower():
                lstTable.remove(row)
                print("Item '" + rowNuke + "' has been removed from list")
                strExists = True
        if strExists == False:
           print("Item '" + rowNuke + "' not found in the list. Please try again.")

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
     objFile = open("ToDoList.txt", "w")
     for item in lstTable:
        objFile.write(str(item["Task"]) + "," + str(item["Priority"] + "\n"))
     objFile.close()
     print("Your items have been saved to ToDoList.txt!")

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
     strEnd = input("Press any key to exit the program")
     break  # and Exit the program