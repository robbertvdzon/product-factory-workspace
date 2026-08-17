---
product: hkh-autopilot
artifact_type: test-session
run_id: test-session-hkh-autopilot-0005
date: 2026-08-17
status: completed
---
# Testsessie 5

## Samenvatting

P0-regressie gevonden: acceptatie, live en admin-acceptatie tonen na laden alleen een lege witte pagina. Alle kernflows zijn daardoor onbruikbaar.

## Geteste onderdelen

- Acceptatie bereikbaarheid en render: FAIL — HTTP 200 en titel aanwezig, maar body blijft leeg; na 15 seconden ontbreekt Flutter-content.
- Live bereikbaarheid en render: FAIL — HTTP 200 en titel aanwezig, maar body blijft leeg en er is geen bruikbare UI.
- Admin-acceptatie render: FAIL — HTTP 200 en titel aanwezig, maar body blijft leeg en er is geen beheerinterface.
- Productvisie/back-knop: BLOCKED — UI rendert niet; link en Back-knop zijn niet bedienbaar.
- Historisch zoeken leeg: BLOCKED — Formulier en zoekknop zijn niet beschikbaar.
- Historisch zoeken met Heemskerk: BLOCKED — Formulier en zoekknop zijn niet beschikbaar.
- Basis toegankelijkheid: FAIL — Geen zichtbare tekst, navigatielandmark of Flutter-semantics-content.