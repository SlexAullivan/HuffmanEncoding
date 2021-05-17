class Node ():

    def __init__(self, letter, occurences, left = None, right = None):
        self.occurences = occurences
        self.letter = letter
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'{self.letter} : {self.occurences}' 

    def findEncodings(self, encodingDict, encodingSequence):
        previousEncoding = encodingSequence

        if not self.left and not self.right:
            encodingDict[self.letter] = encodingSequence
            
        if self.left:
           
            encodingSequence += "0"
            
            self.left.findEncodings(encodingDict, encodingSequence)
            encodingSequence = previousEncoding

        if self.right:
            
            encodingSequence += '1'
          
            self.right.findEncodings( encodingDict, encodingSequence)
            encodingSequence = previousEncoding
        
       

       

   
    
### Helper function to return a list of nodes from a dictionary
def createNodes(OccurenceDictionary):
        
        nodeList = []
        for each in  OccurenceDictionary:
            node = Node(each, OccurenceDictionary[each])
            nodeList.append(node)

        return nodeList


