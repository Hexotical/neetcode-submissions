class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        runner = self.root
        for c in word:
            if c in runner.children:
                runner = runner.children[c]
            else:
                return False
        return runner.isEnd

    def insert(self, word):
        runner = self.root
        for c in word:
            #print(c)
            if c not in runner.children:
                runner.children[c] = TrieNode()
            runner = runner.children[c]
        runner.isEnd = True
        #print(runner.isEnd)
                


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        #So for every square
        #do a dfs and build a trie
        #Then for the words list just run a search through the Trie
        to_ret = set()
        for word in words:
            trie.insert(word)

        visited = set()
        def dfs(row, col, trie_node, word):
            #print(word, row, col)
            if trie_node.isEnd:
                to_ret.add(word)
            if row < 0 or row > len(board)-1:
                return
            if col < 0 or col > len(board[0])-1:
                return
            if (row, col) in visited:
                return
            if board[row][col] not in trie_node.children:
                return
            visited.add((row, col))
            word += board[row][col]
            
            dfs(row-1, col, trie_node.children[board[row][col]], word)
            dfs(row+1, col, trie_node.children[board[row][col]], word)
            dfs(row, col+1, trie_node.children[board[row][col]], word)
            dfs(row, col-1, trie_node.children[board[row][col]], word)
            visited.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie.root, "")
        return list(to_ret)

                    




