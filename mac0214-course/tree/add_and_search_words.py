import string

class Node:

    def __init__(self, char: str):
        self.char = char
        self.eow = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = Node(None)
        
        alphabet = string.ascii_lowercase

        self.char_to_index = {}
        for i, char in enumerate(alphabet):
            self.char_to_index[char] = i

    def addWord(self, word: str) -> None:

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

        if char == ".":
            results = []
            
            if index == len(word)-1:
                for child in node.children:
                    if child is None:
                        results.append(False)
                    else:
                        if child.eow:
                            results.append(True)
                        else:
                            results.append(False)
            else:
                for child in node.children:
                    results.append(self.searchRec(child, index+1, word))
            
            return any(results)

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