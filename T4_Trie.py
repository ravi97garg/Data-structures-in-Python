class Trie:
    def __init__(self):
        self.numberOfWords = 0
        self.root = self.TrieNode()

    class TrieNode:
        def __init__(self):
            self.character = dict()
            self.isWordComplete = False
            self.numberOfWords = 0

    def getTotalNumberOfWords(self):
        return self.numberOfWords

    def insertWord(self, word):
        word = word.lower()
        current = self.root  # check if deep copy needed
        current.numberOfWords += 1
        size = len(word)
        for index in range(size):
            letter = word[index]
            if letter not in current.character:
                current.character[letter] = self.TrieNode()
            current = current.character[letter]
            current.numberOfWords += 1
        current.isWordComplete = True
        self.numberOfWords += 1

    def isWordPresent(self, word):
        word = word.lower()
        current = self.root
        size = len(word)
        for index in range(size):
            letter = word[index]
            if letter in current.character:
                current = current.character[letter]
            else:
                return None
        return current

    def isCompleteWordPresent(self, word):
        word = word.lower()
        lastNode = self.isWordPresent(word)
        if lastNode is None:
            return False
        else:
            return lastNode.isWordComplete

    def numberOfWordWithPrefix(self, word):
        word = word.lower()
        last = self.isWordPresent(word)
        if last is None:
            return 0
        else:
            return last.numberOfWords

    def isPrefixWordPresent(self, word):
        word = word.lower()
        lastNode = self.isWordPresent(word)
        if lastNode is None:
            return False
        else:
            return True


obj = Trie()
obj.insertWord('card')
obj.insertWord('car')
obj.insertWord('bike')
print(obj.isCompleteWordPresent('Card'))
print(obj.numberOfWordWithPrefix('cards'))