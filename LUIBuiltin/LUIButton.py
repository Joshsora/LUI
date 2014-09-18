

from panda3d.lui import *


class LUIButton(LUIObject):

    def __init__(self, text="Button", width=100):
        LUIObject.__init__(self, x=0, y=0, w=width, h=50)

        self.sprite_left  = LUISprite(self, "btn_left", "default")
        self.sprite_mid   = LUISprite(self, "btn_mid", "default")
        self.sprite_right = LUISprite(self, "btn_right", "default")

        self.sprite_mid.width = width - self.sprite_left.width - self.sprite_right.width
        self.sprite_mid.left  = self.sprite_left.width
        self.sprite_right.left = self.sprite_mid.left + self.sprite_mid.width
        self.height = self.sprite_mid.height

        self.text = LUIText(self, text, "default", 16.0)
        self.text.set_centered()
        self.text.z_offset = 10

    def on_click(self, event):
        print "on click!"

    def on_mouseover(self, event):
        for child in [self.sprite_left, self.sprite_mid, self.sprite_right]:
            child.alpha = 0.9

    def on_mouseout(self, event):
        for child in [self.sprite_left, self.sprite_mid, self.sprite_right]:
            child.alpha = 1.0
    
    def on_mousedown(self, event):
        self.sprite_left.texture = ("btn_active_left", "default", False)
        self.sprite_right.texture = ("btn_active_right", "default", False)
        self.sprite_mid.texture = ("btn_active_mid", "default", False)
        self.text.margin_top = 1.0

    def on_mouseup(self, event):
        self.sprite_left.texture = ("btn_left", "default", False)
        self.sprite_right.texture = ("btn_right", "default", False)
        self.sprite_mid.texture = ("btn_mid", "default", False)
        self.text.margin_top = 0.0


if __name__ == "__main__":

    # Test script for LUIButton
    from panda3d.core import *

    load_prc_file_data("", """

        text-minfilter linear
        text-magfilter linear
        notify-level-lui debug

    """)
    import direct.directbase.DirectStart

    LUIAtlasPool.get_global_ptr().load_atlas(
        "default", "../Res/atlas.txt", "../Res/atlas.png")

    base.win.set_clear_color(Vec4(0.5,0.5,0.5,1))

    region = LUIRegion.make("LUI", base.win)
    handler = LUIInputHandler()
    base.mouseWatcher.attach_new_node(handler)
    region.set_input_handler(handler)

    button = LUIButton("Click Me")
    button.set_centered()
    region.root().add_child(button)


    base.accept("f3", region.root().ls)

    run()