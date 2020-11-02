Command = ""
Pin4 = 0
Pin3 = 0
Pin0 = 0
radio.set_group(1)
# basic.clear_screen()
# led.plot(Pin3 / 250, Pin0 / 250)

def on_forever():
    global Pin0, Pin3, Pin4, Command
    while True:
        Pin0 = pins.analog_read_pin(AnalogPin.P0) 
        Pin3 = pins.analog_read_pin(AnalogPin.P3) 
        Pin4 = pins.analog_read_pin(AnalogPin.P4) 
        Command = convert_to_text(Pin0) + "," + convert_to_text(Pin3)
        radio.send_string(Command)
        #basic.show_string(Command)
basic.forever(on_forever)
