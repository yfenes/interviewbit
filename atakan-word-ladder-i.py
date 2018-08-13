class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        if self.distance(start,end) == 1 or self.distance(start,end) == 0:
            return self.distance(start,end)
        else:
            candidates = []
            for w in range(len(dictV)):
                word = dictV[w]
                if self.distance(start,word) == 1:
                    candidates.append(self.ladderLength(word,end,dictV[w:])+1)
            if len(candidates)>0:
                print(candidates)
                return min(candidates)
        return 0

    def distance(self,s,t):
        d = 0
        for i in range(len(s)):
            if s[i]!=t[i]:
                d += 1
            if d>1:
                break
        return d

start = "hit"
end = "cog"

dict1 = ['asd',"hot","dot","dog","lot","log",'tyu']

start =  'aaaab'
end =  'bbabb'
dict1 = 'bbaba babaa abbaa bbbbb bbbab bbaaa bbbab aaabb babbb bbaaa bbaaa bbbba baabb abaab bbaaa bbbaa baabb abbaa' # aaaba abaaa abbba aaaab baaaa abaaa abaab aaabb bbaab babbb ababa'
dict1 = dict1.split()


sol = Solution()
g = sol.ladderLength(start,end,dict1)
print(g)




