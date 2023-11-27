import touch
import display


value = False

def handleTouch():
    if(value):
        box = display.Rectangle(0, 0, 2, 2, 0xC4B454 )
        display.show(box)
    else:
        display.clear()

def handleValue():
    global value
    if(value == False):
        value = True
    else:
        value = False

   
handleTouch() 
touch.callback(touch.A, handleValue)


 