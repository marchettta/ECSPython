from ..components.entity import Entity_t
from ..components.physicscomponent import PhysicsComponent_t
from ..components.rendercomponent import RenderComponent_t
from ..components.inputcomponent import InputComponent_t

from typing import TypeVar, Generic 

class EntityManager_t:
    def __init__(self):
        self.entities: list[Entity_t] = []
        self.physicscomponents: list[PhysicsComponent_t] = []
        self.rendercomponents: list[RenderComponent_t] = []
        self.inputcomponent: list[InputComponent_t] = []
    
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

    def addEntityInputComponent(self, ent:Entity_t):
        ent_ID = ent.getEntityID()
        inp = InputComponent_t(ent_ID)
        self.inputcomponent.append(inp)
        return inp

    def getRenderComponents(self):
        return self.rendercomponents
    
    def getPhysicsComponents(self):
        return self.physicscomponents
    
    def getInputComponents(self):
        return self.inputcomponent
    
    def getPhysicsComponentFromRenderComponent(self, ren: RenderComponent_t):
        entID = ren.getEntityID()
        for phy in self.physicscomponents:
            if phy.getEntityID() == entID:
                return phy
    
    def getRenderComponentFromPhysicsComponent(self, phy: PhysicsComponent_t):
        entID = phy.getEntityID()
        for ren in self.rendercomponents:
            if ren.getEntityID() == entID:
                return ren
    
    def getPhysicsComponentFromInputComponent(self, inp: InputComponent_t):
        entID = inp.getEntityID()
        for phy in self.physicscomponents:
            if phy.getEntityID() == entID:
                return phy