/**
 * Jogo Cara ou Coroa Digital
 */
// Quando o botão A for pressionado:
input.onButtonPressed(Button.A, function () {
    // Mostra um ícone de diamante grande
    basic.showIcon(IconNames.Diamond)
    // Mostra um ícone de diamante pequeno
    basic.showIcon(IconNames.SmallDiamond)
    // Mostra novamente diamante grande
    basic.showIcon(IconNames.Diamond)
    // Mostra novamente diamante pequeno
    basic.showIcon(IconNames.SmallDiamond)
    // A função Math.randomBoolean() gera aleatoriamente:
    // true  -> 50% de chance
    // false -> 50% de chance
    if (Math.randomBoolean()) {
        basic.showLeds(`
            # # # # #
            # # . # #
            . . # . .
            # . . . #
            . # # # .
            `)
        basic.clearScreen()
        basic.showString("CARA")
        basic.clearScreen()
        basic.pause(100)
    } else {
        basic.showLeds(`
            . # . # .
            # . # . #
            . . . . .
            # . . . #
            # # # # #
            `)
        basic.clearScreen()
        basic.showString("COROA")
        basic.clearScreen()
        basic.pause(100)
    }
})

input.onButtonPressed(Button.B, function () {
    // Mostra um ícone de diamante grande
    basic.showIcon(IconNames.Diamond)
    // Mostra um ícone de diamante pequeno
    basic.showIcon(IconNames.SmallDiamond)
    // Mostra novamente diamante grande
    basic.showIcon(IconNames.Diamond)
    // Mostra novamente diamante pequeno
    basic.showIcon(IconNames.SmallDiamond)
    // A função Math.randomBoolean() gera aleatoriamente:
    // true  -> 50% de chance
    // false -> 50% de chance
    if (Math.randomBoolean()) {
        basic.showLeds(`
            # # # # #
            # # . # #
            . . # . .
            # . . . #
            . # # # .
            `)
        basic.clearScreen()
        basic.showString("CARA")
        basic.clearScreen()
        basic.pause(100)
    } else {
        basic.showLeds(`
            . # . # .
            # . # . #
            . . . . .
            # . . . #
            # # # # #
            `)
        basic.clearScreen()
        basic.showString("COROA")
        basic.clearScreen()
        basic.pause(100)
    }
})
