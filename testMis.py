from MisApp import *

def bprint(mytext):
    tw = 78
    print mytext.center(tw,'=')


def main():
    
    gui = TextInterface()
    app = MisApp(gui)
    print app._legal_slides((1,1))
    
    bprint('Game start')
    app.run()
    


    
main()


