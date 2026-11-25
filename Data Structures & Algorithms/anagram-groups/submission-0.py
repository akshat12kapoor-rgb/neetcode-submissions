class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #default dict which initialises values as lists
        for s in strs:#iterates through string
            count = [0]*26 # initialises a new count list  [0,0,0....] for every string
            for c in s:#for every letter in string s
                count[ord(c)-ord('a')] += 1#the value at index of the alphabet that is iterated through is incrememnted by 1
            res[tuple(count)].append(s)#after the iterations for one string is over the global result dict that is associated with the key that describes its alphabetical composition is both initialised and that list value is appended with the string
        return list(res.values())#the list of dict values is returned
         
        







        