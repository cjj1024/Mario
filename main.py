
from scene.scenecontrol import *


def main():
    gamemenu = GameMenu()
    scene_control = SceneControl(gamemenu)
    scene_control.show_scene()


if __name__ == '__main__':
    main()