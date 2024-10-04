def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        # Initialize a new row with 1s
        row = [1] * (i + 1)

        # Calculate the values for the interior of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle
        triangle.append(row)

    return triangle
