---
product: hkh-autopilot
artifact_type: test-session
run_id: test-session-hkh-autopilot-0002
date: 2026-08-16
status: completed
---
# Testsessie 2

## Samenvatting

De regressietest is geblokkeerd: geen interactieve browser beschikbaar en alle drie omgevingen waren vanuit de testomgeving niet bereikbaar wegens DNS-resolutiefout.

## Geteste onderdelen

- Acceptatie – bereikbaarheid en startpagina: BLOCKED — HTTPS-request geprobeerd; DNS-fout: Could not resolve host.
- Live – bereikbaarheid en startpagina: BLOCKED — HTTPS-request geprobeerd; DNS-fout: Could not resolve host.
- Admin acceptatie – bereikbaarheid en login: BLOCKED — HTTPS-request geprobeerd; DNS-fout: Could not resolve host.
- Authenticatie en sessiegedrag: BLOCKED — Geen omgeving bereikbaar en geen interactieve browser beschikbaar.
- Navigatie en primaire gebruikersflows: BLOCKED — Geen pagina kunnen laden.
- Formulieren en validatie: BLOCKED — Geen interactieve pagina kunnen openen.
- Foutpaden en foutmeldingen: BLOCKED — Geen applicatieflow kunnen uitvoeren.
- Toegankelijkheid op hoofdlijnen: BLOCKED — Geen UI kunnen inspecteren.
- Adminflows en beheerfunctionaliteit: BLOCKED — Adminomgeving niet bereikbaar; geen beheeractie uitgevoerd.
- Recent gerepareerde bugs: BLOCKED — Bestaande buglijst bevatte geen bugs en de omgevingen waren niet bereikbaar.