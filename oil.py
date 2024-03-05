import time, pydirectinput, threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

point1 = (265, 875)
point2 = (365, 875)
point3 = (465, 875)
point4 = (565, 875)
exit_key = KeyCode(char='-')
start_stop_key = KeyCode(char='+')

class ClickMouse(threading.Thread):
    def __init__(self, point1, point2, point3, point4):
        super(ClickMouse, self).__init__()
        self.running = False
        self.program_running = True
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        self.join()

    def run(self):
        while self.program_running:
            while self.running:
                time.sleep(3)
                for point in [self.point1, self.point2, self.point3, self.point4]:
                    time.sleep(0.2)
                    pydirectinput.moveTo(*point)
                    pydirectinput.mouseDown(button='left')
                    time.sleep(5)
                    pydirectinput.mouseUp(button='left')
                    time.sleep(0.2)

click_thread = ClickMouse(point1, point2, point3, point4)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()