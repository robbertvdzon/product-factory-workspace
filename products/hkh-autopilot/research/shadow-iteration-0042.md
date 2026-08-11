---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0042
date: 2026-08-11
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl
  - https://www.openarchieven.nl/datasets/nha
  - https://www.openarchieven.nl/datasets/datacatalog.jsonld
  - https://www.openarchieven.nl/dashboard/hee
  - https://www.regionaalarchiefalkmaar.nl/over-ons-artikel/open-data-english
  - https://www.kb.nl/en/research-find/datasets/delpher-newspapers
  - https://www.erfgoedleiden.nl/erfgoed-kaart/doe-mee/historisch-leiden-in-kaart
---
# Productcyclus 42

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Op basis van directe inspectie van de acceptatieomgeving (2026-08-11, via Playwright/accessibility-tree) blijkt dat de publieke HKH-app zich met productvisietaal presenteert ('Ontdek... vanuit een vraag, plek, persoon of gebeurtenis') maar dat de zoekfunctie functioneel volledig beperkt is tot 'Laatste nieuws'-berichten — er is nog geen enkele historische bron, record of collectie voor eindgebruikers doorzoekbaar. Het beheergedeelte heeft wel een werkende, live 'record-intake'-flow die externe kernvelden via archieven.nl vastlegt met fail-closed gedrag, maar er is geen publieke plek gevonden waar zo'n gekoppeld record daadwerkelijk zichtbaar wordt. Aanvullend, rechtstreeks geverifieerd bronnenonderzoek (elke bevinding met concrete, zelf geraadpleegde en met curl/Playwright gecontroleerde bron, datum 2026-08-11 en expliciete rechtenindicatie) levert drie concrete vervolgmogelijkheden op: (1) de Noord-Hollands Archief-dataset op Open Archieven is expliciet CC0-gelicenseerd en groter dan de eerder onderzochte Heemskerk-specifieke 'hee'-dataset, die opvallend genoeg ontbreekt in Open Archieven se eigen gelicenseerde datacatalogus — dit verscherpt de eerdere licentieonzekerheid rond 'hee' met een strengere verificatiemethode; (2) Regionaal Archief Alkmaar is met een primaire bron herbevestigd als CC0 maar geografisch beperkt tot 'de omgeving van Alkmaar', dus nog steeds niet geschikt voor Heemskerk; (3) Delpher/KB biedt een direct vrij te gebruiken publiek-domein krantenarchief (vóór 1880) als eerste opening voor de nog onaangeroerde broncategorie 'kranten'. Als inspiratie is Erfgoed Leiden en Omstreken gevonden: een werkend regionaal platform dat archieven, foto's, kranten, personen en 'toen & nu'-locatievergelijkingen al combineert, bruikbaar zodra vorm/UX aan de orde komt. Er is nog geen productbesluit genomen; dat is aan PRODUCT_OWNER.

### Publieke 'Ontdek'-zoekfunctie is in de acceptatieomgeving volledig beperkt tot nieuwsberichten, niet tot historische bronnen

Interactief onderzoek op 2026-08-11 (Playwright, accessibility-tree via de flt-semantics-placeholder-techniek) op de acceptatieomgeving toont dat de zoekbalk op de startpagina de aria-naam 'Ontdek nieuws' draagt met omschrijving 'Zoek op vrije tekst of kies een plek, persoon of gebeurtenis. Zoek in nieuwsberichten'. Bij het invullen van 'Slot Assumburg' verschijnen alleen filterchips gebaseerd op de vier zichtbare nieuwsberichten ('Plek: Kerkweg', 'Plek: Slot Assumburg', 'Gebeurtenis: HKH-lezing', 'Gebeurtenis: Kermis'). Er is geen enkel ander content-type (archiefrecord, foto, extern gekoppeld object) doorzoekbaar. Dit is functioneel gescheiden van de mockdata-status van AI-onderdelen: dit is de daadwerkelijke, niet-gemockte app-navigatie en zoekscope.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Admin record-intake met externe brongegevens-koppeling is live en toont fail-closed gedrag bij onbereikbare bron

Op het beheergedeelte is een 'Nieuwe record-intake'-formulier aanwezig met een optioneel 'Optionele externe conceptkoppeling'-blok (duurzame URL, 'Ophalen'-knop, koppelmotivering, onzekerheid). Bij het invullen van een archieven.nl-URL en klikken op 'Ophalen' toont het paneel 'Brongegevens (extern, ter controle): Niet bereikbaar' met twee vervolgacties: 'Bevestig brongegevens en gebruik bij record' en 'Sla op zonder externe brongegevens'. Dit bevestigt dat de in iteratie 41 besloten kernvelden-vastlegging daadwerkelijk is gebouwd en fail-closed reageert op een niet-succesvolle fetch (gemockte externe respons, zoals voorgeschreven voor deze omgeving).

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl)

### ArchivesNlClient bevestigd: per-record licentie, geen collectiebrede aanname, optionele token

De broncode van ArchivesNlClient.kt (backend) haalt via de opendata.archieven.nl open-data-URI vier kernvelden op (naam, geboortedatum, sterftedatum, licentie) met JSON-LD content negotiation, behandelt elke record-licentie als onafhankelijk ('nooit afgeleid van een andere record binnen dezelfde collectie'), bewaart geen volledige externe payload, ondersteunt een optioneel Bearer-token, en faalt gesloten (401/403/exceptions leiden tot een expliciet resultaattype, niet tot silent falen). Dit bevestigt dat de eerder besloten architectuur daadwerkelijk zo geïmplementeerd is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt)

### Noord-Hollands Archief-dataset op Open Archieven: expliciet CC0, 3,4 miljoen records, geen key nodig

