class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = []
        ans = nums
        seen = set()
        for valor in ans:
            if valor in seen:
                return True
            seen .add(valor)
            
        return False
        