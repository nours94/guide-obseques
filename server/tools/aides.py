"""
Outil : calculer_aides
Base de connaissance sur les aides financières disponibles après un décès.
"""

AIDES = {
    "capital_deces_cpam": {
        "nom": "Capital décès — Sécurité Sociale (CPAM)",
        "montant": "3 703 € (montant 2024)",
        "conditions": [
            "Le défunt était salarié, chômeur indemnisé, ou bénéficiaire de certaines allocations au moment du décès.",
            "La demande doit être faite dans les 2 ans suivant le décès.",
        ],
        "beneficiaires": [
            "En priorité : les personnes à charge du défunt (conjoint, enfants, ascendants).",
            "À défaut : les autres ayants droit dans l'ordre légal.",
        ],
        "comment_faire": [
            "Télécharger le formulaire Cerfa n°10431 sur ameli.fr.",
            "L'envoyer avec l'acte de décès à la CPAM du défunt.",
            "Délai de traitement : 2 à 4 semaines en moyenne.",
        ],
        "delai_max": "2 ans à compter du décès",
        "profils_eligibles": ["salarié", "chômeur", "retraité ancien salarié", "invalide"],
    },
    "aide_sociale_mairie": {
        "nom": "Aide sociale aux obsèques — Mairie",
        "montant": "Variable selon les communes (500 à 2 500 € en général)",
        "conditions": [
            "La famille ne dispose pas des ressources suffisantes pour financer les obsèques.",
            "Le défunt n'avait pas de bien permettant de couvrir les frais.",
        ],
        "beneficiaires": [
            "Toute famille dans l'impossibilité financière de payer les obsèques.",
        ],
        "comment_faire": [
            "Contacter le CCAS (Centre Communal d'Action Sociale) de la commune du lieu de décès.",
            "Présenter les justificatifs de ressources de la famille.",
            "La commune organise et finance un enterrement décent si la famille ne peut pas.",
        ],
        "delai_max": "À demander le plus tôt possible",
        "profils_eligibles": ["toutes situations de précarité"],
        "important": "Cette aide n'est pas automatique — elle doit être demandée explicitement.",
    },
    "mutuelle": {
        "nom": "Aide de la mutuelle ou complémentaire santé",
        "montant": "Jusqu'à 2 000 € selon les contrats",
        "conditions": [
            "Le défunt était adhérent à une mutuelle ou complémentaire santé.",
            "Le contrat prévoit une aide obsèques (vérifier les conditions générales).",
        ],
        "beneficiaires": ["Conjoint ou ayants droit du défunt."],
        "comment_faire": [
            "Contacter directement la mutuelle du défunt avec l'acte de décès.",
            "Demander si le contrat prévoit une aide obsèques.",
            "Fournir les factures des obsèques pour remboursement.",
        ],
        "delai_max": "Généralement dans les 6 mois suivant le décès",
        "profils_eligibles": ["tous les adhérents à une mutuelle"],
    },
    "contrat_obseques": {
        "nom": "Contrat obsèques souscrit par le défunt",
        "montant": "Variable — couvre tout ou partie des frais selon le contrat",
        "conditions": [
            "Le défunt avait souscrit un contrat obsèques en prévoyance de son vivant.",
        ],
        "beneficiaires": ["Les héritiers ou les bénéficiaires désignés dans le contrat."],
        "comment_faire": [
            "Vérifier les relevés bancaires du défunt pour repérer des prélèvements réguliers vers une assurance.",
            "Contacter l'AGIRA (agira.asso.fr) pour rechercher les contrats d'assurance vie et obsèques.",
            "L'AGIRA répond dans les 15 jours ouvrés.",
            "Si un contrat est trouvé, contacter directement l'assureur.",
        ],
        "delai_max": "Variable selon le contrat",
        "profils_eligibles": ["tous"],
        "conseil": "Beaucoup de familles ignorent l'existence d'un contrat obsèques souscrit par le défunt. Vérifiez systématiquement.",
    },
    "pension_reversion": {
        "nom": "Pension de réversion",
        "montant": "54% de la pension du défunt (régime général) — sous conditions de ressources",
        "conditions": [
            "Avoir été marié avec le défunt (PACS et concubinage ne donnent pas droit à la réversion).",
            "Avoir au moins 55 ans (régime général).",
            "Respecter un plafond de ressources (variable selon la situation).",
        ],
        "beneficiaires": ["Conjoint survivant marié. Également possible en cas de divorce si non remarié."],
        "comment_faire": [
            "Contacter la caisse de retraite du défunt.",
            "Remplir le formulaire de demande de pension de réversion.",
            "Fournir acte de mariage, acte de décès, et justificatifs de ressources.",
        ],
        "delai_max": "Pas de délai — mais les arrérages ne sont versés qu'à partir de la demande",
        "profils_eligibles": ["conjoint marié survivant"],
    },
    "aide_employeur": {
        "nom": "Aide de l'employeur ou du comité social et économique (CSE)",
        "montant": "Variable selon les entreprises (200 à 2 000 €)",
        "conditions": [
            "Le défunt était salarié, ou le demandeur est salarié d'une entreprise avec CSE.",
            "La convention collective ou l'accord d'entreprise prévoit une aide.",
        ],
        "beneficiaires": ["Famille proche du défunt ou salarié ayant perdu un proche."],
        "comment_faire": [
            "Contacter le service RH de l'entreprise du défunt.",
            "Contacter le CSE (Comité Social et Économique) de l'entreprise.",
            "Vérifier la convention collective applicable.",
        ],
        "delai_max": "Dans les semaines suivant le décès",
        "profils_eligibles": ["salariés"],
    },
}