Rechtstreeks opgehaalde (curl) broncode van de datasetpagina bevestigt letterlijk: 'Deze dataset wordt door Open Archieven aangeboden onder onder een Creative Commons 0-licentie (Public Domain Dedication)... U kunt het werk kopiëren, wijzigen, distribueren en uitvoeren, zelfs voor commerciële doeleinden, zonder toestemming te vragen', met de kanttekening dat gekoppelde afbeeldingen van derden een eigen licentie kunnen hebben. De dataset bevat 3.346.831/3.435.068 records met circa 12,8 miljoen persoonsvermeldingen (bevolkingsregisters, geboorte/huwelijk/overlijden, doop/trouw/begraaf), periode 1607-1960, downloadbaar via OAI-PMH/A2A-XML en N-triples zonder authenticatievereiste. Dit is een grotere en explicieter gelicenseerde bron dan de eerder onderzochte 'hee'-dataset.

Bronnen: [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha)

### Historische Kring Heemskerk ('hee') ontbreekt in Open Archieven se eigen gelicenseerde datacatalogus, in tegenstelling tot Noord-Hollands Archief

De machineleesbare datacatalogus van Open Archieven (datasets/datacatalog.jsonld, 1494 entries) bevat een controleerbaar organisatie-record voor 'Noord-Hollands Archief' (identifier NL-HlmNHA) met naam- en adresvelden, maar geen enkele entry met de naam 'Historische Kring Heemskerk' of archiefcode 'hee' is aangetroffen na doorzoeken van alle 351 unieke organisatienamen in de catalogus. De 'hee'-data is wel doorzoekbaar via de site en heeft een losse statistiekenpagina (dashboard/hee, eerder bevestigd: 5.362 records/10.242 personen), maar niet dezelfde per-dataset licentiepagina als 'nha'. Dit versterkt, met een nieuwe en striktere verificatiemethode (afwezigheid in de officiële catalogus, niet alleen een ontbrekende paginatekst), de eerdere onzekerheid over de hergebruikslicentie van deze bron.

