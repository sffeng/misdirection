from MisApp import *

def bprint(mytext):
    tw = 78
    print mytext.center(tw,'=')


def main():


    
    P = [Player((1,1)), Player((8,8))]
    walls = {(1,1,'b'):0, (1,1,'r'):1, (4,5,'b'):2}


    bprint("Testing text interface")
    print "walls: ", walls
    bprint('')

    gui = TextInterface()

    
    return 0


    bprint('_update_board()')
    gui._update_board(P,walls)
    del walls[(1,1,'b')]
    gui._update_board(P,walls)
    P[0].set_position((5,5))
    gui._update_board(P,walls)
    P[1].set_position((4,5))
    gui._update_board(P,walls)
    walls[(2,3,'r')] = 0
    walls[(2,3,'b')] = 1
    walls[(2,4,'b')] = 1
    walls[(2,5,'b')] = 2
    walls[(2,6,'b')] = 2
    gui._update_board(P,walls)


    bprint('_wallcolor()')
    print gui._wallcolor(0)
    print gui._wallcolor(1)
    print gui._wallcolor(2)
    print gui._wallcolor(3)
    
    bprint('_update_player_info()')
    gui._update_player_info(P)
    P[0].use_wall()
    P[1].use_cwall()
    gui._update_player_info(P)
    P[1].use_cwall()
    P[1].use_cwall()
    P[1].use_cwall()
    P[1].use_cwall()
    gui._update_player_info(P)    

    bprint("prompt_player() and close()")
    gui.prompt_player(0)
    gui.prompt_player(1)
    gui.close()

    bprint("Testing get_walltype()")
    walltype = gui.get_walltype()
    print walltype

    bprint("Testing get_move()")
    move = gui.get_move()
    print move


    
main()


