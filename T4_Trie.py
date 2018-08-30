# Merge Sort Tree
# Date Created: 30 August 2018
# Created by Ravi garg


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
        current = self.root
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

    def delete(self, word):
        word = word.lower()
        if not self.isCompleteWordPresent(word):
            raise ValueError("Word not present")
        else:
            self.deleteWord(word, len(word), 0)
            self.numberOfWords -= 1

    def deleteWord(self, word, size, index, current=None):
        if current is None:
            current = self.root
        if index == size:
            current.isWordComplete = False
            return len(current.character) == 0
        else:
            deletable = self.deleteWord(word, size, index + 1, current.character[word[index]])
            if deletable:
                self.root.numberOfWords -= 1
                return len(current.character) == 0
            else:
                return False

    def getLongestPrefix(self, word):
        current = self.root
        endIndex = 0
        size = len(word)
        for index in range(size):
            letter = word[index]
            if letter in current.character:
                if current.isWordComplete:
                    endindex = index
                current = current.character[letter]
            else:
                break
        if endIndex == 0:
            return None
        else:
            return word[0:endIndex]


if __name__ == "__main__":
    obj = Trie()
    obj.insertWord('card')
    obj.insertWord('car')
    obj.insertWord('bike')
    print(obj.isCompleteWordPresent('card'))
    obj.delete('card')
    print(obj.isCompleteWordPresent('card'))
