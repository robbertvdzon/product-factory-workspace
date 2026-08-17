---
product: hkh-autopilot
artifact_type: test-session
run_id: test-session-hkh-autopilot-0006
date: 2026-08-17
status: completed
---
# Testsessie 6

## Samenvatting

Brede Playwright-regressietest uitgevoerd op acceptatie, live en admin. Flutter-rendering, navigatie en admin-shell werken; historische zoekresultaten en lokale lege-zoekvalidatie falen.

## Geteste onderdelen

- Flutter-rendering acceptatie/live/admin: PASS — HTTP 200; na activatie van flt-semantics-placeholder verschijnt de applicatieshell in alle drie omgevingen.
- Productvisie en Back: PASS — Productvisie opent en Back brengt terug naar de homepage.
- Admin-shell en toegankelijkheid: PASS — Beheerinterface, formulieren, knoppen, statusinformatie en checkbox zijn beschikbaar.
- Lege historische zoekopdracht: FAIL — Start onterecht /api/historical-search?start=0&limit=100 en toont retry-UI.
- Historisch zoeken met Heemskerk: FAIL — In acceptatie en live wordt de zoekrequest verstuurd, maar verschijnen geen resultaatkaarten of bronmetadata.