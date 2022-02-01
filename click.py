#! python3
import pynput, time
global autoClick
autoClick = False

def on_press(key):
	global autoClick
	if key == pynput.keyboard.KeyCode.from_char('`'):
		autoClick = False
		print("Turning off autoclicker.")
	elif key == pynput.keyboard.Key.cmd_r:
		autoClick = True
		print("Turning on autoclicker.")

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

mouse = pynput.mouse.Controller()

try:
	while True:
		time.sleep(0.1)	
		if autoClick:
			mouse.click(pynput.mouse.Button.left)
except KeyboardInterrupt:
	exit()
