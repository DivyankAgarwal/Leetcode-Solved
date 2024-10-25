class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute
        '''
        Time Complexity:
        O(n * k log k), where n is the number of strings, and k is the maximum length of a 
        string (since we sort each string).

        Space Complexity:
        O(n * k), as we store each string in the dictionary.
        
    
        '''

        # anagrams = defaultdict(list)  
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))  
        #     anagrams[sorted_word].append(word) 
        
        # return list(anagrams.values())


        #optimal
        '''
        Time Complexity:
        O(n * k): For each word of length k, we build the character count array in O(k), 
        making the complexity O(n * k).
        
        Space Complexity:
        O(n * k): We store each string in the dictionary, and each key (tuple) has a fixed 
        length of 26 (for each letter in the alphabet).
        
        '''

        anagrams = defaultdict(list)  

        for word in strs:
            count = [0] * 26 
            
            for char in word:
                count[ord(char) - ord('a')] += 1  

            
            anagrams[tuple(count)].append(word)  # Use tuple of counts as the key


        print(anagrams)
        return list(anagrams.values()) 
        
