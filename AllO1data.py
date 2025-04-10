class AllOne(object):

    def __init__(self):
        self.masterlist={}
        self.count=0

        

    def inc(self, key):
        self.masterlist[key] = self.masterlist.get(key,0)+1

        """
        :type key: str
        :rtype: None
        """
        

    def dec(self, key):
        if self.masterlist.get(key)==0:
            self.masterlist.remove(key)
        else:
            self.masterlist[key]=self.masterlist.get(key)-1

        """
        :type key: str
        :rtype: None
        """
        

    def getMaxKey(self):
        return max(self.masterlist,key=lambda x: self.masterlist[x]) if self.masterlist else ""
        """
        :rtype: str
        """
        

    def getMinKey(self):
        return min(self.masterlist,key=lambda x: self.masterlist[x]) if self.masterlist else ""
        """
        :rtype: str
        """
        
allone=AllOne()
allone.inc("hello")
allone.inc("worl")
print(allone.getMaxKey())
print(allone.getMinKey())



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()