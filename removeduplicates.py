# Parameters:
#  arr: List[int]
# return type: List[int]

def removeDuplicates(arr):
    hasharr={}
    for number in arr:
        hasharr[number]=hasharr.get(number,0)+1 
    return list(hasharr.keys())

print(removeDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))