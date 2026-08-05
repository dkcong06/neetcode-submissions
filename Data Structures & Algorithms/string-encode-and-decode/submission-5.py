class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output = output + str(len(string)) + "/" + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = 0
            word = ""
            while s[i] != "/":
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            while length > 0:
                word += s[i]
                i += 1
                length -= 1
            output.append(word)
        return output


