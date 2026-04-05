class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams: list[list[str]] = []

        while len(strs) > 0:
            anagram = [strs[0]]

            for word in strs:
                print(f"Comparing {anagram[0]} and {word}")
                if self.isAnagram(anagram[0], word):
                    print(f"Found anagram: {anagram[0]} and {word}\n")
                    anagram.append(word)

            for word in anagram:
                if word in strs:
                    strs.remove(word)

            anagrams.append(list(set(anagram)))

        return anagrams
