# Breadth-First-Traverse example
# 幅優先探索アルゴリズムの例
# https://qiita.com/maebaru/items/53a30c78bad8d0df92af
from collections import deque


class Commit:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(q: deque, callback):
    # キューが空になるまで繰り返す
    while len(q) > 0:
        # キューの先端（左端）からnodeを取り出す
        node = q.popleft()

        if node is not None:
            callback(node.val)
            # nodeの子要素をキューの末尾（右端）に入れる
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


def printer(s: str):
    print(s)


def demo1():
    # Traverse a tree as follows:
    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7
    node1 = Commit(1)
    node2 = Commit(2)
    node3 = Commit(3)
    node4 = Commit(4)
    node5 = Commit(5)
    node6 = Commit(6)
    node7 = Commit(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    # キューを作って
    q = deque()
    # ルートノードをキューに入れる
    q.append(node1)
    # traverseする
    traverse(q, printer)


def demo2():
    # Traverse a tree as follows:
    #     1
    #    / \
    #   2   3
    #  /   /
    # 4    5
    node1 = Commit(1)
    node2 = Commit(2)
    node3 = Commit(3)
    node4 = Commit(4)
    node5 = Commit(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    # キューを作って
    q = deque()
    # ルートノードをキューに入れる
    q.append(node1)
    # traverseする
    traverse(q, printer)
