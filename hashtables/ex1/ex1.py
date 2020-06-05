def get_indices_of_item_weights(weights, length, limit):

    # I need to figure out how to make this linear

    # stores all the sums of all the numbers
sumDict = {}

# This will store the final values
validCombos = []

# walk through all combos of sums and differences in q and store them in sumDic and difDict
for weight1 in weights:
    for
    for numD in q:
        # pulling the numD value from the f(num) dictionary
        funkedNumD = funcDict[numD]

        # computing the difference and sum
        numDif = funkedNumC - funkedNumD
        numSum = funkedNumC + funkedNumD

        # adding that combo to numDif dict with the numDif as the key
        # adds combo to the the list if it doesn't already exist

        # due to the nature of this problem  there is no need to store
        # negative differences if f(x) changes we would need to change this
        if numDif >= 0:
            if numDif not in difDict:
                difDict[numDif] = [(numC, numD)]
            else:
                if (numC, numD) not in difDict[numDif]:
                    difDict[numDif].append((numC, numD))

        # Lets do the same thing for the sum
        if numSum not in sumDict:
            sumDict[numSum] = [(numC, numD)]
        else:
            if(numC, numD) not in sumDict[numSum]:
                sumDict[numSum].append((numC, numD))

# Now we need to see which ones overlap
for key in difDict:
    if key in sumDict:
        # lets now loop through the list in the dict and make tuples out of all combos
        for sumTuple in sumDict[key]:
            for difTuple in difDict[key]:
                newTuple = sumTuple+difTuple
                validCombos.append(newTuple)
# To make it pretty lets sort the tuple list
validCombos.sort()
print(len(validCombos))
return None
