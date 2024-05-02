from math import trunc
# scaling down
# how much something is compressed from 4 individual units to 1
# not always value based but unit based from 4 units to 1

class generate_matrix:
    # get the binary representation and then read from the last remainder up
    def binary_division(self):
        cell_1 = 14 % 2  # ^
        cell_2 = 7 % 2   # |
        cell_3 = 3.5 % 2 # |
        cell_4 = 1.5 % 2 # |

        cell_5 = 12 % 2
        cell_6 = 6 % 2
        cell_7 = 3 % 2
        cell_8 = 1.5 % 2

        cell_9 = 11 % 2
        cell_10 = 5.5 % 2
        cell_11 = 2.75 % 2
        cell_12 = 1.375 % 2

        cell_13 = 8 % 2 
        cell_14 = 4 % 2
        cell_15 = 2 % 2
        cell_16 = 1 % 2

        # reverse the order of cells so the proper binary number is printed to the terminal
        # This is how its written out when read from bottom up

        matrix = [
            [trunc(cell_4),trunc(cell_3),trunc(cell_2),trunc(cell_1)],
            [trunc(cell_8),trunc(cell_7),trunc(cell_6),trunc(cell_5)],
            [trunc(cell_12),trunc(cell_11),trunc(cell_10),trunc(cell_9)],
            [trunc(cell_16),trunc(cell_15),trunc(cell_14),trunc(cell_13)],
        ]

        print(matrix)
        # perform spiral order traversal on this binary matrix
        # we now have a 16 digit binary number

if __name__ == "__main__":
    instance = generate_matrix()
    instance.binary_division()