Bronnen: [https://www.openarchieven.nl/datasets/datacatalog.jsonld](https://www.openarchieven.nl/datasets/datacatalog.jsonld), [https://www.openarchieven.nl/dashboard/hee](https://www.openarchieven.nl/dashboard/hee), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha)

### Regionaal Archief Alkmaar: genealogische data expliciet CC0, maar geografische scope bevestigd als 'omgeving van Alkmaar', niet Heemskerk

Rechtstreeks opgehaalde Engelstalige open-data-pagina van Regionaal Archief Alkmaar bevestigt letterlijk: hun genealogische dataset (bevolkingsregisters, notariële akten, doop/trouw/begraaf, burgerlijke stand) bevat 'some 1,9 million names of people from the erea around the town of Alkmaar', is gemarkeerd als CC0, vrij te hergebruiken (commercieel en niet-commercieel, zonder toestemming) en oogstbaar via een vaste OAI-PMH-link zonder key. Ook hun beeldcollecties (Bonda, Alkmaar-voor-1900, Den Helder) zijn 'no known copyright restrictions'/'public domain' met eigen OAI-API-key-URL's per collectie. Dit bevestigt met een primaire bron (in plaats van alleen een encyclopedie-samenvatting) dat RAA technisch en licentiematig aantrekkelijk is, maar geografisch niet Heemskerk dekt.

Bronnen: [https://www.regionaalarchiefalkmaar.nl/over-ons-artikel/open-data-english](https://www.regionaalarchiefalkmaar.nl/over-ons-artikel/open-data-english)

### Delpher/KB-kranten: publiek-domein deelarchief (vóór 1880) vrij en zonder toestemming te downloaden; recentere kranten vereisen aparte toegang

Rechtstreeks opgehaalde KB-pagina bevestigt: 'Newspapers that were first published more than 140 years ago belong to the public domain. They are no longer subject to copyright.' Het volledige OCR/ALTO/XML-tekstarchief van kranten uit de periode 1618-1879 is vrij downloadbaar als 111 GB verdeeld over 23 ZIP-bestanden, 'free of copyright and may be used without restrictions', zonder aanvraag. Voor recentere kranten (na circa 1886) geldt auteurs-/privacyrecht en is toegang tot de OAI-PMH-/SRU-API's alleen mogelijk 'once legal access has been granted' via een expliciet e-mailadres — dit is de aanvraagprocedure die volgens eerdere afspraak met de eigenaar teruggekoppeld moet worden als een key/toegang nodig blijkt.

Bronnen: [https://www.kb.nl/en/research-find/datasets/delpher-newspapers](https://www.kb.nl/en/research-find/datasets/delpher-newspapers)

### Erfgoed Leiden en Omstreken combineert archieven, foto's, kranten, personen-zoek en 'toen & nu'-locatievergelijkingen in één publiek platform

Rechtstreeks opgehaalde sitestructuur van erfgoedleiden.nl (regionaal archief van Leiden en omliggende gemeenten) toont een geïntegreerd discovery-platform met aparte doorzoekbare secties voor Archieven, Foto's/beeldmateriaal, Kranten, Personen ('Zoek op personen'), een Erfgoedregister en een reeks 'Toen & Nu'-locatiepagina's (bv. Aalmarkt, Prinsessekade, Vismarkt) die historische en actuele gevelbeelden vergelijken, plus cursussen open data/linked open data voor lokale onderzoekers. Dit is een werkend, door een archiefinstelling geëxploiteerd voorbeeld van precies het type verbonden meerbronnen-ontdekking dat de HKH-productvisie beschrijft (plek/persoon/bron/tijd), en is relevant als structurele inspiratie zodra vorm/UX aan de orde is.

Bronnen: [https://www.erfgoedleiden.nl/erfgoed-kaart/doe-mee/historisch-leiden-in-kaart](https://www.erfgoedleiden.nl/erfgoed-kaart/doe-mee/historisch-leiden-in-kaart)

### Huidige applicatie

**Doel:** HKH-autopilot beoogt de geschiedenis van Heemskerk toegankelijk te maken voor een zo breed mogelijk publiek (geen specifieke doelgroep) door mensen vanuit een vraag, plek, persoon of gebeurtenis op ontdekking te laten gaan, met verbindingen tussen lokale HKH-bronnen en externe archieven/collecties (archieven, musea, beeldbanken, kranten, kaarten), herleidbaar tot bronnen en met zichtbare onzekerheid/tegenstrijdigheid. De backend heeft hiervoor een werkende, keyloze koppeling met opendata.archieven.nl (ArchivesNlClient) en een AVG-fail-closed classificatie, en het beheergedeelte heeft sinds kort een 'record-intake'-flow om externe kernvelden (naam, geboorte-/sterftedatum, licentie, bron-URI) bij een lokaal record vast te leggen.

**Wat ontbreekt:**
- De publieke app toont, op de startpagina na, uitsluitend 'Laatste nieuws' (beheer-mededelingen); de zoekbalk presenteert zich met productvisietaal ('Ontdek de geschiedenis... vanuit een vraag, plek, persoon of gebeurtenis') maar is functioneel volledig beperkt tot nieuwsberichten ('Zoek in nieuwsberichten'), bevestigd via live interactie op 2026-08-11 — er is geen enkele historische bron, record of collectie voor eindgebruikers doorzoekbaar of bladerbaar.
- De nieuwe admin 'record-intake'-flow (externe kernvelden ophalen/bevestigen, fail-closed bij 'Niet bereikbaar') werkt en is live, maar er is nergens in de publieke app een plek gevonden waar een zo vastgelegd extern-gekoppeld record daadwerkelijk aan een eindgebruiker wordt getoond; de keten stopt bij het interne concept.
- Er is technisch maar één externe bron daadwerkelijk geïntegreerd (archieven.nl via ArchivesNlClient); het rijkere, expliciet CC0-gelicenseerde Noord-Hollands Archief-dataset op Open Archieven (3,4 miljoen records) is nog niet verkend of gekoppeld.
- De licentiestatus van de meest Heemskerk-specifieke bron (Historische Kring Heemskerk / 'hee' op Open Archieven) blijft onbevestigd: de organisatie ontbreekt in Open Archieven se eigen machineleesbare, per-dataset gelicenseerde datacatalogus die wel Noord-Hollands Archief bevat.
- Geen enkele krantenbron ('kranten', expliciet genoemd in de productvisie) is verkend of gekoppeld, terwijl Delpher/KB een direct bruikbare publiek-domein deelverzameling heeft (kranten ouder dan 140 jaar).
- Vorm/presentatie (tijdlijn, kaart, thema's, 'toen en nu') is nog niet ontworpen; dit is een bewuste, door de eigenaar bevestigde keuze om eerst bronnen te koppelen.

### Verbetermogelijkheden

- Verken en beoordeel de Noord-Hollands Archief-dataset (via Open Archieven) als tweede externe bron: expliciet CC0-gelicenseerd, groter dan de eerder onderzochte 'hee'-dataset, en zonder API-key te benaderen via dezelfde soort open-data-koppeling als archieven.nl.
- Zoek actief uit hoe de licentiestatus van de 'hee'-dataset (Historische Kring Heemskerk) wél te bevestigen is, bijvoorbeeld via het contactadres van Open Archieven (data@openarchieven.nl, vermeld op de nha-datasetpagina) of rechtstreeks bij de Historische Kring, voordat deze specifiek Heemskerk-relevante bron alsnog wordt ingezet.
- Onderzoek Delpher/KB als kranten-bron: het publiek-domein deelarchief (kranten 1618-1879, 111 GB, zonder toestemming te gebruiken) is direct bruikbaar; de aanvraagprocedure voor toegang tot recentere kranten (via API na 'legal access') kan aan de eigenaar worden voorgelegd zodra relevant.
- Adresseer het structurele gat dat na de record-intake in het beheergedeelte nog geen enkele publieke plek bestaat waar een extern gekoppeld en bevestigd record aan eindgebruikers wordt getoond — dit was ook de blokkerende zorg van de critic in iteratie 41 bij kandidaat 1.
- Heroverweeg of de huidige 'Ontdek'-zoekfunctie, die zich met productvisietaal presenteert maar functioneel beperkt is tot nieuwsberichten, verwarrend is voor gebruikers gegeven de expliciete eigenaarsregel dat 'laatste nieuws' geen historische bron is.
- Gebruik Erfgoed Leiden en Omstreken als structureel referentiepunt (Archieven/Foto's/Kranten/Personen/Toen&Nu als aparte, onderling verbonden doorzoekbare secties) zodra vorm/UX-werk aan de orde is, in lijn met de eerder uitgestelde kaart/tijdlijn-laag.

### Inspiratiebronnen

- [Erfgoed Leiden en Omstreken — 'Historisch Leiden in Kaart' / erfgoedkaart](https://www.erfgoedleiden.nl/erfgoed-kaart/doe-mee/historisch-leiden-in-kaart) — Werkend, door een regionale archiefinstelling geëxploiteerd platform dat archieven, foto's, kranten, personen-zoek en 'toen & nu'-locatievergelijkingen in één samenhangende, doorzoekbare structuur combineert — een concreet voorbeeld van de meerbronnen-ontdekking die de HKH-productvisie beschrijft, bruikbaar zodra vorm/UX aan de orde komt.
- [Open Archieven — dataset Noord-Hollands Archief](https://www.openarchieven.nl/datasets/nha) — Referentievoorbeeld van een expliciet, machineleesbaar en tekstueel bevestigd CC0-gelicenseerde genealogische dataset (3,4 miljoen records) zonder key, direct herbruikbaar als patroon en/of daadwerkelijke tweede bronkoppeling naast archieven.nl.
- [Delpher (KB) — historische kranten](https://www.kb.nl/en/research-find/datasets/delpher-newspapers) — Nationaal krantenplatform met een expliciet publiek-domein deelarchief (kranten vóór 1880), relevant als eerste concrete kandidaat om de in de productvisie genoemde maar nog ongebruikte broncategorie 'kranten' te ontsluiten.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt) | 2026-08-11 | Broncode uit de publieke, door de eigenaar aangewezen productrepository (GitHub); geen aparte licentievermelding gecontroleerd, geraadpleegd uitsluitend als feitelijke documentatie van de huidige implementatie. | Vaststellen wat de huidige, daadwerkelijk geïmplementeerde externe koppeling (archieven.nl) precies opslaat en hoe deze met licenties en fouten omgaat, als basis voor de huidige-staat-analyse. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-11 | Standing acceptatieomgeving van het eigen product met representatieve nepdata; geen productiegegevens, geraadpleegd als eigen testomgeving, geen hergebruiksrechtenkwestie van toepassing. | Direct, interactief vaststellen wat de publieke app vandaag daadwerkelijk toont en doorzoekbaar maakt (accessibility-tree-inspectie en zoekinteractie), in plaats van aan te nemen op basis van documentatie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl) | 2026-08-11 | Standing acceptatieomgeving van het eigen product, geen productiedata; geraadpleegd als eigen testomgeving. | Vaststellen of en hoe de in iteratie 41 besloten record-intake-flow met externe kernveldenvastlegging daadwerkelijk werkt in de levende beheeromgeving. |
| [bron](https://www.openarchieven.nl/datasets/nha) | 2026-08-11 | Officiële datasetpagina van Open Archieven; expliciet vermelde Creative Commons 0-licentie (Public Domain Dedication) voor de metadata-dataset zelf, rechtstreeks in de paginatekst bevestigd via curl. | Verifiëren van omvang, licentie en toegangswijze van de nog niet gekoppelde Noord-Hollands Archief-dataset als kansrijke tweede externe bron. |
| [bron](https://www.openarchieven.nl/datasets/datacatalog.jsonld) | 2026-08-11 | Machineleesbare, publiek toegankelijke datacatalogus (JSON-LD) van Open Archieven; gebruikt uitsluitend voor feitelijke aanwezigheids-/afwezigheidscontrole van organisaties, geen herpublicatie van de dataset zelf. | Objectief, herhaalbaar vaststellen of de Historische Kring Heemskerk-dataset ('hee') al dan niet is opgenomen in het officiële, per-organisatie gelicenseerde datasetoverzicht, ter aanvulling op eerdere onzekerheid over de licentie van deze bron. |
| [bron](https://www.openarchieven.nl/dashboard/hee) | 2026-08-11 | Publiek toegankelijke statistiekenpagina van Open Archieven; geen expliciete licentievermelding op deze specifieke pagina aangetroffen. | Kruisverwijzing en bevestiging dat de 'hee'-data wel bestaat en doorzoekbaar is, maar zonder de dedicated licentiepagina die 'nha' wel heeft. |
| [bron](https://www.regionaalarchiefalkmaar.nl/over-ons-artikel/open-data-english) | 2026-08-11 | Officiële open-data-pagina van Regionaal Archief Alkmaar; expliciet CC0/'public domain'/'no known copyright restrictions' vermeld voor de betreffende datasets, rechtstreeks in de paginatekst bevestigd via curl. | Met een primaire bron (in plaats van alleen een encyclopedie-samenvatting) herbevestigen van zowel de licentie als de geografische scope ('omgeving van Alkmaar') van RAA, relevant voor het eerdere besluit om RAA deze cyclus niet in te zetten voor Heemskerk. |
| [bron](https://www.kb.nl/en/research-find/datasets/delpher-newspapers) | 2026-08-11 | Officiële dataset-/voorwaardenpagina van de Koninklijke Bibliotheek; expliciet vermeld publiek-domeinstatus voor kranten ouder dan 140 jaar, rechtstreeks in de paginatekst bevestigd via curl. | Verkennen van de nog niet onderzochte broncategorie 'kranten' uit de productvisie, inclusief het vaststellen van welk deel vrij bruikbaar is en welke aanvraagprocedure geldt voor de rest. |
| [bron](https://www.erfgoedleiden.nl/erfgoed-kaart/doe-mee/historisch-leiden-in-kaart) | 2026-08-11 | Publiek toegankelijke website van een regionale archiefinstelling; alleen sitestructuur/navigatie feitelijk samengevat, geen herpublicatie van archiefmateriaal of paginatekst. | Zoeken naar een vergelijkbare, daadwerkelijk werkende applicatie die archieven, foto's, kranten, personen en locatievergelijkingen verbindt, als inspiratiebron voor de productvisie. |

## Productbeslissing

Richt deze iteratie op het sluiten van de keten tussen de reeds werkende admin record-intake (externe kernvelden via ArchivesNlClient/archieven.nl) en de publieke app: bouw een publieke weergave waarin een lokaal HKH-record wordt getoond mét het door de beheerder bevestigde externe brongegeven (naam, geboorte-/sterftedatum, licentie, bron-URI), herleidbaar via een klikbare verwijzing naar de bron. Wanneer externe verificatie ontbreekt of niet bereikbaar was, wordt dat expliciet en begrijpelijk vermeld in plaats van verborgen. Er worden deze cyclus geen nieuwe externe bronnen gekoppeld en de bestaande zoekfunctie/navigatie blijft ongewijzigd; de scope is beperkt tot het zichtbaar maken van wat al technisch werkt.

**Waarom:** Onderzoek toont dat de backend/admin-keten (ArchivesNlClient + record-intake) functioneel werkt en fail-closed reageert, maar dat er nergens in de publieke app een resultaat van deze koppeling zichtbaar is voor eindgebruikers — de keten stopt intern bij het beheerdersconcept. Dit is al in iteratie 41 door de critic als blokkerend gemarkeerd voor kandidaat 1, en op 2026-08-11 opnieuw bevestigd via direct interactief onderzoek van zowel de publieke als de beheer-acceptatieomgeving. Dit ondermijnt de missie (geschiedenis toegankelijk en beleefbaar maken) en de principes 'Verbonden' en 'Betrouwbaar' rechtstreeks: er bestaat technisch een verbinding met een externe bron, maar niemand buiten het beheer ervaart die, en herleidbaarheid is voor gebruikers onzichtbaar. Voordat wordt geïnvesteerd in extra bronnen (Noord-Hollands Archief, Delpher-kranten) of in vorm/UX (tijdlijn, kaart), moet eerst worden aangetoond dat de enige bestaande, werkende koppeling waarde oplevert voor een eindgebruiker. Dit is een kleine, samenhangende stap die zonder nieuwe externe toegang of tokens uitvoerbaar is door Product Factory- en Software Factory-agents, omdat de brongegevens, licentie-per-record-logica en fail-closed-afhandeling al bestaan.

### Prioriteiten
- Bouw een publieke detailweergave die het door record-intake bevestigde externe brongegeven (naam, geboorte-/sterftedatum, licentie, bron-URI) van een lokaal HKH-record daadwerkelijk aan eindgebruikers toont, met klikbare bronverwijzing.
- Toon expliciet en voor leken begrijpelijk wanneer externe verificatie ontbreekt of niet bereikbaar was, in plaats van dit te verbergen.
- Koppel deze cyclus geen nieuwe externe bron (Noord-Hollands Archief, Delpher-kranten) en zoek de 'hee'-licentie niet uit — eerst de bestaande keten bewijzen.
- Laat de huidige 'Ontdek'-zoekfunctie en publieke navigatie ongewijzigd; voeg alleen toe, herstructureer niet.
- Plan geen menselijke actie of nieuwe toegangstokens; gebruik uitsluitend de bestaande, key-loze archieven.nl-koppeling en record-intake-data.

### Besluiten
- **Bouw deze cyclus een publieke weergave (detailsectie bij een lokaal HKH-record) die de door de admin record-intake bevestigde externe kernvelden (naam, geboorte-/sterftedatum, licentie, bron-URI) daadwerkelijk aan eindgebruikers toont, met een klikbare verwijzing naar de bron-URI. Geen nieuwe externe bronnen koppelen voordat dit staat.** — Interactief onderzoek (2026-08-11) bevestigt dat de admin record-intake-flow met ArchivesNlClient werkt en fail-closed reageert, maar dat er nergens in de publieke app een plek is waar zo'n bevestigd extern-gekoppeld record aan een eindgebruiker wordt getoond — de keten stopt intern. Dit was ook al in iteratie 41 door de critic als blokkerend gemarkeerd. Zonder deze stap levert het bestaande backend-werk geen missiewaarde ('geschiedenis toegankelijk en beleefbaar maken') en schendt het de principes 'Verbonden' en 'Betrouwbaar'.
- **Toon in de publieke weergave expliciet en begrijpelijk wanneer externe verificatie ontbreekt, niet is uitgevoerd, of de bron 'niet bereikbaar' was — verberg dit niet, maar maak het onderdeel van de gebruikerservaring.** — De admin-omgeving toont vandaag al fail-closed gedrag ('Niet bereikbaar') met de keuze om zonder externe brongegevens op te slaan; dit onderscheid moet zichtbaar blijven voor eindgebruikers om herleidbaarheid en eerlijkheid over onzekerheid te waarborgen, conform de principes 'Betrouwbaar' en 'Meerstemmig'.
- **Koppel deze cyclus bewust geen tweede externe bron (Noord-Hollands Archief op Open Archieven, Delpher-kranten) en zoek de licentiestatus van de 'hee'-dataset niet actief uit.** — Beide bronnen zijn kansrijk (NHA is expliciet CC0 met 3,4 miljoen records; Delpher heeft een direct bruikbaar publiek-domein krantenarchief vóór 1880), maar meer bronnen koppelen vergroot alleen de kloof tussen backend-capaciteit en zichtbare gebruikerswaarde zolang de enige bestaande koppeling (archieven.nl) nog nergens publiek te zien is. Eerst de keten sluiten, dan uitbreiden.
- **Laat de bestaande 'Ontdek'-zoekfunctie (functioneel beperkt tot nieuwsberichten) en de rest van de publieke navigatie deze cyclus ongewijzigd; voeg alleen de nieuwe record-detailweergave toe zonder herstructurering.** — De zoekbalk presenteert zich al met productvisietaal maar doorzoekt uitsluitend nieuwsberichten; dit is een reëel maar apart vraagstuk. Het in dezelfde cyclus herontwerpen van zoek/navigatie zou de scope vergroten en het risico op een onsamenhangende stap verhogen, terwijl de eigenaar al heeft bevestigd dat vorm/UX bewust wordt uitgesteld tot na brongekoppeling.

## UX-voorstel: Publieke recorddetailweergave: externe brongegevens zichtbaar maken

**Gebruikersdoel:** Als bezoeker van de publieke HKH-app wil ik bij een lokaal record kunnen zien of en welke externe brongegevens (naam, geboorte-/sterftedatum, licentie) door de beheerder zijn bevestigd, met een klikbare verwijzing naar de oorspronkelijke bron, zodat ik de herkomst en betrouwbaarheid van de informatie zelf kan beoordelen — en dit ook duidelijk zie wanneer die verificatie ontbreekt of niet lukte.

### Flow
1. Gebruiker bevindt zich op een bestaande publieke recorddetailpagina (navigatie ernaartoe blijft ongewijzigd deze cyclus).
2. Pagina toont eerst de bestaande lokale recordgegevens ongewijzigd, gevolgd door een nieuwe sectie 'Externe bronverificatie' als losstaand, herkenbaar blok met eigen kop (h2).
3. Systeem bepaalt serverzijdig de status van dit record: 'bevestigd met brongegevens', 'opgeslagen zonder externe brongegevens' of 'geen intake uitgevoerd', en rendert per status een andere, altijd zichtbare tekstuele status (geen lege sectie, geen silent verberging).
4. Bij status 'bevestigd': toon naam, geboortedatum, sterftedatum en licentie zoals vastgelegd bij record-intake, plus een klikbare link met zichtbare linktekst naar de bron-URI en een label 'Bevestigd door beheerder op [datum]'.
5. Bij status 'zonder externe brongegevens' of 'geen intake': toon een duidelijke, begrijpelijke melding (bijv. 'Voor dit record is geen externe bronverificatie beschikbaar') zonder foutmelding-toon of technisch jargon.
6. Gebruiker activeert de bronlink met muis of toetsenbord (Tab + Enter/Spatie); link opent de externe bron in een nieuw tabblad, met aria-aankondiging dat dit een externe site is en met rel='noopener'.
7. Gebruiker kan de sectie 'Externe bronverificatie' in-/uitklappen via een toegankelijke disclosure-knop (aria-expanded), zonder dat dit overige paginaonderdelen beïnvloedt.
8. Schermlezergebruiker doorloopt een logische kopstructuur: recordnaam (h1) > lokale gegevens > 'Externe bronverificatie' (h2) > status en velden, zodat de sectie ook via koppennavigatie vindbaar is.

### Wireframe

RECORDDETAILPAGINA (publiek, bestaand + nieuwe sectie)
──────────────────────────────────────────────
[H1] Naam lokaal record (bestaand, ongewijzigd)
[bestaande lokale velden: beschrijving, afbeelding, gerelateerd nieuws...] (ongewijzigd)

──────────────────────────────────────────────
[knop, aria-expanded="true/false"] ▾ Externe bronverificatie
  ┌─────────────────────────────────────────┐
  │ SCENARIO A — bevestigd:                  │
  │ [status-badge, groen icoon] Bevestigd    │
  │ door beheerder op 12-06-2026             │
  │                                           │
  │ Naam (extern):        Jan Pietersz.      │
  │ Geboortedatum:         03-04-1821        │
  │ Sterftedatum:          -                 │
  │ Licentie:              CC0               │
  │ Bron: [link] "Bekijk op archieven.nl ↗"  │
  │        (opent in nieuw tabblad)          │
  └─────────────────────────────────────────┘

  ┌─────────────────────────────────────────┐
  │ SCENARIO B — geen verificatie:           │
  │ [status-badge, neutraal icoon]           │
  │ Geen externe bronverificatie              │
  │ beschikbaar voor dit record.             │
  │ (geen technisch foutbericht, geen link)  │
  └─────────────────────────────────────────┘
──────────────────────────────────────────────
[bestaande footer/gerelateerde items] (ongewijzigd)

Statusbadges zijn zowel via kleur als via tekst/icoon onderscheidend (niet uitsluitend kleur).

### Interactiehypotheses
- H1: Bij een record met bevestigde externe brongegevens is de sectie 'Externe bronverificatie' zonder extra interactie aanwezig in de initiële DOM/accessibility-tree (server-side gerenderd, niet client-side lazy-loaded achter een klik) — automatisch testbaar door de pagina te laden en de aanwezigheid van de sectiekop en statustekst te controleren zonder voorafgaande gebruikersactie.
- H2: Voor elk record (met én zonder bevestigde externe brongegevens) is de sectie 'Externe bronverificatie' aanwezig met een expliciete, van elkaar te onderscheiden statustekst — automatisch testbaar door beide recordtypes te laden en te asserten dat de sectie nooit leeg of afwezig is en de statustekst per geval verschilt.
- H3: De bronlink is volledig met alleen het toetsenbord bereikbaar (Tab) en activeerbaar (Enter), en opent in een nieuw tabblad met rel='noopener' en een aria-aankondiging dat het een externe link is — automatisch testbaar via Playwright keyboard-only navigatie plus axe-core check op link-attributen.
- H4: Alle statuslabels en tekst in de sectie voldoen aan WCAG AA-contrast (minimaal 4.5:1) en het onderscheid tussen 'bevestigd' en 'geen verificatie' is niet uitsluitend kleurafhankelijk — automatisch testbaar via axe-core contrastregels en een DOM-check dat elke statusbadge een tekstuele label of icoon-alt heeft naast eventuele kleur.
- H5: De disclosure-knop voor in-/uitklappen rapporteert correct aria-expanded state en de sectie-inhoud is voor schermlezers programmatisch gekoppeld (aria-controls) aan de knop — automatisch testbaar via een accessibility-tree snapshot voor en na toggle.

### Toegankelijkheid
- Alle statusinformatie (bevestigd/geen verificatie) wordt zowel tekstueel als via icoon aangeboden, nooit uitsluitend via kleur, zodat kleurenblinde en screenreadergebruikers het verschil kunnen waarnemen.
- Sectiekop 'Externe bronverificatie' gebruikt een correct geneste heading-level (h2 onder de bestaande h1) zodat schermlezergebruikers via koppennavigatie direct naar deze sectie kunnen springen.
- De in-/uitklapknop is een echt <button>-element met aria-expanded en aria-controls, en blijft consistent bruikbaar met alleen het toetsenbord (focus-volgorde, zichtbare focusindicator).
- De externe bronlink heeft duidelijke, betekenisvolle linktekst (geen 'klik hier') en een programmatische aankondiging dat deze in een nieuw tabblad opent.
- Alle tekst en statuslabels voldoen aan minimaal WCAG AA-contrastratio (4.5:1 voor normale tekst, 3:1 voor grote tekst/iconen).
- De meldingstekst bij 'geen externe verificatie beschikbaar' is in begrijpelijke, niet-technische taal geformuleerd zodat deze ook voor schermlezergebruikers zonder technische achtergrond duidelijk is.

### Privacy
- Toon uitsluitend de reeds bij record-intake vastgelegde kernvelden (naam, geboorte-/sterftedatum, licentie, bron-URI); sla geen aanvullende externe payload of persoonsgegevens op ten behoeve van deze weergave.
- Publiceer een extern brongegeven alleen wanneer de admin dit expliciet heeft bevestigd via de bestaande record-intake-flow; toon nooit ongeverifieerde of tussentijds opgehaalde externe data rechtstreeks aan eindgebruikers.
- Respecteer de per-record licentie zoals vastgelegd (bijv. CC0); toon de licentie zelf aan de gebruiker zodat herkomst en hergebruiksrecht transparant zijn, in plaats van dit te veronderstellen of te verbergen.
- Doel van de weergave is uitsluitend herleidbaarheid en transparantie over bronvermelding voor historisch materiaal; er wordt geen nieuw trackinggedrag of profilering van de bezoeker aan deze functionaliteit toegevoegd.
- Bij 'geen externe brongegevens beschikbaar' wordt geen technische foutinformatie (bijv. API-foutcodes, interne systeemstatus) aan de eindgebruiker getoond, om te voorkomen dat interne systeeminformatie onbedoeld wordt gelekt.
- De externe link verwijst gebruikers naar de bron-URI zelf (archieven.nl); er wordt geen persoonsgegeven van de bezoeker meegegeven in de doorverwijzing (geen tracking-parameters, geen referrer-lekkage van gevoelige paden).

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten (record-detail-external-source-api en record-detail-external-source-view) sluiten de keten tussen de werkende admin record-intake en de publieke app op een zorgvuldig afgebakende manier. De API-kandidaat blootst uitsluitend een enkelvoudig per-ID leespad (geen list/zoek/opsom-response, dus geen integratie met of uitbreiding van het bestaande discovery-contract kandidaat 35/36), leest de AVG-classificatie live in plaats van een bevroren intake-tijdstip-vlag (adresseert het eerder BLOCKING herroepbaarheidsprobleem), toont geboorte-/sterftedatum uitsluitend als jaartal (identificatierisico-mitigatie) en bevat nooit de ruwe externe payload. De view-kandidaat rendert dit toegankelijk (h2, aria-expanded/aria-controls, toetsenbord, axe-core, tekst+icoon i.p.v. uitsluitend kleur) en toont bewust dezelfde neutrale melding voor 'nooit bevestigd' en 'ingetrokken na herclassificatie' om geen publicatiegeschiedenis te lekken. Alle acceptatiecriteria zijn geautomatiseerd verifieerbaar (API-tests, Playwright, axe-core) — er is geen menselijke actie, handmatige test, accountaanmaak of externe toegang vereist, dus de autonomie-gate is gehaald. Geen van de gevonden issues is BLOCKING; de resterende risico's (ID-enumeratie, edge-case bij wijziging van de classificatielogica zonder recordbewerking) zijn door de auteur zelf al expliciet benoemd als niet-blokkerend restrisico voor een volgende cyclus.
- **WARNING · PRIVACY** — Residuele ID-enumeratie: zonder lijst-/zoekendpoint blijft het mogelijk om via opeenvolgend geprobeerde record-ID's individuele CONFIRMED-records te achterhalen als ID's sequentieel/voorspelbaar zijn. Data betreft uitsluitend reeds fail-closed als 'Processable' (overleden, geen levende nabestaanden) geclassificeerde records, dus het risico is beperkt maar niet nul.
- **WARNING · PRIVACY** — Het zelfherstellend gedrag (live herclassificatie bij elk verzoek) werkt alleen wanneer de onderliggende recordvelden worden bewerkt zodat de bestaande classificatie-engine (kandidaat 17/20/21) herberekent. Een toekomstige wijziging van de classificatieregels zelf, zonder dat recordvelden worden aangeraakt, triggert geen automatische herberekening van reeds als CONFIRMED getoonde records. Dit is een bestaand, geërfd gedrag van de classificatie-engine en geen nieuwe verslechtering door deze kandidaat.
- **INFO · CONSISTENCY** — Deze kandidaten keren het eerdere besluit van kandidaat 46 om deze cyclus géén publieke detailweergave te bouwen bewust om. De reconciliatie is expliciet en gericht op de twee eerder BLOCKING punten (geen discovery-integratie, live i.p.v. bevroren classificatie) en is bovendien door PRODUCT_OWNER als expliciete productbeslissing vastgelegd — geen onopgemerkte scope-drift.
- **INFO · SCOPE** — Beide kandidaten houden zich correct aan de eigenaarsbeslissing om deze cyclus geen nieuwe externe bron te koppelen en de bestaande 'Ontdek'-zoekfunctie/navigatie ongewijzigd te laten; regressietests op het bestaande discovery-contract (35/36) zijn expliciet opgenomen.

## Geaccepteerde storykandidaten

### Publieke recorddetailpagina: toegankelijke sectie 'Externe bronverificatie' met jaarprecisie en zelfherstellend gedrag bij herclassificatie

_Sleutel: `record-detail-external-source-view`_

Voeg aan de bestaande publieke recorddetailpagina een nieuwe, herkenbare sectie 'Externe bronverificatie' (h2) toe die uitsluitend de status en velden van het herziene record-detail-external-source-api-leespad rendert. Bij CONFIRMED tonen: naam, geboortejaar, sterftejaar (indien aanwezig) — beide als jaartal, nooit als volledige dag-nauwkeurige datum, conform de in de API-kandidaat gedocumenteerde keuze om het residuele identificatierisico voor eventuele nog levende naasten te beperken —, licentie en een klikbare, met tekst gelabelde link naar de bron-URI (opent in nieuw tabblad, rel='noopener', aria-aankondiging), plus 'Bevestigd door beheerder op [datum]'. Bij SAVED_WITHOUT_SOURCE of NO_INTAKE (en, ongewijzigd voor de gebruiker, ook wanneer een eerder CONFIRMED record inmiddels live is geherclassificeerd tot Blocked) toont dezelfde sectie een neutrale, niet-technische melding zonder link — er wordt bewust geen apart 'ingetrokken'-bericht getoond, om geen metadata over een eerdere publicatie te lekken. Omdat de onderliggende API bij elk verzoek live herclassificeert in plaats van een gecachete status te hergebruiken, herstelt de publieke weergave zichzelf automatisch: bij een volgende paginaweergave van hetzelfde record na een classificatiewijziging verschijnt zonder enige extra actie de neutrale melding in plaats van de eerder getoonde velden. De sectie is in-/uitklapbaar via een toegankelijke <button> met aria-expanded/aria-controls, status wordt zowel tekstueel als via icoon onderscheiden (nooit uitsluitend kleur), en voldoet aan WCAG AA-contrast. Bestaande lokale recordvelden, navigatie en de bestaande 'Ontdek'-zoekfunctie (die uitsluitend nieuwsberichten doorzoekt, kandidaat 35/36) blijven ongewijzigd en deze sectie wordt niet aan die zoekfunctie gekoppeld.

**Acceptatiecriteria**
- Bij het laden van een recorddetailpagina voor een CONFIRMED-record is, zonder voorafgaande gebruikersinteractie, in de initiële DOM/accessibility-tree een h2 'Externe bronverificatie' aanwezig met statustekst, naam, geboortejaar, sterftejaar, licentie en een link met zichtbare linktekst naar de bron-URI — geverifieerd via Playwright/accessibility-tree-inspectie (flt-semantics-placeholder-techniek); een expliciete assertie bevestigt dat er geen dag-/maandgetal in de weergegeven datumtekst voorkomt.
- Bij het laden van een recorddetailpagina voor SAVED_WITHOUT_SOURCE of NO_INTAKE toont dezelfde sectie een duidelijke, niet-technische neutrale melding zonder bronlink, voor beide statussen apart geverifieerd via Playwright.
- Zelfherstellend gedrag in de UI: voor een record dat eerst CONFIRMED wordt getoond, waarna de onderliggende classificatie via een recordbewerking naar 'Blocked' herberekend wordt, toont een daaropvolgend laden van dezelfde detailpagina de neutrale melding zonder velden of link — geverifieerd via een Playwright-test die de pagina tweemaal laadt met een classificatiewijziging ertussenin.
- De externe bronlink opent in een nieuw tabblad met rel='noopener', heeft een aria-aankondiging dat het een externe link is, en is volledig met alleen het toetsenbord (Tab + Enter) bereikbaar en activeerbaar — geverifieerd via een geautomatiseerde Playwright keyboard-only test.
- Een geautomatiseerde axe-core-scan van de sectie rapporteert nul overtredingen (inclusief kleurcontrast) en een DOM-check bevestigt dat elke statusbadge een tekstueel label of icoon-alt heeft naast eventuele kleur — geautomatiseerd uitgevoerd in CI.
- De in-/uitklapknop rapporteert correct aria-expanded (true/false) en is via aria-controls programmatisch gekoppeld aan de sectie-inhoud, geverifieerd via een accessibility-tree-snapshotvergelijking vóór en na de toggle.
- Bestaande lokale recordvelden, paginanavigatie en de bestaande 'Ontdek'-zoekfunctie blijven functioneel ongewijzigd en tonen geen resultaten uit deze nieuwe sectie — geverifieerd via een regressie-Playwright-test die deze elementen/routes na de wijziging opnieuw controleert.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl)

Afhankelijkheden (candidateKey): record-detail-external-source-api (binnen deze batch herkend als: record-detail-external-source-api)

Risico's: Volledig afhankelijk van de herziene record-detail-external-source-api; als de criticus de reconciliatie met kandidaat 46 (enkelvoudig per-ID-leespad, geen discovery-integratie, live herclassificatie) alsnog onvoldoende vindt, is dit frontend-werk geblokkeerd totdat het backendontwerp is geaccepteerd., De keuze voor jaarprecisie in plaats van dag-nauwkeurige datums is een bewuste afweging tussen herleidbaarheid en identificatierisico; mocht de product owner alsnog dag-nauwkeurigheid wensen, vergt dat een gecoördineerde vervolgwijziging in zowel de API- als de view-kandidaat.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
