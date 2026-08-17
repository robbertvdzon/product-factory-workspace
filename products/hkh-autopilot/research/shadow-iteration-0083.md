---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0083
date: 2026-08-17
status: approved
sources:
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://www.openarchieven.nl/api/docs/records/search.php?lang=en
  - https://www.openarchieven.nl/api/docs/records/show.php
  - https://www.openarchieven.nl/api/docs/uri.php
  - https://www.openarchieven.nl/datasets/dom?lang=nl
  - https://www.openarchieven.nl/disclaimer.php
  - https://www.europeana.eu/en/rights/usage-guidelines-for-metadata
  - https://pro.europeana.eu/page/available-rights-statements
  - https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
---
# Productcyclus 83

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De publieke zoekketen faalt nog steeds in productie en acceptatie. Onderzoek toont dat Open Archieven voldoende velden biedt voor een controleerbare resultaatkaart, maar dat metadatarechten, objectrechten en privacystatus afzonderlijk moeten worden behandeld. Dit is onderzoek, geen productbesluit of story.

### Historisch zoeken faalt end-to-end

“Heemskerk” levert in productie en acceptatie volledige bronuitval op, zonder resultaatkaart. Beide omgevingen tonen dezelfde buildlabel sha-06ac831.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Open Archieven biedt kaartrelevante metadata

