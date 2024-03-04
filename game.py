matrix = [
    "XXXXXXXX",
    "XSXXXXXX",
    "X*****XX",
    "XXXXX*XX",
    "XXXXX*XX",
    "XXXXX**X",
    "XXXXXXEX",
    "XXXXXXXX"
   ]


# def print_original_matrix():
#         for row in matrix:
#             print(row)

       
def print_new_matrix(matrix_new, x_player, y_player):
        for row in matrix_new:
            print(row)
                         

def print_matrix_with_player(x_player, y_player):
    for y, row in enumerate(matrix):
        if y == y_player:
            matrix[y] = row[:x_player] + "@" + row[x_player+1:]
    print_new_matrix(matrix, x_player, y_player)
            

def finish_maze(matrix, new_x, new_y):
    if matrix[new_y][new_x] == "E":
        return True
    else:
        return False            

# def matrix_solved(x_player, y_player):
#     if matrix[y_player][x_player] == "E":
#         return True
#     else:
#         return False


def main():
    print("GAME STARTED!")

    x_player, y_player = None, None
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if "S" == cell:
                x_player = x
                y_player = y
                row = row[:x] + "@" + row[x+1:]
                matrix[y] = row
                # print_original_matrix()
                for row in matrix:
                    print(row)
                # break


    while True:
        direction = input("chose direction to walk in").lower()

        if direction == "up":
            new_x, new_y = x_player, y_player-1

        elif direction == "down":
            new_x, new_y = x_player, y_player+1

        elif direction == "left":
            new_x, new_y = x_player-1, y_player

        elif direction == "right":
            new_x, new_y = x_player+1, y_player
        
        else:
            print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
            continue

        #if reaches finish cell#
        if finish_maze(matrix, new_x, new_y):
            print("CONGRATULATIONS!")
            break


        if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix):
            if matrix[new_y][new_x] != "X":
                matrix[y_player] = matrix[y_player][:x_player] + " " + matrix[y_player][x_player+1:]
                matrix[new_y] = matrix[new_y][:x_player] + " " + matrix[new_y][x_player+1:] 

                x_player, y_player = new_x, new_y

                # print_matrix_with_player(x_player, y_player)
                print_matrix_with_player(x_player, y_player)

               
                # if matrix_solved(x_player, y_player):
                #     print("CONGRATS!!!!")
                #     break

            else:
              print("You cant walk into a wall")

        else:
            print("Keep yourself inside the game")




    


if __name__ == "__main__":
    main()
    
