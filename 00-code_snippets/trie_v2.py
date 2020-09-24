from collections import deque


class Node(object):
    """
    A single node of a trie.

    Children of nodes are defined in a dictionary
    where each (key, value) pair is in the form of
    (Node.key, Node() object).
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}


class Trie(object):
    """
    A simple Trie with insert, search, and starts_with methods.
    """

    def __init__(self):
        self.head = Node(None)

    """
    Inserts string in the trie.
    """

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # When we have reached the end of the string, set the curr_node's data to string.
        # This also denotes that curr_node represents the final character of string.
        curr_node.data = string

    """
    Returns if string exists in the trie
    """

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # Reached the end of string,
        # If curr_node has data (i.e. curr_node is not None), string exists in the trie
        if curr_node.data != None:
            return True

    """
    Returns a list of words in the trie
    that starts with the given prefix.
    """

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # Locate the prefix in the trie,
        # and make subtrie point to prefix's last character Node
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # Using BFS, traverse through the prefix subtrie,
        # and look for nodes with non-null data fields.
        queue = deque(subtrie.children.values())

        while queue:
            curr = queue.popleft()
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())

        return result


if __name__ == "__main__":
    # Test
    t = Trie()
    words = ["romane", "romanus", "romulus", "ruben", "rubens", "ruber", "rubicon", "ruler"]
    for word in words:
        t.insert(word)

    print(t.search("romulus"))
    print(t.search("ruler"))
    print(t.search("rulere"))
    print(t.search("romunus"))
    print(t.starts_with("ro"))
    print(t.starts_with("rube"))