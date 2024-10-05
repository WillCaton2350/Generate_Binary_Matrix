
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


if __name__ == "__main__":
    GenerateMatrix()
