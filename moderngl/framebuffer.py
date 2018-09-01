from typing import Tuple


class Framebuffer:
    __slots__ = ['__mglo', '__viewport', 'size', 'extra']

    def __init__(self):
        self.__mglo = None  # type: Any
        self.__viewport = None  # type: Tuple[int, int, int, int]
        self.size = None  # type: Tuple[int, int]
        self.extra = None  # type: Any

    @property
    def viewport(self) -> Tuple[int, int, int, int]:
        return self.__viewport

    @viewport.setter
    def viewport(self, value):
        self.__mglo.viewport = value

    def clear_depth(self, value=1.0):
        self.__mglo.clear(value, -1)

    def clear(self, color, attachment=0):
        self.__mglo.clear(color, attachment)

    def read(self, viewport=None, components=3, attachment=0, alignment=1, dtype='f1', np=False):
        return self.__mglo.read(viewport, components, attachment, alignment, dtype, np)

    def read_into(self, buffer, viewport=None, components=3, attachment=0, alignment=1):
        return self.__mglo.read_into(buffer, viewport, components, attachment, alignment)

    def use(self):
        self.__mglo.use()
