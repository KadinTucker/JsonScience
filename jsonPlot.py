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
        input()
        return []
    return json.load(file)

def main():
    data = []
    while len(data) == 0:
        data = loadJson(input('Load what file? '))
    mpl.pyplot.scatter(data[2], data[4])
    mpl.pyplot.xlabel(data[1])
    mpl.pyplot.ylabel(data[3])
    mpl.pyplot.title(data[0])
    mpl.pyplot.show()

if __name__ == '__main__':
    main()