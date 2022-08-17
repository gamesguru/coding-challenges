class Node:
    def __init__(self, parent_id, id, name):
        self.id = id
        self.parent_id = parent_id
        self.name = name
        self.children = []


def printChildren(node, level=1):
    for c in node.children:
        padding = "  " * level
        print(padding + c.name + " (" + str(c.id) + ")")
        # Recursive call
        printChildren(c, level + 1)


def printAncestors(people, node, level=1):
    print(node.name)
    while node.parent_id != -1:
        node = people[node.parent_id]
        print(node.name)


def printTree(s):
    people = [x.split(",") for x in s.split("|")]
    people = [Node(int(x[0].replace("null", "-1")), int(x[1]), x[2]) for x in people]
    people = {x.id: x for x in people}

    # Build children lists
    for p in people.values():
        p_id = p.parent_id
        if p_id > -1:
            people[p_id].children.append(p)

    # assume first person is root
    root = people[0]
    # print(root.name + " (" + str(root.id) + ")")
    # printChildren(root)

    # challenge 3
    printAncestors(people, people[6])


printTree(
    "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
)
