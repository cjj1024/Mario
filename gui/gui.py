import pygame
import sys


class GUI():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.button_group = pygame.sprite.Group()
        self.menubar_group = pygame.sprite.Group()
        self.inputbox_group = pygame.sprite.Group()
        self.widget_group = pygame.sprite.Group()
        self.label_group = pygame.sprite.Group()
        self.slider_group = pygame.sprite.Group()


    def add_button(self, button, pos=(0, 0)):
        button.adjust_pos(self.rect.x, self.rect.y)
        button.adjust_pos(pos[0], pos[1])
        self.button_group.add(button)


    def add_menubar(self, menubar, pos=(0, 0)):
        menubar.adjust_pos(self.rect.x, self.rect.y)
        menubar.adjust_pos(pos[0], pos[1])
        self.menubar_group.add(menubar)


    def add_inputbox(self, inputbox, pos=(0, 0)):
        inputbox.adjust_pos(self.rect.x, self.rect.y)
        inputbox.adjust_pos(pos[0], pos[1])
        self.inputbox_group.add(inputbox)


    def add_widget(self, widget, pos=(0, 0)):
        widget.adjust_pos(self.rect.x, self.rect.y)
        widget.adjust_pos(pos[0], pos[1])
        self.widget_group.add(widget)


    def add_label(self, label, pos=(0, 0)):
        label.adjust_pos(self.rect.x, self.rect.y)
        label.adjust_pos(pos[0], pos[1])
        self.label_group.add(label)


    def add_slider(self, slider, pos=(0, 0)):
        slider.adjust_pos(self.rect.x, self.rect.y)
        slider.adjust_pos(pos[0], pos[1])
        self.slider_group.add(slider)


    def update(self, screen):
        self.button_group.update()
        self.button_group.draw(screen)

        self.inputbox_group.update()
        self.inputbox_group.draw(screen)

        self.label_group.update()
        self.label_group.draw(screen)

        self.slider_group.update()
        self.slider_group.draw(screen)

        self.widget_group.update(screen)

        self.menubar_group.update(screen)


    def process_event(self, event):
        for button in self.button_group:
            button.process_event(event)
        for inputbox in self.inputbox_group:
            inputbox.process_event(event)
        for widget in self.widget_group:
            widget.process_event(event)
        for menubar in self.menubar_group:
            menubar.process_event(event)
        for slider in self.slider_group:
            slider.process_event(event)