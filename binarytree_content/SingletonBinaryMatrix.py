
class GenerateMatrix:
    __instance = None
    global nums, result
    nums = [114,112,109,118]
    result = []

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(GenerateMatrix,cls).__new__(cls)
            for i in nums:
                val = bin(i)[2:-3] 
                data = [int(i) for i in val]
                result.append(data)
            return result 
        return cls.__instance

if __name__ == "__main__":
    GenerateMatrix()