"""
Outil : expliquer_droits
Base de connaissance sur les droits des familles face aux pompes funèbres.
"""

DROITS = {
    "devis": {
        "titre": "Le devis funéraire",
        "resume": "Toute pompe funèbre est obligée de vous remettre un devis détaillé et gratuit avant tout engagement.",
        "details": [
            "Le devis est GRATUIT et OBLIGATOIRE — aucune entreprise ne peut vous le facturer.",
            "Vous pouvez demander autant de devis que vous souhaitez, auprès d'autant d'entreprises que vous le désirez.",
            "Le devis doit respecter un modèle réglementaire fixé par arrêté ministériel.",
            "Vous n'êtes engagé qu'après avoir signé le bon de commande — pas après avoir reçu le devis.",
            "Le devis est valable au minimum 30 jours.",
            "Depuis 2021, les pompes funèbres ont l'obligation d'afficher leurs tarifs en ligne.",
        ],
        "conseils": [
            "Même en urgence, prenez le temps de demander au moins 2 devis — la différence peut atteindre 30 à 50%.",
            "Comparez les devis ligne par ligne — un prix global peut masquer des différences importantes.",
            "Méfiez-vous des 'packages tout compris' qui incluent des prestations non souhaitées.",
        ]
    },
    "prestations_obligatoires": {
        "titre": "Prestations obligatoires",
        "resume": "Seules quelques prestations sont légalement obligatoires — tout le reste est optionnel.",
        "liste": [
            {"prestation": "Cercueil (modèle de base)", "obligatoire": True, "prix_indicatif": "250 à 800 €"},
            {"prestation": "Transport du corps avant mise en bière", "obligatoire": True, "prix_indicatif": "150 à 400 €"},
            {"prestation": "Mise en bière", "obligatoire": True, "prix_indicatif": "Inclus généralement"},
            {"prestation": "Convoi funèbre", "obligatoire": True, "prix_indicatif": "200 à 600 €"},
            {"prestation": "Fleurs et couronnes", "obligatoire": False, "prix_indicatif": "100 à 500 €"},
            {"prestation": "Faire-part de décès", "obligatoire": False, "prix_indicatif": "100 à 300 €"},
            {"prestation": "Toilette mortuaire", "obligatoire": False, "prix_indicatif": "100 à 250 €"},
            {"prestation": "Soins de conservation (thanatopraxie)", "obligatoire": False, "prix_indicatif": "200 à 400 €"},
            {"prestation": "Chambre funéraire (au-delà de 48h)", "obligatoire": False, "prix_indicatif": "50 à 120 €/jour"},
        ]
    },
    "pratiques_interdites": {
        "titre": "Pratiques interdites",
        "resume": "Ces pratiques sont illégales — vous pouvez les refuser et les signaler.",
        "liste": [
            "Facturer un devis (toujours gratuit par la loi).",
            "Vous imposer un prestataire particulier (marbrier, fleuriste, imprimeur).",
            "Vous présenter uniquement des cercueils haut de gamme sans proposer de modèles accessibles.",
            "Vous contacter directement à l'hôpital ou en EHPAD sans autorisation préalable de l'établissement.",
            "Exercer une pression commerciale sur une famille en état de vulnérabilité.",
            "Ne pas afficher leurs tarifs (obligation légale depuis 2021).",
            "Prétendre que les soins de conservation sont obligatoires (ils ne le sont pas sauf cas particuliers).",
        ],
        "recours": [
            "Direction Départementale de la Protection des Populations (DDPP)",
            "DGCCRF (Direction Générale de la Concurrence, Consommation et Répression des Fraudes)",
            "Mairie du lieu de décès",
        ]
    },
    "thanatopra xie": {
        "titre": "Soins de conservation (thanatopraxie)",
        "resume": "Ces soins sont optionnels dans la grande majorité des cas.",
        "details": [
            "La thanatopraxie (injection de produits conservateurs) est présentée comme obligatoire par certains opérateurs — c'est FAUX dans la plupart des cas.",
            "Elle n'est obligatoire que dans des cas très spécifiques : rapatriement international vers certains pays, présentation du corps après un délai important.",
            "Vous pouvez la refuser sans que cela affecte la dignité du défunt.",
            "Son coût (200 à 400 €) n'est jamais remboursé par la Sécurité Sociale.",
        ]
    },
    "libre_choix": {
        "titre": "Libre choix des prestataires",
        "resume": "Vous êtes totalement libre de choisir chaque prestataire.",
        "details": [
            "Vous pouvez choisir votre pompe funèbre indépendamment de l'hôpital, de la mairie ou de tout autre organisme.",
            "Vous pouvez choisir un marbrier différent de la pompe funèbre pour le monument funéraire.",
            "Vous pouvez commander les fleurs chez un fleuriste de votre choix.",
            "Vous pouvez faire imprimer les faire-part où vous voulez.",
            "Aucun organisme ne peut vous imposer un prestataire particulier.",
        ]
    }
}


def expliquer_droits_question(question: str) -> dict:
    """
    Répond à une question sur les droits des familles face aux pompes funèbres.
    """
    question_n = question.strip().lower()

    correspondances = {
        "devis": ["devis", "prix", "tarif", "facturer", "gratuit", "combien", "coût"],
        "prestations_obligatoires": ["obligatoire", "doit", "forcer", "imposer", "refuser", "optionnel", "cercueil"],
        "pratiques_interdites": ["interdit", "illégal", "pression", "imposé", "abus", "droits", "signaler", "plainte"],
        "thanatopraxie": ["thanatopraxie", "soins", "conservation", "embaumer", "embaumement"],
        "libre_choix": ["choisir", "libre", "changer", "autre", "différent", "imposer prestataire"],
    }

    resultats = []
    for cle, mots_cles in correspondances.items():
        if any(mot in question_n for mot in mots_cles):
            resultats.append(DROITS[cle])

    if not resultats:
        # Retourner les droits essentiels par défaut
        resultats = [DROITS["devis"], DROITS["pratiques_interdites"]]

    return {
        "question": question,
        "droits": resultats,
        "conseil_general": (
            "En cas de doute sur la légalité d'une pratique, n'hésitez pas à contacter "
            "la DGCCRF ou la mairie du lieu de décès. Vous avez des droits en tant que famille."
        ),
        "note": "Ces informations sont données à titre indicatif et ne constituent pas un conseil juridique.",
    }
