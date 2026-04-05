
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams: list[list[str]] = []

        while len(strs) > 0:
            str1 = strs[0]
            strs.remove(str1)

            anagram: list[str] = []
            anagram.append(str1)
            for str2 in strs:
                if set(str1) == set(str2):
                    anagram.append(str2)

            for str2 in anagram:
                if str2 in strs:
                    strs.remove(str2)

            anagrams.append(anagram)

        return anagrams

