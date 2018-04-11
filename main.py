from csv import DictReader
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

filename = "WPP2017_TotalPopulationBySex.csv"

def readData(filename):
    dictionary = dict()
    reader = DictReader(open(filename, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["Location"]
        time = row["Time"]
        population = row["PopTotal"]
        if(country not in dictionary):
            dictionary[country] = dict()
            dictionary[country][time] = population
        else:
            dictionary[country][time] = population
    return dictionary


region = defaultdict()
def readData(filename):
    dictionary = dict()
    reader = DictReader(open(filename, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["Location"]
        time = row["Time"]
        population = row["PopTotal"]
        if row["VarID"] == "2":
            if "Europe" == row["Location"]:
                dictionary[(time, "Europe")] = float(population)
            elif "Northern America" == row["Location"] or "South America" == row["Location"] or "Central America" == row["Location"]:
                if (time,"America") not in dictionary:
                   dictionary[(time, "America")] = float(population)
                else:
                    dictionary[(time, "America")] += float(population)
            elif "Asia" == row["Location"]:
                dictionary[(time, country)] = float(population)
            elif "Africa" == row["Location"]:
                dictionary[(time, country)] = float(population)
            elif "Australia/New Zealand" == row["Location"]:
                dictionary[(time, country)] = float(population)
    return dictionary

dikt = readData("WPP2017_TotalPopulationBySex.csv")
def visualisationWorld():
    europe = []
    america = []
    asia = []
    africa = []
    australia = []
    continents = ["Europe", "America", "Asia", "Africa", "Australia/New Zealand"]
    yearsRange = range(1950, 2018)  #interval is adjustable(1950-2100)
    for continent in continents:
        for i in yearsRange:
            if continent == "Europe": europe.append(dikt[(str(i), continent)])
            elif continent == "America": america.append(dikt[(str(i), continent)])
            elif continent == "Asia": asia.append(dikt[(str(i), continent)])
            elif continent == "Africa": africa.append(dikt[(str(i), continent)])
            elif continent == "Australia/New Zealand": australia.append(dikt[(str(i), continent)])

    x = yearsRange
    plt.stackplot(x, europe, america, asia, africa, australia, labels=['Europe', 'America', "Asia", "Africa", "Australia"])
    plt.legend(loc='upper left')
    plt.show()

visualisationWorld()
