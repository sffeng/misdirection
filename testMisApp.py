import MisApp

def main():

    p1 = MisApp.Player((1,1))
    p2 = MisApp.Player((8,8))
    
    print "******************* Testing text interface... **************"
    print

    
    inter = MisApp.TextInterface()
    app = MisApp.MisApp(inter)
    walls = {(1,1,'b'):0, (1,1,'r'):1, (4,5,'b'):2}
    inter.set_board(p1,p2,walls)
    print app._legal_slides((4,5),walls)
    print app._legal_slides((1,1),walls)
    print app._legal_slides((8,8),walls)
    print app._legal_slides((8,3),walls)
    print app._legal_slides((1,8),walls)
    print app._legal_slides((5,5),walls)

    walls[(5,4,'r')]=0
    inter.set_board(p1,p2,walls)    
    print app._legal_slides((5,5),walls)
    
main()
