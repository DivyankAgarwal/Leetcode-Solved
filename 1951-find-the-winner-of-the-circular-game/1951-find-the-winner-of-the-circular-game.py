class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        #brute
        players = list(range(1, n + 1))  
        index = 0  

       
        while len(players) > 1:
            # Move to the k-th person (k-1 steps forward)
            index = (index + k - 1) % len(players)
            # Remove the k-th person
            players.pop(index)
        
        # The last remaining player is the winner
        return players[0]