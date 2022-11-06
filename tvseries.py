class Series:
    def __init__(self, name: str = "", release: str = "", genre: str = "", rating: float = 0,
                 origin: str = "", numep: int = 0, numse: int = 0):
        self.name = name
        self.release = release
        self.genre = genre
        self.rating = rating
        self.origin = origin
        self.numep = numep
        self.numse = numse


class SeriesManager (Series):
    def __del__(self):
        try:
            print(f"TV Series {self.name} has been deleted.")
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")

    def getInfo(self):
        data = {"name": self.name, "release": self.release, "genre": self.genre, "rating": self.rating,
                "origin": self.origin, "number of episodes": self.numep, "number of seasons": self.numse}
        return data

    def getNumEp(self):
        numep = self.numep
        return numep

    def setNumEp(self, num: int = 0):
        self.numep = num

    def getNumSea(self):
        numse = self.numse
        return numse

    def setNumSea(self, num: int = 0):
        self.numse = num

    def getName(self):
        name = self.name
        return name

    def setName(self, name: str = ""):
        self.name = name

    def getDate(self):
        release = self.release
        return release

    def setDate(self, release: str = ""):
        self.release = release

    def getGenre(self):
        genre = self.genre
        return genre

    def setGenre(self, genre: str = ""):
        self.genre = genre

    def getOrigin(self):
        origin = self.origin
        return origin

    def setOrigin(self, origin: str = ""):
        self.origin = origin

    def getRate(self):
        rating = self.rating
        return rating

    def setRating(self, rating: float = 0):
        self.rating = rating
