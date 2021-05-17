import sys
import heapq
import node
import json


def getFrequencies(file):


    frequencies = {}
    for line in file:
        for character in line:
            occurences = frequencies.get(character, 0)
            occurences += 1
            frequencies[character] = occurences

    return frequencies


def main(argv):
    try: 
        if len(sys.argv) != 2:
            raise Exception
    except:
        print("USAGE: python3 encodeFile.py <file name/ path>")

    inputFile = open(sys.argv[1], "r")

    if not inputFile:
        print("USAGE: python3 encodeFile.py <file name/ path>")

    # iterate over the file to get frequencies
    frequencyDict = getFrequencies(inputFile)
    
    # create nodes out of the dictionary
    nodeList = node.createNodes(frequencyDict)

    nodeList.sort(key= lambda x: x.occurences)
    while len(nodeList) > 1:
        
        left = nodeList[0]
        right = nodeList[1]

        newNode = node.Node(None, left.occurences + right.occurences, left, right)
        nodeList.append(newNode)
        nodeList.pop(0)
        nodeList.pop(0)

        nodeList.sort(key = lambda x: x.occurences)
        
    ### create a dictionary that uses the huffman tree we have just built
    rootNode = nodeList[0]
    encodingDict = {}
    encodeString = ""
    nodeList[0].findEncodings(encodingDict, encodeString)
    
    outputFile = open("output.txt","w")
    outputFile.write(json.dumps(encodingDict))
    outputFile.write("\n")
    inputFile.seek(0)
    for line in inputFile:
        for character in line:
            encoding = encodingDict[character]
            outputFile.write(encoding)

    inputFile.close()
    outputFile.close()


if __name__ == "__main__":
    main(sys.argv[1:])