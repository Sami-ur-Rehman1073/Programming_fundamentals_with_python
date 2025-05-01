def image_rotator(matrix): 

    def transposer(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]          
        return matrix
    
    transposed_img = transposer(matrix)
    
    def reflector(transposed_img):
        for i in range(len(transposed_img)):
            for j in range(len(transposed_img)):
                if j == 0:
                    transposed_img[i][j], transposed_img[i][len(transposed_img)-1] = transposed_img[i][len(transposed_img)-1] , transposed_img[i][j]          
        return  transposed_img
    
    reflected_img = reflector(transposed_img)
    return reflected_img


def print_image(matrix):
    for i in range(len(rotated_img)):
        for j in range(len(rotated_img[i])):
            print(rotated_img[i][j], end = " ")
        print()

original_image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotated_img = image_rotator(original_image)
print("The orignal matrix was: ")
print_image(original_image)
print("The matrix after transformation is : ")
print_image(rotated_img)
