from ..components.entity import Entity_t
from ..components.physicscomponent import PhysicsComponent_t
from ..components.rendercomponent import RenderComponent_t

from typing import TypeVar, Generic 

class EntityManager_t:
    def __init__(self):
        self.entities: list[Entity_t] = []
        self.physicscomponent: list[PhysicsComponent_t] = []
        self.rendercomponent: list[RenderComponent_t] = []
    
