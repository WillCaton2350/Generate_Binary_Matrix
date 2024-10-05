
class GenerateMatrix:
    global nums, result
    nums = [114,112,109,118]
    result = []

    def binary_division(self):
        for i in nums:
            val = bin(i)[2:-3] 
            # slicing starting from the 0 and 1 index removes the standard 0b that identifes the binary representation of an integer. (eg: 0b1101)
            # the bin() function handles the conversion from int to binary using binary division.
            data = [int(i) for i in val] 
            # The bin() function outputs the binary representation as a string so we need to type cast it using int() 
            result.append(data)
        return result 

if __name__ == "__main__":
    instance = GenerateMatrix()
    instance.binary_division()
