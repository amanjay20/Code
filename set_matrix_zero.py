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
