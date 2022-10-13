# from movies import MovieManager
# from tvseries import SeriesManager
# from iomanager import IOManager
# from rich import print
# from user import User, UserManager
from menu import menu

# menu()

# xmltest = []
# xmltest.append(MovieManager("Avatar", "December 18, 2009", "Science fiction", 8.0, "USA"))
# xmltest.append(MovieManager("Titanic", "December 19, 1997", "Romance and disaster", 7.9, "USA"))
# xmltest.append(MovieManager("Minions", "July 10, 2015", "Comedy", 10.0, "USA"))
# IOManager.serializeXML(xmltest)
#
# xmltest2 = IOManager.deserializeXML()
# for element in xmltest2:
#     print(element.__dict__)
#
# jsontest = []
# jsontest.append(SeriesManager("You", "September 9, 2018", "Psychological thriller", 7.0, "USA", 30, 3))
# jsontest.append(SeriesManager("Outer Banks", "April 15, 2020", "Teen drama, Mystery, Thriller, Action-adventure", 6.0, "USA", 20, 2))
# IOManager.serializeJSON(jsontest)
#
# jsontest2 = IOManager.deserializeJSON()
# for element in jsontest2:
#     print(element.name)

# dict1 = {'1234': [['Minions', 'Avatar', 'You'], {'You': 10.0}]}
# a = User(dict1)
# print(a.__dict__)
# b = UserManager.addToJSON(a)
# b = UserManager.removefromJSON("23")
# dict2 = {'TEST': 7.0}
# dict1 = {'You': 2.0}
# print(dict1)
# dict1.update(dict2)
# print(dict1)