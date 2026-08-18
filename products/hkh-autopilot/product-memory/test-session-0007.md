---
product: hkh-autopilot
artifact_type: test-session
run_id: test-session-hkh-autopilot-0007
date: 2026-08-18
status: completed
---
# Testsessie 7

## Samenvatting

Brede, niet-destructieve regressietest van HKH Autopilot op acceptatie, live en admin-acceptatie, uitgevoerd met headless Chromium via Playwright. Bij elke omgeving is de flt-semantics-placeholder geactiveerd en zijn echte screenshots visueel bekeken voordat iets is gerapporteerd.

Verificatie bestaande bugs:
- BUG-7 (lege witte pagina) blijft terecht RESOLVED: alle drie de omgevingen renderen na semantics-activatie een volledige, bruikbare shell (visueel bevestigd).
- BUG-1 (Back op Productvisie) blijft terecht RESOLVED: "Terug naar startpagina", de Back-knop op Historisch zoeken en browser-back keren alle drie terug naar de startpagina.
- BUG-2 blijft OPEN: historische zoekopdrachten leveren in acceptatie én live nul bronnen op, voor vrije tekst, persoon, plek en gebeurtenis, en ook met bronfilter Open Archieven.
- BUG-3 blijft OPEN: een lege zoekopdracht wordt niet lokaal gevalideerd maar naar de server gestuurd, terwijl omgekeerde jaartallen wél lokaal worden afgevangen.

Drie nieuwe defecten gevonden. Het zwaarste is dat "Uitloggen" in de admin-app een volledig grijze lege pagina achterlaat zonder inlogscherm; alleen een handmatige reload herstelt de app en de sessie blijkt dan nog actief. Daarnaast meldt de admin-functie "Ophalen" voor externe brongegevens altijd "Niet bereikbaar" (eigen API geeft 403 op zowel geldige als ongeldige URL, zonder lokale URL-validatie), en toont het zoekscherm "Zoekinterpretatie: naam (name)" terwijl er een gebeurtenis is ingevuld en event=huwelijk correct wordt verstuurd. Verder twee toegankelijkheidspunten: leeg lang-attribuut op alle drie de apps en een Engelstalig label "Back" in een verder Nederlandse UI.

Positief bevonden: nieuwsoverzicht, vrije-tekst nieuws zoeken via Enter met correcte "0 resultaten"-lege toestand en suggestiechips, entiteitschips met servercall, wis-zoekopdracht, mobiele layout 390x844, toetsenbordnavigatie, jaarfiltervalidatie, bronfilter-dropdown, foutpadknoppen (Zoekopdracht aanpassen zet focus terug op Vrije tekst) en de clientvalidatie van beide admin-formulieren inclusief foutsamenvatting. Geen JS- of consolefouten waargenomen.

Twee observaties zijn bewust NIET als bug gemeld omdat visuele controle het DOM-bewijs weersprak: "Wis zoekopdracht" leek het veld niet te legen (alleen de Flutter DOM-proxywaarde bleef staan; het zichtbare veld is wel leeg) en het nieuwszoekveld leek te ontbreken op acceptatie (het stond onder de vouw door lazy rendering).

Geen destructieve of muterende acties uitgevoerd: er is geen nieuwsbericht gepubliceerd en geen record-intake ingediend; alleen validatiepaden met lege velden zijn getest.

## Geteste onderdelen

