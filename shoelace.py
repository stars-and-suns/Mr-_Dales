def shoelace(coords):
    area = 0
    for i in range(len(coords)-1):
        area += coords[i][0] * coords[i+1][1]
        area -= coords[i][1] * coords[i+1][0]
    return area/2
print(shoelace([(0,0),(5,0),(5,2),(3,5),(0,2)]))