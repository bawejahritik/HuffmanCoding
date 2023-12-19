class Node:
    def __init__(self, data = None) -> None:
        self.left = None
        self.right = None
        self.val = data



text = "c" * 32

text += ("d" * 42)
text += ("e" * 120)
text += ("k" * 7)
text += ("l" * 42)
text += ("m" * 24)
text += ("u" * 37)
text += ("z" * 2)

freq = {}

for c in text:
    freq[c] = 1 + freq.get(c, 0)


print(freq)

freq = sorted(freq.items(), key=lambda x:x[1])

print(freq)

while len(freq) > 1:
    root = Node()
    node1 = freq[0]
    node2 = freq[1]

    freq = freq[2:]

    root.val = node1[1] + node2[1]
    root.left = node1[0]
    root.right = node2[0]

    freq.append((root, root.val))
    freq = sorted(freq, key=lambda x:x[1])


def dfs(root, path):
    if root is None:
        return
    
    if type(root) is str:
        print(f'{root} -> {path}')
        return
    
    dfs(root.left, path + "0")
    # print(root.val)
    dfs(root.right, path + "1")

dfs(freq[0][0], "")