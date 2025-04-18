class TextBox:
    def __init__(self, top_left, bottom_right, text, brain):
        self.tl = top_left
        self.br = bottom_right
        self.text = text
        self.brain = brain

    def __draw_box(self, color):
        self.brain.screen.set_pen_color(color)
        tlx, tly = self.tl
        brx, bry = self.br
        self.brain.draw_rectangle(tlx, tly, tlx - brx, tly - bry)
        self.brain.screen.print_at(self.text, (tlx + brx) / 2, (tly + bry) / 2)

    def set_text(self, text):
        self.__draw_box(Color.BLACK)
        self.text = text
        self.__draw_box(Color.WHITE)

