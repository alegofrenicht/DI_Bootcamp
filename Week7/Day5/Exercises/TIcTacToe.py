
def play():

    start = input('Wanna play?(y/n)\n')

    while start == 'y':
        star_line = '* * * * * * *'
        counter = 1
        gui_list = []

        # why you define the function as nested
        def display_board():
            decoration_element = [' ', '-']
            print('TIC TAC TOE')
            for num in range(7):
                if num == 0 or num == 6:
                    print(star_line)
                    gui_list.append(star_line)
                else:
                    if num % 2 == 0:
                        decoration_loop(decoration_element[1])
                    else:
                        decoration_loop(decoration_element[0])


        def decoration_loop(element):
            string = []
            count = 0
            another_count = 0
            last_another_count = 0
            for symbol in range(len(star_line)):
                if symbol == 0 or symbol == len(star_line) - 1:
                    string.append('*')
                    print('*', end='')
                    count += 1
                else:
                    if count % 4 == 0:
                        print('|', end='')
                        string.append('|')
                    else:
                        if another_count % 2 != 0:
                            print(element, end='')
                            string.append(element)
                            last_another_count += 1
                        else:
                            print(element, end='')
                            string.append(element)
                    count += 1
                    another_count += 1
            print('', end='\n')
            gui_list.append(string)


        display_board()
        player_one_word = 'X'
        player_two_word = 'O'
        move_count = 0
        win = False
        move = True
        voc_row = {'1': 1, '2': 3, '3': 5}
        voc_col = {'1': 2, '2': 6, '3': 10}
        winner = ''


        def player_input(player_move, player):
            for row in range(len(gui_list)):
                for column in range(len(gui_list[0])):
                    if row % 2 != 0:
                        if voc_row[player_move[0]] == row and voc_col[player_move[1]] == column:
                            print(player, end='')
                            gui_list[row][column] = player
                        else:
                            print(gui_list[row][column], end='')

                    else:
                        print(gui_list[row][column], end='')

                print('', end='\n')

    # split each code into functions, like is_win_by_row, is_win_by_column, etc... 

        def check_win(board, symbol):
            if board[1][2] == symbol and board[1][6] == symbol and board[1][10] == symbol:
                return True
            elif board[3][2] == symbol and board[3][6] == symbol and board[3][10] == symbol:
                return True
            elif board[5][2] == symbol and board[5][6] == symbol and board[5][10] == symbol:
                return True
            elif board[1][10] == symbol and board[3][10] == symbol and board[5][10] == symbol:
                return True
            elif board[1][2] == symbol and board[3][2] == symbol and board[5][2] == symbol:
                return True
            elif board[1][6] == symbol and board[3][6] == symbol and board[5][6] == symbol:
                return True
            elif board[1][2] == symbol and board[3][6] == symbol and board[5][10] == symbol:
                return True
            elif board[5][2] == symbol and board[3][6] == symbol and board[1][10] == symbol:
                return True


        while move_count < 9:
            if move:
                print(f"player1's turn")
                player_one = input('make your turn (write row and column and divide it with comma):\n').split(',')
                if player_one[0] not in voc_row or player_one[1] not in voc_col:
                    print('your choice is out of range, try again')
                    continue
                if gui_list[voc_row[player_one[0]]][voc_col[player_one[1]]] == player_one_word or \
                        gui_list[voc_row[player_one[0]]][voc_col[player_one[1]]] == player_two_word:
                    print('this place is spotted, try again')
                    continue
                player_input(player_one, player_one_word)
                move_count += 1
                player_one.clear()
                if check_win(gui_list, player_one_word):
                    win = True
                    winner = 'Player 1'
                    break
            else:
                print(f"player2's turn")
                player_two = input('make your turn (write row and column and divide it with space):\n').split(',')
                if player_two[0] not in voc_row or player_two[1] not in voc_col:
                    print('your choice is out of range, try again')
                    continue
                if gui_list[voc_row[player_two[0]]][voc_col[player_two[1]]] == player_two_word or \
                        gui_list[voc_row[player_two[0]]][voc_col[player_two[1]]] == player_one_word:
                    print('this place is spotted, try again')
                    continue
                player_input(player_two, player_two_word)
                move_count += 1
                player_two.clear()
                if check_win(gui_list, player_two_word):
                    win = True
                    winner = 'Player 2'
                    break
            if move is True:
                move = False
            else:
                move = True
        if win:
            print(f'{winner}, congratulations!')
        else:
            print(f"It's draw, game is over")

        start = input('One more game?(y/n)\n')

    print('See you next time')


play()
