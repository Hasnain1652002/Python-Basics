def input_matrix():
    # Initialize an empty matrix
    matrix = []
    
    print("\nEnter aij ")  # Prompt the user to input the matrix coefficients

    # Loop to input a 3x3 matrix
    for i in range(3):
        row = []
        for j in range(3):
            row.append(float(input(f"a{i+1}{j+1}: ")))  # Take user input for each element
        matrix.append(row)  # Append the row to the matrix

    print("\nEnter bij :")  # Prompt for augmented column (right-hand side values)
    
    # Loop to input the rightmost column (b values)
    for i in range(3):
        matrix[i].append(float(input()))  
    
    return matrix  # Return the complete augmented matrix

def display_matrix(matrix, message="Augmented matrix A:"):
    """Function to display the matrix."""
    print(f"\n{message}")
    for i in range(len(matrix)):  
        print(matrix[i])  # Print each row of the matrix

def rowScale(A, r, k):
    """Scales row r by a factor k."""
    for i in range(len(A[r-1])):  # Iterate over all elements in row r
        A[r-1][i] = A[r-1][i] * k  # Multiply each element by k

def rowSwap(A, r1, r2):
    """Swaps row r1 with row r2."""
    A[r1-1], A[r2-1] = A[r2-1], A[r1-1]  # Swap the rows

def rowAddScale(A, r1, r2, k):
    """Performs row operation: Row r2 = Row r2 + k * Row r1."""
    for i in range(len(A[0])):  # Iterate over columns
        A[r2-1][i] = A[r2-1][i] + k * A[r1-1][i]  # Update row r2

def gaussElimination(A):
    """Performs Gaussian elimination to convert A into row echelon form."""
    rows = len(A)  # Number of rows

    for i in range(rows):  # Iterate over each column
        # If pivot element is zero, swap with a nonzero row
        if A[i][i] == 0:
            for j in range(i+1, rows):
                if A[j][i] != 0:
                    rowSwap(A, i+1, j+1)
                    break  # Stop once a swap is made

        # Eliminate values below the pivot
        for j in range(i+1, rows):
            if A[j][i] != 0:  # If the element is nonzero
                factor = -A[j][i] / A[i][i]  # Compute the factor for elimination
                rowAddScale(A, i+1, j+1, factor)  # Perform row operation

    return A  # Return the modified matrix in row echelon form

def check_solutions(A):
    """Determines whether the system has a unique, infinite, or no solution."""
    rows = len(A)
    
    rank_A = 0  # Rank of the coefficient matrix (A)
    rank_A_extended = 0  # Rank of the augmented matrix (A|b)

    for row in A:
        if any(row[:-1]):  # Check if at least one coefficient is nonzero
            rank_A += 1
        if any(row):  # Check if the entire row is nonzero (including last column)
            rank_A_extended += 1

    if rank_A == rank_A_extended == rows:
        return "unique"  # Unique solution exists
    elif rank_A == rank_A_extended and rank_A < rows:
        return "infinite"  # Infinite solutions exist
    elif rank_A < rank_A_extended:
        return "no solution"  # No solution exists
    return "unknown"

def format_solution_infinite(A):
    """Finds the solution in vector equation form for infinite solutions."""
    rows = len(A)
    cols = len(A[0]) - 1  # Number of variables (excluding augmented column)

    pivot_positions = []  # Stores positions of pivot variables
    free_variables = []  # Stores indices of free variables
    
    for i in range(rows):
        for j in range(cols):
            if A[i][j] != 0:
                pivot_positions.append(j)  # Store pivot column index
                break  

    all_variables = set(range(cols))
    dependent_vars = set(pivot_positions)
    free_variables = sorted(all_variables - dependent_vars)  # Identify free variables

    solution_vectors = {}

    for free_var in free_variables:
        vector = [0] * cols
        vector[free_var] = 1  # Set free variable to 1

        for i in range(len(pivot_positions)):
            pivot_col = pivot_positions[i]
            if pivot_col < free_var:
                vector[pivot_col] = -A[i][free_var]  # Compute dependent variable values

        solution_vectors[f"s{len(solution_vectors) + 1}"] = vector  # Store solution

    # Adjust naming of free variables
    if len(solution_vectors) == 1:
        keys = ["s"]
    elif len(solution_vectors) == 2:
        keys = ["s", "t"]
    else:
        keys = list(solution_vectors.keys())

    formatted_solution = " + ".join(f"{keys[i]} * {v}" for i, v in enumerate(solution_vectors.values()))

    return f"\nThis system of linear equations has infinite solutions: {formatted_solution}^T"

def backSubstitution(A):
    """Performs back-substitution on an upper triangular matrix."""
    rows = len(A)
    
    solution_type = check_solutions(A)  # Check the type of solution

    if solution_type == "no solution":
        print("\nThis system of linear equations has no solution.")
        return None
    elif solution_type == "infinite":
        print(format_solution_infinite(A))
        return None

    x = [0] * rows  # Initialize solution vector

    for i in range(rows - 1, -1, -1):  # Start from last row and move up
        x[i] = A[i][-1]  # Initialize with rightmost column (b)

        for j in range(i + 1, rows):  # Subtract known values from previous solutions
            x[i] -= A[i][j] * x[j]

        x[i] /= A[i][i]  # Solve for current variable

    print("\nThis system of linear equations has the unique solution: (", 
          ", ".join(f"{val:.2f}" for val in x), ")^T")

    return x  # Return solution vector

# Example matrices for testing
matrix = input_matrix()

# Display the input matrix
display_matrix(matrix)

# Perform Gaussian elimination
gaussElimination(matrix)

# Display the row echelon form
display_matrix(matrix, "Row echelon form after Gaussian elimination:")

# Perform back substitution to solve for variables
backSubstitution(matrix)
