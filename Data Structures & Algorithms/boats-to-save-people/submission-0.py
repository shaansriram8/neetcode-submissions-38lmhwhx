class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #1, 2, 2, 3, 3-> limit = 3
        cnt = 0
        l, r = 0, len(people)-1
        while l <= r:
            if people[l] + people[r] > limit:
                cnt+=1
                r-=1
            elif people[l] + people[r] <= limit:
                r-=1
                l+=1
                cnt +=1      
        return cnt

        #4, 1, 4

