import MisApp

def main():

    p1 = MisApp.Player((1,1))
    p2 = MisApp.Player((8,8))
    walls = {}
    
    print "******************* Testing text interface... **************"
    inter = MisApp.TextInterface()
    inter.prompt_player(1)
    inter.prompt_player(2)
    inter.set_game(p1,p2)
    inter.set_board(p1,p2,walls)

#    app = MisApp.MisApp()
    


    
main()
