---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0070
date: 2026-08-14
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://open-nha.nl/contact/
  - https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1089932&mivast=0&miview=inv2&mizig=210
  - https://www.archieven.nl/nl/zoeken?miadt=236&miaet=1&micode=3779&minr=1091734&mivast=0&miview=inv2&mizig=210
  - https://www.openarchieven.nl/datasets/nha
  - https://www.openarchieven.nl/api/docs/?lang=en
  - https://www.archieven.nl/nl/zoeken?miadt=236
---
# Productcyclus 70

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een controleerbaar eerste zoekresultaat kan leveren wanneer bronrespons gedeeltelijk of volledig faalt. De huidige UI bewaart de zoekterm, maar toont voor ‘Heemskerk’ geen records. Publieke bronnen tonen wel aantoonbare Heemskerk-dekking bij het Noord-Hollands Archief en herbruikbare metadata via Open Archieven.

### Huidige zoekflow

De app biedt zoeken op vrije tekst, plek, persoon, gebeurtenis, periode en bron. Zoeken op ‘Heemskerk’ toont in productie en acceptatie geen historische bronnen, Europeana als niet geconfigureerd en Open Archieven als onvolledig antwoord.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Aantoonbare Heemskerk-dekking

Noord-Hollands Archief beheert en publiceert archieven voor Heemskerk. Publieke toegangen omvatten onder meer het gemeentebestuur van Heemskerk en Heemskerkse DTB-collecties.

