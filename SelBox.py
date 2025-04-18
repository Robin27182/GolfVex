class SelBox:
    def __init__(self, top_left, bottom_right, event, text, brain):
        self.tl = top_left
        self.br = bottom_right
        self.event = event
        self.text = text
        self.brain = brain
        self.__draw_box()
        
    def __draw_box(self):
        tlx, tly = self.tl
        brx, bry = self.br
        self.brain.draw_rectangle(tlx, tly, tlx - brx, tly - bry)
        self.brain.screen.print_at(self.text, (tlx + brx) / 2, (tly + bry) / 2)

    def is_in_box(self, loc):
        tlx, tly = self.tl
        brx, bry = self.br
        locx, locy = loc
        if brx > locx > tlx and tly > locy > bry:
            return True
        return False

    def update(self):
        if self.is_in_box((self.brain.screen.x_position(), self.brain.screen.y_position())):
            self.event.broadcast()
