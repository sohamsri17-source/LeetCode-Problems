class Solution(object):
    def reverseWords(self):
        s = ['Soham', 'is', 'a', 'good', 'boy']
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s
        

obj = Solution()
print(obj.reverseWords())