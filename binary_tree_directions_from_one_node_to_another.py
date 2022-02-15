# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ITERATIVE SOLUTION USING BFS AND A STACK MUCH FASTER
# TIME O(N) and SPACE O(W) W IS maximum width of the tree
# Recursion could get us faster, but we would be using so much more space bc of the call stacks
#    that is a given when implementing recursive techniques--- i'd rather save space lol
#    but i guess i should ask what the customer would prefer in this situation?
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            queue=deque([])
            path=''
            queue.append((root,path))
            visited=set()
            ans=['','']
            while queue and (ans[0]=='' or ans[1]==''):
                node,path=queue.popleft()
                if node.val==startValue:
                    ans[0]=path
                if node.val==destValue:
                    ans[1]=path
                if node.left and (ans[0]=='' or ans[1]==''):
                    queue.append((node.left,path+'L'))
                if node.right and (ans[0]=='' or ans[1]==''):
                    queue.append((node.right,path+'R'))
            final_ans=''
            i=0
            while i<len(ans[0]) and i<len(ans[1]) and ans[0][i]==ans[1][i]:
                i+=1
            for j in range(i,len(ans[0])):
                final_ans+='U'
            final_ans+=ans[1][i:]
            return final_ans
