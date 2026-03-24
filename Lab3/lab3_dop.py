class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_tree_from_preorder(preorder):
    if not preorder: return None
    root = Node(preorder[0])
    for val in preorder[1:]:
        curr = root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val); break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val); break
                curr = curr.right
    return root

def get_top_view(node):
    if node is None: return []
    return get_top_view(node.left) + [node.val] + get_top_view(node.right)

def draw_dynamic_view(root):
    if not root: return
    
    pos = {}
    links = []
    
    def assign_coords(node, x, y, side):
        pos[node.val] = (x, y)
        
        if node.left:
            if side == "root":
                assign_coords(node.left, x - 10, y, "left_side")
                links.append((x - 5, y, '-'))
            elif side == "left_side":
                assign_coords(node.left, x - 6, y - 4, "left_side")
                links.append((x - 3, y - 2, '\\'))
            elif side == "right_side":
                assign_coords(node.left, x + 6, y + 4, "right_side")
                links.append((x + 3, y + 2, '\\'))
                
        if node.right:
            if side == "root":
                assign_coords(node.right, x + 10, y, "right_side")
                links.append((x + 5, y, '-'))
            elif side == "left_side":
                assign_coords(node.right, x - 6, y + 4, "left_side")
                links.append((x - 3, y + 2, '/'))
            elif side == "right_side":
                assign_coords(node.right, x + 6, y - 4, "right_side")
                links.append((x + 3, y - 2, '/'))

    assign_coords(root, 0, 0, "root")
    
    min_x = min(x for x, y in pos.values())
    max_x = max(x for x, y in pos.values())
    min_y = min(y for x, y in pos.values())
    max_y = max(y for x, y in pos.values())
    
    width = max_x - min_x + 6 
    height = max_y - min_y + 1
    
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    for val, (x, y) in pos.items():
        s = f"{val:<2}"
        grid[y - min_y][x - min_x] = s[0]
        grid[y - min_y][x - min_x + 1] = s[1]
    
    for x, y, char in links:
        grid[y - min_y][x - min_x] = char
        
    for row in grid:
        line = "".join(row).rstrip()
        if line:
            print(line)