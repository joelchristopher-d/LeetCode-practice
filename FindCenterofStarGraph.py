class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1] else edges[0][1]











# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         n = len(edges) + 1
#         degree_count = [0] * (n + 1)
        
#         for edge in edges:
#             u, v = edge
#             degree_count[u] += 1
#             degree_count[v] += 1
        
#         for i in range(1, n + 1):
#             if degree_count[i] == n - 1:
#                 return i
        
#         return -1
