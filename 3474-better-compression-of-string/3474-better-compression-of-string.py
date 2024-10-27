class Solution:
    def betterCompression(self, compressed: str) -> str:
        i = 0
        freq_map = collections.defaultdict(int)
        n = len(compressed)

        while i < n:
            char = compressed[i]
            i+=1

            j = i

            while j < n and compressed[j].isdigit():
                j+=1

            frequency = int(compressed[i:j])


            if char in freq_map:
                freq_map[char] += frequency
            else:
                freq_map[char] = frequency

            i = j

        freq_map = dict(sorted(freq_map.items()))

        print(freq_map)
        result = ''
        for char, fre in freq_map.items():
            result += char
            result+= str(fre)
        
        return result