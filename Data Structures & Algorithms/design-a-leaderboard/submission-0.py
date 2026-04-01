class Leaderboard:

    def __init__(self):
        self.leaderboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
        else:
            self.leaderboard[playerId] += score
    def top(self, K: int) -> int:
        heap = []
        sums = 0
        for val in self.leaderboard.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        for _ in range(K):
            sums += heapq.heappop(heap)
        return sums


    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
