from src import Controller

def main():
    #pygame.init()
    mainWindow = Controller.Controller()
    mainWindow.mainLoop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()