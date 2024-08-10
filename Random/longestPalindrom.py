def longestPalindrome(S):
    def palindrom(s):
        if s == s[::-1]:
            # print(s)
            l = len(s)
            return l
        else:
            return -1
    d = ''
    out = ''
    for i in range(0,len(S)):
        for j in range(0,len(S)):
            l = -1
            length = palindrom(S[i:j+1])
            # print(S[i:j])
            
            if l < length:
                out = S[i:j+1]
            if len(d) < len(out):
                d = out
                # print("BHai uttar",d)
    return d
S = 'abacdfgdcaba'
print(longestPalindrome(S))
