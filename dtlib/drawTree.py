from graphviz import Digraph

def drawTree(model, cols):
    tree = Digraph()

    counter = [0]

    def assign_uid(node):
        if node is None:
            return
        node._uid = f"N{counter[0]}"
        counter[0] += 1
        assign_uid(node.left)
        assign_uid(node.right)

    assign_uid(model.root)

    q = [model.root]

    while q:
        node = q.pop()
        node_id = node._uid

        if node.isleaf:
            tree.node(node_id, label=f"Class: {node.predClass}", shape="rectangle")
        else:
            tree.node(node_id, label=f"{cols[node.ind]}")

        if node.left:
            q.append(node.left)
            tree.edge(node_id, node.left._uid, label="Yes")
        if node.right:
            q.append(node.right)
            tree.edge(node_id, node.right._uid, label="No")

    tree.render('tree', view=True)
