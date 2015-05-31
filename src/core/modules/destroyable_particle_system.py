from src.core.modules.destroyable_entity import DestroyableEntity
from src.core.modules.collidable_particle_system import CollidableParticleSystem
from src.core.modules.space_explosion import SpaceExplosion

class DestroyableParticleSystem(CollidableParticleSystem, DestroyableEntity):
    """
        Represents sprite, which may both give and take damage when hit.
        This one may die.
    """

    def __init__(self, radius):
        CollidableParticleSystem.__init__(self, radius)
        DestroyableEntity.__init__(self, self.radius)

    def die(self, detonate=True):
        """
            Extend default `die` method to remove the correct
            entity from a layer and create an awesome explosion FX!
        """

        if detonate:
            layer = self.parent
            explosion = SpaceExplosion()
            explosion.position = self.get_position()
            layer.add(explosion)

        DestroyableEntity.die(self)
        self.kill()