# https://leetcode.com/problems/implement-trie-prefix-tree

import string

class Node:

    def __init__(self, char: str):
        self.char = char
        self.eow = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = Node(None)
        
        alphabet = string.ascii_lowercase

        self.char_to_index = {}
        for i, char in enumerate(alphabet):
            self.char_to_index[char] = i

    def insert(self, word: str) -> None:
        current_node = self.root

        for i, char in enumerate(word):
            alphabet_idx = self.char_to_index[char]
            child = current_node.children[alphabet_idx]

            if child is None:
                current_node.children[alphabet_idx] = Node(char)
            
            current_node = current_node.children[alphabet_idx]

            if i == len(word)-1:
                current_node.eow = True

    def search(self, word: str) -> bool:
        return self.searchRec(self.root, 0, word)
        
    def searchRec(self, node, index, word):
        if node is None:
            return False
        
        char = word[index]

        alphabet_idx = self.char_to_index[char]
        child = node.children[alphabet_idx]
        
        if index < len(word)-1:
            return self.searchRec(child, index+1, word)

        if child is None:
            return False
        else:
            if child.eow:
                return True
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithRec(self.root, 0, prefix)
        
    def startsWithRec(self, node, index, prefix):
        if node is None:
            return False
        
        char = prefix[index]

        alphabet_idx = self.char_to_index[char]
        child = node.children[alphabet_idx]
        
        if index < len(prefix)-1:
            return self.startsWithRec(child, index+1, prefix)

        if child is None:
            return False
        else:
            return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        

if __name__ == "__main__":

    t = Trie()

    t.insert("apple")
    
    print(t.startsWith("app"))