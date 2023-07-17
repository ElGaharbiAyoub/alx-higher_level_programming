#!/usr/bin/python3
"""class base"""
import json
import os.path


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        jsons = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(jsons)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        if cls.__name__ == "Square":
            inst = cls(1)
        if inst:
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + ".json", "r") as file:
                list_Dicts = cls.from_json_string(file.read())
            return [cls.create(**inst) for inst in list_Dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save ti file csv"""
        import csv

        try:
            csvs = [x.to_dictionary() for x in list_objs]
        except FileNotFoundError:
            csvs = '[]'
        keys = csvs[0].keys()
        with open(cls.__name__ + '.csv', 'w') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        import csv
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []

        csvs = []
        with open(cls.__name__ + '.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except ValueError:
                        pass
                csvs.append(row)
        return [cls.create(**dic) for dic in csvs]
