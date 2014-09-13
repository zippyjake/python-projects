print("Welcome To Battleship")

w = '~'
hit = '*'

grid = [
    [' ',0,1,2,3,4,5,6,7,8,9],
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w],
]

grid[0][0] = hit

for row in grid:
    for col in row:
        print(col,end=' ')
    print(' ')
        
