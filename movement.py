class Movement():
    def __init__(self, Turtle) -> None:
        self.turtle = Turtle
    def up(self):
        self.turtle.forward(20)
    def down(self):
        self.turtle.backward(20)