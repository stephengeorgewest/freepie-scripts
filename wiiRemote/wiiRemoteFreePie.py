def map_wiimote_to_key(wiimote_index, wiimote_button, key):
	# Check the global wiimote object's button state and set the global
	# keyboard object's corresponding key.
	if wiimote[wiimote_index].buttons.button_down(wiimote_button):
		keyboard.setKeyDown(key)
	else:
		keyboard.setKeyUp(key)

def map_wiimote_to_vJoy(wiimote_index, wiimote_button, key):
	if wiimote[wiimote_index].buttons.button_down(wiimote_button):
		vJoy[wiimote_index].setButton(key, True);
	else:
		vJoy[wiimote_index].setButton(key, False);

def map_wiimote_to_vJoyHat(wiimote_index):
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadRight):
		vJoy[wiimote_index].setDigitalPov(0, VJoyPov.Up)
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadLeft):
		vJoy[wiimote_index].setDigitalPov(0, VJoyPov.Down)
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadUp):
		vJoy[wiimote_index].setDigitalPov(0, VJoyPov.Left)
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadDown):
		vJoy[wiimote_index].setDigitalPov(0, VJoyPov.Right)
    
	if not wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadDown) and not wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadUp) and not wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadLeft) and not wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadRight):
		vJoy[wiimote_index].setDigitalPov(wiimote_index, VJoyPov.Nil)

def map_wiimote_to_vJoyAHat(wiimote_index):
	x = 0
	y = 0
	rotate = -9000
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadUp):#up
		x = 1
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadDown):#down
		x = -1
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadLeft):#left
		y = -1
	if wiimote[wiimote_index].buttons.button_down(WiimoteButtons.DPadRight):#right
		y = 1
	if x == 0 and y == 0:
		vJoy[wiimote_index].setAnalogPov(wiimote_index, -1)#center
	else:
		degrees = (math.atan2(y,x)/math.pi*18000 + rotate)%36000
		vJoy[wiimote_index].setAnalogPov(wiimote_index, degrees)
		#diagnostics.debug("x:" + repr(x))
		#diagnostics.debug("y:" + repr(y))
		#diagnostics.debug("angle: " + repr(degrees))

def map_wiimote_to_vJoyAxis(wiimote_index):
	diagnostics.debug("x: " + repr(wiimote[wiimote_index].acceleration.x))
	diagnostics.debug("max: " +repr(vJoy[0].axisMax))
	vJoy[wiimote_index].rx = (wiimote[wiimote_index].acceleration.x+vJoy[0].axisMax)*255
	vJoy[wiimote_index].ry = (wiimote[wiimote_index].acceleration.y+vJoy[0].axisMax)*255
	vJoy[wiimote_index].rz = (wiimote[wiimote_index].acceleration.z+vJoy[0].axisMax)*255

def update():
	# Sideways controls (DPad). Map each of our desired keys.
	map_wiimote_to_vJoyAHat(0)
	map_wiimote_to_vJoy(0, WiimoteButtons.One, 0)
	map_wiimote_to_vJoy(0, WiimoteButtons.Two, 1)
	map_wiimote_to_vJoy(0, WiimoteButtons.Plus, 2)
	map_wiimote_to_vJoy(0, WiimoteButtons.Home, 3)
	map_wiimote_to_vJoy(0, WiimoteButtons.Minus, 4)
	map_wiimote_to_vJoy(0, WiimoteButtons.A, 5)
	map_wiimote_to_vJoy(0, WiimoteButtons.B, 6)

# If we're starting up, then hook up our update function.
if starting:
	wiimote[0].buttons.update += update