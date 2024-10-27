class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        #brute TC: O(n * k)
        # players = list(range(1, n + 1))  
        # index = 0  

       
        # while len(players) > 1:
        
        #     index = (k-1) % len(players)

        #     for _ in range(index):
        #         players.append(players.pop(0))

        #     players.pop(0)

        # return players[0]

        #better TC: O(n2)

        # players = list(range(1, n + 1))  
        # index = 0  

       
        # while len(players) > 1:
        
        #     index = (index + k-1) % len(players)

        #     players.pop(index)

        # return players[0]


        #optimized TC:O(n)

        winner = 0  
        for i in range(2, n + 1):
            winner = (winner + k) % i
        
        return winner + 1  # Convert to 1-based indexing