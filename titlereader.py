"""
Pedro Tortello - 25/08/2020
IBM Behind the code marathon - Challenge #3
Retrieves data from JSON files in order to help with
the creation of queries on IBM Watson Discovery.
"""

from os import listdir
import json

# Retrieves a list of JSON files from the specified folder
folderPath = "ready/"
jsonFiles = [file for file in listdir(folderPath) if file.endswith('.json')]

# Menu loop
while(True):
    # Prints basic information for every JSON file
    for j in range(len(jsonFiles)):
        filename = folderPath + jsonFiles[j]
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(str(j+1) + " - " + data["type"] + "\t" + data["title"])

    # Reads user input to show the "body" content of selected file
    choice = int(input("Ler: "))
    filename = folderPath + jsonFiles[choice - 1]
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data["body"])
        input()
