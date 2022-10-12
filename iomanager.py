import xml.etree.ElementTree as ET
import json
import xml
from movies import Movie
from tvseries import Series


class IOManager:

    @staticmethod
    def serializeXML(data):
        root = ET.Element("Movies")
        for element in data:
            Name = ET.Element("Name")
            Name.text = element.name
            Release = ET.SubElement(Name, "Release")
            Release.text = element.release
            Genre = ET.SubElement(Name, "Genre")
            Genre.text = element.genre
            Rating = ET.SubElement(Name, "Rating")
            Rating.text = str(element.rating)
            Origin = ET.SubElement(Name, "Origin")
            Origin.text = element.origin
            root.append(Name)
        s = ET.tostring(root, encoding="utf-8", method="xml")
        s = s.decode("UTF-8")
        with open(f"xml_data_file.xml", "w") as f:
            f.write(s)

    @staticmethod
    def deserializeXML():
        try:
            toReturn = []
            tree = ET.parse("xml_data_file.xml")
            root = tree.getroot()
            for element in root:
                toReturn.append(Movie(element.text, element[0].text, element[1].text, float(element[2].text), element[3].text))
            return toReturn
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except xml.etree.ElementTree.ParseError:
            print("File is collapsed or empty.")
            exit(0)
        except Exception:
            print("Error.")
            exit(0)

    @staticmethod
    def serializeJSON(data):
        try:
            with open("json_data_file.json", "w") as f:
                f.write(json.dumps(data, default=lambda o: o.__dict__, indent=4))
        except AttributeError:
            print("Incorrected object.")
            exit(0)
        except Exception:
            print("Error.")
            exit(0)

    @staticmethod
    def deserializeJSON():
        try:
            with open("json_data_file.json", "r") as read_file:
                data = json.load(read_file)
                toReturn = []
                for element in data:
                    toReturn.append(Series(element))
            return toReturn
        except FileNotFoundError:
            print("File not found.")
            exit(0)
        except json.JSONDecodeError:
            print("Fail! Error on file.")
            exit(0)
        except Exception as e:
            print(e)
            exit(0)
