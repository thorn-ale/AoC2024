from dataclasses import dataclass


@dataclass
class Vec2i:
    x: int = 0
    y: int = 0

    def __add__(self, other) -> 'Vec2i':
        match other:
            case Vec2i():
                return Vec2i(self.x + other.x, self.y + other.y)
            case _:
                raise TypeError(f'Cannot use operands `+` for Vec2i and {type(other).__name__}')
    
    def __eq__(self, other) -> bool:
        match other:
            case Vec2i():
                return self.x == other.x and self.y == other.y
            case None:
                return False
            case _:
                raise TypeError(f'Cannot use operands `==` for Vec2i and {type(other).__name__}')
    
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

NORTH = Vec2i(-1,  0)
SOUTH = Vec2i( 1,  0)
EAST =  Vec2i( 0,  1)
WEST =  Vec2i( 0, -1)