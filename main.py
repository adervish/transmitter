def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Command = ""
Pin4 = 0
Pin3 = 0
Pin0 = 0
radio.set_group(1)

def on_forever():
    global Pin0, Pin3, Pin4, Command
    while True:
        Pin0 = pins.analog_read_pin(AnalogPin.P0)
        Pin3 = pins.analog_read_pin(AnalogPin.P3)
        Pin4 = pins.analog_read_pin(AnalogPin.P4)
        Command = "" + convert_to_text(Pin0) + "" + convert_to_text(Pin3) + "" + convert_to_text(Pin4)
        radio.send_string(Command)
        led.plot(Pin3 / 250, Pin4 / 250)
basic.forever(on_forever)
