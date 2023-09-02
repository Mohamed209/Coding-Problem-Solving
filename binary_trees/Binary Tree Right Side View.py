class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        res = []  # initialize result array to return later.
        q = collections.deque()
        q.append(root)
        # while q is not empty
        while q:
            # length of curr level
            level_len = len(q)
            # iterate through each level
            for i in range(level_len):
                curr = q.popleft()
                # if we are at last index then append item to the result array.
                if i == level_len - 1:
                    res.append(curr.val)
                # add curr.left and curr.right to q if not empty
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        # return result array
        return res
