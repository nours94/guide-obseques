"""
Outil : expliquer_demarches
Base de connaissance sur les démarches après un décès.
"""

DEMARCHES = {
    "domicile": {
        "titre": "Décès à domicile",
        "urgence": "Dans les premières heures",
        "etapes": [
            "Appeler le médecin traitant ou le 15 (SAMU) pour constater le décès et obtenir le certificat de décès.",
            "Ne pas déplacer le corps avant le passage du médecin.",
            "Appeler les pompes funèbres de votre choix — vous êtes entièrement libre du choix de l'entreprise.",
            "Déclarer le décès à la mairie du lieu de décès dans les 24 heures (hors week-ends et jours fériés). Les pompes funèbres peuvent effectuer cette démarche à votre place.",
            "Demander au minimum 10 exemplaires de l'acte de décès à la mairie.",
        ],
        "conseils": [
            "Si le décès survient la nuit ou le week-end, le 15 peut envoyer un médecin de garde.",
            "Le corps peut rester au domicile jusqu'à 6 jours dans des conditions d'hygiène adaptées.",
            "En période de forte chaleur (canicule), le transfert en chambre funéraire est vivement recommandé le plus tôt possible.",
            "Vous pouvez demander le transfert en chambre funéraire si vous ne souhaitez pas garder le défunt au domicile.",
        ],
        "delais": {
            "constat_medical": "Immédiat",
            "declaration_mairie": "Sous 24h (hors jours non ouvrés)",
            "obseques": "Dans les 6 jours suivant le décès",
        }
    },
    "hopital": {
        "titre": "Décès à l'hôpital ou en EHPAD",
        "urgence": "Dans les premières heures",
        "etapes": [
            "L'établissement établit le certificat de décès automatiquement — vous n'avez pas à faire appel à un médecin.",
            "L'hôpital conserve le corps en chambre mortuaire gratuitement pendant 3 jours (au-delà, des frais peuvent s'appliquer).",
            "Choisir librement votre pompe funèbre — l'hôpital ne peut pas vous imposer un prestataire particulier.",
            "Déclarer le décès à la mairie du lieu de décès dans les 24 heures.",
            "Récupérer les effets personnels du défunt auprès de l'établissement.",
        ],
        "conseils": [
            "L'hôpital peut vous remettre une liste de pompes funèbres — vous n'êtes pas obligé de choisir parmi elles.",
            "Demandez à l'établissement quels documents ils peuvent vous fournir directement (acte de décès, etc.).",
            "Si le défunt était sous tutelle, contactez le tuteur pour les décisions relatives aux obsèques.",
        ],
        "delais": {
            "conservation_hopital": "3 jours gratuits en chambre mortuaire",
            "declaration_mairie": "Sous 24h (hors jours non ouvrés)",
            "obseques": "Dans les 6 jours suivant le décès",
        }
    },
    "etranger": {
        "titre": "Décès à l'étranger",
        "urgence": "Procédure longue — prévoir plusieurs jours",
        "etapes": [
            "Contacter l'ambassade ou le consulat français du pays de décès — ils vous guideront sur la procédure locale.",
            "Obtenir l'acte de décès local et le faire traduire par un traducteur assermenté.",
            "Faire légaliser ou apostiller l'acte de décès selon le pays.",
            "Faire établir un laissez-passer mortuaire (permis d'inhumer) pour le rapatriement international.",
            "Contacter une pompe funèbre spécialisée dans les rapatriements internationaux.",
            "Vérifier si le défunt avait une assurance rapatriement (assurance voyage, carte bancaire premium).",
            "Une fois le corps rapatrié en France, procéder aux obsèques normalement.",
        ],
        "conseils": [
            "Vérifiez immédiatement les assurances du défunt : carte bancaire Visa Premier, Mastercard Gold, assurance voyage — beaucoup couvrent le rapatriement.",
            "Le délai de 6 jours pour les obsèques est suspendu pendant la procédure de rapatriement.",
            "Le consulat français peut vous aider à trouver une pompe funèbre locale fiable.",
            "Conservez toutes les factures liées au rapatriement pour les remboursements d'assurance.",
        ],
        "delais": {
            "contact_consulat": "Immédiat",
            "rapatriement": "Variable selon le pays (3 à 15 jours)",
            "obseques_france": "Dans les 6 jours après arrivée en France",
        }
    },
    "canicule": {
        "titre": "Décès en période de canicule ou fortes chaleurs",
        "urgence": "Situation d'urgence — agir rapidement",
        "etapes": [
            "Contacter immédiatement les pompes funèbres — les délais sont plus courts en période de canicule.",
            "Demander le transfert en chambre funéraire le plus tôt possible pour préserver la dignité du défunt.",
            "Si la chambre funéraire est saturée, contacter plusieurs établissements dans un rayon élargi.",
            "En dernier recours, contacter la mairie — la commune a l'obligation d'organiser l'inhumation si la famille ne peut pas.",
            "Déclarer le décès à la mairie dans les 24 heures comme habituellement.",
        ],
        "conseils": [
            "En période de canicule, les chambres funéraires peuvent être saturées — commencez les démarches immédiatement.",
            "Si vous devez garder le corps au domicile temporairement : maintenir la pièce fraîche (climatisation, volets fermés), contacter les pompes funèbres pour des conseils de conservation.",
            "Le plan canicule national prévoit des dispositifs d'urgence — votre mairie peut vous orienter.",
            "N'hésitez pas à contacter des pompes funèbres dans des villes voisines si les locales sont saturées.",
            "La préfecture peut autoriser des dérogations aux délais légaux en cas de saturation avérée.",
        ],
        "delais": {
            "transfert_recommande": "Dans les 12 à 24 heures idéalement",
            "declaration_mairie": "Sous 24h (hors jours non ouvrés)",
            "obseques": "Dans les 6 jours — des dérogations sont possibles en cas de force majeure",
        }
    },
    "accident": {
        "titre": "Décès accidentel ou suspect",
        "urgence": "Ne pas toucher au corps avant l'autorisation",
        "etapes": [
            "Appeler immédiatement le 15 (SAMU) et le 17 (Police) ou le 18 (Pompiers).",
            "Ne pas toucher ni déplacer le corps — c'est une obligation légale jusqu'à l'autorisation des autorités.",
            "La police ou le procureur de la République doit autoriser la levée du corps.",
            "Un médecin légiste peut être requis pour déterminer les causes du décès.",
            "Une fois l'autorisation obtenue, les démarches reprennent comme pour un décès normal.",
        ],
        "conseils": [
            "En cas de décès sur la voie publique, la police prend en charge l'organisation du transfert du corps.",
            "Si une enquête judiciaire est ouverte, les obsèques peuvent être retardées — des dérogations au délai de 6 jours sont alors accordées.",
            "Conservez tous les documents liés à l'accident pour les démarches d'assurance.",
        ],
        "delais": {
            "autorisation_levee_corps": "Variable selon enquête (quelques heures à plusieurs jours)",
            "declaration_mairie": "Sous 24h après autorisation",
            "obseques": "Dans les 6 jours après autorisation de levée du corps",
        }
    }
}


