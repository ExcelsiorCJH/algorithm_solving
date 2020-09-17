# Code Snippets



## 01. Graph

### 1) DFS (Depth-First Search)

```python
graph = {
    1: [2, 3, 4],
    2: [5], 
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
```



#### 재귀 구조

```python
def recursive_dfs(graph, v, discovered=[]):
    discovered.append(v)
    for w in graph[v]: # graph is dict{int: List}
        if not w in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered
```



#### 스택을 이용한 반복 구조

```python
def iterative_dfs(graph, start_v):
    discovered = []
    stack = [start_v]
    
    # graph is dict{int: List}
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```



### 2) BFS(Breadth-First Search)

#### Deque를 이용한 반복 구조

```python
from collections import deque

def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = deque([start_v])
    # graph is dict{int: List}
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```



### 3) DFS 동서남북 탐색

```python
# up, down, left, right
directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

def dfs(graph, x, y, directions):
    visited = []
    stack = [(x, y)]

    while stack:
        sx, sy = stack.pop()
        # ch = graph[sx][sy]
        if (sx, sy) not in visited:
            visited.append((sx, sy))
            for nx, ny in directions:
                nx += sx
                ny += sy
                if (
                    (0 <= nx < N and 0 <= ny < N)
                    # and graph[nx][ny] == ch
                    and (nx, ny) not in visited
                ):
                    stack.append((nx, ny))
    return visited
```



## 02. Binary Search Tree(BST)
```python
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root = None

    # 1) insert
    def insert(self, value):
        self.root = self._insert_value(self.root, value)
        return self.root is not None

    def _insert_value(self, node, value):
        if not node:
            node = Node(value)
        elif value <= node.value:
            node.left = self._insert_value(node.left, value)
        elif value > node.value:
            node.right = self._insert_value(node.right, value)
        return node

    # 2) search
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.value == key:
            return root is not None
        elif key < root.value:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # 3) delete
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.value:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.value:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
```

- examples

```python
vals = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BST()
for val in vals:
    bst.insert(val)
    
# Find
print(bst.find(15))  # True
print(bst.find(17))  # False

# Delete
print(bst.delete(55))  # True
print(bst.delete(14))  # True
print(bst.delete(11))  # False
```

