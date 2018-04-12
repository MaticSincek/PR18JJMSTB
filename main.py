
from csv import DictReader
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


filename = "WPP2017_TotalPopulationBySex.csv"

# def readData(filename):
#     dictionary = dict()
#     reader = DictReader(open(filename, 'rt', encoding='utf-8'))
#     for row in reader:
#         country = row["Location"]
#         time = row["Time"]
#         population = row["PopTotal"]
#         if(country not in dictionary):
#             dictionary[country] = dict()
#             dictionary[country][time] = population
#         else:
#             dictionary[country][time] = population
#     return dictionary


region = defaultdict()
def worldPopulationVisualisation(filename):
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
    europe = []
    america = []
    asia = []
    africa = []
    australia = []
    continents = ["Europe", "America", "Asia", "Africa", "Australia/New Zealand"]
    yearsRange = range(1950, 2018)  #interval is adjustable(1950-2100)
    for continent in continents:
        for i in yearsRange:
            if continent == "Europe": europe.append(dictionary[(str(i), continent)])
            elif continent == "America": america.append(dictionary[(str(i), continent)])
            elif continent == "Asia": asia.append(dictionary[(str(i), continent)])
            elif continent == "Africa": africa.append(dictionary[(str(i), continent)])
            elif continent == "Australia/New Zealand": australia.append(dictionary[(str(i), continent)])
    x = yearsRange
    plt.stackplot(x, europe, america, asia, africa, australia, labels=['Europe', 'America', "Asia", "Africa", "Australia"])
    plt.legend(loc='upper left')
    plt.show()

#worldPopulationVisualisation("WPP2017_TotalPopulationBySex.csv")


#Age group demographyc pyramid
def ageGroupVisualisation(filename, year, continent):
    dictionaryM = dict()
    dictionaryF = dict()
    reader = DictReader(open(filename, 'rt', encoding='utf-8'))
    for row in reader:
        time = row["Time"]
        populationM = row["PopMale"]
        populationF = row["PopFemale"]
        age = row["AgeGrp"]
        if row["VarID"] == "2" and time == str(year):
            if continent == "America":
                if "Northern America" == row["Location"] or "South America" == row["Location"] or "Central America" == \
                        row["Location"]:
                    if age not in dictionaryM:
                        dictionaryM[age] = float(populationM)
                    else:
                        dictionaryM[age] += float(populationM)
                    if age not in dictionaryF:
                        dictionaryF[age] = float(populationF)
                    else:
                        dictionaryF[age] += float(populationF)
            elif continent == row["Location"]:
                dictionaryM[age] = float(populationM)
                dictionaryF[age] = float(populationF)
    labels = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+"]
    populationM = []
    populationF = []
    for lb in labels:
        populationM.append(dictionaryM[lb])
        populationF.append(dictionaryF[lb])

    y = np.arange(len(populationM))
    fig, axes = plt.subplots(ncols=2, sharey=True)
    axes[0].barh(y, populationM, align='center', color='blue', zorder=10)
    axes[0].set(title='Male population')
    axes[1].barh(y, populationF, align='center', color='purple', zorder=10)
    axes[1].set(title='Female population')

    axes[0].invert_xaxis()
    axes[0].set(yticks=y, yticklabels=labels)
    axes[0].yaxis.tick_right()

    for ax in axes.flat:
        ax.margins(0.03)
        ax.grid(True)

    fig.tight_layout()
    fig.subplots_adjust(wspace=0.20)
    plt.show()

#ageGroupVisualisation("WPP2017_PopulationByAgeSex_Medium.csv", 2018, "Asia")

def birthsGDPCorrelation(filenameBirths, filenameGDP, year):
    dictionaryBirths = dict()
    reader = DictReader(open(filenameBirths, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["Location"]
        time = row["Time"]
        births = row["TFR"]
        timeInterval = time.split("-")
        if row["VarID"] == "2" and int(timeInterval[0]) <= year and int(timeInterval[1]) >= year:
            if(births != ""):
                dictionaryBirths[country] = float(births)

    dictionaryGDP = dict()
    reader = DictReader(open(filenameGDP, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["Name"]
        GDP = row["GDPPC"]
        if country in dictionaryBirths:
            dictionaryGDP[country] = float(GDP)

    gdp = []
    births = []
    for key, value in dictionaryBirths.items():
        if key in dictionaryGDP:
            births.append(value)
            gdp.append((dictionaryGDP[key]))

    plt.rcdefaults()
    fit = np.polyfit(gdp, births, 1)
    fit_fn = np.poly1d(fit)
    plt.plot(gdp, births, 'go', gdp, fit_fn(gdp), '--k', ms=4)
    plt.xlim(0, max(gdp)+1)
    plt.ylim(0, max(births) + 1)
    plt.xlabel("GDP per capita in US Dollar")
    plt.ylabel("Number of live births per 1000")
    plt.title("Birth-gdp correlation in "+ str(year))
    plt.show()

#birthsGDPCorrelation("WPP2017_Period_Indicators_Medium.csv", "GDP.csv", 2017)



def religionBirthCorrelation(filenameBirths, filenameReligion, year):
    dictionaryBirths = dict()
    reader = DictReader(open(filenameBirths, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["Location"]
        time = row["Time"]
        births = row["TFR"]
        timeInterval = time.split("-")
        if row["VarID"] == "2" and int(timeInterval[0]) <= year and int(timeInterval[1]) >= year:
            if (births != ""):
                dictionaryBirths[country] = float(births)

    dictionaryReligion = dict()
    reader = DictReader(open(filenameReligion, 'rt', encoding='utf-8'))
    for row in reader:
        country = row["country"]
        nonReligious = row["percentage_non_religious"]
        if country in dictionaryBirths:
            dictionaryReligion[country] = float(nonReligious)

    nonReligious = []
    births = []
    for key, value in dictionaryBirths.items():
        if key in dictionaryReligion:
            births.append(value)
            nonReligious.append((dictionaryReligion[key]))

    plt.rcdefaults()
    fit = np.polyfit(nonReligious, births, 1)
    fit_fn = np.poly1d(fit)
    plt.plot(nonReligious, births, 'go', nonReligious, fit_fn(nonReligious), '--k', ms=4)
    plt.xlim(0, max(nonReligious) + 1)
    plt.ylim(0, max(births) + 1)
    plt.xlabel("Percentage of non-religious population")
    plt.ylabel("Number of live births per 1000")
    plt.title("Birth-religion correlation in " + str(year))
    plt.show()

#religionBirthCorrelation("WPP2017_Period_Indicators_Medium.csv", "religion.csv", 2017)