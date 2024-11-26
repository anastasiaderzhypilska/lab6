matrix = [
    [-3, -5, -45, -71, -5],
    [0, 1, 3, 2, 7],
    [11, 9, 45, 0, 4],
    [9, 19, 55, 44, 90],
    [-3, -4, -1, -5, 0]
]

def geometric_mean(column):
    product = 1  
    count = 0  
    
    for i in range(len(column)):
        if column[i] != 0: 
            if column[i] < 0:
                value = -column[i]  
            else:
                value = column[i]
            product = product * value
            count = count + 1
    
    if count > 0:
        root = 1 / float(count)
        result = 1
        for _ in range(int(root * 1000)):  
            result = result * (product ** (1 / 1000))
        return result
    else:
        return 0

def selection_sort_desc(row):
    n = 0
    for _ in row:  
        n = n + 1
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if row[j] > row[max_idx]:
                max_idx = j
        temp = row[i]
        row[i] = row[max_idx]
        row[max_idx] = temp

col_means = []
for col in range(len(matrix[0])):  
    column = []
    for row in range(len(matrix)):  
        column.append(matrix[row][col])
    col_means.append(geometric_mean(column))

sum_of_means = 0
for i in range(len(col_means)):
    sum_of_means = sum_of_means + col_means[i]

print("Середні геометричні значення для стовпців:", col_means)
print("Сума середніх геометричних:", sum_of_means)

for i in range(len(matrix)):
    selection_sort_desc(matrix[i])

print("Матриця після сортування рядків:")
for row in matrix:
    print(row)