class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = dict()
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        runner = self.root
        for c in word:
            if c not in runner.children:
                runner.children[c] = TrieNode()
            runner = runner.children[c]
        runner.isEnd = True

    def norm_search(self, word:str, root):
        if not word and root.isEnd == True:
            return True
        elif not word:
            return False
        runner = root
        for i, c in enumerate(word):
            #print(c)
            if c == ".":
                return self.sub_search(word[i:], runner)
            else:
                if c not in runner.children:
                    return False
                else:
                    runner = runner.children[c]
        return runner.isEnd


    def sub_search(self, word:str, root):
        runner = root
        #Called when the first character is a period
        check = False
        for c in root.children:
            #Gotta explore all possible
            check |= self.norm_search(word[1:], root.children[c])
            #print(c, check)
        return check


    def search(self, word: str) -> bool:
        #print(word)
        runner = self.root
        for i, c in enumerate(word):
            if c != ".":
                if c not in runner.children:
                    return False
                else:
                    runner = runner.children[c]
            else:
                return self.sub_search(word[i:], runner)
        
        return runner.isEnd
        
