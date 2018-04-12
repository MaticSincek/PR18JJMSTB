from csv import DictReader
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

filename = "WPP2017_Period_Indicators_Medium.csv"

#-----Tukaj vstavi argument-------
argument = "SRB"
#---------------------------------

region = defaultdict()
def readData(filename):
    dictionary = defaultdict(list)
    reader = DictReader(open(filename, 'rt', encoding='utf-8'))
    for row in reader:
        print(row)
        country = row["Location"]
        time = row["Time"]
        births = row[argument]
        if row["VarID"] == "2":
            if "Europe" == row["Location"]:
                dictionary["Europe"].append(float(births))
            elif "Northern America" == row["Location"]:
                dictionary["Northern America"].append(float(births))
            elif "Southern America" == row["Location"]:
                dictionary["Southern America"].append(float(births))
            elif "Asia" == row["Location"]:
                dictionary["Asia"].append(float(births))
            elif "Africa" == row["Location"]:
                dictionary["Africa"].append(float(births))
            elif "Australia/New Zealand" == row["Location"]:
                dictionary["Australia"].append(float(births))
    return dictionary

region = readData(filename)
time_periods = list(range(1955,2016,5))

x = np.array(range(13))
plt.xticks(x, time_periods)

plt.plot(x, np.array(region["Northern America"][:13]), label='Severna Amerika')
plt.plot(x, np.array(region["Europe"][:13]), label='Evropa')
#ax.plot(x, np.array(region["Southern America"][:13]), label='Južna Amerika')
plt.plot(x, np.array(region["Asia"][:13]), label='Azija')
plt.plot(x, np.array(region["Africa"][:13]), label='Afrika')
plt.plot(x, np.array(region["Australia"][:13]), label='Avstralija')

print(region["Europe"][:13])
print(region["Africa"][:13])

#plt.yticks(np.arange(0, 10000, 1000))
plt.legend(loc='middle left')

plt.show()