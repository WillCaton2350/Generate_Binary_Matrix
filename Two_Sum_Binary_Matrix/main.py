# Generate Binary Matrix w/ Two Sum

class GenerateMatrix:
    def main(self):
        nums = [5,4,3,2,1]
        target = 9
        matrix = []

        seen_pairs = set()

        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] + nums[k] == target \
                    and (i,k) not in seen_pairs:
                    seen_pairs.add((i,k))
                    matrix.append([i,k,i,k])
                    matrix.append([i,k,k,i])

        print(matrix)
        return matrix

if __name__ == "__main__":
    instance = GenerateMatrix()
    instance.main()