Bronnen: [https://open-nha.nl/contact/](https://open-nha.nl/contact/), [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1089932&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1089932&mivast=0&miview=inv2&mizig=210), [https://www.archieven.nl/nl/zoeken?miadt=236&miaet=1&micode=3779&minr=1091734&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&miaet=1&micode=3779&minr=1091734&mivast=0&miview=inv2&mizig=210)

### Herbruikbare NHA-metadata

De NHA-dataset via Open Archieven bevat miljoenen documentmetadata en persoonsvermeldingen en biedt OAI-PMH/A2A, exports en datasetmetadata onder CC0. Afbeeldingen en derde-partij-viewers vallen niet automatisch onder CC0.

Bronnen: [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha)

### Herleidbaarheid en bronveerkracht

Open Archieven documenteert recordzoeken, record-URI’s, content negotiation, OpenSearch, OAI-PMH, caching en een limiet van vier verzoeken per seconde per IP. Dit ondersteunt afzonderlijke bronstatussen, stabiele links en gecontroleerd retrygedrag.

Bronnen: [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en)

### Zoekinspiratie

Archieven.nl combineert eenvoudig en uitgebreid zoeken met filters, sortering, weergavekeuze en hulpteksten. Dit is relevant voor latere verfijning nadat de eerste bronresultaten betrouwbaar zijn.

Bronnen: [https://www.archieven.nl/nl/zoeken?miadt=236](https://www.archieven.nl/nl/zoeken?miadt=236), [https://www.archieven.nl/nl/zoeken?miadt=236&mif1=Heemskerk&mif2=1874-1891&milang=nl&mistart=140&mivast=0&miview=tbl&mizig=37](https://www.archieven.nl/nl/zoeken?miadt=236&mif1=Heemskerk&mif2=1874-1891&milang=nl&mistart=140&mivast=0&miview=tbl&mizig=37)

### Huidige applicatie

**Doel:** Een brede publieke historische ontdekapp voor iedereen die iets wil weten over een gebouw, straat, persoon, gebeurtenis of ander onderwerp uit de geschiedenis van Heemskerk. De app verbindt lokale kennis met externe historische bronnen en wil antwoorden herleidbaar, toegankelijk en betrouwbaar maken.

**Wat ontbreekt:**
- Voor ‘Heemskerk’ zijn geen records of geldige deelresultaten zichtbaar.
- Bronuitval wordt niet per bron uitgesplitst in status, aantallen, ophaaltijd of foutcategorie.
- Stabiele identifiers, permanente bronlinks en rechtenstatussen ontbreken in de zichtbare uitkomst.
- Acceptatie bevat geen bruikbare historische mockrecords voor resultaat- en foutscenario’s.
- De beheeracceptatie toont zonder login een geverifieerde beheerder en mutatieve formulieren.

### Verbetermogelijkheden

- Valideer afzonderlijk of de Open Archieven-adapter NHA-dekking en juiste datasetidentiteit ophaalt.
- Toon per bron expliciete statussen voor resultaten, geen resultaten, bronuitval, ongeldige respons en niet geconfigureerd.
- Toon alleen geldige records met bronmetadata, stabiele identifier, permanente link en afzonderlijke rechtenstatus.
- Respecteer Open Archieven-rate-limits en caching bij zoeken en opnieuw proberen.
- Gebruik acceptatiescenario’s voor geldige metadata, onvolledige respons, bronuitval en onbekende rechten.
- Gebruik Archieven.nl als inspiratie voor zoekverfijning en hulpteksten nadat de basisrespons betrouwbaar is.

### Inspiratiebronnen

- [Archieven.nl / Noord-Hollands Archief](https://www.archieven.nl/nl/zoeken?miadt=236) — Zoekverfijning, filters, sortering, weergavekeuze en contextuele hulp.
- [Open Archieven NHA-dataset](https://www.openarchieven.nl/datasets/nha) — OAI-PMH/A2A, datasetidentiteit en scheiding tussen metadata- en objectrechten.
- [Open Archieven API](https://www.openarchieven.nl/api/docs/?lang=en) — Record-URI’s, content negotiation, caching, OpenSearch en rate limiting.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-14 | Publieke repository; concrete licentie niet vastgesteld. | Opgegeven productrepository voor productdoel en documentatie; webweergave kon niet inhoudelijk worden opgehaald. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-14 | Publieke interface; rechten op externe inhoud niet vastgesteld. | Werkelijk geopend, bekeken, naar historisch zoeken genavigeerd en read-only gezocht. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-14 | Representatieve mockdata; rechten/licentie niet vastgesteld. | Werkelijk geopend, bekeken, naar historisch zoeken genavigeerd en read-only gezocht. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-14 | Publieke beheerinterface; rechten/licentie op mockinhoud niet vastgesteld. | Werkelijk geopend en bekeken zonder login; geen mutatieve acties uitgevoerd. |
| [bron](https://open-nha.nl/contact/) | 2026-08-14 | Publieke informatieve website; licentie niet vastgesteld. | Bevestigt NHA-beheer en publicatie voor Heemskerk. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1089932&mivast=0&miview=inv2&mizig=210) | 2026-08-14 | Metadata vermeldt CC0; rechten op scans/objecten afzonderlijk controleren. | Concrete Heemskerkse archieftoegang. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236&miaet=1&micode=3779&minr=1091734&mivast=0&miview=inv2&mizig=210) | 2026-08-14 | Metadata vermeldt CC0; objectrechten afzonderlijk controleren. | Concrete Heemskerkse historische collectie. |
| [bron](https://www.openarchieven.nl/datasets/nha) | 2026-08-14 | Datasetmetadata onder CC0; afbeeldingen en derde-partij-viewers uitgesloten. | Bevestigt omvang, distributies en rechtennuance. |
| [bron](https://www.openarchieven.nl/api/docs/?lang=en) | 2026-08-14 | API-documentatie; inhoudsrechten bronafhankelijk. | Bevestigt API-capaciteiten, URI’s, caching en rate limits. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236) | 2026-08-14 | Collectie- en objectrechten zijn niet volledig vastgesteld. | Inspiratie voor zoekinteractie en verfijning. |

## Productbeslissing

Bouw een smalle, toetsbare bronveerkracht-MVP voor historisch zoeken op ‘Heemskerk’, met Open Archieven als eerste bron. Toon uitsluitend geldige recordmetadata met stabiele identifier en permanente bronlink; toon daarnaast per bron een expliciete status voor resultaten, geen resultaten, bronuitval, ongeldige respons en niet-geconfigureerd.

**Waarom:** Deze richting sluit direct aan op epic theme-hkh-autopilot-0002 en pakt het belangrijkste gevalideerde gat aan: zoeken levert momenteel geen records en maakt bronuitval niet controleerbaar zichtbaar. De NHA-dekking voor Heemskerk en de Open Archieven-metadata maken een eerste resultaat technisch en inhoudelijk toetsbaar. Rate limits, caching en stabiele record-URI’s ondersteunen gecontroleerd ophalen en herleidbaarheid. Aannames: de bestaande Open Archieven-adapter kan zonder nieuwe eigenaarstoegang worden gevalideerd; ontbrekende of onzekere rechteninformatie blokkeert een recordweergave niet zolang de rechtenstatus afzonderlijk als onbekend wordt getoond. De scope is bewust klein en bevat geen nieuwe zoekverfijning. De richting is zo afgebakend dat Product Factory- en Software Factory-agents haar zelfstandig kunnen uitvoeren, waarmee de eerdere agentbridge-time-out wordt hersteld door een begrensde uitvoeringsscope.

### Prioriteiten
- Valideer Open Archieven-aanvraag, NHA-datasetidentiteit en Heemskerk-dekking.
- Normaliseer alleen records met bronnaam, stabiele identifier, titel of omschrijving, datum indien aanwezig en permanente bronlink.
- Toon per bron een afzonderlijke, begrijpelijke status en foutcategorie.
- Pas caching, gecontroleerde retries en de gedocumenteerde limiet van vier verzoeken per seconde per IP toe.
- Voeg acceptatiescenario’s toe voor geldige metadata, lege resultaten, bronuitval, ongeldige respons en onbekende rechten.

### Besluiten
- **Gebruik Open Archieven als eerste externe bron voor de MVP.** — De roadmap noemt deze bron expliciet als eerstvolgende uitvoeringsfocus; de NHA-dataset biedt herbruikbare metadata en aantoonbare aansluiting op Heemskerk.
- **Maak bronstatus zichtbaar naast zoekresultaten.** — De huidige productie- en acceptatie-uitkomst maakt niet duidelijk welke bron succesvol, leeg, onvolledig of niet geconfigureerd is. De API-documentatie ondersteunt gecontroleerd ophalen, caching en afzonderlijke foutafhandeling.
- **Toon permanente bronlinks en scheid metadatarechten van objectrechten.** — Open Archieven ondersteunt stabiele record-URI’s; de NHA-dataset vermeldt CC0 voor metadata, terwijl afbeeldingen en derde-partij-viewers daarvan zijn uitgesloten.
- **Gebruik Noord-Hollands Archief als inhoudelijke dekkingstoets voor Heemskerk.** — Publieke toegangen bevestigen concrete Heemskerkse archieven en DTB-collecties bij het NHA.

## UX-voorstel: Bronveerkracht-MVP: zoeken naar Heemskerk

**Gebruikersdoel:** Een gebruiker wil controleerbare historische resultaten over Heemskerk vinden en kunnen zien welke bron succesvol, leeg of niet beschikbaar was.

### Flow
1. 1. Open historisch zoeken; focus staat op het vrije-tekstveld.
2. 2. Vul ‘Heemskerk’ in en activeer ‘Zoeken’ met toetsenbord of knop.
3. 3. Toon een laadstatus per bron zonder de zoekterm te verliezen.
4. 4. Toon alleen records met geldige titel of omschrijving, bron, stabiele identifier en permanente bronlink.
5. 5. Toon per bron een begrijpelijke status: resultaten, geen resultaten, bronuitval, ongeldige respons of niet geconfigureerd.
6. 6. Laat de gebruiker een record openen via de permanente bronlink en optioneel opnieuw proberen bij tijdelijke bronuitval.
7. 7. Toon bij elk record de rechtenstatus van metadata en objecten afzonderlijk; gebruik ‘Onbekend’ wanneer deze informatie ontbreekt.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
[Zoekterm __________________ Heemskerk] [Zoeken]

Status zoekopdracht
Zoekopdracht: Heemskerk

Bronnen
┌ Open Archieven — Noord-Hollands Archief ┐
│ Status: 3 resultaten gevonden            │
│ Laatst opgehaald: vandaag 14:32          │
└──────────────────────────────────────────┘

Resultaten
┌ Titel of omschrijving                    ┐
│ Datum: indien beschikbaar                │
│ Bron: Noord-Hollands Archief             │
│ Identifier: stabiele-ID                  │
│ Metadatarechten: CC0 / Onbekend          │
│ Objectrechten: Afzonderlijk controleren  │
│ [Open permanente bronlink]               │
└──────────────────────────────────────────┘

[Herhaal voor geldige records]

Bronstatussen zonder resultaten:
- Geen resultaten: ‘Deze bron antwoordde geldig, maar vond niets.’
- Bronuitval: ‘Deze bron is tijdelijk niet bereikbaar.’ [Opnieuw proberen]
- Ongeldige respons: ‘De bron gaf een onbruikbaar antwoord; er zijn geen records getoond.’
- Niet geconfigureerd: ‘Deze bron is niet beschikbaar voor deze zoekopdracht.’

[Hulptekst: Waarom zie ik verschillende bronstatussen?]

### Interactiehypotheses
- Als geldige records altijd een bron, stabiele identifier en permanente link tonen, kunnen geautomatiseerde controles 100% van de zichtbare records op herleidbaarheid valideren.
- Als elke bron afzonderlijk een status en foutcategorie krijgt, kan een agent per scenario betrouwbaar onderscheiden tussen resultaten, leeg resultaat, bronuitval, ongeldige respons en niet-geconfigureerde bron.
- Als ongeldige of onvolledige records volledig uit de resultaten worden weggelaten, verschijnen er geen records zonder minimale metadata of herleidbare bronlink.
- Als een tijdelijke bronfout een begrensde retry en caching gebruikt, blijft herhalen binnen de limiet van vier verzoeken per seconde per IP.
- Als rechteninformatie naast de recordmetadata staat en ontbrekende informatie als ‘Onbekend’ wordt weergegeven, worden metadatarechten niet ten onrechte geïnterpreteerd als rechten op scans of afbeeldingen.
- Als de zoekterm behouden blijft bij laad-, fout- en lege toestanden, kan een geautomatiseerde UI-test aantonen dat de zoekcontext niet verloren gaat.

### Toegankelijkheid
- Gebruik semantische koppen, labels en een formulier met programmatisch gekoppeld zoekveld.
- Maak zoeken volledig toetsenbordbedienbaar; gebruik zichtbare focus-indicatoren en logisch tabvolgorde.
- Kondig laadstatus en gewijzigde bronstatussen aan via een toegankelijk live region zonder focus onverwacht te verplaatsen.
- Gebruik tekst én betekenisvolle statuslabels; kleur mag nooit de enige statusindicator zijn.
- Zorg voor voldoende contrast voor tekst, knoppen, links, foutmeldingen en focusranden.
- Geef permanente bronlinks duidelijke linkteksten en een waarschuwing wanneer een link een extern domein opent.
- Gebruik foutmeldingen die uitleggen wat gebeurde en welke herstelactie beschikbaar is.
- Maak records en bronstatussen begrijpelijk voor schermlezers met consistente structuur en lijstsemantiek.

### Privacy
- Bewaar uitsluitend de zoekterm en technische zoekstatus zolang dat nodig is voor het uitvoeren en tonen van de zoekopdracht; sla zoekgeschiedenis niet standaard op.
- Verstuur alleen de noodzakelijke zoekterm naar de geconfigureerde bron en deel geen accountgegevens, locatiegegevens of andere persoonsgegevens.
- Gebruik caching zonder persoonsgegevens of individuele gebruikersprofielen; cache alleen bronrespons die noodzakelijk is voor betrouwbaarheid.
- Log technische foutcategorieën, responstijden en bronstatussen zonder vrije zoektermen wanneer die termen persoonsnamen kunnen bevatten.
- Documenteer doel en grondslag wanneer zoektermen of technische logs toch tijdelijk worden bewaard, met beperkte bewaartermijn en toegangscontrole.
- Toon bronrechten afzonderlijk: CC0 voor metadata betekent niet automatisch dat scans, afbeeldingen of externe viewers vrij herbruikbaar zijn.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is smal, toetsbaar en agent-uitvoerbaar. Er zijn geen blokkerende problemen; de overige aandachtspunten zijn niet-blokkerend.
- **WARNING · PRIVACY** — De cache moet zoekopdrachten kunnen onderscheiden zonder ruwe zoektermen langdurig te bewaren. Leg daarom expliciet vast dat een niet-herleidbare sleutel of veilige digest wordt gebruikt en dat bewaartermijnen configureerbaar zijn.
- **WARNING · CONSISTENCY** — De limiet van vier verzoeken per seconde is bronafhankelijk en kan wijzigen. Maak de limiet configureerbaar en test het gedrag via fixtures of contracttests.
- **INFO · SCOPE** — De kandidaat specificeert niet hoe een verzoekbudget per bron en zoekvenster precies wordt afgebakend. Dit kan tijdens implementatie worden ingevuld zonder eigenaarbesluit, zolang het gedrag deterministisch en geautomatiseerd getest blijft.

## Geaccepteerde storykandidaten

### Gecontroleerd verzoekbudget en caching voor Open Archieven

_Sleutel: `openarchieven-verzoekbudget-en-cachebeleid`_

Als historische zoekdienst wil ik Open Archieven-verzoeken begrenzen en waar passend cachen, zodat herhaalde zoekacties en retries de externe bron niet overbelasten en binnen de gedocumenteerde limiet blijven. De client gebruikt een deterministisch verzoekbudget per bron en zoekvenster, voorkomt gelijktijdige dubbele aanvragen voor dezelfde zoekopdracht en maakt cachegebruik technisch toetsbaar zonder zoektermen of persoonsgegevens langdurig op te slaan.

**Acceptatiecriteria**
- Een geautomatiseerde test toont aan dat gelijktijdige identieke aanvragen worden samengevoegd tot maximaal één extern verzoek.
- Een geautomatiseerde test toont aan dat identieke zoekopdrachten binnen de ingestelde cacheduur geen nieuw Open Archieven-verzoek uitvoeren.
- Een geautomatiseerde test toont aan dat retries en nieuwe aanvragen de gedocumenteerde limiet van vier verzoeken per seconde per IP niet overschrijden.
- Cache-items bevatten uitsluitend de noodzakelijke bronrespons en technische metadata; vrije zoektermen, persoonsnamen en ruwe bronpayloads worden niet langdurig opgeslagen.
- Een verlopen of onbruikbare cache-entry leidt tot een nieuwe aanvraag volgens hetzelfde verzoekbudget en geeft bij overschrijding een afzonderlijk, veilig foutresultaat terug.
- Bestaande resultaten, bronstatussen en permanente bronlinks blijven ongewijzigd wanneer een antwoord uit de cache wordt geleverd.

Bronnen: [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha)

Afhankelijkheden: story:74, story:75, story:79 (herkend als bestaande stories: 74, 75, 79)

Risico's: Een te lange cacheduur kan actuele bronwijzigingen tijdelijk verbergen; de duur moet configureerbaar en in tests expliciet zijn., Een gedeeld verzoekbudget kan gelijktijdige gebruikers beïnvloeden; de implementatie moet uitputting veilig en begrijpelijk afhandelen., De bron kan rate-limitgedrag wijzigen, waardoor contracttests of configuratie moeten worden aangepast.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
