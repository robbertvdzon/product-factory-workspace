---
product: product-factory
artifact_type: test-session
run_id: test-session-product-factory-0002
date: 2026-08-16
status: completed
---
# Testsessie 2

## Samenvatting

Brede niet-destructieve regressietest uitgevoerd op acceptatie en de afgemelde live-omgeving. Acceptatie functioneert over de geteste hoofdflows, dialogen, detailweergaven en mobiele layout. Twee nieuwe P2-problemen gevonden: trage live-authenticatiefallback en ontbrekende toetsenbordfocus voor twee controls. Tijdelijke testbestanden en screenshots zijn verwijderd; bronbestanden en gegevens zijn niet gewijzigd.

## Geteste onderdelen

- Browser-provider: BLOCKED — De verplichte Browser-plugin meldde "Browser is not available: iab". Conform de opdracht is daarna headless Chrome met Playwright gebruikt.
- Acceptatie – initiële laadflow: PASS — HTTP 200, titel "Product Factory" en dashboard met 2 producten, 1 interne storykandidaat en 3 shadow-iteraties. Geen consolefouten, page errors of mislukte requests.
- Acceptatie – vernieuwen: PASS — "Vernieuwen" uitgevoerd; dashboarddata bleef beschikbaar en alle geregistreerde API-fetches retourneerden HTTP 200.
- Acceptatie – Overzicht: PASS — Overzicht geopend met productstatus, bugstatus, cyclus- en beheercontrols.
- Acceptatie – Roadmap: PASS — Roadmap geopend; lege status "Nog geen roadmap-sessies" correct weergegeven.
- Acceptatie – Productsessies: PASS — Drie eerdere cycli zichtbaar met verschillende eindtoestanden. Cyclus 3 geopend; opdracht, voortgang, resultaat en beslisbron werden getoond en de dialoog is gesloten zonder actie.
- Acceptatie – Stories: PASS — Story "Kaartweergave met foto-pins" zichtbaar en detailweergave met acceptatiecriteria/criticusbeoordeling geopend en gesloten.
- Acceptatie – Epics: PASS — Epic-roadmap geopend. De zichtbare epic-control opende de dialoog "Nieuwe epic"; deze is zonder toevoegen gesloten.
- Acceptatie – Bugs: PASS — Buglijst geopend met consistente lege status: 0 open en "Nog geen bugs geregistreerd".
- Acceptatie – Testsessies: PASS — Testsessies geopend; planning en bestaande sessie "Testsessie 1 FAILED" werden weergegeven. Een nieuwe sessie is niet gestart.
- Acceptatie – Overleggen: PASS — Bestaand overleg geopend; lege berichtenstatus en afsluitcontrol zichtbaar. Gesloten zonder bericht of statuswijziging.
- Acceptatie – Product toevoegen: PASS — Formulier met Slug, Naam, Missie, AI-engine en planningsvelden geopend en via "Annuleren" gesloten; er is geen product toegevoegd.
- Acceptatie – Instellingen: PASS — Instellingen voor HKH Autopilot met integratie-, limiet-, AI- en planningsvelden geopend en via "Annuleren" gesloten; niets opgeslagen.
- Acceptatie – Geheugen: PASS — Actief geheugen en versiegeschiedenis geopend; bestaande versie zichtbaar en paneel via "Sluiten" verlaten.
- Acceptatie – productselector: BLOCKED — Selector geopend en zonder wijziging gesloten. De browserpopup bood via de beschikbare semantische inspectie alleen een Dismiss-control, waardoor wisselen niet betrouwbaar kon worden geverifieerd.
- Acceptatie – formulieren en foutvalidatie: BLOCKED — Velden en veilige annuleerflows zijn getest. Lege formulieren zijn niet ingediend omdat dit mogelijk productdata kon creëren of wijzigen.
- Acceptatie – toetsenbordtoegankelijkheid: FAIL — Tijdens 45 Tab-toetsaanslagen werden 15 van 17 zichtbare dashboardbuttons bereikt. "Epics" en "Instellingen" kwamen in geen van de waargenomen focuscycli aan bod, hoewel beide met de muis bedienbaar waren.
- Acceptatie – toegankelijke namen en koppen: PASS — Hoofdpagina exposeerde twee koppen en de belangrijkste bedieningselementen hadden toegankelijke buttonnamen; formuliervelden hadden labels.
- Acceptatie – mobiele layout: PASS — Op 390×844 zonder horizontale documentoverflow geladen. Overzicht en Bugs zijn bediend; de buglijst en lege status pasten zichtbaar binnen het mobiele viewport.
- Acceptatie – onbekende route: PASS — Een onbekend pad retourneerde HTTP 200 en viel gecontroleerd terug op het dashboard zonder crash, consolefout of mislukte request.
- Live – afgemelde desktopstart: FAIL — HTTP 200. Na 5 en 10 seconden was alleen een laadindicator zichtbaar. Bij 20 seconden verscheen de Google-inlogkaart; deze bleef vervolgens stabiel zichtbaar tot 60 seconden.
- Live – Google-inlogscherm: PASS — Na de vertraging verscheen "Log in met een toegestaan Google-account" met een Google-knop die in het Google-iframe als button met toegankelijke naam beschikbaar was.
- Live – mobiele authenticatiepagina: PASS — Op 390×844 verscheen uiterlijk na 20 seconden een correct passende inlogkaart met toegankelijke Google-inlogknop.
- Live – ingelogde dashboardflows: BLOCKED — Geen toegestaan Google-account beschikbaar. Authenticatie is niet omzeild; interne live-navigatie en gegevensflows zijn daarom niet getest.
- Admin: BLOCKED — Geen adminomgeving geconfigureerd.