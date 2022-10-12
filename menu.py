from iomanager import IOManager
from rich import print
from movies import MovieManager
from tvseries import SeriesManager
from customerrors import ValueIsNotValid, UserExists
from user import User, UserManager


def UserExistence():
    try:
        id = input(f"Print user's ID: ")
        data = UserManager.readJSON()
        if id not in data:
            raise UserExists
    except UserExists:
        print("This User's ID doesn't exist!")
        exit(0)
    return id


def menu():
    print("Select what you want to do:\n 1) Print all films\n 2) Print all TV Series\n "
          "3) Read XML file\n 4) Write a film to XML file\n "
          "5) Read JSON file\n 6) Write a series to JSON file\n "
          "7) Find a film by name\n 8) Find a TV Series by name\n "
          "9) Show User menu")

    while True:
        try:
            n = int(input())
            if n > 9 or n < 1:
                raise ValueIsNotValid
            break
        except ValueIsNotValid:
            print('Number has to be between 1 and 9 included!')
        except ValueError:
            print('You have to print a number!')

    if n == 1:
        films = IOManager.deserializeXML()
        k = 1
        for element in films:
            print(str(k) + ". " + element.name)
            k += 1

    if n == 2:
        series = IOManager.deserializeJSON()
        k = 1
        for element in series:
            print(str(k) + ". " + element.name['name'])
            k += 1

    if n == 3:
        films = IOManager.deserializeXML()
        for element in films:
            print(element.__dict__)

    if n == 4:
        func = ['name', 'release date', 'genre', 'rating', 'country of origin']
        variables = []
        for i in func:
            variables.append(input(f"Print movie's {i}: "))
        movies = [MovieManager(variables[0], variables[1], variables[2], float(variables[3]), variables[4])]
        IOManager.serializeXML(movies)
        print('Done!')

    if n == 5:
        series = IOManager.deserializeJSON()
        for element in series:
            print(element.name)

    if n == 6:
        func = ['name', 'release date', 'genre', 'rating',
                'country of origin', 'number of episodes', 'number of seasons']
        variables = []
        for i in func:
            variables.append(input(f"Print movie's {i}: "))
        series = [SeriesManager(variables[0], variables[1], variables[2], float(variables[3]),
                                variables[4], int(variables[5]), int(variables[6]))]
        IOManager.serializeJSON(series)
        print('Done!')

    if n == 7:
        a = input(f"Print film's name: ")
        films = IOManager.deserializeXML()
        for element in films:
            if element.name == a:
                print('\n' + '\n'.join(f'{key}: {value}' for key, value in element.__dict__.items()))
                exit(0)
        print("Film not found.")

    if n == 8:
        a = input(f"Print series's name: ")
        films = IOManager.deserializeJSON()
        for element in films:
            if element.name['name'] == a:
                print('\n' + '\n'.join(f'{key}: {value}' for key, value in element.name.items()))
                exit(0)
        print("Series not found.")

    if n == 9:
        print("Select what you want to do:\n 1) Print User's watched films and series\n "
              "2) Print User's rated films and series\n "
              "3) Add new User\n 4) Remove User\n 5) Add/Remove film or series to User\n "
              "6) Add/Remove rating to film or series to User")

        while True:
            try:
                n = int(input())
                if n > 6 or n < 1:
                    raise ValueIsNotValid
                break
            except ValueIsNotValid:
                print('Number has to be between 1 and 6 included!')
            except ValueError:
                print('You have to print a number!')

        if n == 1:
            id = UserExistence()
            data = UserManager.readChosenJSON(id)[0]
            if len(data) != 0:
                print(data)
            else:
                print("No watched films and series found.")

        if n == 2:
            id = UserExistence()
            if len(UserManager.readChosenJSON(id)[1]) != 0:
                 print((UserManager.readChosenJSON(id))[1])
            else:
                print("No rated films and series found.")

        if n == 3:
            func = ['id', 'watched', 'rated']
            variables = []
            dictrate = {}
            for i in func:
                if i == 'id':
                    try:
                        variables.append(input(f"Print user's {i}: "))
                        data = UserManager.readJSON()
                        if variables[0] in data:
                            raise UserExists
                    except UserExists:
                        print("This User's ID already exists!")
                        exit(0)
                if i == 'watched':
                    variables.append(input(f"Print user's {i} films and series separated by space: "))
                if i == 'rated':
                    while True:
                        text = input(f"Print {i} film's and serie's name: ")
                        if text != '':
                            try:
                                text2 = float(input(f"Print {text}'s rating: "))
                                dictrate[str(text)] = text2
                            except ValueError:
                                print("Rating has to be a float number! Try again.")
                        else:
                            break
            if len(variables[1]) == 0:
                b = ""
            else:
                b = variables[1].split()

            dict1 = {variables[0]: [b, dictrate]}
            UserManager.addToJSON(User(dict1))
            print(f"Done! Added User with {variables[0]}'s ID")

        if n == 4:
            id = UserExistence()
            UserManager.removefromJSON(id)
            print(f"Done! Removed User with {id}'s ID")

        if n == 5: # DONE
            id = UserExistence()
            action = input(f"What you want to do? Add/Remove\n")
            watchrate = 1
            if action == "Add":
                added = input(f"Print watched films and series separated by space: ")
                if len(added) == 0:
                    added = ""
                else:
                    added = added.split()
                    for i in added:
                        if i in UserManager.readChosenJSON(id)[0]:
                            print(f"Removed {i} because it was already watched.")
                            added.remove(i)
                UserManager.addToChosenJSON(id, added, watchrate)
                print(f"Done! Added {len(added)} objects!")
            elif action == "Remove":
                removed = input(f"Print user's watched films and series separated by space: ")
                if len(removed) == 0:
                    removed = ""
                else:
                    removed = removed.split()
                    for i in removed:
                        if i not in UserManager.readChosenJSON(id)[0]:
                            print(f"Removed {i} because it wasn't watched.")
                            removed.remove(i)
                UserManager.removefromchosenJSON(id, removed, watchrate)
                print(f"Done! Removed {len(removed)} objects!")
            else:
                print("Wrong action. Try again")
                exit(0)

        if n == 6: # DONE
            id = UserExistence()
            action = input(f"What you want to do? Add/Remove\n")
            watchrate = 2
            if action == "Add":
                added = {}
                while True:
                    film = input(f"Print rated films and series: ")
                    if film != '':
                        try:
                            rating = float(input(f"Print {film}'s rating: "))
                            added[str(film)] = rating
                        except ValueError:
                            print("Rating has to be a float number! Try again.")
                    else:
                        break
                if len(added) == 0:
                    added = {}
                UserManager.addToChosenJSON(id, added, watchrate)
                print(f"Done! Added {len(added)} objects!")
            elif action == "Remove":
                removed = []
                while True:
                    film = input(f"Print rated films and series: ")
                    if film != '':
                        removed.append(film)
                    else:
                        break
                if len(removed) == 0:
                    print("No films or series chosen to be removed.")
                    exit(0)
                UserManager.removefromchosenJSON(id, removed, watchrate)
                print(f"Done! Removed {len(removed)} objects!")
            else:
                print("Wrong action. Try again")
                exit(0)
