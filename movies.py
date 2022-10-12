class Movie:
    def __init__(self, name: str = "", release: str = "", genre: str = "", rating: float = 0, origin: str = ""):
        self.name = name
        self.release = release
        self.genre = genre
        self.rating = rating
        self.origin = origin


class MovieManager (Movie):
    def __del__(self):
        try:
            print()
            # print(f"Movie {self.name} has been deleted.")
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")

    def getInfo(self):
        data = {"name": self.name, "release": self.release, "genre": self.genre, "rating": self.rating,
                "origin": self.origin}
        return data

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
