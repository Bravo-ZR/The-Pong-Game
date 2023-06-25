
class SetUP():
    def __init__(self, Screen) -> None:
        self.screen = Screen
        self.screen.bgcolor('black')
        self.screen.setup(width=800,height=600)
        self.screen.title('Pong Game')
        self.screen.tracer(False)
        