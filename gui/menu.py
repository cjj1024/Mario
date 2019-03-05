from . menuitem import *


class Menu(Button):
    def __init__(self, size=INIT_MENU_SIZE,text=None, text_size=INIT_MENU_TEXT_SIZE,
                 text_color=INIT_MENU_TEXT_COLOR):
        Button.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color,
                        normal_color=INIT_MENU_COLOR, hover_color=INIT_MENU_HOVER_COLOR,
                        active_color=INIT_MENU_ACTIVE_COLOR)

        self.total_height = self.rect.height

        self.is_expand = False

        self.menuitem_group = pygame.sprite.Group()


    def update(self, screen):
        super().update()
        self.menuitem_group.update()
        if self.is_expand:
            self.menuitem_group.draw(screen)


    def add_menuitem(self, menuitem):
        menuitem.adjust_pos(self.rect.x - menuitem.rect.x, self.rect.y + self.total_height - menuitem.rect.y)
        self.total_height += menuitem.rect.height
        self.menuitem_group.add(menuitem)


    def active(self):
        self.is_expand = not self.is_expand


    # rel为相对位移
    def drag(self, rel):
        self.rect.x += rel[0]
        self.rect.y += rel[1]
        for menuitem in self.menuitem_group:
            menuitem.rect.x += rel[0]
            menuitem.rect.y += rel[1]


    def adjust_pos(self, x, y):
        super().adjust_pos(x, y)

        for menuitem in self.menuitem_group:
            menuitem.adjust_pos(x, y)


    def process_event(self, event):
        super(Menu, self).process_event(event)

        if self.is_expand:
            for menuitem in self.menuitem_group:
                menuitem.process_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_expand = False