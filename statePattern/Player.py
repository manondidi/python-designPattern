class Player:
    def __init__(self):
        self.state = 'normal'

    def click_button(self):
        if self.state == 'normal':
            self.state = 'playing'
        elif self.state == 'playing':
            self.state = 'pause'
        elif self.state == 'pause':
            self.state = 'playing'
        print(self.state)


# 模拟了播放器的 播放按钮
if __name__ == '__main__':
    player = Player()
    player.click_button()
    player.click_button()
    player.click_button()
    player.click_button()
