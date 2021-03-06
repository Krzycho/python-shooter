import random

from src.core.modules.resource_manager import ResourceManager
from src.core.modules.shooting_sprite import ShootingSprite
from src.core.modules.plasma_ball import PlasmaBall

class Enemy(ShootingSprite):
    """
        Base class for enemies.
    """

    def __init__(self, image=None):
        if image is None:
            image = ResourceManager.get_enemy_image()

        ShootingSprite.__init__(self, image, rotation=-90)

        self.hit_damage = 100
        self.missle_direction = -1
        self.movement_speed = 3.0
        self.bonus_classes = []
        self.detonate = True

    def update(self, _delta_time=1.0):
        """
            Here all the intelligence hides.
        """

        if not self.is_alive():
            self.die()
            return

        self.move()

    def move(self, delta_time=1.0):
        """
            This method simply moves enemy along the level,
            towards player.
        """

        delta = self.movement_speed * 0.3 * int(delta_time)

        self.set_x(self.get_x() - delta)

    def on_hit_entity(self, other):
        """
            Default collision handler: take damage, die if needed.
        """

        if isinstance(self, type(other)):
            return

        if isinstance(other, PlasmaBall) and isinstance(self, type(other.owner)):
            return

        self.take_damage(other.hit_damage)

        if not self.is_alive():
            self.die()

    def drop_bonuses(self):
        """
            Returns all the bonuses it has.
        """

        if self.was_destroyed:
            return

        for bonus_class in self.bonus_classes:
            start_x, start_y = self.get_position()
            rand_x, rand_y = random.randrange(10, 50), random.randrange(10, 50)
            position = (start_x + rand_x, start_y + rand_y)
            bonus = bonus_class(position=position)
            layer = self.sprite.parent
            layer.register_bonus(bonus)

    def die(self):
        """
            Override `die` method to throw out all the bonuses!
        """

        self.drop_bonuses()

        ShootingSprite.die(self)
