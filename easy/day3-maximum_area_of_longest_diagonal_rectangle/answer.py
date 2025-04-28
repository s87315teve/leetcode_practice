class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal=0
        
        for dimension in dimensions:
            temp_diagonal=dimension[0]**2+dimension[1]**2
            if temp_diagonal>max_diagonal:
                max_diagonal=temp_diagonal
                max_area=dimension[0]*dimension[1]
                max_area_list=[]
                max_area_list.append(max_area)
            elif temp_diagonal==max_diagonal:
                max_area=dimension[0]*dimension[1]
                max_area_list.append(max_area)

        return max(max_area_list)