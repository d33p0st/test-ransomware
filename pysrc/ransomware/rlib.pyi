class Scanner:
    def __init__(self, directory: str) -> None: ...
    def scan(self) -> None: ...
    def files(self) -> list[str]: ...
    def isolate(self, type: str) -> list[str]: ...