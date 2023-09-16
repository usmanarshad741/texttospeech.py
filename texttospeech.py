import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from gtts import gTTS
from googletrans import Translator
from playsound import playsound

# List of supported languages and their corresponding language codes
languages = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Italian': 'it',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Chinese': 'zh-cn',
    'Russian': 'ru',
    'Arabic': 'ar',
}


def translate_and_speak():
    text = text_entry.get("1.0", "end-1c")  # Get text from the scrolled text widget
    selected_language = language_var.get()

    if selected_language in languages:
        target_language = languages[selected_language]
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language).text

        tts = gTTS(translated_text, lang=target_language)
        tts.save("output.mp3")
        playsound("output.mp3")
    else:
        output_label.config(text="Selected language is not supported!")


# Create the main window
root = tk.Tk()
root.title("Text to Speech Translator")
root.geometry("400x400")
root.configure(bg="green")

# Label
label = ttk.Label(root, text="Enter text:")
label.pack(pady=10)

# Scrolled Text Entry
text_entry = scrolledtext.ScrolledText(root, width=30, height=10)
text_entry.pack()

# Language Selection
language_var = tk.StringVar()
language_var.set('English')  # Default language
language_label = ttk.Label(root, text="Select Language:")
language_label.pack()
language_menu = ttk.OptionMenu(root, language_var, *languages.keys())
language_menu.pack()

# Translate and Speak Button
convert_button = ttk.Button(root, text="Translate and Speak", command=translate_and_speak)
convert_button.pack(pady=10)

# Output Label
output_label = ttk.Label(root, text="")
output_label.pack()

# Run the GUI main loop
root.mainloop()
