import sys
sys.setrecursionlimit(20000000)
class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.num)

class Tree:
    def __init__(self):
        self.root = None
    def get_root(self):
        return self.root
    def insert(self, x, y, num):
        new_node = Node(x, y, num)
        cur = self.root
        if cur == None:
            self.root = new_node
            return
        while True:
            parent = cur
            if x < cur.x: 
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return
                
    def preorder_traverse(self, cur):
        global preorder
        if not cur:
            return
        preorder.append(cur.num)
        self.preorder_traverse(cur.left)
        self.preorder_traverse(cur.right)
        
    def postorder_traverse(self, cur):
        global postorder
        if not cur:
            return
        self.postorder_traverse(cur.left)
        self.postorder_traverse(cur.right)
        postorder.append(cur.num)
    
def solution(nodeinfo):
    global preorder, postorder
    preorder = []
    postorder = []
    answer = []
    for i in range(1, len(nodeinfo)+1):
        nodeinfo[i-1].append(i)
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))
    tree = Tree()
    tree.insert(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])
    for i in range(1, len(nodeinfo)):
        tree.insert(nodeinfo[i][0], nodeinfo[i][1], nodeinfo[i][2])
    tree.preorder_traverse(tree.get_root())
    tree.postorder_traverse(tree.get_root())
    answer.append(preorder)
    answer.append(postorder)
    return answer
