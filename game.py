import cocos

class Start(cocos.layer.Layer):
    def __init__(self):
        super(Start, self).__init__()

    def create_label(self, text, xpos, ypos):
        label = cocos.text.Label(
            text,
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = xpos, ypos
        self.add(label)

def main():
    # Creates the window
    cocos.director.director.init()

    # Creates the layer with some text on it
    l_start = Start()
    l_start.create_label("I got the strap", 320, 240)
    l_start.create_label("I gotta carry 'em", 320, 200)

    # Creates a scene with the layer on it
    main_scene = cocos.scene.Scene(l_start)

    # Renders the scene
    cocos.director.director.run(main_scene)

if __name__ == "__main__":
    main()
