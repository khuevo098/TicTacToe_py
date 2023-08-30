import myFunc

print('Welcome to Tic Tac Toe!')
while True:
    # Initiate the board
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    myFunc.display_board(board)
    # Set the game up here
    who_first = myFunc.choose_first()
    player1 = ''
    player2 = ''
    if who_first == 1:
        player1 = myFunc.player_input()
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    else:
        player2 = myFunc.player_input()
        if player2 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'
    marker_No1 = {"1": player1}
    marker_No2 = {"2": player2}
    game_on = True
    if who_first == 1:
        while game_on:
            print('|Player 1''s Turn|')
            game_on = myFunc.player_turn(board, player1, marker_No1)

            if not game_on:
                break

            print('|Player 2''s Turn|')
            game_on = myFunc.player_turn(board, player2, marker_No2)
    else:
        while game_on:
            print('|Player 2''s Turn|')
            game_on = myFunc.player_turn(board, player2, marker_No2)

            if game_on == False:
                break

            print('|Player 1''s Turn|')
            game_on = myFunc.player_turn(board, player1, marker_No1)
    if not myFunc.replay():
        break