def expliquer_demarches_situation(situation: str) -> dict:
    """
    Retourne le guide de démarches adapté à la situation du décès.
    """
    situation_n = situation.strip().lower()

    # Correspondance flexible
    correspondances = {
        "domicile": ["domicile", "maison", "chez lui", "chez elle", "à la maison", "domicile"],
        "hopital": ["hôpital", "hopital", "clinique", "ehpad", "maison de retraite", "établissement", "urgences"],
        "etranger": ["étranger", "etranger", "abroad", "hors de france", "vacances", "voyage"],
        "canicule": ["canicule", "chaleur", "été", "chaud", "saturation", "chambre funéraire pleine", "plein"],
        "accident": ["accident", "accidentel", "suspect", "police", "judiciaire", "meurtre", "suicide", "voie publique"],
    }

    for cle, mots_cles in correspondances.items():
        if any(mot in situation_n for mot in mots_cles):
            demarche = DEMARCHES[cle]
            return {
                "situation": cle,
                "titre": demarche["titre"],
                "urgence": demarche["urgence"],
                "etapes": demarche["etapes"],
                "conseils": demarche["conseils"],
                "delais": demarche["delais"],
                "note": "Ces informations sont données à titre indicatif. En cas de doute, contactez la mairie ou les pompes funèbres.",
            }

    # Situation générique si non reconnue
    return {
        "situation": "generale",
        "titre": "Démarches générales après un décès",
        "urgence": "Dans les premières heures",
        "etapes": DEMARCHES["domicile"]["etapes"],
        "conseils": [
            "Précisez-moi le lieu du décès (domicile, hôpital, étranger) pour des conseils plus adaptés.",
            "Les premières démarches sont similaires dans la plupart des cas.",
        ],
        "delais": DEMARCHES["domicile"]["delais"],
        "note": "Ces informations sont données à titre indicatif. En cas de doute, contactez la mairie ou les pompes funèbres.",
    }
