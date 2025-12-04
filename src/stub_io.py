class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def lue(self, value):
        if self.inputs:
            return self.inputs.pop(0)
        return ""

    def kirjoita(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)
