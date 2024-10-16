class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute

        # anagrams = defaultdict(list)  
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))  
        #     anagrams[sorted_word].append(word) 
        
        # return list(anagrams.values())


        #optimal

        anagrams = defaultdict(list)  

        for word in strs:
            count = [0] * 26 
            
            for char in word:
                count[ord(char) - ord('a')] += 1  
            print(count)
            
            anagrams[tuple(count)].append(word)  # Use tuple of counts as the key


        
        return list(anagrams.values()) 
        