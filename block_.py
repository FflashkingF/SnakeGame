
import global_

class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def is_inside(self) -> bool:
        return 0 <= self.x < global_.WINDOW_SIZE - global_.SIZE and 0 <= self.y < global_.WINDOW_SIZE - global_.SIZE

    def __eq__(self, other) -> bool:
        return isinstance(other, Block) and self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f'Block({self.x}, {self.y})'

    def __repr__(self) -> str:
        return self.__str__()