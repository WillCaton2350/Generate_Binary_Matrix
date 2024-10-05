
class GenerateMatrix:
    global nums, result
    nums = [114,112,109,118]
    result = []

    def binary_division(self):
        for i in nums:
            val = bin(i)[2:-3] 
            data = [int(i) for i in val]
            result.append(data)
        return result 

if __name__ == "__main__":
    instance = GenerateMatrix()
    instance.binary_division()
