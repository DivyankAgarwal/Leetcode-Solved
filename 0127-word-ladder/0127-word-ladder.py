from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #So, the time complexity is O(N × M × 26) ≈ O(N × M) (since 26 is a constant

        q = deque()
        q.append((beginWord,1))

        st = set()

        for word in wordList:
            st.add(word)
        
        print(st)

        if beginWord in st:
            st.remove(beginWord)

        while q:
            
            word, step = q.popleft()

            if word == endWord:
                return step

            #TC: len(wordlist) x wordlength x 26 * O(1) for set

            for i in range(len(word)):
                originalChar = word[i]

                for newchar in range(ord('a'), ord('z')+1):

                    word_list = list(word)
                    word_list[i] = chr(newchar)

                    newWord = ''.join(word_list)

                    if newWord in st:
                        q.append((newWord,step+1))
                        st.remove(newWord)

                word_list[i] = originalChar

        return 0

        '''
        Expected Answer: BFS is preferable in this problem because it finds the shortest 
        transformation path. DFS might explore deeper paths first and would require 
        backtracking, making it less efficient for finding the shortest path.
        BFS ensures level-by-level exploration, so as soon as you reach the endWord, 
        you can be confident it's the shortest path.
        In DFS, you might end up traversing longer paths first, making it inefficient 
        for shortest path problems.

        
        '''
        

        