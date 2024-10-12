# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if not root:
            return []

        def markParent(parent_map, root):
            q = deque()

            q.append(root)

            while q:
                root = q.popleft()

                if root.left:
                    parent_map[root.left] = root
                    q.append(root.left)

                if root.right:
                    parent_map[root.right] = root
                    q.append(root.right)

            return parent_map

        
        
        parent_map = markParent(collections.defaultdict(), root)

        print(parent_map)

        q = deque()
        visited = set()

        q.append(target)
        visited.add(target)
        distance = 0
        result = []

        while q:

            if distance == k:
                result.extend(node.val for node in q)
                return result

            n = len(q)

            for i in range(n):

                root = q.popleft()

                if root.left and root.left not in visited:
                    q.append(root.left)
                    visited.add(root.left)

                if root.right and root.right not in visited:
                    q.append(root.right)
                    visited.add(root.right)


                if root in parent_map and parent_map[root] not in visited:
                    q.append(parent_map[root])
                    visited.add(parent_map[root])

            
            distance +=1

        return result

                