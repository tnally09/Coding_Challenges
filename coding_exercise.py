# Please write a class in the language of your choice that 
# contains the following two public methods:

# aboveBelow:
# accepts two arguments
#     An unsorted collection of integers (the list)
#     an integer (the comparison value)
# returns a hash/object/map/etc. with the keys "above" and 
# "below" with the corresponding count of integers from the 
# list that are above or below the comparison value

# Example usage:
# input: [1, 5, 2, 1, 10], 6
# output: { "above": 1, "below": 4 }


# stringRotation:
# accepts two arguments
#     a string (the original string)
#     a positive integer (the rotation amount)
# returns a new string, rotating the characters in the original 
# string to the right by the rotation amount and have the overflow 
# appear at the beginning

# Example usage:
# input: "MyString", 2
# output: "ngMyStri"



class CodingExercise():
    def __init__(self, integerList, compValue, originalString, rotValue):
        self.integerList = integerList
        self.compValue = compValue
        self.originalString = originalString
        self.rotValue = rotValue

        self.aboveBelow(self.integerList, self.compValue)
        self.stringRotation(self.originalString, self.rotValue)


    def aboveBelow(self, integerList, compValue):
        n = len(integerList)
        # intialize above/below keys at 0
        countDict = {
            'above': 0,
            'below': 0
        }

        for i in range(n):
            # compound above/below counts to countDict
            if integerList[i] < compValue:
                countDict['below'] += 1
            elif integerList[i] > compValue:
                countDict['above'] += 1
            
            # nothing specified in problem statement for when integerList[i] == compValue
            # but could add some sort of additional statement and key/value pair to countDict
            # if desired
            # example:
            # elif integerList[i] == compValue:
            #     countdict['equal'] += 1

        return countDict

    def stringRotation(self, originalString, rotValue):
        n = len(originalString)
        rotString = [0] * n
        
        for i in range(n):
            rotString[(i + rotValue) % n] = originalString[i]

        return rotString






integerList = [1, 5, 2, 1, 10]
compValue = 6
originalString = 'MyString'
rotValue = 2

CodingExercise(integerList, compValue, originalString, rotValue)




