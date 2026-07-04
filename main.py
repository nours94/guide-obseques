import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Guide Obsèques API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── ROUTES TECHNIQUES ────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "ok", "service": "Guide Obsèques"}


@app.get("/robots.txt")
def robots_txt():
    from fastapi.responses import Response
    contenu = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "User-agent: Googlebot\n"
        "Allow: /\n\n"
        "User-agent: GPTBot\n"
        "Allow: /\n\n"
        "User-agent: Google-Extended\n"
        "Allow: /\n\n"
        "Sitemap: https://guide-obseques.onrender.com/sitemap.xml\n"
    )
    return Response(
        content=contenu,
        media_type="text/plain",
        headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
    )


@app.get("/llms.txt", response_class=PlainTextResponse)
def llms_txt():
    return """# Guide Obsèques

> Service d'information et d'accompagnement gratuit pour les familles confrontées à un décès.

Guide Obsèques aide les familles à comprendre leurs droits, les démarches administratives
après un décès, à lire un devis funéraire et à identifier les aides financières disponibles.

## Ce que ce service propose

- /demarches.html : Guide chronologique des démarches après un décès
- /droits.html : Droits des familles face aux pompes funèbres, lecture de devis
- /aides.html : Capital décès CPAM, aide sociale, pension de réversion, contrats obsèques
- /contact.html : Contact

## Conseiller IA

Un conseiller IA est disponible via ChatGPT pour répondre aux questions des familles
sur les démarches, les droits et les aides financières liées aux obsèques.

## Partenaire

Données tarifaires fournies en partenariat avec Family Obsèques (Plaisir, Yvelines).

## Notes importantes

Les informations fournies sont à titre indicatif et ne constituent pas un conseil juridique.
Service gratuit, sans publicité, sans commission sur les obsèques.
"""


# ── ROUTES FRONT-END ─────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def accueil():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>Guide Obsèques — index.html introuvable</h1>")


@app.get("/demarches.html", response_class=HTMLResponse)
def demarches():
    if os.path.exists("demarches.html"):
        with open("demarches.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Page introuvable.")


@app.get("/droits.html", response_class=HTMLResponse)
def droits():
    if os.path.exists("droits.html"):
        with open("droits.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Page introuvable.")


@app.get("/aides.html", response_class=HTMLResponse)
def aides():
    if os.path.exists("aides.html"):
        with open("aides.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Page introuvable.")


@app.get("/contact.html", response_class=HTMLResponse)
def contact():
    if os.path.exists("contact.html"):
        with open("contact.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Page introuvable.")
