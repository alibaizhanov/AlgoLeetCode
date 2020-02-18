class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
            if numRows == 0:
                return []
            if numRows == 1:
                return [[1]]

            res = [[1]]

            for x in range(1, numRows): 
                # Build a new row.
                row = []
                row.append(1)
                if x > 1:
                    for y in range(1, x): 
                        row.append(lastRow[y] + lastRow[y - 1])
                row.append(1)

                lastRow = row

                res.append(list(row))

            return res