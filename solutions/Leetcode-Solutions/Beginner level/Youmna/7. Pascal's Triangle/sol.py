class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        for raw in range(0,numRows): 
            tria=[]
            for col in range(raw+1): 
                if col == 0 or col == raw: 
                    tria.append(1)
                else:
                    res = pascal[-1][col-1] + pascal[-1][col] 
                    tria.append(res)
            pascal.append(tria) 
        return pascal