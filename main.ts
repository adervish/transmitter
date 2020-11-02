let Command = ""
let Pin4 = 0
let Pin3 = 0
let Pin0 = 0
radio.setGroup(1)
//  basic.clear_screen()
//  led.plot(Pin3 / 250, Pin0 / 250)
// basic.show_string(Command)
basic.forever(function on_forever() {
    
    while (true) {
        Pin0 = pins.analogReadPin(AnalogPin.P0)
        Pin3 = pins.analogReadPin(AnalogPin.P3)
        Pin4 = pins.analogReadPin(AnalogPin.P4)
        Command = convertToText(Pin0) + "," + convertToText(Pin3)
        radio.sendString(Command)
    }
})
