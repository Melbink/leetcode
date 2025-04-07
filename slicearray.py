def longestSubstringWithoutRepeating(str):
    left=0
    maxlen=0
    dictstr={}
    for index,value in enumerate(str):
        if value in dictstr and dictstr[value]>=left:  
            left=dictstr[value]+1 
        dictstr[value]=index    
        maxlen=max(maxlen,index-left+1)
    return maxlen
print(longestSubstringWithoutRepeating("abcabcbb"))