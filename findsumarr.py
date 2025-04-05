# Parameters:
#  arr: List[int]
#  k: int
# return type: bool

def findPair(arr, k):
    for item in arr:
        right=k-item
        if right == item:
            occurance=arr.count(item)
        if right in arr and occurance> 1:
            return True
    return False
       
print(findPair([5, 5, 5, 5, 5],5))