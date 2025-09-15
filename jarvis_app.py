from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser

class JarvisLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Jarvis greeting
        self.label = Label(text="Hello Boss, Jarvis Online.", font_size=20)
        self.add_widget(self.label)

        # Input for commands
        self.command_input = TextInput(hint_text="Type your command...", multiline=False)
        self.add_widget(self.command_input)

        # Button to send command
        self.send_button = Button(text="Send", size_hint=(1, 0.2))
        self.send_button.bind(on_press=self.process_command)
        self.add_widget(self.send_button)

    def process_command(self, instance):
        query = self.command_input.text.lower()

        if "open google" in query:
            webbrowser.open("https://www.google.com")
            self.label.text = "Opening Google..."
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            self.label.text = "Opening YouTube..."
        elif "exit" in query or "stop" in query:
            App.get_running_app().stop()
        else:
            self.label.text = "Sorry Boss, I didn’t understand that."

class JarvisApp(App):
    def build(self):
        return JarvisLayout()

if __name__ == "__main__":
    JarvisApp().run()