import json

def main():


    ## The output should be stored within a file called output.txt
    text = open("output.txt","r")
    decode = open("decoded.txt","w")

    ### grab the JSON dictionary from the first line
    firstline = text.readline()
    ### Make that first line into a dictionary
    encoding = json.loads(firstline)
    invEncoding = {v: k for k,v in encoding.items()}
   

    currentCode = ""
    for line in text:
        for c in line:
            currentCode += c
            if invEncoding.get(currentCode):
                decode.write(invEncoding[currentCode])
                currentCode = ""
            


if __name__ == "__main__":
    main()