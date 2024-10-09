class StockSpanner:

    def __init__(self):
        self.st = []
        

    def next(self, price: int) -> int:
        result = 1

        while self.st and self.st[-1][0] <= price:
            result += self.st.pop()[1]

        self.st.append([price,result])

        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)