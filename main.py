tasks = []

def addUserTask():
    user_task = input("Wpisz zadanie do wykonania: ")
    tasks.append(user_task)
    print(f"{user_task} zostało dodane do listy zadań. \n")


def tasksList(editOption):

    if not tasks:
        print("Nie masz jeszcze żadnych zadań do wykonania. \n")
    else:
        print("Twoje zadania do wykonania:")
        for index, task in enumerate(tasks):
            print(f"Zadanie #{index}. {task}")

        if editOption:
            print("Czy chcesz edytować któreś z zadań?")
            print("-----------------------------------")
            print("1. Tak")
            print("2. Nie")
            user_wants_to_edit = int(input(">: "))
            if user_wants_to_edit == 1:
                task_to_edit = int(input("Podaj numer zadania do edycji: "))
                if task_to_edit >=0 and task_to_edit < len(tasks):
                    edited_task = input("Wpisz nową treść zadania do wykonania: ")
                    tasks[task_to_edit] = edited_task
                    print("Zadanie zostało pomyślnie edytowane. \n")
                else:
                    print(f"Zadanie #{task_to_edit} nie istnieje. \n")
            else:
                return
        else:
            return
         

            
 

def delateUserTask():
    tasksList(False)
    try:
        deleted_task = int(input("Wybierz zadanie do usuniecią: "))
        if deleted_task >=0 and deleted_task < len(tasks):
            tasks.pop(deleted_task)
            print("Zadanie zostało usunięte z listy. \n")
        else:
            print(f"Zadanie #{deleted_task} nie istnieje. \n")
    except:
        print("Niewłaściwy wybór.")



if __name__ == "__main__":
    print("Witaj w aplikacji Lista rzeczy do zrobienia \n")

    while True:
        
        print("Co chciałbyś zrobić - wybierz jedną z opcji")
        print("-------------------------------------------")
        print("1. Dodaj zadanie do wykonania")
        print("2. Usuń zadanie z listy")
        print("3. Wyświetl liste zadań")
        print("4. Zakończ")
        print("\n")

        user_choice = input("Wybierz opcje: ")


        if(user_choice == "1"):
            addUserTask()

        elif(user_choice == "2"):
            delateUserTask()

        
        elif(user_choice == "3"):
            tasksList(True)

        elif(user_choice == "4"):
            break
        
        else:
            print("Wybierz poprawną opcję.")

    print("Żegnaj! \n")
