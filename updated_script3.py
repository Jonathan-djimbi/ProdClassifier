
import pandas as pd
from collections import Counter
import re

# Fonction de nettoyage et de division du texte
def clean_and_split(text):
    # Supprime les caractères non alphanumériques et convertit le texte en minuscules
    text = re.sub(r'\W+', ' ', text.lower())
    return text.split()

# Fonction pour assigner une catégorie à un produit en fonction des mots-clés
def assign_category(text, categorie_mots_cles):
    cleaned_text = clean_and_split(text)
    category_matches = {category: 0 for category in categorie_mots_cles.keys()}
    for word in cleaned_text:
        for category, keywords in categorie_mots_cles.items():
            if word in keywords:
                category_matches[category] += 1
    best_category, max_matches = max(category_matches.items(), key=lambda pair: pair[1])
    if max_matches == 0:
        return 'Non classé'
    return best_category
