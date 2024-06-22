import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        self.container = gui.HBox(width=800, height=480)
        
        self.buttons_container = gui.VBox(width=150, height='100%')
        self.display_container = gui.VBox(width=450, height='100%')
        
        self.label_display = gui.Label('Отображение', width='100%', height=30)
        
        self.button_link = gui.Button('Ссылка', width=100, height=30)
        self.button_emotion = gui.Button('Эмоция', width=100, height=30)
        self.button1 = gui.Button('Кнопка1', width=100, height=30)
        
        self.button_link.onclick.do(self.on_button_link_click)
        self.button_emotion.onclick.do(self.on_button_emotion_click)
        self.button1.onclick.do(self.on_button1_click)
        
        self.buttons_container.append(self.button_link)
        self.buttons_container.append(self.button_emotion)
        self.buttons_container.append(self.button1)
        
        self.display_container.append(self.label_display)
        
        self.container.append(self.buttons_container)
        self.container.append(self.display_container)
        
        return self.container
    
    def on_button_link_click(self, widget):
        self.label_display.set_text('https://example.com')
    
    def on_button_emotion_click(self, widget):
        self.label_display.set_text('😊')
    
    def on_button1_click(self, widget):
        self.buttons_container.empty()
        
        self.button_dog = gui.Button('Собака', width=100, height=30)
        self.button_back = gui.Button('Назад', width=100, height=30)
        
        self.button_dog.onclick.do(self.on_button_dog_click)
        self.button_back.onclick.do(self.on_button_back_click)
        
        self.buttons_container.append(self.button_dog)
        self.buttons_container.append(self.button_back)
    
    def on_button_dog_click(self, widget):
        self.label_display.set_text('🐶')
    
    def on_button_back_click(self, widget):
        self.buttons_container.empty()
        
        self.buttons_container.append(self.button_link)
        self.buttons_container.append(self.button_emotion)
        self.buttons_container.append(self.button1)

if __name__ == "__main__":
    start(MyApp)

