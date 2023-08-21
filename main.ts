let Turn_R = 0
let Turn_L = 0
basic.showLeds(`
    . # . # .
    . # . # .
    . # . # .
    # . . . #
    # # # # #
    `)
basic.showLeds(`
    . # . . .
    . # . # #
    . # . . .
    # . . . #
    # # # # #
    `)
basic.showLeds(`
    . # . # .
    . # . # .
    . # . # .
    # . . . #
    # # # # #
    `)
let strip = neopixel.create(DigitalPin.P5, 24, NeoPixelMode.RGB)
while (true) {
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
    k_Bit.LED_brightness(255)
    k_Bit.Led(COLOR.green)
    k_Bit.run(DIR.RunForward, 20)
    if (k_Bit.ultra() <= 12 && k_Bit.obstacle(MotorObs.LeftSide) <= 6) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            # . . . #
            `)
        while (k_Bit.obstacle(MotorObs.LeftSide) <= 6) {
            k_Bit.Led(COLOR.red)
            Turn_L = 0
            Turn_R = 1
            k_Bit.Motor(MotorObs.RightSide, MotorDir.Back, 20)
            k_Bit.Motor(MotorObs.LeftSide, MotorDir.Forward, 20)
            basic.pause(500)
            break
        }
    } else if (k_Bit.ultra() <= 12 && k_Bit.obstacle(MotorObs.RightSide) <= 6) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            # . . . #
            `)
        while (k_Bit.obstacle(MotorObs.RightSide) <= 6) {
            k_Bit.Led(COLOR.red)
            Turn_L = 1
            Turn_R = 0
            k_Bit.Motor(MotorObs.RightSide, MotorDir.Forward, 20)
            k_Bit.Motor(MotorObs.LeftSide, MotorDir.Back, 20)
            basic.pause(500)
            break
        }
    }
    
    basic.showLeds(`
        . # . # .
        . # . # .
        . # . # .
        # . . . #
        # # # # #
        `)
}
