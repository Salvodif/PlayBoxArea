
from libs.colors import SDFColors
from libs.base_shape.shape import SDFShape


class SDFCircle(SDFShape):
    def __init__(self, center: tuple[int, int], radius: tuple[int, int], color: SDFColors):
        self.__center = center
        self.__radius = radius
        self.__color = color

