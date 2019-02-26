class MySum:
    def _add_(self, other1, other2):
        if isinstance(self, set):
            return self | other1 | other2
        elif self == '4':
            return '%s plus %s plus %s' % (self,other1,other2)

        self=self+other1+other2
        return self

firstNum=5
secondNum=7
thirdNum=9
total=firstNum+secondNum+thirdNum
print('The sum of {0} and {1} and {2} is {3}'.format(firstNum, secondNum,thirdNum, total))

firstList = [1,2,3,4,5]
secondList = [6,7,8,9,10]
thirdList = [11,12]
concatenatedNewList=firstList+secondList+thirdList
print('The concatenated new list is {} '.format(concatenatedNewList))

stringOne="Overloading / Overriding Example of "
stringTwo="Python String "
stringThree="for our class"
concatenatedNewString=stringOne+stringTwo+stringThree
print('The concatenated new string is {} '.format(concatenatedNewString))

result=MySum._add_("5", "7", "9")
print("Example of overloading the _add_ method: " + result)
