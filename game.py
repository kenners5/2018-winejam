"""Wine Jam 2018 @kenners"""
import cocos
import pyglet
from cocos.actions import Delay, Repeat, Reverse, ScaleBy

class Start(cocos.layer.ColorLayer):

    """Our hero"""
    hero = None

    """Event handler"""
    is_event_handler = True

    def create_label(self, text, xpos, ypos, hero=False):
        """Create a label on this layer."""
        label = cocos.text.Label(
            text,
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = xpos, ypos
        if hero:
            self.hero = label
        self.add(label)

    def create_sprite(self, asset_path, coords, scale=1, z_layer=1):
        """Create a sprite on this layer."""
        sprite = cocos.sprite.Sprite(asset_path)
        sprite.position = coords
        sprite.scale = scale
        self.hero = sprite
        self.add(sprite, z=z_layer)

class Keys(cocos.layer.Layer):

    """Our hero"""
    hero = None

    """Event handler"""
    is_event_handler = True

    """Keys pressed"""
    keys_pressed = set()

    def create_label(self, text, xpos, ypos, hero=False):
        """Create a label on this layer."""
        label = cocos.text.Label(
            text,
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = xpos, ypos
        if hero:
            self.hero = label
        self.add(label)

    def create_sprite(self, asset_path, coords, scale=1, z_layer=1):
        """Create a sprite on this layer."""
        sprite = cocos.sprite.Sprite(asset_path)
        sprite.position = coords
        sprite.scale = scale
        self.hero = sprite
        self.add(sprite, z=z_layer)

    def on_key_press(self, key, _):
        """Event handler"""
        self.keys_pressed.add(key)
        key_names = [pyglet.window.key.symbol_string(k)
                     for k in self.keys_pressed]
        self.hero.element.text = 'Keys: {}'.format(key_names)


def main():
    """Main entry point."""
    # Creates the window
    cocos.director.director.init()

    # Creates the layer with some text on it
    l_start = Start(64, 64, 224, 255) # rgba
    l_start.create_label("I got the strap", 320, 240)
    l_start.create_label("I gotta carry 'em", 320, 200)
    l_start.create_sprite('gambino.jpg', (320, 375), scale=0.75)
    bounce = ScaleBy(2, duration=1)
    l_start.hero.do(Delay(2) + Repeat(bounce + Reverse(bounce)))

    l_keys = Keys()
    l_keys.create_label("Waiting...", 200, 100, hero=True)

    # Creates a scene with the layer on it
    main_scene = cocos.scene.Scene(l_start, l_keys)

    # Renders the scene
    cocos.director.director.run(main_scene)

if __name__ == "__main__":
    main()
