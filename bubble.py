
def bubbleSort(numberList):
    for i in range(len(numberList)):
        for j in range(len(numberList) - 1):
            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]


def bubbleSort1(numberList):
    has_swapped = True
    num_of_iterations = 0
    while(has_swapped):
        has_swapped = False
        for i in range(len(numberList) - num_of_iterations - 1):
            if numberList[i] > numberList[i+1]:
                # Swap
                numberList[i], numberList[i+1] = numberList[i+1], numberList[i]
                has_swapped = True
        num_of_iterations += 1



#numberList = [9,4,6,5,8,7,2,5,3,1,7]
numberList = ['c','d','a','t','n','b','k','l','e','i','z']
bubbleSort(numberList)
#bubbleSort1(numberList)

print(numberList)
