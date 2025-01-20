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

