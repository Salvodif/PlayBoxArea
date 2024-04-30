from libs.game import Game

if __name__ == '__main__':
    game = Game()

    while game.running:
        game.clear_scr()
        game.check_keyboard()
        game.update()

    game.quit()
