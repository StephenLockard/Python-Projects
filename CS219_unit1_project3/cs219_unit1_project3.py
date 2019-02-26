class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = list()


def add_guest(root, Guest):
    if Guest < root.data[0]:
        if root.left is None:
            root.left = Node()
            root.left.data.append(Guest)
        else:
            add_guest(root.left, Guest)
    else:
        if Guest > root.data[0]:
            if root.right is None:
                root.right = Node()
                root.right.data.append(Guest)
            else:
                add_guest(root.right, Guest)
        else:
            root.data.append(Guest)


def print_guest(root):
    if root is None:
        return
    print(root.data)
    print_guest(root.left)
    print_guest(root.right)


root = Node()
root.data.append("M")
for i in range(0, 6):
    add_guest(root, input("Add the guests name:"))
print("Left Side:")
print_guest(root.left)
print("Right Side:")
print_guest(root.right)
