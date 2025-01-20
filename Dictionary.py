import tkinter as tk
from tkinter import ttk

dictionary = {
    "french": {
        'hello': 'salut',
        'come': 'viens',
        'go': 'aller',
        'stay': 'rester',
        'here': 'ici',
        'near': 'près',
        'far': 'loin',
        'happy': 'heureux',
        'sad': 'triste',
        'filled': 'rempli',
        'hungry': 'affamé',
        'money': 'argent',
        'please': 'sil vous plaît',
        'name': 'nom',
        'food': 'nourriture',
        'sorry': 'désolé',
        'love': 'amour',
        'what': 'que',
        'thank you': 'merci',
        'congratulations': 'félicitations'
    },
    
    "japanese": {
        'hello': 'konnichiwa',
        'come': 'kuru',
        'go': 'iku',
        'stay': 'tomeru',
        'apple': 'ringo',
        'water': 'mizu',
        'milk': 'miruku',
        'happy': 'shiawase',
        'boy': 'otokonoko',
        'girl': 'onnanoko',
        'hungry': 'onaka suita',
        'money': 'okane',
        'please': 'onegai',
        'good night': 'oyasumi',
        'good morning': 'ohayou',
        'sorry': 'gomen',
        'love': 'ai',
        'restaurant': 'resutoran',
        'thank you': 'arigatou',
        'clothes': 'fuku'
    },
    "Yoruba": {
        'hello': 'pele o',
        'come': 'wa',
        'go': 'lo',
        'stay': 'duro',
        'here': 'nibi',
        'near': 'nitosi',
        'far': 'ji na',
        'happy': 'dun',
        'sad': 'ibanuje',
        'filled': 'kun',
        'hungry': 'ebi npa',
        'money': 'owo',
        'please': 'jowo',
        'name': 'oruko',
        'food': 'onje',
        'sorry': 'ma binu',
        'love': 'ife',
        'what': 'kini?',
        'thank you': 'o se',
        'congratulations': 'ku oriire'
    },
    "spanish": {
        'hello': 'hola',
        'come': 'venir',
        'go': 'Ir',
        'stay': 'quedarse',
        'here': 'aqui',
        'near': 'cerca',
        'far': 'lejos',
        'happy': 'feliz',
        'sad': 'triste',
        'filled': 'ileno',
        'hungry': 'habriento',
        'money': 'dinero',
        'please': 'por favor',
        'name': 'nombre',
        'food': 'comida',
        'sorry': 'lo siento',
        'love': 'amor',
        'what': 'que',
        'thank you': 'gracias',
        'congratulations': 'felicidas'
    },
    "hausa": {
        "come": "zo",
        "go": "je",
        "father": "wani",
        "rice": "shinkafa",
        "fool": "wawa",
        "home": "gida",
        "need": "bukata",
        "again": "sake",
        "good morning": "barka da safiya",
        "good afternoon": "barka da yamma",
        "good bye": "lafiya lau",
        "good evening": "barka da yamma",
        "me": "ni",
        "one": "daya",
        "two": "biyu",
        "thank you": "na gode",
        "stop": "daina",
        "water": "ruwa",
        "hello": "sannu",
        "give me": "jaara"
    },




}

def search_word():
    # Searches for the translation of the entered English word and updates the result label.
    word = word_entry.get().lower()
    selected_language = language_var.get()

    if selected_language in dictionary:
        translation = dictionary[selected_language].get(word)
        if translation:
            result_label.config(text=f"{word} in {selected_language}: {translation}")
        else:
            result_label.config(text=f"Word '{word}' not found in {selected_language}.")
    else:
        result_label.config(text="Please select a valid language.")

def show_words():
    # Displays the words available in the selected language.
    words_listbox.delete(0, tk.END)
    selected_language = language_var.get()

    if selected_language in dictionary:
        for word in dictionary[selected_language].keys():
            words_listbox.insert(tk.END, word)
    else:
        words_listbox.insert(tk.END, "Please select a valid language.")

  # App begins
root = tk.Tk()
root.geometry("600x300")
root.title("Multi Language Dictionary")

language_var = tk.StringVar(value='french')
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(dictionary.keys()))
language_dropdown.pack() 
word_entry = tk.Entry(root)
word_entry.pack()

search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()

words_listbox = tk.Listbox(root)
words_listbox.pack()

show_button = tk.Button(root, text="Show the available words", command=show_words)
show_button.pack()

root.mainloop()




