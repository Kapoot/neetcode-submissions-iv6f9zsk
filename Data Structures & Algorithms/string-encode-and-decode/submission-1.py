class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            string  = str(len(word)) + '#' + word
            encoded.append(string)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = []
            while s[i] != '#':
                length.append(s[i])
                i += 1
            length = str(''.join(length))
            i += 1
            word = []
            for _ in range(int(length)):
                word.append(s[i])
                i += 1
            res.append(''.join(word))
        return res


            


                


