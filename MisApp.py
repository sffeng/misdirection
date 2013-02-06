# Using matrix notation for the board, forget the chess notation

from termcolor import colored

class MisApp:
    def __init__(self, gui):
        self.walls = {}  # Walls will be a dictionary of walls
        self.players = [Player((1,1)), Player((8,8))]  # 2 players
        self.gui = gui  # omg gui
        self.turn = 0  # Whose turn?
        
    def run(self):
        while not self.game_over():
            self.play_move()
        self.gui.close()
    
    def play_move(self):

        # Collect and process a legal move
        self.gui.prompt_player(self.turn)
        move = self.gui.get_move()
        while not self.is_legal_move(move):
            move = self.gui.get_move()

        # Process and update gui
        self.process_move(move)
        self.gui.set_board(self.players,self.walls)
        self.turn = (self.turn + 1) % 2 


    def process_move(self,move):  # Update game for a legal move
        
        if length(move) == 2:  # slide
            self.players[self.turn].set_position(move)
            
        elif length(move) == 3:  # wall move
            
            if move in self.walls:  # remove wall, then get another placement
                
                del self.walls[move]
                self.gui.set_board(self.players,self.walls)
                
                wallmove = self.gui.get_move()
                while self._is_legal_wall(wallmove) != 2: 
                    wallmove = self.gui.get_move()
                self.process_move(wallmove) # A little recursion
                
            else:  # straight up wall palcement
                
                walltype = self.gui.get_walltype()
                while not self._is_legal_walltype(walltype):
                    walltype = self.gui.get_walltype()
                
                self.walls[move] = walltype  # finally add the wall
        else:
            print "OMG Something wrong, should not be here!!"


    def _is_legal_walltype(self,walltype):


    def game_over(self): 
        return self.player1.get_position == (8,8) or \
            self.player2.get_position == (1,1)
    # add stalemate or cannot move loss            
        
    def is_legal_move(self,move):

        if length(move) == 2 and move in self._legal_slides():
            print "Moving to the space", move
            return 1
        elif length(move) == 3:
            return self._is_legal_wall(move)
        else:
            print "Error: Didn't input correct type of move, try again!"
            return 0
            
    def _is_legal_wall(self,move):

        # Test if wall location is empty and if have walls
        if move in self.walls:
            if self.walls[move] == self.current_player_num:
                print "Move OK: you are opening a wall (or door)"
                return 1
            elif self.walls[move] == 0:
                print "Error: You cannot move neutral walls!"
                return 0
            else:
                print "Error: wall at location"
                return 0

        # Test if player has enough walls (already considered 0 walls and 
        # moving a door
        elif self.current_player.get_total_walls() <= 0:
            print "You have no more walls to place!"
            return 0
        
        # Everything passed, it is an ok move
        print "Move OK: Placing a wall at", move
        return 2
            
        
    def _legal_slides(self):

        pos = self.current_player.get_position()
        
        possible_slides = [ (pos[0]-1,pos[1]), (pos[0]+1,pos[1]), \
                                (pos[0],pos[1]-1), (pos[0],pos[1]+1)]
        wall_blocks = []
        # consider walls
        for (x,y,c) in self.walls:
            if (x,y) == pos and c == 'r':
                wall_blocks.append( (x,y+1) )
            elif (x,y) == pos and c == 'b':
                wall_blocks.append( (x+1,y) )
            elif (x,y+1) == pos and c == 'r':
                wall_blocks.append( (x,y) )
            elif (x+1,y) == pos and c == 'b':
                wall_blocks.append( (x,y) )
        possible_slides = [p for p in possible_slides if not p in wall_blocks]
                
        # consider boundary
        possible_slides = [p for p in possible_slides \
                               if  ( (1 <= p[0] <= 8) and (1 <= p[1] <= 8) )]
        return possible_slides
            


class TextInterface:
    def __init__(self):
        self.textwidth = 79
        self._print_intro()
        
    def _print_intro(self):
        print "Welcome to Misdirection (text interface)!! "

    def prompt_player(self,player_number):
        print "Player %d's turn".center(self.textwidth,'=') % (player_number)

    def set_game(self, player1, player2):
        print "Player 1 (A): %d regular, %d colored walls".center(self.textwidth) \
            %(player1.get_walls(), player1.get_cwalls())
        print "Player 2 (B): %d regular, %d colored walls".center(self.textwidth) \
            %(player2.get_walls(), player2.get_cwalls())
        
    def set_board(self,players,walls):
        p1pos = player1.get_position()
        p2pos = player2.get_position()
        
        for row in range(1,18):
            linestr = "|"
            if row == 1 or row == 17: linestr = "-"
            for col in range(1,9):
                linestr += self._get_cellstr(row,col,(p1pos,p2pos),walls)
            print linestr#.center(self.textwidth)

    def _get_cellstr(self,row,col,pos,walls):

        cellstr = '   '
        cell_end_mark = ' '
        
        # Draw walls
        if (row/2,col,'b') in walls and row%2 == 1:
            tmp = (row/2,col,'b')
            cellstr = colored('===',self._get_wallcolor(walls[tmp]),attrs=['bold'])
        elif (row/2,col,'r') in walls and row%2 == 0:
            tmp = (row/2,col,'r')            
            cell_end_mark = colored('I', self._get_wallcolor(walls[tmp]),attrs=['bold'])

        # Draw players
        if row%2 == 0 and (row/2,col) in pos:
            if pos.index((row/2,col)): cellstr = colored(' B ','cyan',attrs=['bold'])
            else: cellstr = colored(' A ','red',attrs=['bold'])

        # Handle top/bottom lines
        if row==1 or row == 17: 
            cellstr = '----'
            return cellstr

        # Boundaries of cells
        if col == 8: cellstr += '|'
        elif row%2 == 0: cellstr += cell_end_mark
        else: cellstr += '-'

        return cellstr


    def _get_wallcolor(self,wallind):
        if wallind == 0: return 'grey'
        elif wallind == 1: return 'red'
        elif wallind == 2: return 'cyan'
        else: print "OMG wallcolor invalid!!!!!!!!!!!!"
    
    def get_wallmove(self):
        print "Input new location for wall"
        wallmove = self.interface.get_move()
        while length(wallmove)!=3 and self._is_legal_wall(wallmove)!=2:
            print "Invalid move, try again"
            wallmove = self.interface.get_move()


    def get_move(self):
        print "get move"

    def get_move_wall(self):
        print "get move wall"

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

    def get_total_walls(self):
        return (self.get_cwalls() + self.get_walls())
