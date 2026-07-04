"""
Outil : recommander_partenaire
Recommande un partenaire funéraire selon la région de la famille.
"""

PARTENAIRES = {
    "yvelines": {
        "nom": "Family Obsèques",
        "description": "Pompes funèbres familiales à Plaisir et Septeuil, au service des familles des Yvelines.",
        "slogan": "Notre famille au service de votre famille",
        "zones": ["Plaisir", "Septeuil", "Yvelines", "78", "Île-de-France Ouest"],
        "telephone": "01.87.08.49.98",
        "disponibilite": "24h/24 — 7j/7",
        "site": "https://family-obseques.fr",
        "note_google": "4.9/5 (67 avis)",
        "services": [
            "Inhumation et crémation",
            "Rapatriement national et international",
            "Prévoyance obsèques",
            "Monuments funéraires",
            "Avis de décès",
        ],
        "points_forts": [
            "Entreprise familiale indépendante — pas une franchise nationale",
            "Disponible 24h/24, 7j/7",
            "Devis gratuit et transparent",
            "Très bien noté par les familles (4.9/5)",
        ],
    },
}

RESSOURCES_GENERALES = {
    "trouver_pompe_funebre": [
        "Service-public.fr — annuaire des pompes funèbres habilitées par département",
        "La mairie de votre commune peut vous fournir une liste des pompes funèbres habilitées",
        "La DGCCRF publie la liste des entreprises sanctionnées — à vérifier avant de choisir",
    ],
    "verifier_habilitation": (
        "Toute pompe funèbre doit être habilitée par la préfecture. "
        "Vous pouvez vérifier cette habilitation auprès de la mairie ou de la préfecture du lieu de décès."
    ),
    "comparer_devis": (
        "Demandez toujours au moins 2 devis avant de signer. "
        "Le devis est gratuit et obligatoire. "
        "La différence de prix pour des prestations identiques peut atteindre 30 à 50%."
    ),
}


def recommander_partenaire_region(region: str, type_besoin: str = "general") -> dict:
    """
    Recommande un partenaire funéraire selon la région et le type de besoin.
    """
    region_n = region.strip().lower()

    partenaire_trouve = None

    for cle, partenaire in PARTENAIRES.items():
        zones_lower = [z.lower() for z in partenaire["zones"]]
        if any(zone in region_n or region_n in zone for zone in zones_lower):
            partenaire_trouve = partenaire
            break

    if partenaire_trouve:
        return {
            "partenaire_recommande": partenaire_trouve,
            "region_demandee": region,
            "message": (
                f"Pour votre région, Guide Obsèques recommande {partenaire_trouve['nom']}. "
                f"C'est une entreprise {partenaire_trouve['description'].lower()} "
                f"disponible {partenaire_trouve['disponibilite']}."
            ),
            "conseil": (
                "N'oubliez pas que vous êtes libre de choisir n'importe quelle pompe funèbre habilitée. "
                "Cette recommandation est basée sur notre partenariat de confiance avec cet établissement."
            ),
            "ressources": RESSOURCES_GENERALES,
        }
    else:
        return {
            "partenaire_recommande": None,
            "region_demandee": region,
            "message": (
                f"Guide Obsèques n'a pas encore de partenaire funéraire dans votre région ({region}). "
                "Voici comment trouver une pompe funèbre de confiance près de chez vous."
            ),
            "comment_trouver": RESSOURCES_GENERALES["trouver_pompe_funebre"],
            "conseils_choix": [
                "Vérifiez l'habilitation préfectorale de l'entreprise.",
                "Demandez plusieurs devis (gratuits et obligatoires).",
                "Vérifiez les avis Google et les recommandations de proches.",
                "Préférez les entreprises indépendantes aux grandes chaînes nationales si possible.",
                "Posez des questions sur leur disponibilité 24h/24.",
            ],
            "ressources": RESSOURCES_GENERALES,
        }
