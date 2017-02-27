#!/usr/bin/python
#Filename: rbtree.py
import os

class RbtreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.red = False


class Rbtree:
    def __init__(self):
        self.NIL = RbtreeNode(None)
        self.root = self.NIL
        self.DotString = ''
        self.Step = 0

    def insert(self, nodedata):
        self.Step += 1
        rbtreenode = RbtreeNode(nodedata)
        z = rbtreenode
        z.parent=self.NIL
        z.left=self.NIL
        z.right=self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
            self.root.parent=self.NIL
            self.root.red=False
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.red = True
        self.insertFixup(z)

    def insertFixup(self, z):
        while z.parent.red == True:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.red == True:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.parent.right:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.red == True:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.parent.left:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.leftRotate(z.parent.parent)
        self.root.red = False

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def printTree(self):
        curRow = []
        curRow.append(self.root)
        self.printRow(curRow)

    def printRow(self, curRow):
        nextRow = []
        for a in curRow:
            if a != self.NIL:
                if a.left != self.NIL:
                    nextRow.append(a.left)
                if a.right != self.NIL:
                    nextRow.append(a.right)
                color = 'black'
                if a.red:
                    color = 'red'
                print str(a.data)+'['+color+']',
            if a == curRow[-1]:
                print "\n"
                if len(nextRow) == 0:
                    break
                else:
                    self.printRow(nextRow)


    def printTreeDots(self):
        self.DotString = 'graph{\nratio=fill;size="8,4";\n'
        if self.root.data is not None:
            self.DotString += 'node' + str(self.root.data) + '[' + 'label=' + str(self.root.data) + ', color=black];\n'
            self.printCurNode(self.root)
        else:
            self.DotString += 'node0[label=NIL, color=black];\n'

        self.DotString += '}'
        print(self.DotString)
        f=open("./rbtree.dot", 'wt')
        if f is not None:
            f.write(self.DotString)
            f.close()
            os.system("dot -Tjpg rbtree.dot -o rbtree" + str(self.Step) + ".jpg")


    def printCurNode(self, node):
        if node == self.NIL:
            return

        if node.left.data is not None:
            self.DotString += 'node' + str(node.left.data) + '[' + 'label=' + str(node.left.data) + ', color=' + ('black' if node.left.red is False else 'red' ) + ']' + ';\n'
            self.DotString += 'node' + str(node.data) + ' -- ' + 'node' + str(node.left.data) + ';\n'
        else:
            self.DotString += 'node' + str(node.data) + 'lc [label=NIL, color=black];\n'
            self.DotString += 'node' + str(node.data) + ' -- ' + 'node' + str(node.data) + 'lc;\n'

        if node.right.data is not None:
            self.DotString += 'node' + str(node.right.data) + '[' + 'label=' + str(node.right.data) + ', color=' + ('black' if node.right.red is False else 'red' ) + ']' + ';\n'
            self.DotString += 'node' + str(node.data) + ' -- ' + 'node' + str(node.right.data) + ';\n'
        else:
            self.DotString += 'node' + str(node.data) + 'rc [label=NIL, color=black];\n'
            self.DotString += 'node' + str(node.data) + ' -- ' + 'node' + str(node.data) + 'rc;\n'
        self.printCurNode(node.left)
        self.printCurNode(node.right)


rbtree = Rbtree()
rbtree.printTreeDots()
rbtree.insert(1)
rbtree.printTreeDots()
rbtree.insert(3)
rbtree.printTreeDots()
rbtree.insert(5)
rbtree.printTreeDots()
rbtree.insert(7)
rbtree.printTreeDots()
rbtree.insert(9)
rbtree.printTreeDots()
rbtree.insert(8)
rbtree.printTreeDots()
rbtree.insert(6)
rbtree.printTreeDots()
rbtree.insert(4)
rbtree.printTreeDots()
rbtree.insert(2)
rbtree.printTreeDots()
rbtree.insert(0)
rbtree.printTree()
rbtree.printTreeDots()
