from dataclasses import dataclass


@dataclass
class Vec2i:
    x: int = 0
    y: int = 0

    def is_bounded(self, min_bound: 'Vec2i', max_bound: 'Vec2i') -> bool:
        return (
            self.x >= min_bound.x
            and self.y >= min_bound.y
            and self.x < max_bound.x
            and self.y < max_bound.y
        )

    def __add__(self, other: object) -> 'Vec2i':
        match other:
            case Vec2i():
                return Vec2i(self.x + other.x, self.y + other.y)
            case _:
                raise TypeError(
                    f'Cannot use operands `+` for Vec2i and {type(other).__name__}'
                )

    def __sub__(self, other: object) -> 'Vec2i':
        match other:
            case Vec2i():
                return Vec2i(self.x - other.x, self.y - other.y)
            case _:
                raise TypeError(
                    f'Cannot use operands `-` for Vec2i and {type(other).__name__}'
                )

    def __mul__(self, other: object) -> 'Vec2i':
        match other:
            case Vec2i():
                return Vec2i(self.x * other.x, self.y * other.y)
            case int():
                return Vec2i(self.x * other, self.y * other)
            case _:
                raise TypeError(
                    f'Cannot use operands `*` for Vec2i and {type(other).__name__}'
                )

    def __eq__(self, other: object) -> bool:
        match other:
            case Vec2i():
                return self.x == other.x and self.y == other.y
            case None:
                return False
            case _:
                raise TypeError(
                    f'Cannot use operands `==` for Vec2i and {type(other).__name__}'
                )

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: object) -> bool:
        match other:
            case Vec2i():
                if self.x == other.x:
                    return self.y > other.y
                return self.x > other.x
            case _:
                raise TypeError(
                    f'Cannot use operands `>` for Vec2i and {type(other).__name__}'
                )

    def __lt__(self, other: object) -> bool:
        match other:
            case Vec2i():
                if self.x == other.x:
                    return self.y < other.y
                return self.x < other.x
            case _:
                raise TypeError(
                    f'Cannot use operands `<` for Vec2i and {type(other).__name__}'
                )

    def __ge__(self, other: object) -> bool:
        match other:
            case Vec2i():
                return self.__eq__(other) or self.__gt__(other)
            case _:
                raise TypeError(
                    f'Cannot use operands `>=` for Vec2i and {type(other).__name__}'
                )

    def __le__(self, other: object) -> bool:
        match other:
            case Vec2i():
                return self.__eq__(other) or self.__lt__(other)
            case _:
                raise TypeError(
                    f'Cannot use operands `<=` for Vec2i and {type(other).__name__}'
                )

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.x, self.y))


NORTH = Vec2i(-1, 0)
SOUTH = Vec2i(1, 0)
EAST = Vec2i(0, 1)
WEST = Vec2i(0, -1)
NORTH_EAST = NORTH + EAST
NORTH_WEST = NORTH + WEST
SOUTH_EAST = SOUTH + EAST
SOUTH_WEST = SOUTH + WEST
