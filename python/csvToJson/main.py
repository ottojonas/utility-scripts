import csv
import json
from icecream import ic


def csv_to_json(csvFile, jsonFile):
    with open(csvFile, mode="r") as file:
        csvReader = csv.DictReader(file)
        data = [row for row in csvReader]

    with open(jsonFile, mode="w") as file:
        json.dump(data, file, indent=4)

    ic(f"CSV to JSON conversion complete {jsonFile}")


csv_to_json("csvFilePlaceholder", "data.json")
