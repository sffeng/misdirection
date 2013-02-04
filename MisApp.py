# Using matrix notation for the board, forget the chess notation

class MisApp:
    def __init__(self, interface):
        self.walls = {}  # Walls will be a dictionary of walls
        self.player1 = Player((1,1))
        self.player2 = Player((8,8))
        self.interface = interface
        self.current_player = self.player1  # starts as first player's move
        self.current_player_num = 1  # I need to do this better
        
    def run(self):
        while self.game_over():
            self.play_move()
        self.interface.close()
    
    def play_move(self):

        # Collect and process a legal move
        self.interface.prompt_player(self.current_player_num)
        move = self.interface.get_move()
        while not is_legal_move(move):
            move = self.interface.get_move()
        self.process_move(move)

        self.current_player_num = self.current_player_num % 2 + 1
        
        if self.current_player_num == 1:
            self.current_player = self.player1
        else:
            self.current_player = self.player2


    def process_move(self,move):  # Update game and interface
        
        if move[0] == 0:  # slide piece to move[1]
            self.current_player.set_position(move[1])
            
        elif move[0] == 1:  # place wall at move[1]
            self.walls[move[1]] = 0
            
        elif move[0] == 2:  # place colored wall at move[1]
            self.walls[move[1]] = self.current_player_num
            
        elif move[0] == 3:  # del (colored) wall at move[1], place at move[2]
            del self.walls[move[1]]
            self.walls[move[2]] = 0

        else:
            print "OMG Something wrong, should not be here!!"

        #  update the interface with new board, player status
        self.interface.set_board(self.player1,self.player2,self.walls)
        self.interface.set_game(self.player1,self.player2)


    def game_over(self): 
        return self.player1.get_position == (8,8) or \
            self.player2.get_position == (1,1)
# add stalemate or cannot move loss            
        
    def is_legal_move(self,move):
        return 1  # for now everything is legal
        
    def _legal_slides(self,pos):
        possible_slides = [ (pos[0]-1,pos[1]-1), (pos[0]-1,pos[1]+1), (pos[0]+1,pos[1]-1), (pos[0]+1,pos[1]+1)] 
        return 1
            


class TextInterface:
    def __init__(self):
        self.textwidth = 79
        self._print_intro()
        
    def _print_intro(self):
        print "Welcome to Misdirection (text interface)!! "

    def prompt_player(self,player_number):
        print "Player %d's turn".center(self.textwidth,'=') % (player_number)

    def set_game(self, player1, player2):
        print "Player 1: %d regular, %d colored walls".center(self.textwidth) \
            %(player1.get_walls(), player1.get_cwalls())
        print "Player 2: %d regular, %d colored walls".center(self.textwidth) \
            %(player2.get_walls(), player2.get_cwalls())
        
    def set_board(self,player1,player2,walls):

        for row in range(1,18):

            # Print first character of each line
            if row % 2 == 1: mark = "-"
            else: mark = "|"
            linestr = mark

            for col in range(1,9):
                if row % 2 == 1:
                    
                    
                    
                    cellmark =  "---"


                    
                else: 
                    cellmark = "   "
                    
                linestr += cellmark
                linestr += mark
            print linestr.center(self.textwidth)


        
    def _print_straight_line(self):
        print "-----------------------------"
        print "|   |   |   |   |   |   |   |"
        print "-----------------------------"

    def get_move(self):
        print "get move"

    def close(self):
        print "Game finished, goodbye!!"
        



class Player:
    def __init__(self,initial_position):
        self.position = initial_position
        self.cwalls = 9
        self.walls = 9
        
    def set_position(self,position):
        self.position = position

    def use_wall(self):
        self.walls -= 1

    def use_cwall(self):
        self.cwalls -= 1

    def get_position(self):
        return self.position

    def get_cwalls(self):
        return self.cwalls

    def get_walls(self):
        return self.walls
