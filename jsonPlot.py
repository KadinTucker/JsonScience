"""
Matplotlib: plot data from JSON file
By Kadin Tucker
"""

import json
import matplotlib as mpl

"""
Used JSON Format:
    [
        "Plot Title",
        "X-axis label",
        [x axis points],
        "Y-axis label",
        [y axis points]
    ]
"""
def loadJson(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Failed to load ' + filename + '!')
        return
    return json.load(file)

def determineValidityOfData(data):
    assert type(data[0]) is str, "Missing plot title."
    assert type(data[1]) is str, "Missing x-axis title."
    assert type(data[3]) is str, "Missing y-axis title."
    assert len(data[2]) == data[4], "X and Y value lists are not the same length."

def main():
    data = loadJson(input('Load what file? '))
    determineValidityOfData(data)
    mpl.pyplot.scatter(data[2], data[4])
    mpl.pyplot.xlabel(data[1])
    mpl.pyplot.ylabel(data[3])
    mpl.pyplot.title(data[0])
    mpl.pyplot.show()

if __name__ == '__main__':
    main()