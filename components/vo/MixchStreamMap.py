class MixchStreamMap:
    def __init__(self, stream_name: str):
        self.__stream_name = stream_name
        self.__stream_fragment_names = []

    def append(self, fragment_name: str):
        self.__stream_fragment_names.append(fragment_name)
        return self

    def last(self) -> str:
        return self.__stream_fragment_names[-1] if self.isNotEmpty() else ""

    def all(self) -> list:
        return self.__stream_fragment_names

    def isNotEmpty(self) -> bool:
        return len(self.__stream_fragment_names) > 0

    def getName(self) -> str:
        return self.__stream_name
