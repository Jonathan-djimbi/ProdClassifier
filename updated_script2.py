
import pandas as pd
import zipfile

# Fonction pour catégoriser les produits en fonction des mots-clés et déterminer leur statut
def categorize_product_with_uncertainty(row, keywords_mapping, original_category_column):
    # Parcourt tous les mots-clés pour vérifier leur présence dans les attributs du produit
    for keyword, new_category in keywords_mapping.items():
        if (keyword in str(row['post_title']).lower() or
            keyword in str(row['post_content']).lower() or
            keyword in str(row['post_name']).lower()):
            return new_category, 'Successfully Categorized'
    # Si aucun mot-clé n'est trouvé, retourne la catégorie originale avec statut incertain
    return row[original_category_column], 'Needs Review'
