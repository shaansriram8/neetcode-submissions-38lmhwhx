class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hashmap = {}

        hand.sort()
        print(hand)
        for val in hand:
            hashmap[val] = hashmap.get(val, 0) + 1

        stop = len(hand) // groupSize

        for key, val in hashmap.items():
            for j in range(hashmap[key]):
                if hashmap[key] == 0:
                    continue
                print("outer", key)
                for i in range(groupSize):
                    print(key+i)
                    if key + i not in hashmap or hashmap[key+i] == 0:
                        return False
                    hashmap[key+i] -= 1
                    print("freq", hashmap[key+i])
        return True
            
            

        

        