def calculer_aides_disponibles(situation_famille: str) -> dict:
    """
    Retourne les aides financières disponibles selon la situation de la famille.
    """
    situation_n = situation_famille.strip().lower()

    aides_recommandees = []
    aides_possibles = []

    # Capital décès CPAM — très largement applicable
    if any(mot in situation_n for mot in ["salarié", "travail", "employé", "chômeur", "retraité", "invalide", "malade"]):
        aides_recommandees.append(AIDES["capital_deces_cpam"])
    else:
        aides_possibles.append(AIDES["capital_deces_cpam"])

    # Aide sociale mairie — si difficultés financières
    if any(mot in situation_n for mot in ["difficultés", "argent", "pauvre", "faibles revenus", "aide", "pas de moyens", "saturé", "canicule"]):
        aides_recommandees.append(AIDES["aide_sociale_mairie"])
    else:
        aides_possibles.append(AIDES["aide_sociale_mairie"])

    # Mutuelle — toujours à vérifier
    aides_possibles.append(AIDES["mutuelle"])

    # Contrat obsèques — toujours à vérifier
    aides_possibles.append(AIDES["contrat_obseques"])

    # Pension de réversion — si conjoint survivant
    if any(mot in situation_n for mot in ["conjoint", "époux", "épouse", "femme", "mari", "veuf", "veuve", "marié"]):
        aides_recommandees.append(AIDES["pension_reversion"])

    # Aide employeur — si salarié
    if any(mot in situation_n for mot in ["salarié", "travail", "employé", "entreprise", "cse", "comité"]):
        aides_recommandees.append(AIDES["aide_employeur"])

    # Si aucune aide spécifique identifiée, proposer toutes les aides
    if not aides_recommandees:
        aides_recommandees = list(AIDES.values())
        aides_possibles = []

    return {
        "situation": situation_famille,
        "aides_recommandees": aides_recommandees,
        "aides_a_verifier": aides_possibles,
        "conseil_urgent": (
            "Commencez par demander le capital décès CPAM si le défunt était salarié ou chômeur — "
            "c'est l'aide la plus importante et la plus méconnue (3 703 € en 2024)."
        ),
        "demarche_simplifiee": (
            "Vous pouvez prévenir plusieurs organismes en une seule démarche via "
            "mon.service-public.fr → 'Signaler un décès'."
        ),
        "note": "Les montants sont donnés à titre indicatif. Vérifiez les montants actualisés auprès des organismes concernés.",
    }
