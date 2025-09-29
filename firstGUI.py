import tkinter as tk
from tkinter import font

class GreetingTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Greeting Translator")
        master.geometry("450x250") # Set an initial size for the window

        # --- Data for Translations ---
        self.translations = {
            "Spanish": {"welcome": "Bienvenido", "hello": "Hola"},
            "French": {"welcome": "Bienvenue", "hello": "Bonjour"},
            "German": {"welcome": "Willkommen", "hello": "Guten Tag"},
            "English": {"welcome": "Welcome", "hello": "Hello"}
        }

        # --- GUI Widgets ---
        self.create_widgets()

    def create_widgets(self):
        # Frame for the buttons to keep them organized
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20) # Add some padding above and below

        # Create a button for each language
        for language in self.translations.keys():
            button = tk.Button(
                button_frame,
                text=language,
                width=10,
                command=lambda lang=language: self.show_translation(lang)
            )
            # The 'lang=language' in the lambda is crucial to capture the correct language for each button
            button.pack(side="left", padx=5)

            # Bind mouse hover events
            button.bind("<Enter>", lambda event, lang=language: self.show_hover_greeting(event, lang))
            button.bind("<Leave>", self.clear_hover_greeting)

        # Label to display the translated "Welcome" greeting
        # Using a larger, bold font to make it stand out
        self.translation_label = tk.Label(
            self.master,
            text="Select a language to see the greeting",
            font=font.Font(family="Helvetica", size=18, weight="bold"),
            pady=20 # Add vertical padding
        )
        self.translation_label.pack()

        # A "status bar" at the bottom to show the "Hello" on hover
        self.hover_label = tk.Label(
            self.master,
            text="",
            bd=1,
            relief="sunken",
            anchor="w" # Anchor text to the west (left)
        )
        self.hover_label.pack(side="bottom", fill="x")

    def show_translation(self, language):
        """Updates the main label with the 'Welcome' translation when a button is clicked."""
        welcome_text = self.translations[language]["welcome"]
        self.translation_label.config(text=welcome_text)

    def show_hover_greeting(self, event, language):
        """Shows 'Hello' in the status bar when hovering over a button."""
        hello_text = self.translations[language]["hello"]
        self.hover_label.config(text=f" In this language, 'hello' is: {hello_text}")

    def clear_hover_greeting(self, event):
        """Clears the status bar when the mouse leaves a button."""
        self.hover_label.config(text="")

# --- Main program execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingTranslatorApp(root)
    root.mainloop()