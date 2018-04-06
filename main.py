from csv import DictReader

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
