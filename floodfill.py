'''
    This algorithm uses BFS (breadth first search) to fill an image by adjacent pixels of the same color
    It simulates the flood fill tool of image editing software

    Taken by: https://www.youtube.com/watch?v=xlVX7dXLS64    
'''

def floodFill(image, row, col, color):
    start = image[row][col]
    queue = [(row, col)]
    visited = set()
    while len(queue) > 0:
        row, col =  queue.pop(0)
        visited.add((row, col))
        image[row][col] = color
        for row, col in neighbors(image, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return image

def neighbors(image, row, col, start):
    indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in indices if isValid(image, row, col) and image[row][col] == start]

def isValid(image, row, col):
    return 0 <= row < len(image) and 0 <= col < len(image[0])

# An image for testing the algorithm
myImage = [[0, 0, 0, 1, 2, 2, 0],
           [1, 0, 1, 1, 2, 0, 0],
           [1, 0, 0, 1, 2, 2, 2],
           [2, 2, 2, 1, 0, 2, 0],
           [1, 2, 0, 0, 2, 2, 1],
           [0, 0, 2, 1, 1, 0, 0],
           [2, 2, 1, 1, 0, 0, 2]]

# Testing the algorithm
print('Original image:')
for row in myImage:
    print(row)
print()

print('Flood filled image:')
row, col = map(int, input('Enter the row and column of the starting pixel: ').split())
color = int(input('Enter the color to fill: '))
print()

floodFill(myImage, row, col, color)
for row in myImage:
    print(row)

