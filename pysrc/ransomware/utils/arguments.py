from argpi import ArgumentDescription, Arguments as A, FetchType

class Arguments:
    def __init__(self):
        self.arguments = A().__capture__()

        # start
        self.arguments.__add__(
            "--start",
            ArgumentDescription()
                .shorthand("-s")
        )

        # recover
        self.arguments.__add__(
            "--recover",
            ArgumentDescription()
                .shorthand('-r')
        )

        # directories
        self.arguments.__add__(
            "--directories",
            ArgumentDescription()
                .shorthand("-d")
        )

        # types
        self.arguments.__add__(
            "--types",
            ArgumentDescription()
                .shorthand("-t")
        )

        # start-runtime
        self.arguments.__add__(
            "--start-runtime",
            ArgumentDescription()
                .shorthand('-sr')
        )

        # recover
        self.arguments.__add__(
            "--rec",
            ArgumentDescription().shorthand('-rec')
        )
        
        # help
        self.arguments.__add__(
            "--help",
            ArgumentDescription()
                .shorthand('-h')
        )

        self.arguments.__analyse__()
    
    @property
    def get(self) -> A:
        return self.arguments
    
    @property
    def fetchtypes(self):
        return FetchType