---
product: product-factory
artifact_type: roadmap-session
run_id: roadmap-session-product-factory-0001
date: 2026-08-11
status: completed
---
# Roadmap-sessie 1

## Samenvatting

Roadmap was leeg; op basis van cycli 23–28 en het overlegdossier van 2026-08-10 zijn twee lopende thema's aangemaakt die beide door de eigenaar als even belangrijk zijn bestempeld: (1) het hoofdscherm herinrichten rond de drie kernacties (cyclus starten/resultaten/stories), waarvan cyclus 28 een eerste kleine stap zette; (2) traceerbaarheid van afkeuringen (reden + wie/wat besliste, zonder tegenstrijdigheden tussen overzicht en detail), waarvan meerdere deelbugs al zijn opgelost maar de eigenaar recent nog aangaf dat "wie besliste" niet altijd zichtbaar is in het overzicht. Drie eenmalig afgehandelde technische bevindingen (contradictie-fix geverifieerd, verdict-opslagbug gevonden en gerepareerd, misleidend guardrail-label gecorrigeerd) zijn toegevoegd als afgehandelde onderzoeksvragen, zodat ze niet opnieuw hoeven te worden onderzocht.

## Roadmap op dit moment

### Traceerbaarheid van afkeuring: reden en beslisser zichtbaar zonder tegenstrijdigheid — HIGH · OPEN

Doorlopende lijn sinds cyclus 23: eerst kwam er een zichtbaar Reden-blok bij afkeuring/aanpassing (cyclus 23), daarna werden diverse tegenstrijdigheden tussen overzicht en detailscherm gevonden en opgelost (cyclus 24: verdict werd overschreven door vaste 'afgekeurd'-tekst; cyclus 27/28: 'oordeel ontbreekt' terwijl overzicht wel een oordeel toonde, fix geverifieerd live), en misleidende labels gecorrigeerd (cyclus 25/26: 'guardrail-conflict' → 'technische fout'; leestekens rond onderzoeksbevindingen opgeschoond). Ondanks deze progressie gaf de eigenaar in het overleg van 2026-08-10 expliciet aan dat afkeuringen nog niet traceerbaar zijn: niet duidelijk is óf een mens, evaluatie-agent of guardrail-check de beslissing nam, en dit moet zichtbaar zijn in het overzicht zelf (niet alleen opzoekbaar in detail). Cyclus 26 concludeerde dat bestaande badges dit grotendeels al oplossen, maar dat lijkt niet te stroken met de recentere eigenaarsfeedback — dit verdient verificatie in een volgende cyclus. Door eigenaar even belangrijk geacht als het hoofdscherm-thema.

### Hoofdscherm herinrichten rond drie kernacties — HIGH · OPEN

Eigenaar wil op het hoofdscherm snel (a) een nieuwe cyclus kunnen starten, (b) zien wat eerdere cycli hebben opgeleverd, (c) de daaruit voortgekomen stories zien. Het scherm bestaat nog uit zeven gelijkwaardige blokken zonder die nadruk. Cyclus 28 zette een eerste, bewust kleine stap: de knop 'Start productcyclus nu' prominent en apart bovenaan, en instellingen-achtige info (missie, repo, limieten, AI-instellingen) verplaatst naar het instellingenscherm. De volledige herindeling van het hoofdscherm (incl. cyclusoverzicht-lijst met status/datum/reden per regel zoals in het overlegdossier geschetst) is bewust nog niet gedaan omdat dat te groot/risicovol ineens zou zijn. Expliciet door eigenaar bevestigd als topprioriteit in overleg van 2026-08-10.