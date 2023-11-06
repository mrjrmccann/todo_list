todo_list = []

def add_todo():
    new_item = input("What would you like to add? ")
    todo_list.append(new_item)
    print(*todo_list, sep="\n")

def remove_todo():
    remove_item = input("What would you like to remove? ")
    if remove_item in todo_list:
        todo_list.remove(remove_item)
    elif remove_item + "(done)" in todo_list:
        todo_list.remove(remove_item + "(done)")
    else:
        print("That item is not in the todo list, try again")
    print(*todo_list, sep="\n")

def cross_off():
    cross_item = input("What would you like to mark as done? ")
    if cross_item in todo_list:
        target_item = todo_list.index(cross_item)
        todo_list[target_item] = cross_item + "(done)"
    else:
        print("That item is not in the todo list, try again")
    print(*todo_list, sep="\n")

def main():
    while True:
        action = input("Would you like to add(add), remove(remove), view(view) or mark something as done(mark) on the to do list? (q to quit) ")
        if action == "add":
            add_todo()
        elif action == "remove":
            remove_todo()
        elif action == "mark":
            cross_off()
        elif action == "view":
            print(*todo_list, sep="\n")
        elif action == "q":
            print("Goodbye")
            break
        else:
            print("Invalid selection. Try again")

main()

