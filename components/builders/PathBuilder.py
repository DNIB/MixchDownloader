class PathBuilder:
    def __init__(self, base: str):
        self.__base = base
        self.__components = []

    def append(self, component: str):
        self.__components.append(component)
        return self

    def getTs(self) -> str:
        return self.getRaw() + ".ts"

    def getTxt(self) -> str:
        return self.getRaw() + ".txt"

    def getRaw(self) -> str:
        path = self.__base
        for component in self.__components:
            path += "/" + component
        return path
