import MisApp

def main():

    p1 = MisApp.Player((4,3))
    p2 = MisApp.Player((8,8))
    walls = {(1,1,'b'):0, (1,1,'r'):1, (4,5,'b'):2}
    
    print "******************* Testing text interface... **************"
    print "walls: ", walls
    print
    print
    inter = MisApp.TextInterface()
    inter.prompt_player(1)
    inter.prompt_player(2)
    inter.set_game(p1,p2)
    inter.set_board(p1,p2,walls)

#    app = MisApp.MisApp()
    


    
main()
