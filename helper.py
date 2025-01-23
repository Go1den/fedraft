def flatten(listOfLists):
    flatList = [item for sublist in listOfLists for item in sublist]
    return flatList

def maxAddress(updateList):
    largestAddress = max(updateList, key=lambda x: int(x[0], 16))
    return int(largestAddress[0], 16)
