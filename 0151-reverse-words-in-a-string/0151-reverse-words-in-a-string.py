class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        st = []
        word = ''

        i = 0

        while i < n:
       
            if s[i] == ' ':
                if word != '':
                    st.append(word)
                    word = ''
                i+=1               
            else:
                word += s[i]
                i+=1

        if word != '':
            st.append(word)
        
        return ' '.join(reversed(st))
        