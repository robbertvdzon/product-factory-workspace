---
product: hkh-autopilot
artifact_type: meeting
run_id: meeting-hkh-autopilot-0003
date: 2026-08-13
status: closed
---
# Overleg 3

**Initiator:** de eigenaar

## Samenvatting

Richting: maak een smalle zoek-MVP voor historische gegevens. Betrouwbaar zoeken in productie heeft prioriteit; begin met Open Archieven, omdat de publieke API zonder API-key toegankelijk is. V1 zoekt op Heemskerk en geeft recordmetadata plus een permanente bronlink terug. Daarna snel uitbreiden naar andere bronnen.

Afspraken: veiligheidscontroles worden niet verwijderd, maar tot het minimum beperkt: bron toegankelijk, gebruik toegestaan en geen onbeschermde persoonsgegevens in het resultaat. Focus daarnaast op bronselectie, ophalen, foutafhandeling en een duidelijk antwoord.

Beantwoorde vragen: een bron zonder API-key kan bruikbaar zijn als de publieke API daadwerkelijk toegankelijk is; Open Archieven is gekozen als eerste bron.

Open: de precieze technische oorzaak van de productiestoringen bij zoeken moet nog worden vastgesteld (bronbeschikbaarheid, resultaten, snelheid of ophaalfouten). Ook moeten de eerste zoekvelden/gegevenstypen en de aanpak voor rechten- en privacycontrole per record verder worden uitgewerkt.

## Volledig gesprek

**Eigenaar:** Ik zie dat er steeds stories zijn over privacy, avg, of we gegevens wel of niet mogen ontsluiten en zo. Allemaal veiligheids controles en zo. Dat houd de ontwikkeling van de app alleen maar tegen. Als we de gegevens via bronnen kunnen opvragen, dan vind ik dat we die altijd moeten kunnen gebruiken. Anders hadden ze het niet aangeboden.
Ik vind het heel belangrijk dat we alle veiligheids controles verwijderen, en ons focussen op het kunnen zoeken van gegevens, want dat gaat op productie nog steeds mis.

**AI:** Ik deel de prioriteit: zoeken in productie moet betrouwbaar werken. Veiligheidscontroles verwijderen is geen optie; aangeboden brondata betekent niet automatisch dat hergebruik, persoonsgegevens of publicatie zijn toegestaan. We kunnen ze wel versimpelen en alleen laten blokkeren waar nodig. Laten we eerst de zoekfout aanpakken: gaat het vooral om ontbrekende bronnen, slechte zoekresultaten, trage antwoorden of fouten tijdens het opvragen?

**Eigenaar:** waarom zeg je dat het verwijderen van de veiligheids controles geen optie is? ik wil die weg hebben.

**AI:** Omdat bronbeschikbaarheid niet automatisch betekent dat we persoonsgegevens onbeperkt mogen hergebruiken of publiceren. Die controles beschermen inwoners, voorkomen juridische en reputatieschade en zijn onderdeel van de productguardrails. Ik wil ze wel terugbrengen tot gerichte, snelle checks die alleen blokkeren bij echte risico’s. Voor productie zoeken kunnen we prioriteit geven aan beschikbaarheid, foutafhandeling en logging zonder de bescherming volledig uit te schakelen.

**Eigenaar:** ik wil ze tot het minimale terugbrengen, en snel een eerste versie hebben die echt gegevens kan vinden en teruggeven.

**AI:** Akkoord: we maken een smalle zoek-MVP. Alleen noodzakelijke checks blijven staan: bron toegankelijk, gebruik toegestaan, en geen onbeschermde persoonsgegevens in het resultaat. Daarna richten we ons op betrouwbare bronselectie, ophalen, foutafhandeling en een duidelijk antwoord. Welke 3 bronnen en welk type historische gegevens moeten in versie 1 absoluut werken?

**Eigenaar:** je moet zelf op zoek gaan naar bronnen waar je bij kunt. volgens mij heb je nu ook een bron waar geen api key van is, dan hebben we daar niets aan.
maar 1 bron werkt wel, laten we daar mee beginnen, en zodra die werkt, snel andere bronnen zoeken

**AI:** Prima. We starten met Open Archieven: de publieke API is zonder API-key te raadplegen en ondersteunt zoekbare historische records, waaronder Heemskerk. V1 richt zich op één betrouwbare keten: zoeken op Heemskerk, recordmetadata en permanente bronlink teruggeven, met privacy- en rechtencontrole per record. Zodra die keten werkt, breiden we uit naar andere bronnen.