class Actions:
    def __init__(self, input):
        self.input = input

    def M(self):
        return f'M Entered'

    def V(self):
        return f'V Entered'

    def E(self):
        return f'E Entered'

    def Q(self):
        return f'Q Entered'

    def __str__(self):
        return f'incorrect input'