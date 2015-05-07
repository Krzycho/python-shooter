import cocos

class Sprite(object):
    @staticmethod
    def window_size():
        return cocos.director.director.get_window_size()

    def __init__(self, image_path, position=(0, 0), rotation=0, bound_to_window=False):
        self.sprite = cocos.sprite.Sprite(image_path)
        self.sprite.position = position
        self.sprite.rotation = rotation
        self.sprite.anchor = (0, 0)
        self.bound_to_window = bound_to_window
        self._window_size = Sprite.window_size()

    def width(self):
        return self.sprite.width

    def height(self):
        return self.sprite.height

    def set_position(self, x_pos, y_pos):
        if self.bound_to_window:
            x_pos = max(x_pos, self.sprite.width / 2)
            x_pos = min(x_pos, self._window_size[0] - self.sprite.width / 2)

            y_pos = max(y_pos, self.sprite.height / 2)
            y_pos = min(y_pos, self._window_size[1] - self.sprite.height / 2)

        self.sprite.position = x_pos, y_pos

    def set_x(self, x_pos):
        _, y_pos = self.position()
        self.set_position(x_pos, y_pos)

    def set_y(self, y_pos):
        x_pos, _ = self.position()
        self.set_position(x_pos, y_pos)

    def position(self):
        return self.sprite.position

    def x(self):
        return self.sprite.position[0]

    def y(self):
        return self.sprite.position[1]