"""Wine Jam 2018 @kenners"""
import cocos
from cocos.actions import Delay, Repeat, Reverse, ScaleBy
import pyglet

def keypress(raw):
    """Translate raw keypress number to a string."""
    return pyglet.window.key.symbol_string(raw).lower()

class Message(cocos.layer.ColorLayer):
    """The word is the message"""

    def create_label(self, text, xpos, ypos):
        """Create a label on this layer."""
        label = cocos.text.Label(
            text,
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = xpos, ypos
        self.add(label)

class Hero(cocos.layer.Layer):
    """Our hero"""
    hero = None

    """Event handler"""
    is_event_handler = True

    def create_sprite(self, asset_path, coords, scale=1, z_layer=1):
        """Create a sprite on this layer."""
        sprite = cocos.sprite.Sprite(asset_path)
        sprite.position = coords
        sprite.scale = scale
        self.hero = sprite
        self.add(sprite, z=z_layer)

    def on_key_press(self, key, _):
        """Move the sprite based on keypress"""
        print "debug: {} / {}".format(key, keypress(key))
        coords = list(self.hero.position)
        if keypress(key) == "left":
            coords[0] -= 5
        elif keypress(key) == "right":
            coords[0] += 5
        elif keypress(key) == "up":
            coords[1] += 5
        elif keypress(key) == "down":
            coords[1] -= 5

        self.hero.position = coords[0], coords[1]

def main():
    """Main entry point."""
    # Creates the window
    cocos.director.director.init()

    # Creates the layer with some text on it
    l_msg = Message(64, 64, 224, 255) # rgba
    l_msg.create_label("I got the strap", 320, 240)
    l_msg.create_label("I gotta carry 'em", 320, 200)

    l_hero = Hero()
    l_hero.create_sprite('gambino.jpg', (320, 375), scale=0.75)
    bounce = ScaleBy(2, duration=1)
    l_hero.hero.do(Delay(2) + Repeat(bounce + Reverse(bounce)))

    # Creates a scene with the layer on it
    main_scene = cocos.scene.Scene(l_msg, l_hero)

    # Renders the scene
    cocos.director.director.run(main_scene)

if __name__ == "__main__":
    main()
