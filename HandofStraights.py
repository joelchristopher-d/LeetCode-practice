class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        keys = sorted(count)

        for key in keys:
            if count[key] > 0:
                num = count[key]
                for i in range(groupSize):
                    if count[key + i] < num:
                        return False
                    count[key + i] -= num

        return True      
