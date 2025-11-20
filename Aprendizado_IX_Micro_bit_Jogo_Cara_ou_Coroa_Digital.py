"""

Jogo Cara ou Coroa Digital

"""
# Quando o botão A for pressionado:

def on_button_pressed_a():
    # Mostra um ícone de diamante grande
    basic.show_icon(IconNames.DIAMOND)
    # Mostra um ícone de diamante pequeno
    basic.show_icon(IconNames.SMALL_DIAMOND)
    # Mostra novamente diamante grande
    basic.show_icon(IconNames.DIAMOND)
    # Mostra novamente diamante pequeno
    basic.show_icon(IconNames.SMALL_DIAMOND)
    # A função Math.randomBoolean() gera aleatoriamente:
    # true  -> 50% de chance
    # false -> 50% de chance
    if Math.random_boolean():
        basic.show_leds("""
            # # # # #
            # # . # #
            . . # . .
            # . . . #
            . # # # .
            """)
        basic.clear_screen()
        basic.show_string("CARA")
        basic.clear_screen()
        basic.pause(100)
    else:
        basic.show_leds("""
            . # . # .
            # . # . #
            . . . . .
            # . . . #
            # # # # #
            """)
        basic.clear_screen()
        basic.show_string("COROA")
        basic.clear_screen()
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # Mostra um ícone de diamante grande
    basic.show_icon(IconNames.DIAMOND)
    # Mostra um ícone de diamante pequeno
    basic.show_icon(IconNames.SMALL_DIAMOND)
    # Mostra novamente diamante grande
    basic.show_icon(IconNames.DIAMOND)
    # Mostra novamente diamante pequeno
    basic.show_icon(IconNames.SMALL_DIAMOND)
    # A função Math.randomBoolean() gera aleatoriamente:
    # true  -> 50% de chance
    # false -> 50% de chance
    if Math.random_boolean():
        basic.show_leds("""
            # # # # #
            # # . # #
            . . # . .
            # . . . #
            . # # # .
            """)
        basic.clear_screen()
        basic.show_string("CARA")
        basic.clear_screen()
        basic.pause(100)
    else:
        basic.show_leds("""
            . # . # .
            # . # . #
            . . . . .
            # . . . #
            # # # # #
            """)
        basic.clear_screen()
        basic.show_string("COROA")
        basic.clear_screen()
        basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)
