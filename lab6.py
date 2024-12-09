class MatrixOperations:
    def __init__(self, matrix, enable_sorting=True):
    
        self.matrix = matrix  
        self.enable_sorting = enable_sorting  

    @staticmethod
    def geometric_mean_decorator(func):
        
        def wrapper(numbers):
            product = 1  
            count = 0 
            for num in numbers:
                if num > 0: 
                    product *= num
                    count += 1
            if count == 0:
                return 0  
            geometric_mean = product ** (1 / count)  
            return func(geometric_mean)  
        return wrapper

    def sort_matrix_by_row(self):
        
        for row in self.matrix:  
            for i in range(len(row)):  
                max_idx = i  
                for j in range(i + 1, len(row)):  
                    if row[j] > row[max_idx]:
                        max_idx = j  
                row[i], row[max_idx] = row[max_idx], row[i]  

    def calculate_column_geometric_means(self):
      
        num_rows = len(self.matrix)  
        num_cols = len(self.matrix[0]) 
        column_means = []  
        

        @self.geometric_mean_decorator
        def compute_geometric_mean(geometric_mean):
            return geometric_mean  

        for col in range(num_cols):  
            column = [self.matrix[row][col] for row in range(num_rows)]  
            mean = compute_geometric_mean(column)  
            column_means.append(mean)  

        return column_means  

    def calculate_f_sum(self, column_means):
       
        return sum(column_means)  

    def view_results(self):
       
        if self.enable_sorting:
            print("Відсортована матриця:")  
            self.sort_matrix_by_row()  
        else:
            print("Матриця без сортування:")  

        for row in self.matrix:  
            print(row)

        column_means = self.calculate_column_geometric_means()  

        print("\nСередні геометричні значення для кожного стовпця:")
        print([round(mean, 2) for mean in column_means])  

        f_sum = self.calculate_f_sum(column_means)  

        print("\nЗначення функції F(fi(aij)):")
        print(round(f_sum, 2))  

matrix = [
    [-3, -5, -45, -71, -5],  
    [0, 1, 3, 2, 7],         
    [11, 9, 45, 0, 4],       
    [9, 19, 55, 44, 90],     
    [-3, -4, -1, -5, 0]      
]

print("\nМатриця без сортування:")
matrix_operations_no_sort = MatrixOperations(matrix, enable_sorting=False)  
matrix_operations_no_sort.view_results() 
