class Solution:
    def romanToInt(self, s: str) -> int:
        arrroman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sumarr=0
        for l in range(len(s)):
            if s[l] in []
            match s[l]:
                case "I":
                    if s[l+1]=="V" or s[l+1]=="X":
                        sumarr=sumarr+arrroman[s[l+1]]-arrroman[s[l]]
                        l=l+1
                case "X":
                    if s[l+1]=="L" or s[l+1]=="C":
                        sumarr=sumarr+arrroman[s[l+1]]-arrroman[s[l]]
                        l=l+1
                case "C":
                    if s[l+1]=="D" or s[l+1]=="M":
                        sumarr=sumarr+arrroman[s[l+1]]-arrroman[s[l]]
                        l=l+1
                

sol=Solution()
print(sol.romanToInt("IV"))
