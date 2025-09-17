# 🔹 Brute Force Approach
# Idea:
# Traverse the matrix and mark the rows and columns to be zeroed in a separate copy, then update the matrix.

# Time Complexity: O((m * n) * (m + n))
# Space Complexity: O(1) (ignoring the input modification constraint, because we are modifying in-place with a placeholder)

def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    # Use a placeholder value that can't be in input
    placeholder = -999999

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # Mark row
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] = placeholder
                # Mark column
                for k in range(m):
                    if matrix[k][j] != 0:
                        matrix[k][j] = placeholder

    # Replace all placeholders with 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == placeholder:
                matrix[i][j] = 0