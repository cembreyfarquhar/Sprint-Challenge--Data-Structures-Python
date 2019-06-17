import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# 4.4s -> .8s
# duplicates = []
# for name_2 in names_2:
# 	if name_2 in names_1:
# 		duplicates.append(name_2)
## BST class
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        # print(f'Contains: {target}')
        if self.value == target:
            return True
        if self.value > target:
            if self.left and self.left.contains(target):
                return True
            else:
                return False
        elif self.value < target:
            if self.right and self.right.contains(target):
                return True
            else:
                return False

## create tree

bst = BinarySearchTree(names_1[0])

for name_1 in names_1:
	bst.insert(name_1)

duplicates = []
for name_2 in names_2:
	if bst.contains(name_2):
		duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

