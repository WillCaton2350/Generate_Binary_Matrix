'''Refactored'''
class GenerateMatrix:
    __instance = None
    nums = [114,112,109,118]
    result = []

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(GenerateMatrix,cls).__new__(cls)
            cls.main()
        return cls.__instance
    
    @classmethod
    def main(cls):
        if not cls.result:
            for i in cls.nums:
                val = bin(i)[2:-3] 
                data = [int(i) for i in val]
                cls.result.append(data)
            return cls.result


# I want this to be dynamic, not static. I need to find a way to make the static nums array dynamic, allowing it to function like mutable parameters.
# As well as the length of each array in the matrix. They should be defined in the parameters. The Indices of each array in the matrix.


if __name__ == "__main__":
    GenerateMatrix()
