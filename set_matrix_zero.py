# # class Solution:
# #     def setZeroes(self, matrix: List[List[int]]) -> None:
# #         m, n = len(matrix), len(matrix[0])
# #         first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
# #         first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

# #     # Use first row and col as markers
# #         for i in range(1, m):
# #             for j in range(1, n):
# #                 if matrix[i][j] == 0:
# #                     matrix[i][0] = 0
# #                     matrix[0][j] = 0

# #     # Zero out cells based on markers
# #         for i in range(1, m):
# #             for j in range(1, n):
# #                 if matrix[i][0] == 0 or matrix[0][j] == 0:
# #                     matrix[i][j] = 0

# #     # Update first row if needed
# #         if first_row_has_zero:
# #             for j in range(n):
# #                 matrix[0][j] = 0

# #     # Update first column if needed
# #         if first_col_has_zero:
# #             for i in range(m):
# #                 matrix[i][0] = 0
# 🔹 Optimal Approach (In-Place, O(1) Space)
# Idea:
# Use the first row and first column as markers. Keep two flags to track if the first row and column originally had any zero.

# Time Complexity: O(m * n)
# Space Complexity: O(1)
# brute force set matrix zero 
# ✅ Brute Force Idea:

# For every element in the matrix, if it’s zero, mark its row and column to be set to zero later.

# But if we directly set rows and columns to 0 as we find zeros, it will affect future checks.

# So, we use an auxiliary matrix or special marker (e.g., a placeholder value like -1 or any number not in the matrix) to mark cells to be zeroed.

# from typing import List

# def setZeroes(matrix: List[List[int]]) -> None:
#     n = len(matrix)
#     m = len(matrix[0])
    
#     # Step 1: Create auxiliary matrix to store marks
#     mark = [[False for _ in range(m)] for _ in range(n)]
    
#     # Step 2: Mark the cells to be zeroed
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 mark[i][j] = True
    
#     # Step 3: For each marked cell, set entire row and column to zero
#     for i in range(n):
#         for j in range(m):
#             if mark[i][j]:
#                 # Set row to zero
#                 for col in range(m):
#                     matrix[i][col] = 0
#                 # Set column to zero
#                 for row in range(n):
#                     matrix[row][j] = 0
