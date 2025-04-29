class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        temp_s=""
        
        for i in range(len(s)):
            # print(f"temp_s: {temp_s}")
            # print(f"new char: {s[i]}")
            if s[i] in temp_s:
                # print(f"s[i] in temp_s")
                temp_length=len(temp_s)
                if temp_length>max_length:
                    max_length=temp_length
                drop_idx=temp_s.find(s[i])
                # print(f"drop_idx: {drop_idx}")
                temp_s=temp_s[drop_idx+1:]
                temp_s+=s[i]
            else:
                temp_s+=s[i]
                temp_length=len(temp_s)
                if temp_length>max_length:
                    max_length=temp_length
        # print(f"new temp_s: {temp_s}")
        return max_length
