
class search_sorted_matrix:
    def binary_search(self,matrix:list,target:int):
        # STATES
        N = len(matrix[0]) # columns
        M = len(matrix) # rows

        # BASE CASE
        if not matrix:
            return False
        
        def main(row):
            # STATES 
            # POINTERS
            left: int = 0 # first index
            right = N - 1 # last index

            while left <= right: # since we have a sorted matrix, we are dealing with acending values in each array of the matrix. 
                # ex:
                # 1 -> 5
                # 7 -> 11
                # 13 -> 17
                mid_point = (left + right) // 2 # this searches each side of the set mid point
                # splits the matrix into two and stores that in the mid point variable
                if matrix[row][mid_point] == target: # checks the mid point and the whole row  for the target number
                    return True
                elif matrix[row][mid_point] < target: # else keep looking for it by adjusting by 1 / checking each index of the martix
                    left = mid_point + 1
                    # this is the incrementor (adjusting)
                else:
                    right = mid_point - 1 
                    # this is the decrementor (adjusting)

            # if you can't find the target variable then return false
            return False
        
        for i in range(M): # this iterates over each index of row{s} in the matrix
            if main(i): # 
                return True
        return False

if __name__ == "__main__":
    instance = search_sorted_matrix()
    try:
        matrix = [
            [1, 3, 5, 7], 
            [7, 9, 11, 13], 
            [15, 17, 19, 21],
            [23, 25, 27, 29],
        ]
        target = 5
        print(instance.binary_search(matrix, target))
    except KeyboardInterrupt:
        print(' gracefully exiting...')
        exit(0)
        

# first find the mid point 
# we find te mid point to split each row in the matrix in half
# then we search the left side for the target variable
# if it is not found then we got to the right side (which is recognized as a new array / row)
# since it is recognized as a new array we need to set another mid point and search the left side of said array 
# then with the remaining indecies in the array we search for the target variable if the target variable was not found in the other indecies. 