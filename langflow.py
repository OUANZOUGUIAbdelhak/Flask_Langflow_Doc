from langflow.custom import Component
from langflow.io import Output, MessageTextInput
from langflow.schema import Data
import requests

class EnvoyerDonneesVerreTableComponent(Component):
    display_name = "Envoyer Données Verre à la Table"
    description = "Envoyer la composition détaillée du verre et les informations de référence du document au serveur Flask."
    icon = "table"

    inputs = [
        MessageTextInput(
            name="texte_extrait",
            display_name="Texte Extrait",
            info=(
                "Texte extrait contenant la référence du document et les informations sur la composition du verre."
            ),
            value=(
                "1. Type du document : ARTICLE OPEN\n"
                "2. Titre du document : Can a simple topological-constraints-based model predict the initial dissolution rate of borosilicate and aluminosilicate glasses?\n"
                "3. Référence : npj Materials Degradation (2020) 4:6 ; https://doi.org/10.1038/s41529-020-0111-4\n"
                "4. Premier Auteur : Stéphane Gin\n"
                "5. Nombre de types de verres : 16\n"
                "6. Verre_type1 : NBS14/18\n"
                "7. SiO₂(Verre_type1) : 67.8\n"
                "8. B₂O₃(Verre_type1) : 18.0\n"
                "9. Na₂O(Verre_type1) : 14.2\n"
                "10. Al₂O₃(Verre_type1) : Non disponible\n"
                "11. Fines(Verre_type1) : Non disponible\n"
                "12. Densité(Verre_type1) : 2.451\n"
                "13. Homogénéité(Verre_type1) : Homogène\n"
                "14. % B(IV)(Verre_type1) : 66\n"
                "15. Irradié(Verre_type1) : N\n"
                "16. Caractéristiques si irradié(Verre_type1) : Non applicable\n"
                "17. Température(Verre_type1) : 90\n"
                "18. Statique/dynamique(Verre_type1) : Statique\n"
                "19. Plage granulo si poudre(Verre_type1) : 100-125\n"
                "20. Surface spécifique géométrique si poudre(Verre_type1) : 19.9\n"
                "21. Surface spécifique BET si poudre(Verre_type1) : Non disponible\n"
                "22. Qualité polissage si monolithe(Verre_type1) : Non applicable\n"
                "23. Masse verre(Verre_type1) : 0.095\n"
                "24. S(verre)(Verre_type1) : 19.9\n"
                "25. V(solution)(Verre_type1) : 0.231\n"
                "26. Débit solution(Verre_type1) : Non disponible\n"
                "27. pH initial (T amb)(Verre_type1) : Non disponible\n"
                "28. pH initial (T essai)(Verre_type1) : 9\n"
                "29. Compo solution(Verre_type1) : Eau déionisée + LiOH\n"
                "30. Durée expérience(Verre_type1) : 5.5\n"
                "31. pH final (T amb)(Verre_type1) : Non disponible\n"
                "32. pH final (T essai)(Verre_type1) : 9.0\n"
                "33. Normalisation vitesse (Spm ou SBET)(Verre_type1) : Non disponible\n"
                "34. V₀(Si)(Verre_type1) : 12.0\n"
                "35. r²(Si)(Verre_type1) : 0.999\n"
                "36. Ordonnée origine(Verre_type1) : 0.2\n"
                "37. V₀(B)(Verre_type1) : Non disponible\n"
                "38. Ordonnée origine(Verre_type1) : Non disponible\n"
                "39. V₀(Na)(Verre_type1) : Non disponible\n"
                "40. r²(Na)(Verre_type1) : Non disponible\n"
                "41. Ordonnée origine(Verre_type1) : Non disponible\n"
                "42. V₀(ΔM)(Verre_type1) : Non disponible\n"
                "43. Congruence(Verre_type1) : Congruent\n"
                "44. Verre_type2 : NBSA\n"
                "45. SiO₂(Verre_type2) : 64.9\n"
                "46. B₂O₃(Verre_type2) : 17.3\n"
                "47. Na₂O(Verre_type2) : 13.7\n"
                "48. Al₂O₃(Verre_type2) : 4.1\n"
                "49. Fines(Verre_type2) : Non disponible\n"
                "50. Densité(Verre_type2) : 2.405\n"
                "51. Homogénéité(Verre_type2) : Homogène\n"
                "52. % B(IV)(Verre_type2) : 48\n"
                "53. Irradié(Verre_type2) : N\n"
                "54. Caractéristiques si irradié(Verre_type2) : Non applicable\n"
                "55. Température(Verre_type2) : 90\n"
                "56. Statique/dynamique(Verre_type2) : Statique\n"
                "57. Plage granulo si poudre(Verre_type2) : 100-125\n"
                "58. Surface spécifique géométrique si poudre(Verre_type2) : 41.6\n"
                "59. Surface spécifique BET si poudre(Verre_type2) : Non disponible\n"
                "60. Qualité polissage si monolithe(Verre_type2) : Non applicable\n"
                "61. Masse verre(Verre_type2) : 0.198\n"
                "62. S(verre)(Verre_type2) : 41.6\n"
                "63. V(solution)(Verre_type2) : 0.490\n"
                "64. Débit solution(Verre_type2) : Non disponible\n"
                "65. pH initial (T amb)(Verre_type2) : Non disponible\n"
                "66. pH initial (T essai)(Verre_type2) : 9\n"
                "67. Compo solution(Verre_type2) : Eau déionisée + LiOH\n"
                "68. Durée expérience(Verre_type2) : 10.6\n"
                "69. pH final (T amb)(Verre_type2) : Non disponible\n"
                "70. pH final (T essai)(Verre_type2) : 8.9\n"
                "71. Normalisation vitesse (Spm ou SBET)(Verre_type2) : Non disponible\n"
                "72. V₀(Si)(Verre_type2) : 2.6\n"
                "73. r²(Si)(Verre_type2) : 0.997\n"
                "74. Ordonnée origine(Verre_type2) : -0.02\n"
                "75. V₀(B)(Verre_type2) : Non disponible\n"
                "76. Ordonnée origine(Verre_type2) : Non disponible\n"
                "77. V₀(Na)(Verre_type2) : Non disponible\n"
                "78. r²(Na)(Verre_type2) : Non disponible\n"
                "79. Ordonnée origine(Verre_type2) : Non disponible\n"
                "80. V₀(ΔM)(Verre_type2) : Non disponible\n"
                "81. Congruence(Verre_type2) : Congruent\n"
                "82. Verre_type3 : NBSAC\n"
                "83. SiO₂(Verre_type3) : 61.2\n"
                "84. B₂O₃(Verre_type3) : 16.3\n"
                "85. Na₂O(Verre_type3) : 12.8\n"
                "86. Al₂O₃(Verre_type3) : 3.9\n"
                "87. Fines(Verre_type3) : Non disponible\n"
                "88. Densité(Verre_type3) : 2.471\n"
                "89. Homogénéité(Verre_type3) : Homogène\n"
                "90. % B(IV)(Verre_type3) : 53\n"
                "91. Irradié(Verre_type3) : N\n"
                "92. Caractéristiques si irradié(Verre_type3) : Non applicable\n"
                "93. Température(Verre_type3) : 90\n"
                "94. Statique/dynamique(Verre_type3) : Statique\n"
                "95. Plage granulo si poudre(Verre_type3) : 100-125\n"
                "96. Surface spécifique géométrique si poudre(Verre_type3) : 42.0\n"
                "97. Surface spécifique BET si poudre(Verre_type3) : Non disponible\n"
                "98. Qualité polissage si monolithe(Verre_type3) : Non applicable\n"
                "99. Masse verre(Verre_type3) : 0.200\n"
                "100. S(verre)(Verre_type3) : 42.0\n"
                "101. V(solution)(Verre_type3) : 0.496\n"
                "102. Débit solution(Verre_type3) : Non disponible\n"
                "103. pH initial (T amb)(Verre_type3) : Non disponible\n"
                "104. pH initial (T essai)(Verre_type3) : 9\n"
                "105. Compo solution(Verre_type3) : Eau déionisée + LiOH\n"
                "106. Durée expérience(Verre_type3) : 5.5\n"
                "107. pH final (T amb)(Verre_type3) : Non disponible\n"
                "108. pH final (T essai)(Verre_type3) : 8.9\n"
                "109. Normalisation vitesse (Spm ou SBET)(Verre_type3) : Non disponible\n"
                "110. V₀(Si)(Verre_type3) : 9.9\n"
                "111. r²(Si)(Verre_type3) : 0.986\n"
                "112. Ordonnée origine(Verre_type3) : -0.08\n"
                "113. V₀(B)(Verre_type3) : Non disponible\n"
                "114. Ordonnée origine(Verre_type3) : Non disponible\n"
                "115. V₀(Na)(Verre_type3) : Non disponible\n"
                "116. r²(Na)(Verre_type3) : Non disponible\n"
                "117. Ordonnée origine(Verre_type3) : Non disponible\n"
                "118. V₀(ΔM)(Verre_type3) : Non disponible\n"
                "119. Congruence(Verre_type3) : Congruent\n"
            ),
            tool_mode=True,
        ),
    ]

    outputs = [
        Output(display_name="Réponse", name="sortie", method="construire_sortie"),
    ]

    def construire_sortie(self) -> Data:
        texte_extrait = self.texte_extrait
        print(f"Texte Extrait: {texte_extrait}")

        try:
            # Nettoyer et analyser le texte
            lignes = [ligne.strip() for ligne in texte_extrait.split("\n") if ligne.strip()]

            # Extraction des données
            type_doc = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("1. Type du document :")), None)
            titre = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("2. Titre du document :")), None)
            reference = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("3. Référence :")), None)
            premier_auteur = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("4. Premier Auteur :")), None)
            nombre_types_verres = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith("5. Nombre de types de verres :")), None)

            # Extraction des informations pour chaque type de verre
            verre_data = []
            for i in range(1, 4):  # Pour les trois premiers types de verre
                verre_type = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{6 + (i-1)*43}. Verre_type{i} :")), None)
                sio2 = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{7 + (i-1)*43}. SiO₂(Verre_type{i}) :")), None)
                b2o3 = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{8 + (i-1)*43}. B₂O₃(Verre_type{i}) :")), None)
                na2o = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{9 + (i-1)*43}. Na₂O(Verre_type{i}) :")), None)
                al2o3 = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{10 + (i-1)*43}. Al₂O₃(Verre_type{i}) :")), None)
                fines = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{11 + (i-1)*43}. Fines(Verre_type{i}) :")), None)
                densite = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{12 + (i-1)*43}. Densité(Verre_type{i}) :")), None)
                homogeneite = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{13 + (i-1)*43}. Homogénéité(Verre_type{i}) :")), None)
                pourcentage_b_iv = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{14 + (i-1)*43}. % B(IV)(Verre_type{i}) :")), None)
                irradie = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{15 + (i-1)*43}. Irradié(Verre_type{i}) :")), None)
                caracteristiques_irradie = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{16 + (i-1)*43}. Caractéristiques si irradié(Verre_type{i}) :")), None)
                temperature = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{17 + (i-1)*43}. Température(Verre_type{i}) :")), None)
                statique_dynamique = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{18 + (i-1)*43}. Statique/dynamique(Verre_type{i}) :")), None)
                plage_granulo = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{19 + (i-1)*43}. Plage granulo si poudre(Verre_type{i}) :")), None)
                surface_geometrique = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{20 + (i-1)*43}. Surface spécifique géométrique si poudre(Verre_type{i}) :")), None)
                surface_bet = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{21 + (i-1)*43}. Surface spécifique BET si poudre(Verre_type{i}) :")), None)
                qualite_polissage = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{22 + (i-1)*43}. Qualité polissage si monolithe(Verre_type{i}) :")), None)
                masse_verre = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{23 + (i-1)*43}. Masse verre(Verre_type{i}) :")), None)
                s_verre = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{24 + (i-1)*43}. S(verre)(Verre_type{i}) :")), None)
                v_solution = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{25 + (i-1)*43}. V(solution)(Verre_type{i}) :")), None)
                debit_solution = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{26 + (i-1)*43}. Débit solution(Verre_type{i}) :")), None)
                ph_initial_amb = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{27 + (i-1)*43}. pH initial (T amb)(Verre_type{i}) :")), None)
                ph_initial_essai = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{28 + (i-1)*43}. pH initial (T essai)(Verre_type{i}) :")), None)
                compo_solution = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{29 + (i-1)*43}. Compo solution(Verre_type{i}) :")), None)
                duree_experience = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{30 + (i-1)*43}. Durée expérience(Verre_type{i}) :")), None)
                ph_final_amb = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{31 + (i-1)*43}. pH final (T amb)(Verre_type{i}) :")), None)
                ph_final_essai = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{32 + (i-1)*43}. pH final (T essai)(Verre_type{i}) :")), None)
                normalisation_vitesse = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{33 + (i-1)*43}. Normalisation vitesse (Spm ou SBET)(Verre_type{i}) :")), None)
                v0_si = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{34 + (i-1)*43}. V₀(Si)(Verre_type{i}) :")), None)
                r_carre_si = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{35 + (i-1)*43}. r²(Si)(Verre_type{i}) :")), None)
                ordonnee_origine_si = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{36 + (i-1)*43}. Ordonnée origine(Verre_type{i}) :")), None)
                v0_b = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{37 + (i-1)*43}. V₀(B)(Verre_type{i}) :")), None)
                ordonnee_origine_b = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{38 + (i-1)*43}. Ordonnée origine(Verre_type{i}) :")), None)
                v0_na = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{39 + (i-1)*43}. V₀(Na)(Verre_type{i}) :")), None)
                r_carre_na = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{40 + (i-1)*43}. r²(Na)(Verre_type{i}) :")), None)
                ordonnee_origine_na = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{41 + (i-1)*43}. Ordonnée origine(Verre_type{i}) :")), None)
                v0_dm = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{42 + (i-1)*43}. V₀(ΔM)(Verre_type{i}) :")), None)
                congruence = next((ligne.split(":", 1)[1].strip() for ligne in lignes if ligne.startswith(f"{43 + (i-1)*43}. Congruence(Verre_type{i}) :")), None)

                verre_data.append({
                    "verre_type": verre_type,
                    "sio2": sio2,
                    "b2o3": b2o3,
                    "na2o": na2o,
                    "al2o3": al2o3,
                    "fines": fines,
                    "densite": densite,
                    "homogeneite": homogeneite,
                    "pourcentage_b_iv": pourcentage_b_iv,
                    "irradie": irradie,
                    "caracteristiques_irradie": caracteristiques_irradie,
                    "temperature": temperature,
                    "statique_dynamique": statique_dynamique,
                    "plage_granulo": plage_granulo,
                    "surface_geometrique": surface_geometrique,
                    "surface_bet": surface_bet,
                    "qualite_polissage": qualite_polissage,
                    "masse_verre": masse_verre,
                    "s_verre": s_verre,
                    "v_solution": v_solution,
                    "debit_solution": debit_solution,
                    "ph_initial_amb": ph_initial_amb,
                    "ph_initial_essai": ph_initial_essai,
                    "compo_solution": compo_solution,
                    "duree_experience": duree_experience,
                    "ph_final_amb": ph_final_amb,
                    "ph_final_essai": ph_final_essai,
                    "normalisation_vitesse": normalisation_vitesse,
                    "v0_si": v0_si,
                    "r_carre_si": r_carre_si,
                    "ordonnee_origine_si": ordonnee_origine_si,
                    "v0_b": v0_b,
                    "ordonnee_origine_b": ordonnee_origine_b,
                    "v0_na": v0_na,
                    "r_carre_na": r_carre_na,
                    "ordonnee_origine_na": ordonnee_origine_na,
                    "v0_dm": v0_dm,
                    "congruence": congruence
                })

            # Préparer les données
            url = 'http://127.0.0.1:5001/add_glass_data'
            donnees = {
                "type": type_doc,
                "titre": titre,
                "reference": reference,
                "premier_auteur": premier_auteur,
                "nombre_types_verres": nombre_types_verres,
                "verre_data": verre_data
            }
            print(f"Envoi des données: {donnees}")

            reponse = requests.post(url, json=donnees)

            if reponse.status_code == 200:
                return Data(value="Données du verre ajoutées avec succès!")
            else:
                return Data(value=f"Erreur lors de l'ajout des données du verre. Code d'état: {reponse.status_code} - {reponse.text}")

        except Exception as e:
            return Data(value=f"Exception survenue: {str(e)}")
