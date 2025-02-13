from ..components.entity import Entity_t
from ..components.physicscomponent import PhysicsComponent_t
from ..components.rendercomponent import RenderComponent_t

from typing import TypeVar, Generic 

class EntityManager_t:
    def __init__(self):
        self.entities: list[Entity_t] = []
        self.physicscomponents: list[PhysicsComponent_t] = []
        self.rendercomponents: list[RenderComponent_t] = []
    
    def createEntity(self):
        ent = Entity_t()
        self.entities.append(ent)
        return ent
    
    def addEntityPhysicsComponent(self, ent: Entity_t, x, y, vx, vy):
        ent_ID = ent.getEntityID()
        phy = PhysicsComponent_t(ent_ID, x, y, vx, vy)
        self.physicscomponents.append(phy)
        return phy
    
    def addEntityRenderComponent(self,ent: Entity_t, png_image):
        ent_ID = ent.getEntityID()
        ren = RenderComponent_t(ent_ID, png_image)
        self.rendercomponents.append(ren)
        return ren

    def getRenderComponents(self):
        return self.rendercomponents
    
    def getPhysicsComponents(self):
        return self.physicscomponents
    
    def getPhysicsComponentFromRenderComponent(self, ren: RenderComponent_t):
        entID = ren.getEntityID()
        for phy in self.physicscomponents:
            if phy.getEntityID() == entID:
                return phy