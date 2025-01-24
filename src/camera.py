class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, viewport_size):
        self.dx = 0
        self.dy = 0
        self._viewport_size = viewport_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self._viewport_size[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self._viewport_size[1] // 2)