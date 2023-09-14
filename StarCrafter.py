import pyautogui
import time
import pygetwindow as gw
import win32api, win32con
import keyboard


# Quantity slider coords (1593,936)
quantity_slider_end = (1593,938)
mouse_start_position = (770, 900)

def get_x(x):
    return 65535 / 2560 * x

def get_y(y):
    return 65535 / 1440 * y


def set_mouse(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(get_x(x)), int(get_y(y)), 0, 0)

def mouse_move(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)


def wiggle():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,3,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,-3,0)


    

# Click the left mouse button
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) 

# Press the e key on the keyboard
def press_key(x):
    pyautogui.keyDown(x)
    time.sleep(0.1)
    pyautogui.keyUp(x)
    time.sleep(0.1)

def back_to_game():
    win = gw.getWindowsWithTitle('Starfield')[0]
    win.activate()
    time.sleep(0.2)
    press_key('esc')
    time.sleep(0.1)

# check if craft button is yellow
def check_craft():
    # If the pixel at (2200,1200) is 183,183,183
    return pyautogui.pixel(2200,1200) == (226, 150, 32)

def check_scroll():
    return pyautogui.pixel(695,1280) == (19, 51, 66) or pyautogui.pixel(695,1280) == (18, 51, 66)


# craft max amount
def craft_max_amount():
    # Collect mouse position
    mouse_pos = pyautogui.position()
    press_key('e')
    time.sleep(0.3)
    # Move mouse to end of quantity slider
    set_mouse(*quantity_slider_end)
    wiggle()
    time.sleep(0.3)
    click()
    time.sleep(0.3)
    press_key('e')
    # Move mouse back to original position
    time.sleep(0.3)
    set_mouse(*mouse_pos)
    time.sleep(0.3)


# move mouse wheel down 1 click
def scroll_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1, 0)

def scroll_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1, 0)




def the_loop():
    while check_craft() == True:
        craft_max_amount()








def do_stuff():
    # back_to_game()
    # time.sleep(0.3)
    # wiggle()
    while True:
        if keyboard.is_pressed('q'):
            print('Done')
            quit()
        else:
            set_mouse(*mouse_start_position)
            time.sleep(0.5)
            iteration = 19
            for x in range(iteration):
                the_loop()
                time.sleep(0.3)
                scroll_down()
                time.sleep(0.3)
                iteration -= 1
            final_four = 4
            for x in range(final_four):
                mouse_move(0,90)
                time.sleep(0.3)
                the_loop()
                time.sleep(0.3)
                final_four -= 1
            set_mouse(*mouse_start_position)
            time.sleep(0.3)
            wiggle()
            for x in range(19):
                scroll_up()
                time.sleep(0.1)
        

do_stuff()