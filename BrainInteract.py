from TextBox import TextBox
from SelBox import SelBox

class BrainInteract:
    def __init__(self, brain):
        brain.screen.pressed(self.select_update)
        self.brain = brain
        self.selectables = {}
        self.texts = {}

    def select_update(self):
        for selectable in self.selectables:
            selectable.update()

    def make_sel(self, name, top_left, bottom_right, event, text):
        new_sel = SelBox(top_left, bottom_right, event, text, self.brain)
        self.selectables[name] = new_sel

    def make_text(self, name, top_left, bottom_right, text):
        new_text = TextBox(top_left, bottom_right, text, self.brain)
        self.texts[name] = new_text

    def edit_text(self, name, text):
        self.texts[name].set_text(text)

    def append_text(self, name, text):
        text_box = self.texts[name]
        text_box.set_text(text_box.text + text)