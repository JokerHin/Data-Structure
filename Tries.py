class TrieNode: #O(m)
    def __int__(self):
        self.children = {}
        self.is_word = False

class Tries:
    def __int__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def delete(self,word):
        node = self.root
        stack = []
        for char in word:
            if char not in node.children:
                return
            stack.append((node,char))
            node = node.children[char]

        if not node.is_word:
            return

        node.is_word = False

        while stack:
            parent,char = stack.pop()

            if not node.children and not node.is_word:
                del parent.children[char]
            else:
                break

            node = parent
