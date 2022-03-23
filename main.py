#import pygame
#import your controller

#def main():
    #pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
#if __name__ == '__main__':
    #main()

def makeList():
  myList = [0, 0, 0, 0]
  for i in range(4):
    myList[i] = int(input("Enter an integer: "))
    
  return myList

def swapList(myList):
  myList[0], myList[3] = myList[3], myList[0]
  
  return myList

def main():
  list = makeList()
  for i in range(4):
    print(list[i])
    
  myList = swapList(list)
  print(myList)

main()