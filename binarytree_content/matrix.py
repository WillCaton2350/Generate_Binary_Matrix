
class search_sorted_matrix:
    def binary_search(self,matrix:list,target:int):
        N = len(matrix[0])
        M = len(matrix)
        if not matrix:
            return False

        def main(row):
            left: int = 0
            right = N - 1

            while left <= right:
                mid_point = (left + right) // 2
                if matrix[row][mid_point] == target:
                    return True
                elif matrix[row][mid_point] == target:
                    left = mid_point + 1
                else:
                    right = mid_point - 1
            return False

        for i in range(M):
            if main(i):
                return True
        return False

if __name__ == " __main__":
    instance = search_sorted_matrix()
    try:
        matrix = [
            [1, 3, 5, 7],
            [9, 11, 13, 15],
            [17, 19, 21, 23],
            [25, 27, 29, 31],
        ]
        target = 13
        print(instance.binary_search(matrix,target))
    except KeyboardInterrupt:
        exit(0)