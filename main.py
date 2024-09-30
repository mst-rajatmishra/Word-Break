class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)  # Use a set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

# Example usage:
# solution = Solution()
# print(solution.wordBreak("leetcode", ["leet", "code"]))  # Output: True
# print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
# print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
