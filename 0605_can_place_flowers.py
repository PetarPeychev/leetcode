class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots = 0
        space = 1
        for bed in flowerbed:
            if bed == 0:
                space += 1
            else:
                spots += (max(space - 1, 0)) // 2
                space = 0

        if space > 1:
            spots += space // 2

        return spots >= n