Search v1.1 beschrijft velden zoals identifier, archive_org, eventtype, eventdate, eventplace, sourcetype en permanente URL. Show v1.1 voegt bronhouder, collectie, RecordIdentifier, RecordGUID, provenance en oorspronkelijke bronlinks toe.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php?lang=en](https://www.openarchieven.nl/api/docs/records/search.php?lang=en), [https://www.openarchieven.nl/api/docs/records/show.php](https://www.openarchieven.nl/api/docs/records/show.php)

### Persistente bronidentiteit is beschikbaar

Open Archieven ondersteunt archivecode-UUID-URI’s en meerdere machineleesbare representaties via content negotiation.

Bronnen: [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php)

### Metadatarechten en scanrechten verschillen

Open Archieven vermeldt CC0 voor aangeboden metadata, maar sluit rechten op afbeeldingen en externe viewers uit. De disclaimer waarschuwt bovendien voor onvolledigheid en privacy-/rechtenrisico’s.

Bronnen: [https://www.openarchieven.nl/datasets/dom?lang=nl](https://www.openarchieven.nl/datasets/dom?lang=nl), [https://www.openarchieven.nl/disclaimer.php](https://www.openarchieven.nl/disclaimer.php)

### Statuscommunicatie blijft onvoldoende onderscheidend

De huidige UI toont een foutstatus en retry-acties, maar geen broncount, nulresultaatstatus of controleerbare per-bronstatus. WCAG noemt zoeken, resultaatcount en nulresultaat expliciet als programmatisch herkenbare statusberichten.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

### Huidige applicatie

**Doel:** hkh-autopilot is een publieke historische ontdekkingstoepassing voor een brede doelgroep. De app moet geschiedenis van Heemskerk verbinden met bredere historische collecties en bezoekers via vragen, plekken, personen en gebeurtenissen naar betrouwbare, herleidbare bronnen leiden.

**Wat ontbreekt:**
- Productie en acceptatie tonen geen resultaatkaart voor “Heemskerk”.
- Bronnaam, stabiele identifier, permanente link, datering/plaats, bronhouder, ophaaldatum en rechten-/privacystatus zijn niet zichtbaar.
- De huidige foutstatus onderscheidt niet duidelijk transportfout, ongeldig antwoord, nulresultaat en gedeeltelijke bronuitval.
- De relatie tussen beheerfunctie, bronresultaatdata en publieke presentatie is read-only niet vast te stellen.
- Metadatarechten en rechten op scans/viewers worden niet afzonderlijk zichtbaar gemaakt.

### Verbetermogelijkheden

- Gebruik het officiële Search v1.1-contract als expliciete adaptergrens en classificeer transport-, HTTP-, JSON-, mapping-, nulresultaat- en bronuitvalstatussen afzonderlijk.
- Map een minimale resultaatkaart op identifier, archive_org, sourcetype, eventdate, eventplace en url.
- Gebruik RecordIdentifier, RecordGUID, provenance en SourceDigitalOriginal afzonderlijk voor herleidbaarheid.
- Toon metadatarechten apart van scan-/viewerrechten en gebruik onbekend als veilige default bij ontbrekende verificatie.
- Maak één programmatisch waarneembare statusregio met zoeken, resultaatcount, nulresultaat, gedeeltelijke uitval en volledige uitval.
- Test Search v1.1, Show v1.1 en HTTP 301/404/410-contracten zonder onnodige opslag van ruwe persoonsgegevens.

### Inspiratiebronnen

- [Open Archieven API](https://www.openarchieven.nl/api/docs/records/show.php) — Voorbeeld van stabiele identiteit, provenance, bronhouder en oorspronkelijke bronlinks.
- [Europeana rights statements](https://pro.europeana.eu/page/available-rights-statements) — Voorbeeld van gestandaardiseerde, machineleesbare rechtenstatus per object.
- [Europeana metadata guidelines](https://www.europeana.eu/en/rights/usage-guidelines-for-metadata) — Voorbeeld van bronbehoud, attributie en onderscheid tussen metadata en objectgebruik.
- [W3C status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) — Voorbeeld voor toegankelijke zoekstatussen zonder focusverplaatsing.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-17 | Geen specifieke licentie- of rechtenverklaring zichtbaar in de geraadpleegde flow. | Actuele productieflow en reproduceerbare zoekfout. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-17 | Representatieve nepdata; specifieke UI-rechten onbekend. | Actuele acceptatieflow en pariteitsvergelijking. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-17 | Dummy-beheeromgeving; specifieke UI-rechten onbekend. | Read-only controle van bronresultaat- en privacyfuncties. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-17 | Repositorylicentie niet vastgesteld. | Publieke repositoryreferentie voor productdossier en documentatie. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php?lang=en) | 2026-08-17 | Licentie van de documentatiepagina niet expliciet vastgesteld. | API-contract voor zoeken en resultaatvelden. |
| [bron](https://www.openarchieven.nl/api/docs/records/show.php) | 2026-08-17 | Licentie van de documentatiepagina niet expliciet vastgesteld. | API-contract voor detailmetadata en provenance. |
| [bron](https://www.openarchieven.nl/api/docs/uri.php) | 2026-08-17 | Licentie van de documentatiepagina niet expliciet vastgesteld. | Contract voor persistente URI’s en representaties. |
| [bron](https://www.openarchieven.nl/datasets/dom?lang=nl) | 2026-08-17 | CC0 voor aangeboden metadata; externe scans/viewers vallen daar niet onder. | Concrete licentie-indicatie. |
| [bron](https://www.openarchieven.nl/disclaimer.php) | 2026-08-17 | Geen brede hergebruiklicentie; rechten- en privacywaarschuwingen zijn van toepassing. | Beoordeling van onzekerheid en risico’s. |
| [bron](https://www.europeana.eu/en/rights/usage-guidelines-for-metadata) | 2026-08-17 | Europeana vermeldt CC0 voor metadata met bron- en attributierichtlijnen. | Vergelijkbaar patroon voor open metadata. |
| [bron](https://pro.europeana.eu/page/available-rights-statements) | 2026-08-17 | Gestandaardiseerde rights statements worden als URI’s beschreven. | Vergelijkbaar per-object rechtenpatroon. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | 2026-08-17 | W3C Document License/permissive license rules. | Toegankelijkheidsreferentie voor dynamische zoekstatussen. |

## Productbeslissing

Herstel de Open Archieven-zoekketen voor de zoekopdracht “Heemskerk” en lever één controleerbare resultaatweergave op. Classificeer transport-, HTTP-, JSON-, mapping-, nulresultaat-, gedeeltelijke uitval- en volledige uitvalstatussen afzonderlijk. Toon per resultaat minimaal bronnaam, gebeurtenisplaats en -datum, stabiele identifier, permanente link, provenance en afzonderlijke metadata-, scan- en viewerrechtenstatussen. Maak alle zoekstatussen programmatisch waarneembaar.

**Waarom:** BUG-2 is een open P1-bug en heeft daarom voorrang op roadmapuitbreiding. Productie en acceptatie tonen momenteel volledige bronuitval en geen resultaatkaarten, terwijl Open Archieven volgens het onderzochte Search- en Show-contract voldoende velden biedt voor een herleidbare kaart. De richting herstelt de primaire ingang naar historische ontdekking, versterkt betrouwbaarheid en verbondenheid met externe collecties, en voorkomt dat metadatarechten ten onrechte als scanrechten worden geïnterpreteerd. De statusweergave maakt bovendien duidelijk onderscheid tussen fout, nulresultaat en gedeeltelijke uitval en ondersteunt toegankelijke feedback.

### Prioriteiten
- Reproduceer en herstel de adapter tegen het officiële Open Archieven Search v1.1-contract in productie- en acceptatieconfiguratie.
- Definieer en test een versioned intern resultaat- en statuscontract met afzonderlijke foutcategorieën.
- Toon een minimale herleidbare resultaatkaart met stabiele identiteit, bronmetadata, provenance en permanente link.
- Toon metadatarechten afzonderlijk van rechten op scans en externe viewers; gebruik onbekend als veilige standaard bij ontbrekende verificatie.
- Voeg één programmatisch waarneembare statusregio toe voor zoekvoortgang, resultaatcount, nulresultaat, gedeeltelijke uitval en volledige uitval en valideer de zoekopdracht “Heemskerk”. 

### Besluiten
- **Maak herstel van BUG-2 de eerstvolgende productrichting.** — De bug is P1, open en opnieuw bevestigd in zowel acceptatie als productie; de primaire historische zoeking levert momenteel geen bronnen op.
- **Gebruik Open Archieven Search v1.1 als expliciete adaptergrens en map minimaal identifier, archive_org, sourcetype, eventdate, eventplace en url.** — Het onderzochte API-contract beschrijft deze velden en maakt daarmee een controleerbare resultaatkaart mogelijk.
- **Gebruik Show v1.1 voor aanvullende herleidbaarheid via RecordIdentifier, RecordGUID, provenance en oorspronkelijke bronlinks.** — Detailmetadata en provenance zijn nodig om gebruikers van samenvatting naar oorspronkelijke bron te laten doorklikken.
- **Behandel persistente URI’s en machineleesbare representaties als afzonderlijke bronidentiteit.** — Open Archieven ondersteunt archivecode-UUID-URI’s en content negotiation, wat duurzame bronverwijzing ondersteunt.
- **Toon metadatarechten los van scan- en viewerrechten en blokkeer geen metadataweergave uitsluitend vanwege ontbrekende scanrechten; markeer onbekend wanneer verificatie ontbreekt.** — De onderzochte voorwaarden noemen CC0 voor aangeboden metadata, maar sluiten rechten op afbeeldingen en externe viewers uit en waarschuwen voor privacy- en rechtenrisico’s.

## UX-voorstel: Herstel historische zoekketen voor “Heemskerk”

**Gebruikersdoel:** Een bezoeker zoekt op “Heemskerk” en krijgt betrouwbare, herleidbare historische resultaten met duidelijke zoekstatussen en afzonderlijke rechteninformatie.

### Flow
1. Bezoeker opent Historisch zoeken.
2. Bezoeker voert “Heemskerk” in en activeert Zoeken.
3. De interface toont in één programmatisch waarneembare statusregio dat de zoekactie loopt.
4. De applicatie toont resultaatcount en per resultaat een controleerbare resultaatkaart.
5. De bezoeker opent de permanente link of bronverwijzing voor verdere raadpleging.
6. Bij nulresultaat, gedeeltelijke uitval of volledige uitval toont de interface de specifieke status en een passende herstelactie.
7. Geautomatiseerde contract-, mapping-, status- en toegankelijkheidstests valideren de flow met Search v1.1-, Show v1.1- en HTTP 301/404/410-scenario’s.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
Label: Zoekterm
[ Heemskerk                                      ]
[Zoeken]

[aria-live=status]
Zoeken voltooid. 12 resultaten gevonden. 1 bron gedeeltelijk niet beschikbaar.

[Resultaat 1]
Titel: Gebeurtenis in Heemskerk
Bron: Open Archieven
Gebeurtenisplaats: Heemskerk
Gebeurtenisdatum: 14 mei 1890
Type: Geboorte
Stabiele identifier: [RecordIdentifier]
Provenance: [bronhouder / collectie]
Metadatarechten: CC0 / Onbekend
Scanrechten: Niet geverifieerd / Onbekend
Viewerrechten: Externe bron bepaalt / Onbekend
[Permanente bronlink] [Oorspronkelijke bronlink]

[Resultaat 2]
Zelfde veldstructuur.

[Bronstatussen]
Open Archieven: Geslaagd — 12 resultaten
Bron B: Gedeeltelijke uitval — resultaten mogelijk onvolledig

Bij nulresultaat:
[aria-live=status] Zoekactie voltooid. Geen resultaten gevonden voor “Heemskerk”.
Controleer spelling of probeer een bredere zoekterm.

Bij volledige uitval:
[aria-live=alert] De bron kon niet worden bereikt. Er zijn geen resultaten beschikbaar.
[Opnieuw proberen]

### Interactiehypotheses
- Als gebruikers per resultaat bron, datum, plaats, stabiele identifier en permanente link zien, kunnen geautomatiseerde inhoudstests vaststellen dat elke geldige resultaatkaart herleidbare kernvelden bevat.
- Als transport-, HTTP-, JSON-, mapping-, nulresultaat-, gedeeltelijke-uitval- en volledige-uitvalstatussen afzonderlijke machineleesbare waarden hebben, kunnen contracttests elke status deterministisch onderscheiden.
- Als metadatarechten, scanrechten en viewerrechten afzonderlijke velden zijn, zal geen resultaatkaart scanrechten afleiden uit metadatarechten; dit is toetsbaar met fixtures waarin rechten ontbreken of conflicteren.
- Als zoekvoortgang, resultaatcount en foutstatus in één aria-live-regio worden gepubliceerd zonder focusverplaatsing, kunnen accessibilitytests de status programmatisch detecteren en blijft toetsenbordnavigatie stabiel.
- Als ontbrekende rechteninformatie standaard als “Onbekend” wordt getoond, worden niet-geverifieerde gebruiksrechten niet als toestemming gepresenteerd; dit is toetsbaar met ontbrekende-rechtenfixtures.
- Als permanente bronidentiteit en provenance zichtbaar zijn, bevatten alle doorzoekbare resultaten een stabiele verwijzing die na herladen of opnieuw ophalen gelijk blijft.

### Toegankelijkheid
- Gebruik semantische HTML-landmarks, één duidelijke H1, gelabeld zoekveld en een expliciete submitknop.
- Maak alle interactieve elementen volledig toetsenbordbedienbaar met zichtbare focusindicatoren en logische tabvolgorde.
- Publiceer voortgang, resultaatcount, nulresultaat en bronuitval via een programmatisch waarneembare aria-live-statusregio; verplaats de focus niet automatisch.
- Gebruik voldoende kleurcontrast en combineer kleur altijd met tekstuele statuslabels en iconen met toegankelijke namen.
- Geef resultaatkaarten een consistente koppenstructuur en beschrijvende linkteksten, inclusief bronnaam of bestemming.
- Zorg dat foutmeldingen naast kleur ook tekst bevatten en aan het zoekveld of de relevante actie gekoppeld zijn.
- Valideer met geautomatiseerde accessibilitytests voor toetsenbordfocus, naam/rol/waarde, contrast en statusberichten.

### Privacy
- Sla de zoekterm alleen op als dat noodzakelijk is voor de actieve zoekactie; bewaar geen zoekhistorie standaard.
- Toon alleen bronmetadata die voor historische ontdekking nodig is en beperk persoonsgegevens uit records tot de minimale context.
- Behandel privacystatus afzonderlijk van rechtenstatus en toon “Onbekend” wanneer privacybeoordeling ontbreekt.
- Kopieer of host geen scans of afbeeldingen lokaal; verwijs naar de externe bron en toon de externe rechten- en privacystatus.
- Log geen ruwe zoektermen of recordinhoud zonder duidelijk doel, passende grondslag en beperkte bewaartermijn.
- Gebruik stabiele identifiers en provenance voor herleidbaarheid, maar vermijd aanvullende profilering van bezoekers.
- Test dat API-fouten, logs en analytics geen onnodige persoonsgegevens of volledige ruwe responses opslaan.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige eigenaaractie. Er is wel overlap met reeds gepubliceerde adapter-, foutdiagnose- en resultaatkaartstories, maar dat blokkeert niet.
- **INFO · CONSISTENCY** — De kandidaat overlapt inhoudelijk met bestaande stories 74, 75, 82, 88 en 90. Behoud de scope expliciet als runtime-doorstroomfix en voorkom dubbel werk.

## Geaccepteerde storykandidaten

### Geldige Open Archieven-respons doorgeven aan publieke zoekroute

_Sleutel: `openarchieven-succespayload-doorstroom`_
_Bug: `BUG-2`_

Als bezoeker wil ik dat een geldige Open Archieven Search v1.1-respons als succesvolle bronrespons door de publieke zoekroute stroomt, zodat zoeken op “Heemskerk” niet ten onrechte eindigt in de generieke bronfoutstatus. Deze gerichte BUG-2-fix test en herstelt uitsluitend de runtime-doorstroom van een geldige adapterrespons naar de bestaande resultaat- en statuscontracten; configuratiepariteit, nieuwe bronnen en nieuwe resultaatvelden vallen buiten scope.

**Acceptatiecriteria**
- Een gecontroleerde Search v1.1-fixture met minimaal één geldig resultaat wordt in de publieke zoekroute geclassificeerd als geslaagde bronrespons en niet als bronfout.
- De bestaande resultaatkaart ontvangt de verplichte gemapte velden uit de geldige respons, inclusief bronnaam, gebeurtenisplaats, gebeurtenisdatum, stabiele identifier en permanente link; ontbrekende optionele velden blijven onbekend.
- Een geldige respons met nul resultaten wordt als nulresultaat geclassificeerd en niet als transport-, HTTP-, JSON- of mappingfout.
- Ongeldige, niet-JSON-, HTTP-fout- en transportresponses blijven hun bestaande afzonderlijke foutcategorie behouden.
- Geautomatiseerde contracttests dekken een geldige Heemskerk-respons, geldig nulresultaat en minimaal één ongeldige respons, en slagen in zowel productie- als acceptatieconfiguratie zonder handmatige stappen.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://www.openarchieven.nl/api/docs/records/search.php?lang=en](https://www.openarchieven.nl/api/docs/records/search.php?lang=en)

Afhankelijkheden: story:90, story:75 (herkend als bestaande stories: 90, 75)

Risico's: De actuele productierespons kan afwijken van de onderzochte Search v1.1-fixture, waardoor aanvullende contractmapping nodig is., Een wijziging in de succesclassificatie kan bestaande gedeeltelijke-uitval- of mappingfouten onbedoeld als succes tonen; regressietests moeten dit afvangen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
