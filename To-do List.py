print("To-Do List")
print("""
    Add
    Remove
    Clear
    Exit
    Show list
    """)
todo = []
while True:
    

    opt = input("Pick any option: ").lower()
    
    if opt == "exit":
        break
    
    if opt == "clear":
        if not todo:
            print("Your List Is Empty")
            continue
        else:
            todo.clear()
            print("Successfully Cleaned")
        
    elif opt == "remove":
        remove = input("What do you want to remove: ")
        if remove in todo:  
            todo.remove(remove)
            print(f"{remove} Removed")
        else:
            print("Not Found")
            continue
            
            
    elif opt == "show":
        if not todo:
            print("Your List is Empty")
        else:
            for num, i in enumerate(todo, start=1):
                print(num, i)
    
       
    elif opt == "add":
        add_sth = input("Add: ")
        todo.append(add_sth)
        print(f"{add_sth} Added.")
        
        
    
    
    else:
        print("Not in Option")
        continue