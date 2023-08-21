from microbit import *
import neopixel
import k_Bit

Turn_R = 0
Turn_L = 0

basic.show_leds("""
    . # . # .
    . # . # .
    . # . # .
    # . . . #
    # # # # #
    """)

basic.show_leds("""
    . # . . .
    . # . # #
    . # . . .
    # . . . #
    # # # # #
    """)

basic.show_leds("""
    . # . # .
    . # . # .
    . # . # .
    # . . . #
    # # # # #
    """)

strip = neopixel.NeoPixel(pin5, 24)

while True:
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    k_Bit.LED_brightness(255)
    k_Bit.led(COLOR.GREEN)
    k_Bit.run(DIR.RUN_FORWARD, 20)

    if k_Bit.ultra() <= 12 and k_Bit.obstacle(MotorObs.LEFT_SIDE) <= 6:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            # . . . #
            """)

        while k_Bit.obstacle(MotorObs.LEFT_SIDE) <= 6:
            k_Bit.led(COLOR.RED)
            Turn_L = 0
            Turn_R = 1
            k_Bit.motor(MotorObs.RIGHT_SIDE, MotorDir.BACK, 20)
            k_Bit.motor(MotorObs.LEFT_SIDE, MotorDir.FORWARD, 20)
            basic.pause(500)
            break

    elif k_Bit.ultra() <= 12 and k_Bit.obstacle(MotorObs.RIGHT_SIDE) <= 6:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            # . . . #
            """)

        while k_Bit.obstacle(MotorObs.RIGHT_SIDE) <= 6:
            k_Bit.led(COLOR.RED)
            Turn_L = 1
            Turn_R = 0
            k_Bit.motor(MotorObs.RIGHT_SIDE, MotorDir.FORWARD, 20)
            k_Bit.motor(MotorObs.LEFT_SIDE, MotorDir.BACK, 20)
            basic.pause(500)
            break

    basic.show_leds("""
        . # . # .
        . # . # .
        . # . # .
        # . . . #
        # # # # #
        """)
