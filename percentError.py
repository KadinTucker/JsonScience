"""
Percent Error calculator using JSON
By Kadin Tucker
"""

import json

"""
Used JSON Format:
    [
        [expected],
        [observed]
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

def generateErrorList(data):
    error = []
    for i in range(len(data[0])):
        error.append(abs(data[0][i] - data[1][i]) / data[0][i])
    return error

def main():
    data = loadJson(input("Generate % error from what file? "))
    assert len(data[0]) == len(data[1]), "Length of data sets is not the same!"
    output = open(input("Send to what filename? "), 'w')
    json.dump(generateErrorList(data), output) 

if __name__ == '__main__':
    main()