class Solution:
    def encode(self, strs: list[str]) -> str:
        return "\n".join(strs)

    def decode(self, s: str) -> list[str]:
        if s == "":
            return []
        return s.split("\n")
