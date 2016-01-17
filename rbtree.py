#!/usr/bin/python
#Filename: rbtree.py

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

    def insert(self, nodedata):
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

rbtree = Rbtree()
rbtree.insert(1)
rbtree.insert(3)
rbtree.insert(5)
rbtree.insert(7)
rbtree.insert(9)
rbtree.insert(8)
rbtree.insert(6)
rbtree.insert(4)
rbtree.insert(2)
rbtree.insert(0)
