class Matrix:
    def __init__(self, data):
        # Create a matrix from a list of lists.
        self.data = data

    def add(self, other_matrix):
        # Add two matrices. They must be the same size.
        if len(self.data) != len(other_matrix.data) or len(self.data[0]) != len(other_matrix.data[0]):
            return "Error: Matrices must be the same size to add them."
        
        # Add the matrices element by element
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] + other_matrix.data[i][j])
            result.append(row)
        return result

    def multiply(self, other_matrix):
        # Multiply two matrices. They must have matching dimensions.
        if len(self.data[0]) != len(other_matrix.data):
            return "Error: Matrices can't be multiplied!"
        
        # Multiply the matrices step by step
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other_matrix.data[0])):
                # Multiply and sum the corresponding elements
                product = 0
                for k in range(len(self.data[0])):
                    product += self.data[i][k] * other_matrix.data[k][j]
                row.append(product)
            result.append(row)
        return result

    def transpose(self):
        # Transpose the matrix (flip rows and columns)
        result = []
        for j in range(len(self.data[0])):
            row = []
            for i in range(len(self.data)):
                row.append(self.data[i][j])
            result.append(row)
        return result

    def scalar_multiply(self, scalar):
        # Multiply the matrix by a scalar value
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] * scalar)
            result.append(row)
        return result

    def determinant(self):
        # Calculate the determinant of a 2x2 matrix
        if len(self.data) == 2 and len(self.data[0]) == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        return "Error: Determinant only defined for 2x2 matrices."

    def display(self):
        # Display the matrix
        for row in self.data:
            print(row)

# Example usage:
if __name__ == "__main__":
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    # Add the matrices
    print("Matrix addition result:")
    result_add = matrix1.add(matrix2)
    if isinstance(result_add, list):
        for row in result_add:
            print(row)  # Should show [[6, 8], [10, 12]]
    else:
        print(result_add)  # Error message if matrices can't be added
    
    # Multiply the matrices
    print("\nMatrix multiplication result:")
    result_mul = matrix1.multiply(matrix2)
    if isinstance(result_mul, list):
        for row in result_mul:
            print(row)  # Should show [[19, 22], [43, 50]]
    else:
        print(result_mul)  # Error message if matrices can't be multiplied

    # Transpose a matrix
    print("\nMatrix transpose result:")
    result_transpose = matrix1.transpose()
    for row in result_transpose:
        print(row)  # Should show [[1, 3], [2, 4]]
    
    # Scalar multiplication
    print("\nMatrix scalar multiplication result (multiply by 2):")
    result_scalar = matrix1.scalar_multiply(2)
    for row in result_scalar:
        print(row)  # Should show [[2, 4], [6, 8]]
    
    # Determinant
    print("\nMatrix determinant result:")
    result_determinant = matrix1.determinant()
    print(result_determinant)  # Should show -2
