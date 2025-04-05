class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        recint={}
        newlist=[]        
        for i in range(len(recipes)):
                recint[recipes[i]]=ingredients[i]
        #print(recint)
        for receipe in recipes:
            if recint[receipe] in supplies:
                newlist+=receipe
            else:
                for recintres in recint.keys():
                    if recintres in recint[receipe]:
                        if recint[recintres] in supplies:
                            newlist+=receipe
                    else:
                        next
        return newlist

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour"]
sol = Solution()
print(sol.findAllRecipes(recipes, ingredients, supplies))