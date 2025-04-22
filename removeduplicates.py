# Parameters:
#  arr: List[int]
# return type: List[int]
class solution:
    def removeDuplicates(arr):
        hasharr={}
        for number in arr:
            hasharr[number]=hasharr.get(number,0)+1 
        return list(hasharr.keys())

