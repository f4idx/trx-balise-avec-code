def on_button_pressed_a():
    global mode
    mode = "TX"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mode
    mode = "RX"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    pass
radio.on_received_value(on_received_value)

signal = 0
mode = ""
radio.set_frequency_band(11)
radio.set_group(1)
radio.set_transmit_power(7)
code = "abcd12345"
codeRX = "nule"
mode = "RX"

def on_forever():
    global signal
    if mode == "RX":
        signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
        if signal < -90:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """)
        elif signal < -80:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . # . . .
                # # . . .
                """)
        elif signal < -70:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . # # . .
                # # # . .
                """)
        elif signal < -60:
            basic.show_leds("""
                . . . . .
                . . . # .
                . . # # .
                . # # # .
                # # # # .
                """)
        elif signal < -50:
            basic.show_leds("""
                . . . . #
                . . . # #
                . . # # #
                . # # # #
                # # # # #
                """)
        elif signal < -40:
            basic.show_leds("""
                . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
                """)
        elif signal >= -40:
            basic.show_string(codeRX)
        else:
            pass
    elif mode == "TX":
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . # . .
            . # . # .
            . . # . .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            # . . . #
            . . . . .
            . # # # .
            . . # . .
            """)
        radio.send_string(code)
    else:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
