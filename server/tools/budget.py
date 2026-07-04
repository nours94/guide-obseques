"""
Outil : estimer_budget
Estimation des fourchettes de prix selon le type de cérémonie et les options choisies.
"""

BUDGETS = {
    "inhumation": {
        "type": "Inhumation (enterrement)",
        "description": "Le corps est mis en terre dans un cercueil, dans un cimetière.",
        "fourchette_basse": 2500,
        "fourchette_haute": 6000,
        "fourchette_typique": 3500,
        "prestations": {
            "cercueil_base": {"min": 250, "max": 800, "description": "Cercueil réglementaire de base"},
            "cercueil_haut_gamme": {"min": 800, "max": 3000, "description": "Cercueil avec finitions premium"},
            "transport_corps": {"min": 150, "max": 400, "description": "Transport avant mise en bière"},
            "convoi": {"min": 200, "max": 600, "description": "Convoi funèbre jusqu'au cimetière"},
            "concession": {"min": 300, "max": 2000, "description": "Concession au cimetière (selon durée et commune)"},
            "monument": {"min": 500, "max": 5000, "description": "Monument funéraire (optionnel)"},
            "fleurs": {"min": 100, "max": 500, "description": "Fleurs et couronnes (optionnel)"},
            "faire_part": {"min": 80, "max": 300, "description": "Faire-part (optionnel)"},
        },
        "conseils": [
            "La concession au cimetière est un coût souvent oublié — vérifiez si le défunt en avait déjà une.",
            "Le monument funéraire peut être commandé plus tard — vous n'êtes pas obligé de le commander en même temps.",
            "Certaines communes proposent des concessions gratuites sous conditions de ressources.",
        ]
    },
    "cremation": {
        "type": "Crémation",
        "description": "Le corps est incinéré dans un crématorium. Les cendres peuvent être dispersées ou conservées dans une urne.",
        "fourchette_basse": 2000,
        "fourchette_haute": 5000,
        "fourchette_typique": 3000,
        "prestations": {
            "cercueil_base": {"min": 250, "max": 800, "description": "Cercueil réglementaire obligatoire même pour la crémation"},
            "transport_corps": {"min": 150, "max": 400, "description": "Transport avant mise en bière"},
            "convoi_crematorium": {"min": 200, "max": 500, "description": "Convoi jusqu'au crématorium"},
            "frais_crematorium": {"min": 300, "max": 600, "description": "Frais du crématorium"},
            "urne": {"min": 50, "max": 500, "description": "Urne cinéraire (optionnel)"},
            "dispersion_cendres": {"min": 0, "max": 200, "description": "Dispersion en mer ou en nature (optionnel)"},
            "columbarium": {"min": 200, "max": 1000, "description": "Case en columbarium (optionnel)"},
        },
        "conseils": [
            "La crémation est généralement moins coûteuse que l'inhumation, mais l'écart se réduit selon les options.",
            "Les cendres peuvent être dispersées gratuitement dans la nature (hors voie publique et propriété privée sans autorisation).",
            "La dispersion en mer nécessite des formalités — se renseigner auprès de la mairie.",
        ]
    },
    "ceremonie_religieuse": {
        "type": "Supplément cérémonie religieuse",
        "fourchette_basse": 200,
        "fourchette_haute": 800,
        "description": "Frais liés à l'église, mosquée, synagogue ou autre lieu de culte.",
        "prestations": {
            "frais_eglise": {"min": 150, "max": 400, "description": "Frais d'église (offrande, organiste, etc.)"},
            "transport_eglise": {"min": 50, "max": 200, "description": "Transport supplémentaire vers l'église"},
        }
    },
    "ceremonie_laique": {
        "type": "Cérémonie laïque",
        "fourchette_basse": 300,
        "fourchette_haute": 1200,
        "description": "Cérémonie civile dans une salle des obsèques ou un autre lieu.",
        "prestations": {
            "maitre_ceremonie": {"min": 200, "max": 600, "description": "Maître de cérémonie"},
            "salle": {"min": 100, "max": 400, "description": "Location de salle (souvent incluse en chambre funéraire)"},
            "musique": {"min": 0, "max": 200, "description": "Musique ou sonorisation"},
        }
    }
}

PRESTATIONS_OPTIONNELLES = {
    "thanatopraxie": {"min": 200, "max": 400, "description": "Soins de conservation — optionnel et souvent inutile"},
    "chambre_funeraire": {"min": 50, "max": 120, "description": "Chambre funéraire par jour (au-delà de 48h)"},
    "toilette_mortuaire": {"min": 100, "max": 250, "description": "Toilette et habillage du défunt"},
    "avis_journaux": {"min": 100, "max": 400, "description": "Avis de décès dans la presse"},
    "livret_obseques": {"min": 80, "max": 200, "description": "Livret de cérémonie"},
}


def estimer_budget_obseques(type_ceremonie: str, options: list = None) -> dict:
    """
    Estime le budget des obsèques selon le type de cérémonie et les options.
    """
    type_n = type_ceremonie.strip().lower()
    options = options or []

    # Déterminer le type de cérémonie
    if any(mot in type_n for mot in ["inhumation", "enterrement", "terre", "cimetière", "tombe"]):
        budget_base = BUDGETS["inhumation"]
    elif any(mot in type_n for mot in ["crémation", "cremation", "incinération", "cendres", "urne"]):
        budget_base = BUDGETS["cremation"]
    else:
        budget_base = BUDGETS["inhumation"]  # Par défaut

    # Calculer le budget total avec options
    total_min = budget_base["fourchette_basse"]
    total_max = budget_base["fourchette_haute"]

    supplements = []

    if any(mot in " ".join(options).lower() for mot in ["religieux", "église", "mosquée", "synagogue", "culte"]):
        supplements.append(BUDGETS["ceremonie_religieuse"])
        total_min += BUDGETS["ceremonie_religieuse"]["fourchette_basse"]
        total_max += BUDGETS["ceremonie_religieuse"]["fourchette_haute"]

    if any(mot in " ".join(options).lower() for mot in ["laïque", "laique", "civil", "salle"]):
        supplements.append(BUDGETS["ceremonie_laique"])
        total_min += BUDGETS["ceremonie_laique"]["fourchette_basse"]
        total_max += BUDGETS["ceremonie_laique"]["fourchette_haute"]

    return {
        "type_ceremonie": budget_base["type"],
        "description": budget_base["description"],
        "budget_minimum": total_min,
        "budget_maximum": total_max,
        "budget_typique": budget_base["fourchette_typique"],
        "detail_prestations": budget_base["prestations"],
        "supplements_ceremonies": supplements,
        "prestations_optionnelles": PRESTATIONS_OPTIONNELLES,
        "conseils": budget_base["conseils"] + [
            "Ces fourchettes sont données à titre indicatif — demandez toujours plusieurs devis.",
            "Un devis détaillé est obligatoire et gratuit auprès de toute pompe funèbre.",
            "Des aides financières peuvent réduire significativement le reste à charge — renseignez-vous auprès de la CPAM.",
        ],
        "note": "Les prix varient selon les régions et les prestataires. Ces estimations reflètent des moyennes nationales françaises en 2024.",
    }
