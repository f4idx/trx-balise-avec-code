input.onButtonPressed(Button.A, function () {
    mode = "TX"
})
radio.onReceivedString(function (receivedString) {
    codeRX = receivedString
})
input.onButtonPressed(Button.B, function () {
    mode = "RX"
})
let signal = 0
let codeRX = ""
let mode = ""
radio.setFrequencyBand(11)
radio.setGroup(1)
radio.setTransmitPower(7)
let code = "CODE: abcd12345"
mode = "RX"
basic.forever(function () {
    if (mode == "RX") {
        signal = radio.receivedPacket(RadioPacketProperty.SignalStrength)
        if (signal < -90) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                `)
        } else if (signal < -80) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . # . . .
                # # . . .
                `)
        } else if (signal < -70) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . # # . .
                # # # . .
                `)
        } else if (signal < -60) {
            basic.showLeds(`
                . . . . .
                . . . # .
                . . # # .
                . # # # .
                # # # # .
                `)
        } else if (signal < -50) {
            basic.showLeds(`
                . . . . #
                . . . # #
                . . # # #
                . # # # #
                # # # # #
                `)
        } else if (signal < -45) {
            basic.showLeds(`
                . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
                `)
        } else if (signal >= -45) {
            basic.showString(codeRX)
        } else {
        	
        }
    } else if (mode == "TX") {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # . # .
            . . # . .
            . . . . .
            `)
        basic.showLeds(`
            . . # . .
            . . . . .
            # . . . #
            . . . . .
            . . # . .
            `)
        radio.sendString(code)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
