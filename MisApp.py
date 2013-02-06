# Using matrix notation for the board, forget the chess notation

from termcolor import colored

class MisApp:
    def __init__(self, gui):
        self.walls = {}  # Walls will be a dictionary of walls
        self.players = [Player((1,1)), Player((8,8))]  # 2 players
        self.gui = gui  # omg gui
        self.turn = 0  # Whose turn?
        
    def run(self):
        self.gui.update(self)
        while not self.game_over():
            self.play_move()
        self.gui.close()
    
    def game_over(self): 
        if self.players[0].get_position() == (8,8) \
                or self.players[0].get_position() == (1,1):
            return 1
        else: return 0
          
    def play_move(self):

        # Collect and process a legal move
        self.gui.prompt_player(self.turn)
        move = self.gui.get_move()
        while not self._is_legal_move(move):
            move = self.gui.get_move()

        # Process and update gui
        self.process_move(move)
        self.turn = (self.turn + 1) % 2         
        self.gui.update(self)


    def process_move(self,move):  # Update game for a legal move
        
        if len(move) == 2:  # slide
            self.players[self.turn].set_position(move)
            
        elif len(move) == 3 and move in self.walls:  # remove & get wall place
            del self.walls[move]
            self.gui.update(self)
            
            wallmove = self.gui.get_move()
            while self._is_legal_wall(wallmove) != 2: 
                wallmove = self.gui.get_move()
            self.process_move(wallmove) # A little recursion
                
        elif len(move) == 3 and move not in self.walls:  # place wall
            walltype = self.gui.get_walltype()
            while not self._is_legal_walltype(walltype):
                walltype = self.gui.get_walltype()
            self.walls[move] = walltype  # finally add the wall
        else:
            print "OMG Something wrong, should not be here!!"

    def _is_legal_walltype(self,walltype):
        if walltype == 2 and self.players[self.turn].get_walls() > 0:
            return True
        elif walltype == self.turn and \
                self.players[self.turn].get_cwalls() > 0:
            return True
        else: 
            return False

    def _is_legal_move(self,move):
        if len(move) == 2 and move in self._legal_slides():
            return 1
        elif len(move) == 3 and self._is_legal_wall(move):
            return self._is_safe_wall(move)
        else:
            return 0

    def _is_safe_wall(self,move):
        ########################## NEED TO FINISH ###########
        return 1

    def _is_legal_wall(self,move):
        # Test if wall location is empty and if have walls
        if move in self.walls:
            if self.walls[move] == self.turn: # opening door
                return 1
            else:
                return 0

        # Enough walls? (already returned 1 if opening door)
        elif self.players[self.turn].get_total_walls() <= 0:
            return 0
        else:
            return 2


    def _legal_slides(self):

        pos = self.players[self.turn].get_position()
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
        self.textwidth = 50
        self._print_intro()

    def _print_intro(self):
        print "Welcome to Misdirection (text interface)!! "

    def update(self,app):
        # update player info
        self._update_player_info(app.players)
        self._update_board(app.players,app.walls)
        return 1

    def _update_board(self,players,walls):
        p1pos = players[0].get_position()
        p2pos = players[1].get_position()
        
        for row in range(1,18):
            linestr = "|"
            if row == 1 or row == 17: linestr = "-"
            for col in range(1,9):
                linestr += self._get_cellstr(row,col,(p1pos,p2pos),walls)
            print linestr


    def _get_cellstr(self,row,col,pos,walls):

        cellstr = '   '
        end_mark = ' '
        
        # Draw walls
        if (row/2,col,'b') in walls and row%2 == 1:
            tmp = (row/2,col,'b')
            cellstr = colored('===',self._wallcolor(walls[tmp]),attrs=['bold'])
        elif (row/2,col,'r') in walls and row%2 == 0:
            tmp = (row/2,col,'r')            
            end_mark = colored('I', self._wallcolor(walls[tmp]),attrs=['bold'])

        # Draw players
        if row%2 == 0 and (row/2,col) in pos:
            if pos.index((row/2,col)): 
                cellstr = colored(' B ','cyan',attrs=['bold'])
            else: 
                cellstr = colored(' A ','red',attrs=['bold'])

        # Handle top/bottom lines
        if row==1 or row == 17: 
            cellstr = '----'
            return cellstr

        # Boundaries of cells
        if col == 8: cellstr += '|'
        elif row%2 == 0: cellstr += end_mark
        else: cellstr += '-'

        return cellstr

    def _wallcolor(self,wallind):
        if wallind == 0: return 'cyan'
        elif wallind == 1: return 'red'
        elif wallind == 2: return 'grey'
        else: 
            print "OMG wallcolor invalid!!!!!!!!!!!!"
            return None

    def _update_player_info(self,players):
        print "Player 1 (A): %d regular, %d colored walls"\
            %(players[0].get_walls(), players[0].get_cwalls())
        print "Player 2 (B): %d regular, %d colored walls"\
            %(players[1].get_walls(), players[1].get_cwalls())
        print
        
    def close(self):
        print "Game finished, goodbye!!"

    def prompt_player(self,player_number):
        print "Player %d's turn" % (player_number+1)

    def get_move(self):
        move = input("Enter a move with parentheses:  ")
        return move

    def get_walltype(self):
        wall = input("Enter the type of wall to place (0,1,2)  ")
        return wall


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
