def longestCommonSubsequence(text1: str, text2: str) -> int:

    # create a 2D array with text1 in column 0 moving vertically through the rows
    # and text2 in row 1 moving horizontally through the columns

    height = len(text1) + 2
    width = len(text2) + 2

    outer, inner = [], []
    for row in range(height):
        for col in range(width):
            if any([row == 0 and col == 0,
                    row == 1 and col == 0,
                    row == 0 and col == 1]):
                inner.append(" ")
            elif row == 0 and col >= 2:
                inner.append(text2[col - 2])
            elif col == 0 and row >= 2:
                inner.append(text1[row - 2])
            elif any([row == 1 and col >= 1,
                      row >= 1 and col == 1]):
                inner.append("0")
            else:
                if inner[0] == outer[0][col]:
                    inner.append(str(int(outer[-1][col - 1]) + 1))
                else:
                    inner.append(str(max([int(inner[-1]), int(outer[-1][col])])))

        outer.append(inner)
        inner = []

    for i in outer:
        print(i)

    return int(outer[-1][-1])


# longestCommonSubsequence("bsbininm", "jmjkbkjkv")
print(longestCommonSubsequence("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq"))