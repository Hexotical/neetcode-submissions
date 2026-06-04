class TreeNode:
    def __init__(self):
        self.end = False
        self.successors = dict()

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        runner = self.root
        for i, c in enumerate(word):
            if c not in runner.successors:
                runner.successors[c] = TreeNode()
            runner = runner.successors[c]
        runner.end = True

    def search(self, word: str) -> bool:
        runner = self.root
        for c in word:
            if c in runner.successors:
                runner = runner.successors[c]
            else:
                return False
        return runner.end

    def startsWith(self, prefix: str) -> bool:
        runner = self.root
        for c in prefix:
            if c in runner.successors:
                runner = runner.successors[c]
            else:
                return False
        return True
        
        