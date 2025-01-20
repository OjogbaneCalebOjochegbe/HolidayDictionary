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