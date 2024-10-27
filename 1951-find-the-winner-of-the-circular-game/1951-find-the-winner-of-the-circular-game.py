class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        #brute
        players = list(range(1, n + 1))  
        index = 0  

       
        while len(players) > 1:
        
            remove_ind = (index + k - 1) % len(players)
            # index = (index + k - 1) % len(players)

            # Remove the k-th person
            players.pop(remove_ind)

            index = remove_ind
        
        # The last remaining player is the winner
        return players[0]