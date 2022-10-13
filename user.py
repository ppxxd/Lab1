import json


class User:
    def __init__(self, id: str = ""):
        self.id = id

    def __del__(self):
        try:
            print()
            # print(f"User {self.id} has been deleted.")
        except AttributeError:
            print("Incorrected object")
        except Exception:
            print("Error")

    def getID(self):
        id = self.id
        return id

    def setID(self, id: str = ""):
        self.id = id


class UserManager:
    @staticmethod
    def WriteToFile(data):  # DONE
        try:
            b = data.__dict__['id']
            with open("users.json", "w") as f:
                f.write(json.dumps(b, indent=4))
        except AttributeError:
            print("Incorrected object.")
            exit(0)
        except Exception:
            print("Error.")
            exit(0)

    @staticmethod
    def readJSON():  # DONE
        try:
            with open("users.json", "r") as read_file:
                data = json.load(read_file)
            return data
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def removefromJSON(idname: str = ""):  # DONE
        try:
            with open('users.json', 'r', encoding='utf-8') as read_file:
                data = json.load(read_file)
                print(data)
                if data.get(idname):
                        del data[idname]
            with open('users.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, indent=2))
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def addToJSON(entry):  # DONE
        try:
            b = (entry.__dict__)['id']
            with open('users.json', 'r', encoding='utf-8') as read_file:
                data = json.load(read_file)
                data.update(b)
            with open('users.json', "w") as file:
                    json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def readChosenJSON(idname):  # DONE
        try:
            with open("users.json", "r") as read_file:
                data = json.load(read_file)
                for idx, obj in enumerate(data):
                    if obj == str(idname):
                        return data[str(idname)]
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def addToChosenJSON(idname, entry, action):  # DONE
        try:
            with open('users.json', 'r', encoding='utf-8') as read_file:
                data = json.load(read_file)
                if action == "w":  # watched
                    idx = 0
                    for i in entry:
                        data[str(idname)][idx].append(i)
                elif action == "r":  # rated
                    idx = 1
                    data[str(idname)][idx].update(entry)
            with open('users.json', "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def removefromchosenJSON(idname, entry, action):  # DONE
            try:
                with open('users.json', 'r', encoding='utf-8') as read_file:
                    data = json.load(read_file)
                    if action == "w":  # watched
                        idx = 0
                        for i in entry:
                            data[str(idname)][idx].remove(i)
                    elif action == "r":  # rated
                        idx = 1
                        for k in entry:
                            data[str(idname)][idx].pop(k, None)
                with open('users.json', "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                print("File not found.")
                exit(0)
            except json.JSONDecodeError:
                print("Fail! Error on file.")
                exit(0)
            except Exception as e:
                print(e)
                exit(0)
