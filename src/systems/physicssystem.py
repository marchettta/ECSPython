from ..manager.entitymanager import EntityManager_t
from ..components.physicscomponent import  PhysicsComponent_t
from ..systems.rendersystem import RenderSystem_t

class PhysicsSystem_t:
    def __init__(self):
        pass

    def update(self, em: EntityManager_t, renSystem: RenderSystem_t):
        for phy in em.getPhysicsComponents():
            ren = em.getRenderComponentFromPhysicsComponent(phy)
            heigth = ren.height
            width = ren.width
            if phy.x <=0 or phy.x + width >= renSystem.width:
                phy.vx = -phy.vx
            if phy.y <=0 or phy.y + heigth >= renSystem.height:
                phy.vy = -phy.vy
            
            phy.x += phy.vx
            phy.y += phy.vy

