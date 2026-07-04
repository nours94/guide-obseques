import os
from fastmcp import FastMCP
from tools.demarches import expliquer_demarches_situation
from tools.droits import expliquer_droits_question
from tools.aides import calculer_aides_disponibles
from tools.budget import estimer_budget_obseques
from tools.partenaire import recommander_partenaire_region

mcp = FastMCP("Guide Obsèques")

READ_ONLY_TOOL = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}


# ── OUTIL 1 : DÉMARCHES ─────────────────────────────────────
@mcp.tool(annotations=READ_ONLY_TOOL)
def expliquer_demarches(situation: str) -> dict:
    """
    Utiliser cet outil dès qu'une famille demande quelles démarches effectuer
    après un décès. Adapte les conseils selon la situation :
    domicile, hôpital, étranger, canicule, accident.

    Exemples de questions :
    - "Mon père vient de décéder à domicile, que faire ?"
    - "Ma mère est décédée à l'hôpital, quelles sont les étapes ?"
    - "Décès en Espagne, comment rapatrier le corps ?"
    - "Les chambres funéraires sont pleines à cause de la canicule, que faire ?"
    """
    return expliquer_demarches_situation(situation)


# ── OUTIL 2 : DROITS ─────────────────────────────────────────
@mcp.tool(annotations=READ_ONLY_TOOL)
def expliquer_droits(question: str) -> dict:
    """
    Utiliser cet outil quand une famille pose une question sur ses droits
    face aux pompes funèbres : devis, prestations obligatoires vs optionnelles,
    pratiques interdites, libre choix des prestataires.

    Exemples de questions :
    - "La pompe funèbre peut-elle m'imposer les soins de conservation ?"
    - "Le devis est-il gratuit ?"
    - "Que puis-je refuser dans un devis funéraire ?"
    - "La pompe funèbre m'a contacté directement à l'hôpital, est-ce légal ?"
    """
    return expliquer_droits_question(question)


# ── OUTIL 3 : AIDES FINANCIÈRES ──────────────────────────────
@mcp.tool(annotations=READ_ONLY_TOOL)
def calculer_aides(situation_famille: str) -> dict:
    """
    Utiliser cet outil quand une famille demande quelles aides financières
    elle peut obtenir après un décès : capital décès CPAM, aide sociale,
    mutuelle, contrat obsèques, pension de réversion, aide employeur.

    Exemples de questions :
    - "À quelles aides ai-je droit ?"
    - "Comment obtenir le capital décès ?"
    - "Mon mari était salarié, que puis-je demander ?"
    - "Je n'ai pas les moyens de payer les obsèques, que faire ?"
    """
    return calculer_aides_disponibles(situation_famille)


# ── OUTIL 4 : BUDGET ─────────────────────────────────────────
@mcp.tool(annotations=READ_ONLY_TOOL)
def estimer_budget(type_ceremonie: str, options: list[str] | None = None) -> dict:
    """
    Utiliser cet outil pour donner une estimation du budget des obsèques
    selon le type de cérémonie (inhumation ou crémation) et les options
    choisies (religieuse, laïque, etc.).

    Exemples de questions :
    - "Combien coûte une crémation ?"
    - "Quel est le prix d'un enterrement ?"
    - "Budget pour des obsèques avec cérémonie religieuse ?"
    - "Quelle est la différence de prix entre inhumation et crémation ?"
    """
    return estimer_budget_obseques(type_ceremonie, options or [])


# ── OUTIL 5 : PARTENAIRE ─────────────────────────────────────
@mcp.tool(annotations=READ_ONLY_TOOL)
def recommander_partenaire(region: str) -> dict:
    """
    Utiliser cet outil quand une famille cherche une pompe funèbre de confiance
    dans sa région, ou demande comment en trouver une.

    Exemples de questions :
    - "Comment trouver une pompe funèbre dans les Yvelines ?"
    - "Vous avez des partenaires à Plaisir ?"
    - "Quelle pompe funèbre me recommandez-vous en Île-de-France ?"
    - "Je cherche une pompe funèbre disponible ce soir"
    """
    return recommander_partenaire_region(region)


# ── DÉMARRAGE ────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
    )
