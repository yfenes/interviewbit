class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        graph = self.create_graph(start, end, dictV)

        if graph == None:
        	return 0

        shortest = self.find_shortest_path(graph, start, end)


        if shortest==None:
        	return 0
        
        return len(shortest)

   
    def create_graph(self, start, end, dictV):
    	graph = {}
        for i in range(len(dictV)):

        	if self.distance(dictV[i],start)==1:
        		graph.setdefault(dictV[i],[]).append(start)
        		graph.setdefault(start,[]).append(dictV[i])
        	
        	if self.distance(dictV[i],end)==1:
        		graph.setdefault(dictV[i],[]).append(end)
        		graph.setdefault(end,[]).append(dictV[i])

        	for j in range(len(dictV)):
        		if i==j:
        			continue
        		if self.distance(dictV[i],dictV[j])==1:
        			graph.setdefault(dictV[i],[]).append(dictV[j])
        			graph.setdefault(dictV[j],[]).append(dictV[i])
        return graph

    def find_shortest_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


    def distance(self,s,t):
        d = 0
        for i in range(len(s)):
            if s[i]!=t[i]:
                d += 1
            if d>1:
                break
        return d

start = "hit"
end = "klj"

dict1 = ["hot","dot","dog","lot","log",'tyu']

start =  'aaaab'
end =  'bbabb'
dict1 = 'bbaba babaa abbaa bbbbb bbbab bbaaa bbbab aaabb babbb bbaaa bbaaa bbbba baabb abaab bbaaa bbbaa baabb abbaa' # aaaba abaaa abbba aaaab baaaa abaaa abaab aaabb bbaab babbb ababa'
dict1 = dict1.split()

s = Solution()
g = s.ladderLength(start,end,dict1)

print(g)

import json

#print(json.dumps(g, indent = 4))




