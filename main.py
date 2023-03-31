#Carter Belnap
#March 31st 2023
#Databasing Integration Program

import os, time, sqlite3 
names =["Carter","Matt","Bob","Francis","Kenzie","Andrew","Nancy","Lucas","Makenna","Sarah","Justin","Rick","Emily","Jessica","Will"]
run=True
connection = sqlite3.connect("database.db") 
cursor = connection.cursor()

connection.close()
def create_connection(database):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Exception as e:
        print(e)
    return conn

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

def name():
    print(names)
    print("Press Enter To Exit")
    select = input()

    if select == "":
        menu()
    else:
        menu()

def add():
    new_name = input("Add Student: ")
    names.append([new_name])
    print("Student Added")
    time.sleep(1)

def menu():
    while run==True:
        #Menu
        os.system("cls")
        print("Search And Sort Program")
        time.sleep(0.05)
        print("1. Student List")
        time.sleep(0.05)
        print("2. Search Student")
        time.sleep(0.05)
        print("3. Sort List A-Z")
        time.sleep(0.05)
        print("4. Add Student")
        time.sleep(0.05)
        print("5. Exit")

        #Selection 1-5
        try:
            print("Selection: ")
            select = input()

            if select == "1":
                os.system("cls") 
                name()
                
            elif select == "2":
                os.system("cls")
                look = input("Who Are You Looking For:")
                find = binary_search(names, 0, len(names)-1, look)
                if find == -1:
                    print(f"No, {look} Is Not In The List.")
                    
                else:
                    print(f"Yes, {look} Is In The List At {find}")
                    
            elif select == "3":
                bubbleSort(names)
                time.sleep(.5)
                print("List Sorted")
                time.sleep(1)

            elif select == "4":
                os.system("cls")
                add()

            elif select == "5":
                print("Goodbye")
                time.sleep(.5)
                break

            else:
                print("Please Enter A Valid Selection")
                time.sleep(1)

        except Exception as e:
            print(f"Please Print A Valid Input {e}")

menu()