- Opstarten en renderen acceptatie (https://hkh-autopilot-acceptance.vdzonsoftware.nl): PASS — HTTP 200, flt-semantics-placeholder geactiveerd, screenshot visueel bekeken: kop 'Historisch Heemskerk', knop 'Lees onze productvisie', statuskaart 'Service beschikbaar' met sha-06ac831, 'Laatste nieuws' met 5 berichten. Geen console- of pageerrors.
- Opstarten en renderen live (https://hkh-autopilot.vdzonsoftware.nl): PASS — HTTP 200, semantics geactiveerd, screenshot bekeken: identieke shell, 'Service beschikbaar', 'Er zijn nog geen nieuwsberichten.' en sectie 'Ontdek nieuws'. /api/news geeft {"items":[],"total":0} - lege dataset, geen renderfout.
- Opstarten en renderen admin-acceptatie: PASS — HTTP 200, semantics geactiveerd, screenshot bekeken: 'HKH Beheer', 'Beheerder geverifieerd preview-admin@hkh-autopilot.invalid', formulieren 'Nieuw bericht' en 'Nieuwe record-intake' volledig zichtbaar.
- BUG-7 hercontrole: lege witte pagina in alle drie de omgevingen: PASS — Alle drie de omgevingen tonen na activatie van flt-semantics-placeholder een volledige semantics-tree en een visueel gevulde screenshot. Blijft terecht RESOLVED.
- BUG-1 hercontrole: Productvisie openen en terugnavigeren: PASS — Acceptatie: 'Lees onze productvisie' opent kop 'Productvisie' met volledige tekst en productprincipes; knop 'Terug naar startpagina' keert terug naar 'Historisch Heemskerk'. Blijft terecht RESOLVED.
- Back-knop Historisch zoeken en browser-back: PASS — Acceptatie: Back-knop op 'Historisch zoeken' keert terug naar de startpagina; page.goBack() vanaf het zoekscherm levert eveneens de startpagina op.
- BUG-2 hercontrole: historisch zoeken vrije tekst 'Heemskerk' op acceptatie: FAIL — GET /api/historical-search?q=Heemskerk (200) gevolgd door status 'Geen historische bronnen konden worden geraadpleegd. Europeana: niet geconfigureerd. Open Archieven stuurde een onvolledig antwoord. Zoekinterpretatie: naam (name).' Nul resultaten.
- BUG-2 hercontrole: historisch zoeken 'Heemskerk' op live: FAIL — Live-omgeving toont exact dezelfde status: 'Geen historische bronnen konden worden geraadpleegd. Europeana: niet geconfigureerd. Open Archieven stuurde een onvolledig antwoord.' Nul resultaten.
- Historisch zoeken via velden Persoon, Plek en Gebeurtenis: FAIL — Acceptatie: Persoon=Jansen, Plek=Heemskerk en Gebeurtenis=overlijden leveren elk dezelfde bronuitvalstatus en nul resultaten op. Bevestigt de breedte van BUG-2.
- Historisch zoeken met bronfilter Open Archieven: PASS — Dropdown 'Bron (optioneel)' toont menuitems 'Europeana' en 'Open Archieven'; na keuze wordt de knop 'Bron (optioneel) Open Archieven' en verdwijnt Europeana correct uit de foutmelding. Het filter werkt zoals verwacht.
- BUG-3 hercontrole: lege historische zoekopdracht: FAIL — Acceptatie: klik op 'Zoeken' zonder enig criterium stuurt GET /api/historical-search?start=0&limit=100 (200) en toont de bronuitvalmelding in plaats van een lokale melding om een zoekterm in te vullen.
- Jaarfiltervalidatie (omgekeerde jaren en letters): PASS — Acceptatie: Vanafjaar=2000 met Eindjaar=1800 en Vanafjaar=abcd leveren beide lokaal 'De historische zoekfilters zijn ongeldig.' op zonder servercall.
- Foutpadknoppen 'Opnieuw proberen' en 'Zoekopdracht aanpassen': PASS — 'Opnieuw proberen' voert een nieuwe poging uit en meldt 'Nieuwe poging mislukt; de bronfout wordt hieronder afzonderlijk gemeld.' 'Zoekopdracht aanpassen' verwijdert het foutblok en zet de focus terug op het veld 'Vrije tekst'.
- Weergave zoekinterpretatie bij gebeurtenisveld: FAIL — Acceptatie: alleen Gebeurtenis=huwelijk ingevuld verstuurt correct event=huwelijk, maar de UI meldt 'Zoekinterpretatie: naam (name).' - identiek aan de melding bij Persoon=Jansen.
- Nieuwsoverzicht acceptatie: PASS — Vijf nieuwskaarten met titel, datum en samenvatting correct gerenderd (Kerkweg 28-07-2026 t/m Wandeling langs verdwenen winkels 30-06-2026); visueel gecontroleerd op screenshot.
- Nieuws vrije-tekst zoeken via Enter: PASS — Acceptatie: typen van 'kermis' gevolgd door Enter roept /api/news?q=kermis aan en toont '1 resultaat gevonden' met het kermisbericht; 'Kerkweg' via echte muisklik plus Enter levert eveneens 1 correct resultaat.
- Nieuws lege-resultatentoestand: PASS — Acceptatie: zoekterm 'zzzqqqxyz' levert '0 resultaten gevonden' met groep 'Geen resultaten gevonden voor deze zoekopdracht. Probeer een van deze suggesties:' en vier suggestiechips.
- Nieuws entiteitschips (Plek/Gebeurtenis): PASS — Acceptatie: klik op 'Plek: Kerkweg' roept /api/news?entity=Kerkweg aan en filtert de lijst; 'Gebeurtenis: Kermis' roept /api/news?entity=Kermis aan.
- Knop 'Wis zoekopdracht': PASS — Acceptatie: na zoeken op 'Assumburg' en klik op 'Wis zoekopdracht' toont de screenshot een leeg veld met placeholder 'Zoek in nieuwsberichten' en is het resultatenblok verdwenen. (De DOM-proxywaarde bleef staan; dat is een Flutter-intern artefact, niet zichtbaar voor de gebruiker.)
- Mobiele layout 390x844: PASS — Acceptatie: startpagina en 'Historisch zoeken' schalen correct; alle velden, dropdown en knoppen zijn zonder horizontale scroll leesbaar en bereikbaar op de screenshot.
- Toetsenbordnavigatie startpagina: PASS — Acceptatie: Tab-volgorde bereikt 'Lees onze productvisie' en 'Historisch zoeken' in een sluitende cyclus; focus blijft zichtbaar binnen de app.
- Taalattribuut van het document: FAIL — document.documentElement.lang is een lege string op acceptatie, live én admin, terwijl de volledige UI Nederlandstalig is.
- Labeltaal van de terugknop: FAIL — Op 'Historisch zoeken' heeft de terugknop de toegankelijke naam 'Back' (Engels), terwijl Productvisie 'Terug naar startpagina' gebruikt in een verder volledig Nederlandse UI.
- Admin: clientvalidatie nieuw nieuwsbericht: PASS — Klik op 'Publiceren' met lege velden markeert Titel en Bericht als [invalid] met 'Vul een titel in.' en 'Vul een bericht in.' en doet geen enkele publicatiecall (alleen admin/me). Er is niets gepubliceerd.
- Admin: clientvalidatie record-intake met foutsamenvatting: PASS — Klik op 'Intake indienen' met lege velden toont groep 'Foutsamenvatting' met acht aanklikbare foutverwijzingen plus veldmeldingen; geen netwerkcall, dus geen record aangemaakt.
- Admin: dropdown Privacyclassificatie: PASS — Toont menuitems 'geen persoonsgegevens', 'mogelijk persoonsgegevens' en 'persoonsgegevens'; sluit met Escape.
- Admin: externe brongegevens ophalen: FAIL — Zowel 'niet-een-url' als de geldige URL https://www.openarch.nl/ leiden tot 403 op /api/record-intake/external-archive-preview en de melding 'Niet bereikbaar'; geen lokale URL-validatie.
- Admin: historische bronresultaten zoeken: PASS — Leeg zoeken en q=Heemskerk roepen /api/admin/historical-search correct aan (200) en tonen de nette lege toestand '0 historische resultaten geladen. Geen historische bronresultaten gevonden.' De lege uitkomst is een gevolg van BUG-2, niet van de beheerweergave.
- Admin: uitloggen: FAIL — Na klik op 'Uitloggen' blijft de pagina minstens 15 seconden volledig egaal grijs (screenshot visueel gecontroleerd), semantics-tree leeg, geen flt-semantics-placeholder, URL ongewijzigd, geen console- of pageerrors. Pas een handmatige reload herstelt de app, en dan is preview-admin nog steeds ingelogd.
- JavaScript- en consolefouten: PASS — Bij het laden en bedienen van alle drie de omgevingen zijn geen console-errors en geen pageerrors waargenomen.
- Visuele vergelijking met referentiebeeld bronuitval: PASS — Referentiebeeld media-c7e32e06 (toestand C, bron faalde, gemarkeerd als huidige live-toestand) is opgehaald en bekeken; de letterlijke statustekst over Open Archieven, Europeana en 'naam (name)' komt exact overeen met wat de draaiende app toont. Bevestigt dat BUG-2 de bekende live-toestand is.