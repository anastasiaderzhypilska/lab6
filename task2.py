class Matrix:
    def __init__(self, data):
        self.data = data

    def sorting_decorator(method):
        def wrapper(self, *args, **kwargs):
            for i in range(self.get_row_count(self.data)):
                self.selection_sort_desc(self.data[i])
            print("Рядки були відсортовані перед виконанням методу.")
            return method(self, *args, **kwargs)
        return wrapper

    def get_row_count(self, matrix):
        count = 0
        for _ in matrix:
            count += 1
        return count

    def get_col_count(self, matrix):
        count = 0
        for _ in matrix[0]:
            count += 1
        return count

    def geometric_mean(self, column):
        product = 1  
        count = 0  

        for i in range(self.get_row_count(column)):
            if column[i] != 0:  
                value = -column[i] if column[i] < 0 else column[i]
                product *= value
                count += 1

        if count > 0:
            root = 1 / float(count)
            result = 1
            for _ in range(int(root * 1000)):  
                result *= (product ** (1 / 1000))
            return result
        else:
            return 0

    def selection_sort_desc(self, row):
        n = len(row)

        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if row[j] > row[max_idx]:
                    max_idx = j
            temp = row[i]
            row[i] = row[max_idx]
            row[max_idx] = temp

    @sorting_decorator
    def calculate_column_means(self):
        col_means = []
        col_count = self.get_col_count(self.data)
        row_count = self.get_row_count(self.data)

        for col in range(col_count):
            column = []
            for row in range(row_count):
                column.append(self.data[row][col])
            col_means.append(self.geometric_mean(column))
        return col_means

    @sorting_decorator
    def sum_of_column_means(self):
        col_means = self.calculate_column_means()
        total = 0
        for mean in col_means:
            total += mean
        return total

    def __sub__(self, other):
        if self.get_row_count(self.data) != self.get_row_count(other.data) or \
           self.get_col_count(self.data) != self.get_col_count(other.data):
            raise ValueError("Матриці повинні мати однакові розміри для віднімання.")

        result = []
        for i in range(self.get_row_count(self.data)):
            row = []
            for j in range(self.get_col_count(self.data)):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __str__(self):
        max_len = 0
        for i in range(self.get_row_count(self.data)):
            for j in range(self.get_col_count(self.data)):
                max_len = max(max_len, len(str(self.data[i][j])))

        result = ""
        for i in range(self.get_row_count(self.data)):
            row = self.data[i]
            for j in range(len(row)):
                result += f"{row[j]:>{max_len}} "  
            result += "\n"
        return result.strip()


matrix_data1 = [
    [-3, -5, -45, -71, -5],
    [0, 1, 3, 2, 7],
    [11, 9, 45, 0, 4],
    [9, 19, 55, 44, 90],
    [-3, -4, -1, -5, 0]
]

matrix_data2 = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1],
    [10, 20, 30, 40, 50],
    [0, 0, 0, 0, 0]
] 

matrix1 = Matrix(matrix_data1)
matrix2 = Matrix(matrix_data2)

print("Перша матриця:")
print(matrix1)

print("\nДруга матриця:")
print(matrix2)

result_matrix = matrix1 - matrix1

print("\nРезультат віднімання матриць:")
print(result_matrix)