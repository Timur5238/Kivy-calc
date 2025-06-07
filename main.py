from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Минимальная рабочая версия калькулятора
class Calculator(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = Label(text='0', font_size=50, halign='right', size_hint=(1, 0.4))
        layout.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for text in row:
                btn = Button(text=text, font_size=30)
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)
            
        return layout
    
    def on_button_press(self, instance):
        current = self.display.text
        text = instance.text
        
        if text == 'C':
            self.display.text = '0'
        elif text == '=':
            try:
                self.display.text = str(eval(current))
            except:
                self.display.text = 'Error'
        else:
            if current == '0' or current == 'Error':
                self.display.text = text
            else:
                self.display.text += text

if __name__ == '__main__':
    Calculator().run()