---
product: hkh-autopilot
artifact_type: test-session
run_id: test-session-hkh-autopilot-0003
date: 2026-08-16
status: completed
---
# Testsessie 3

## Samenvatting

Brede niet-destructieve regressietest uitgevoerd via headless Playwright-fallback; tijdelijke testbestanden zijn verwijderd. Drie nieuwe bugs vastgesteld.

## Geteste onderdelen

- Browserbeschikbaarheid: BLOCKED — Browser-provider gaf geen beschikbare browsers; headless Playwright-fallback gebruikt.
- Acceptatie landingpage: PASS — HTTP 200, servicestatus beschikbaar, vijf nieuwsitems zichtbaar.
- Live landingpage: PASS — HTTP 200, servicestatus beschikbaar; geen runtime- of requestfouten.
- Productvisie openen: PASS — Productvisie opent met inhoud en productprincipes.
- Productvisie terugnavigatie: FAIL — Back-knop verandert scherm of URL niet; bevestigd op acceptatie en live.
- Historisch zoeken formulier: PASS — Alle verwachte zoekvelden, bronkeuze en Zoek-knop zichtbaar.
- Lege historische zoekopdracht: FAIL — Lege submit veroorzaakt bronfout in plaats van lokale validatie.
- Historische zoekopdracht met kerkweg: FAIL — Geen resultaten; Europeana niet geconfigureerd en Open Archieven geeft een fout/ongeldige respons.
- Admin dashboard: PASS — Beheerder geverifieerd; publicatie-, intake- en bronresultaatflows zichtbaar.
- Admin lege publicatie: PASS — Titel- en berichtvalidatie verschijnt; niets gepubliceerd.
- Admin lege record-intake: PASS — Acht concrete validatiefouten verschijnen; geen record aangemaakt.
- Admin lege bronzoekopdracht: PASS — 0 historische resultaten en duidelijke lege-resultaatmelding.
- Mobiele landingpage: PASS — 390px viewport zonder horizontale overflow.
- Runtime- en netwerkcontrole: PASS — Geen console-errors of request failures tijdens de flows.