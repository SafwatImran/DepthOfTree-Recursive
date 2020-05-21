import threading
import sys
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class Node : 

    def __init__(self,data=None,parent=None,depth=None):
        self.parent=parent
        self.child=[]
        self.data=data
        self.depth = depth

    def insert (self, n):
        if self.data:
            self.child.append(n)
        else:
            self.data = self.data
    def getParent(self):
        return self.parent


    def calculateDepth(self,arrayOfNodes):
        array = arrayOfNodes
        if self.parent==-1:
            self.depth = 1 
        else:
            p = self.parent
            self.depth = Node.calculateDepth(array[p],array) + 1
        return self.depth

    

def treeheight(n, parents):
    nodes = []
    for i in range(n):
        nodes.append(Node(i,parents[i]))
    
    

    for k in range(n):
        a = Node.getParent(nodes[k])
        if a!=-1:
            nodes[a].insert(k)

    
    maxDepth=0
    for x in range(n):
        y = nodes[x]
        maxDepth = max(maxDepth,(Node.calculateDepth(nodes[x],nodes)))
    print(maxDepth)    


def main():
    numberOfNodes = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))

    treeheight(numberOfNodes,parents)

threading.Thread(target=main).start()