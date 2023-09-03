# Problem: https://leetcode.com/problems/valid-palindrome/
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  54 ms / 17.80 MB /  a few seconds ago

class Solution:
    def isPalindrome(self, st: str) -> bool:
        
        st = "".join([c for c in st if c.isalnum()]).lower()

        n = len(st)

        l = 0
        r = n-1

        pal = True
        while l <= r:
            if st[l] != st[r]:
                pal = False
                break
            l += 1
            r -= 1
        
        return pal

if __name__ == "__main__":

    sol = Solution()
    t = ["A man, a plan, a canal: Panama", "race a car", " "]
    for ts in t:
        print(sol.isPalindrome(ts))