---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0021
date: 2026-08-08
status: approved
sources:
  - https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens
  - https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen
  - https://opendata.archieven.nl/nl/over-open-data
  - https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210
  - https://www.historischekringheemskerk.nl/cgi-bin/bidprent.pl
  - https://www.historischekringheemskerk.nl/organisatie/beleidsplan/
  - https://datasetregister.netwerkdigitaalerfgoed.nl/faq-ontwikkelaars.php
---
# Productcyclus 21

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoeksvraag deze iteratie: bestaat er een reëel, gedocumenteerd autorisatievrij (of tenminste deterministisch te configureren) extern toegangspad voor het verificatie-anker buiten HKH, én een vaste, citeerbare juridische regel waarmee automatisch — zonder ad-hoc mensenoordeel — kan worden vastgesteld of een lokaal record (met name bidprentjes/genealogische gegevens) onder de AVG valt? Dit volgt direct uit de blokkerende kritiekpunten van iteratie 16 over een niet-onderbouwd JWT-/autorisatieprofiel en het ontbreken van een gesloten privacybeleid voor grondslagbepaling.\n\nBevindingen: (1) Voor het externe deel is er goed nieuws — archieven.nl/Noord-Hollands Archief biedt een gedocumenteerde, niet-geauthenticeerde machine-toegangs-API (resolvebare URI's met content-negotiation, periodieke harvesting) zonder dat een HKH-specifiek tokenprotocol nodig is, al kon een expliciete CC0-vermelding op de specifieke Heemskerk-archieftoegangspagina dit keer niet worden herbevestigd. (2) Voor de juridische grondslagvraag is er een citeerbare, deterministische regel: de AVG is volgens de Autoriteit Persoonsgegevens en Overweging 27 AVG niet van toepassing op gegevens van overleden personen — dit kan als vast beslispunt dienen voor bidprentjes van overleden personen, mits het record geen identificeerbare gegevens van nog levende nabestaanden bevat. (3) Voor de intake van HKH's eigen lokale records blijft er geen publiek, machinaal toegankelijk kanaal: beeldbank, archief, bidprentjes en zelfs de eigen privacybeleidspagina van HKH gaven vandaag (2026-08-08) opnieuw 403/blokkeringsfouten. HKH heeft wel sinds 2018 een formeel privacyreglement, maar de concrete clausules zijn niet extern te verifiëren — dit blijft dus een eigenaarsafhankelijke input die niet uit publieke bronnen kan worden afgeleid. Conclusie: het externe-ankerprobleem en een deel van het privacy-beslisprobleem (overledenen) zijn nu onderbouwd met echte, citeerbare bronnen; de intake-autorisatie voor HKH's eigen collectie en de exacte HKH-privacyclausules blijven onopgeloste, eigenaarsafhankelijke afhankelijkheden.

### AVG is expliciet niet van toepassing op persoonsgegevens van overleden personen (Overweging 27 AVG)

De officiële informatiepagina van de Autoriteit Persoonsgegevens bevestigt dat de AVG uitsluitend geldt voor gegevens van 'levende natuurlijke personen'; gegevens van overledenen vallen buiten de reikwijdte. Dit wordt onderbouwd met een concreet citeerbaar rechtsgrond: Overweging 27 AVG ('De onderhavige verordening is niet van toepassing op de persoonsgegevens van overleden personen'), zoals aangehaald in een bericht over een Kamervraag-antwoord van de minister. Wel blijft zorgvuldigheid geboden: gegevens van nog levende nabestaanden die in hetzelfde record voorkomen vallen wél onder de AVG, en biometrische gegevens/lichamelijke integriteit van overledenen genieten aparte grondwettelijke bescherming los van de AVG.

Bronnen: [https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens](https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens), [https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen](https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen)

### Noord-Hollands Archief/archieven.nl biedt een echt gedocumenteerd, autorisatievrij machine-toegangspad

Het open-datplatform van archieven.nl (waaronder data van het Noord-Hollands Archief) beschrijft een concreet, niet-geauthenticeerd technisch toegangspad: resolvebare URI's volgens het patroon http://opendata.archieven.nl/id/<adtid>/<guid> met content-negotiation naar N-Triples, Turtle, RDF/XML en JSON-LD, plus periodieke harvesting (EAD-bestanden dagelijks, Dublin Core/A2A/RDF wekelijks gegenereerd). Hergebruik wordt toegestaan onder Creative Commons-voorwaarden, al is per dataset niet altijd duidelijk of naamsvermelding verplicht is. Dit is een reëel alternatief voor het eerder gevraagde maar onbestaande HKH-specifieke JWT-/tokenprofiel: voor het externe verificatie-anker (Heemskerk-archieftoegang bij NHA) is geen eigenaarsafhankelijk autorisatiebeleid nodig, alleen voor de intake van het HKH-eigen lokale record.

Bronnen: [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

### Licentievermelding op de specifieke Heemskerk-archieftoegangspagina kon dit keer niet worden herbevestigd

Bij herraadpleging van de eerder aangehaalde archieftoegangspagina 'Ambachts- en Gemeentebestuur van Heemskerk' (inv.nr. 1032) was op de zichtbare pagina-inhoud geen expliciete CC0- of andere licentievermelding aanwezig; de pagina fungeert vooral als introductie/toegangspunt naar de archieftoegang, niet als individuele stukbeschrijving met zichtbare rechtenlabel. De eerdere aanname dat deze specifieke pagina CC0 vermeldt, kon deze sessie niet worden gereproduceerd en moet dus per paginaniveau opnieuw geverifieerd worden in plaats van generiek te worden aangenomen voor de hele collectie.

Bronnen: [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210)

### HKH's eigen systemen blijven vandaag geblokkeerd voor geautomatiseerde toegang, inclusief het beleidsplan

Herhaalde raadpleging op 2026-08-08 bevestigt dat de beeldbank-, archief- en bidprentjes-cgi-scripts van HKH nog steeds 'geen toegang'/403-foutmeldingen geven bij geautomatiseerde verzoeken (zichtbaar o.a. in geïndexeerde paginatitels als 'B2: Geen toegang beeldbank'). Ook de pagina met het formele privacyreglement/beleidsplan van HKH (www.historischekringheemskerk.nl/organisatie/beleidsplan/) gaf een 403-fout bij deze poging. Dit bevestigt de eerdere conclusie dat er geen publiek, machinaal toegankelijk intakekanaal bestaat voor HKH-eigen recordniveau-data; alleen door zoekresultaten geïndexeerde snippets zijn beschikbaar, niet de volledige paginatekst.

Bronnen: [https://www.historischekringheemskerk.nl/cgi-bin/bidprent.pl](https://www.historischekringheemskerk.nl/cgi-bin/bidprent.pl), [https://www.historischekringheemskerk.nl/organisatie/beleidsplan/](https://www.historischekringheemskerk.nl/organisatie/beleidsplan/)

### HKH heeft sinds 2018 een formeel privacyreglement, maar de concrete inhoud (grondslag, bewaartermijn) is dit keer niet te verifiëren

Via zoekresultaten is vastgesteld dat het bestuur van HKH sinds 25 mei 2018 een 'PRIVACYREGLEMENT' hanteert (onderdeel van het beleidsplan, met een vernieuwde versie voor 2024-2027), opgesteld naar aanleiding van de AVG. De exacte clausules over verwerkingsgrondslag, doelbinding, bewaartermijnen of specifieke regels voor genealogische gegevens (bidprentjes) of persoonsherkenbare foto's konden niet worden opgehaald omdat de pagina zelf niet bereikbaar was (403). Dit blijft dus een onopgeloste afhankelijkheid: een eventueel gesloten privacybeleid voor automatische besluitvorming kan niet worden afgeleid uit publieke webbronnen zonder dat HKH de tekst rechtstreeks aanlevert.

Bronnen: [https://www.historischekringheemskerk.nl/organisatie/beleidsplan/](https://www.historischekringheemskerk.nl/organisatie/beleidsplan/)

### Netwerk Digitaal Erfgoed heeft een gestandaardiseerd Datasetregister met REST API/SPARQL, maar HKH is niet aantoonbaar aangesloten

Het Datasetregister van het Netwerk Digitaal Erfgoed (beheerd door het Nationaal Archief) laat erfgoedinstellingen datasetbeschrijvingen publiceren volgens schema.org/Dataset-standaard, doorzoekbaar via website, REST API of SPARQL-endpoint. Dit is een reëel, gedocumenteerd machine-toegangspatroon voor Nederlandse erfgoedinstellingen in het algemeen, maar er is in deze raadpleging geen aanwijzing gevonden dat Historische Kring Heemskerk hierin is geregistreerd. Dit is dus een mogelijk toekomstig integratiepad, geen huidig beschikbaar toegangskanaal voor HKH-data.

Bronnen: [https://datasetregister.netwerkdigitaalerfgoed.nl/faq-ontwikkelaars.php](https://datasetregister.netwerkdigitaalerfgoed.nl/faq-ontwikkelaars.php)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens) | 2026-08-08 | Officiële Nederlandse overheidsinstantie (toezichthouder); directe fetch gaf 403, inhoud is afgeleid uit geïndexeerde zoekresultaatsnippet. Hergebruikstatus van de exacte paginatekst niet expliciet vastgesteld, maar overheidsvoorlichting is doorgaans vrij citeerbaar voor feitelijke duiding. | Autoritatieve, officiële bevestiging dat de AVG uitsluitend van toepassing is op levende natuurlijke personen, essentieel voor een deterministische privacyregel voor genealogische/bidprentjesdata. |
| [bron](https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen) | 2026-08-08 | Journalistiek nieuwsartikel, auteursrechtelijk beschermd; hier alleen gebruikt als feitenbron voor een citaat uit een ministerieel Kamerantwoord, geen doorpublicatie van de volledige tekst. | Geeft het concrete citeerbare rechtsgrond (Overweging 27 AVG) en ministeriële bevestiging dat AVG niet geldt voor overledenen, met nuance over nabestaanden. |
| [bron](https://opendata.archieven.nl/nl/over-open-data) | 2026-08-08 | Officiële documentatiepagina van het gezamenlijke Nederlandse archievenplatform archieven.nl; data zelf onder Creative Commons-voorwaarden aangeboden (exacte CC-variant per dataset wisselend, naamsvermelding soms vereist). | Toont een concreet, technisch gedocumenteerd en autorisatievrij machine-toegangspad (resolvebare URI's, content-negotiation, harvesting) dat kan dienen als extern verificatie-anker zonder eigen HKH-tokenprotocol. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210) | 2026-08-08 | Publieke archieftoegangspagina van Noord-Hollands Archief via archieven.nl; op deze specifieke pagina geen zichtbare expliciete licentievermelding aangetroffen bij herraadpleging vandaag. | Directe controle van de eerder aangehaalde Heemskerk-archieftoegang als extern controlegeval; nuanceert eerdere CC0-aanname op paginaniveau. |
| [bron](https://www.historischekringheemskerk.nl/cgi-bin/bidprent.pl) | 2026-08-08 | Eigen collectiecontent van HKH; toegang geweigerd (geblokkeerd voor geautomatiseerde/bot-achtige toegang), inhoud zelf dus niet geraadpleegd, alleen foutmelding en geïndexeerde paginatitel gezien. | Herbevestigt vandaag dat automatische raadpleging van HKH's eigen bidprentjes-/beeldbanksystemen nog steeds geblokkeerd is, relevant voor de intake-haalbaarheidsvraag. |
| [bron](https://www.historischekringheemskerk.nl/organisatie/beleidsplan/) | 2026-08-08 | Eigen beleidspagina van HKH; auteursrecht bij HKH. Directe fetch gaf 403-foutmelding; alleen een korte samenvatting via zoekresultaatsnippet kon worden ingezien, geen volledige paginatekst. | Enige gevonden aanwijzing dat HKH een formeel privacyreglement/beleidsplan (sinds 2018, vernieuwd 2024-2027) voert, relevant voor de vraag naar een vooraf vastgesteld privacybeleid, maar inhoud kon niet worden geverifieerd. |
| [bron](https://datasetregister.netwerkdigitaalerfgoed.nl/faq-ontwikkelaars.php) | 2026-08-08 | Officiële documentatie van het Netwerk Digitaal Erfgoed / Nationaal Archief; technische documentatie, geen expliciete hergebruiklicentie vermeld voor de paginatekst zelf, wel bedoeld voor publiek/ontwikkelaarsgebruik. | Beschrijft een algemeen, gestandaardiseerd Nederlands erfgoed-API-patroon (REST/SPARQL) dat relevant is als mogelijk toekomstig alternatief toegangspad, ook al is HKH er niet op aangesloten. |

## Productbeslissing

Richt deze iteratie op één samenhangende, zelfstandig uitvoerbare stap: koppel HKH aan het externe, autorisatievrije open-datapad van archieven.nl/Noord-Hollands Archief (resolvebare URI's met content-negotiation) als verificatie-anker voor Heemskerkse geschiedenis, en combineer dit met een vaste, deterministische privacyregel — de AVG geldt niet voor overleden personen (Overweging 27 AVG) — om genealogische/bidprentjes-achtige records automatisch te kunnen classificeren zonder ad-hoc mensenoordeel. Bouw geen automatische intake voor HKH's eigen collecties (beeldbank, archief, bidprentjes): deze blijven vandaag technisch geblokkeerd (403) en vereisen een niet te vermijden, eigenaarsafhankelijke actie (export/API-toegang of de volledige privacyreglement-tekst). Verifieer hergebruikslicenties op archieven.nl per record, niet collectiebreed.

**Waarom:** Het onderzoek levert nu twee reëel bruikbare, citeerbare bouwstenen die eerdere blokkerende kritiekpunten wegnemen: een gedocumenteerd autorisatievrij extern toegangspad (archieven.nl) in plaats van een niet-onderbouwd HKH-tokenprofiel, en een autoritatieve juridische regel (AVG geldt niet voor overledenen) die automatische privacybeslissingen mogelijk maakt zonder mensenoordeel. Voor HKH's eigen collectie-intake blijft er echter geen publiek machinaal kanaal beschikbaar; herhaalde verificatie vandaag bevestigt blokkades op zowel de collectiesystemen als het beleidsplan. Volgens de guardrails mag alleen een werkelijk noodzakelijke externe-toegangsafhankelijkheid later eigenaarsactie vragen — dat is hier exact de HKH-eigen intake, dus die stellen we expliciet uit in plaats van te forceren met aannames.

### Prioriteiten
- Koppel het HKH-platform aan archieven.nl/NHA open data als extern verificatie-anker via resolvebare URI's, zonder eigen tokenprotocol te bouwen.
- Implementeer de AVG-uitzondering voor overleden personen als vaste automatische privacybeslisregel voor genealogische/bidprentjes-records.
- Verifieer hergebruikslicentie per record/pagina bij archieven.nl in plaats van een collectiebrede aanname te hanteren.
- Markeer automatische intake van HKH's eigen collecties als geblokkeerd totdat de eigenaar exporttoegang of de volledige privacyreglement-tekst levert.
- Houd de scope klein: eerst het externe anker en de privacyregel opleveren, HKH-eigen intake bewust uitstellen.

### Besluiten
- **Bouw het externe verificatie-anker voor Heemskerk-geschiedenis op archieven.nl / Noord-Hollands Archief open data: resolvebare URI's (http://opendata.archieven.nl/id/<adtid>/<guid>) met content-negotiation naar N-Triples/Turtle/RDF-XML/JSON-LD, zonder HKH-specifiek autorisatietoken.** — Dit is het enige onderzochte externe toegangspad dat technisch gedocumenteerd én autorisatievrij is, en voorkomt zo het eerder afgekeurde, niet-onderbouwde JWT-/tokenprofiel voor externe koppeling.
- **Codeer de AVG-uitzondering voor overleden personen (Overweging 27 AVG) als vaste, deterministische privacyregel: genealogische/bidprentjes-records van overleden personen mogen automatisch als verwerkbaar worden geclassificeerd, mits het record geen identificeerbare gegevens van nog levende nabestaanden bevat.** — Autoritatief citeerbare rechtsgrond die ad-hoc mensenoordeel over privacy vervangt door een reproduceerbare beslisregel, precies wat nodig is voor zelfstandige uitvoering door agents.
- **Stel automatische intake van HKH's eigen lokale collecties (beeldbank, archief, bidprentjes-cgi) uit totdat de eigenaar een werkend exportkanaal/API-toegang levert of de volledige tekst van het privacyreglement (2018, vernieuwd 2024-2027) beschikbaar stelt; dit is de enige geaccepteerde, niet te vermijden afhankelijkheid van eigenaarsactie.** — Herhaalde controle op 2026-08-08 bevestigt 403-blokkades op zowel de collectiesystemen als de beleidsplanpagina; er bestaat geen publiek machinaal kanaal, en de guardrail staat alleen een écht noodzakelijke externe-toegangsafhankelijkheid toe.
- **Behandel hergebruikslicenties (CC0 of anderszins) op archieven.nl-content per pagina/dataset als apart te verifiëren, niet als generieke aanname voor de hele Heemskerk-collectie.** — De eerder aangenomen CC0-vermelding op de specifieke Heemskerk-archieftoegangspagina kon vandaag niet worden herbevestigd, dus een collectiebrede aanname zou een onbewezen claim in het product introduceren.

## UX-voorstel: Extern verificatie-anker (archieven.nl) + automatische AVG-classificatie voor genealogische records

**Gebruikersdoel:** Als curator-agent van hkh-autopilot wil ik dat elk lokaal genealogisch/bidprentje-record automatisch wordt gekoppeld aan het externe, autorisatievrije open-datapad van archieven.nl/Noord-Hollands Archief en automatisch (zonder mensbeoordeling) wordt geclassificeerd als verwerkbaar of geblokkeerd op basis van de AVG-regel voor overleden personen (Overweging 27 AVG), zodat alleen aantoonbaar verwerkbare records worden vrijgegeven.

### Flow
1. Systeem selecteert een lokaal record (bidprentje/genealogisch item) uit de wachtrij 'te classificeren'.
2. Systeem bevraagt de resolvebare archieven.nl-URI (http://opendata.archieven.nl/id/<adtid>/<guid>) met content-negotiation naar JSON-LD om een extern verificatierecord op te halen.
3. Systeem matcht kernvelden (naam, geboorte-/overlijdensdatum) van het lokale record tegen het opgehaalde externe record om een verificatiekoppeling vast te leggen; bij geen match krijgt het record status 'Unverified'.
4. Automatische privacy-regelmotor bepaalt: is het onderwerp overleden EN bevat het record geen identificeerbare gegevens van nog levende nabestaanden? Zo ja -> 'Processable'; zo nee -> 'Blocked'.
5. Systeem controleert en registreert de hergebruikslicentie per opgehaald extern record afzonderlijk (geen collectiebrede aanname); ontbrekende licentie-informatie zet het record op 'License unknown'.
6. Systeem slaat alleen de minimale verificatiedata op (externe URI, gematchte velden, classificatie, licentiestatus) — geen volledige duplicatie van externe of geblokkeerde brondata.
7. Resultatenoverzicht toont per record één statusbadge: Verified+Processable, Verified+Blocked, License unknown, of Unverified, elk met tekstlabel en icoon.
8. Records met status anders dan Verified+Processable+License bevestigd worden automatisch uitgesloten van publicatie en gaan naar een geblokkeerde wachtrij zonder verdere menselijke stap.
9. Indien de archieven.nl-integratie ooit een toegangstoken vereist, toont het systeem één invoerveld voor het externe token (enige toegestane niet-geautomatiseerde stap); token wordt versleuteld opgeslagen, nooit getoond in logs of UI na invoer.
10. Geautomatiseerde testsuite (agent-uitvoerbaar) draait fixture-records door de volledige flow om classificatie-, licentie- en statuslogica te verifiëren zonder menselijke tester.

### Wireframe

SCHERM: Record-classificatiewachtrij
┌──────────────────────────────────────────────────────────┐
│ Titel: "Genealogische records — automatische classificatie"│
│ [Zoekveld] [Filter: Alle | Processable | Blocked | Unverified | License unknown] │
├──────────────────────────────────────────────────────────┤
│ Lijst (toetsenbord-navigeerbaar, elk item = <li> met role=listitem, focusbaar): │
│  • Record #1032 — Jan de Vries (†1954)                    │
│      Badge: [✔ Processable] (groen icoon + tekstlabel)    │
│      Extern anker: archieven.nl/id/236/1090322 (link, aria-label "opent externe bron in nieuw tabblad") │
│      Licentie: CC0 (per record geverifieerd, datum: 2026-08-08) │
│  • Record #1033 — Anna Bakker (†1998, dochter nog in leven)│
│      Badge: [✖ Blocked] (rood icoon + tekstlabel)          │
│      Reden: "Bevat gegevens van levende nabestaande"       │
│  • Record #1034 — onbekend                                │
│      Badge: [? Unverified] (grijs icoon + tekstlabel)      │
│      Reden: "Geen match gevonden op archieven.nl"          │
├──────────────────────────────────────────────────────────┤
│ Detailpaneel (opent bij Enter/klik op record, focus verplaatst naar paneel-titel): │
│  Titel: Record #1032 — Jan de Vries                        │
│  Sectie "Verificatie": externe URI, opgehaalde velden (naam, datum), tijdstip laatste check │
│  Sectie "Privacyclassificatie": regel toegepast + korte uitleg ("AVG geldt niet voor overleden personen, geen levende nabestaanden gedetecteerd") │
│  Sectie "Licentie": status + brondatum verificatie          │
│  [Terug-knop] (toetsenbord-bereikbaar, aria-label "Terug naar lijst") │
│  Geen goedkeurings- of publicatieknop voor de curator: classificatie en publicatie-eligibiliteit zijn volledig automatisch bepaald. │
├──────────────────────────────────────────────────────────┤
│ Optioneel paneel (alleen zichtbaar indien archief-endpoint ooit auth vereist): │
│  Label: "Extern toegangstoken vereist"                     │
│  [Invoerveld type=password, aria-required, aria-describedby=tokenHint] │
│  Hint-tekst: "Token wordt versleuteld opgeslagen en nooit getoond." │
│  [Opslaan-knop]                                             │
└──────────────────────────────────────────────────────────┘

### Interactiehypotheses
- Gegeven een record van een overleden persoon zonder gegevens van levende nabestaanden classificeert het systeem dit in 100% van de geautomatiseerde fixture-tests als 'Processable'.
- Gegeven een record dat gegevens van een nog levende nabestaande bevat, classificeert het systeem dit altijd als 'Blocked' en plaatst het in de geblokkeerde wachtrij, geverifieerd via unit tests met minstens 3 fixture-varianten.
- Voor elk extern gekoppeld archieven.nl-record wordt de hergebruikslicentie per record gecontroleerd en niet overgenomen van een eerder gecachte collectiebrede status; test met twee records (één met, één zonder zichtbare licentie) toont verschillende licentiestatussen.
- Wanneer archieven.nl geen match retourneert voor de opgevraagde URI, toont het systeem status 'Unverified' en sluit het record automatisch uit van elke publicatieactie, geverifieerd met een record met een niet-bestaande guid.
- Statusbadges zijn met een geautomatiseerde toegankelijkheidsaudit (bijv. axe-core) te controleren op tekstlabel + contrastratio ≥4.5:1, niet uitsluitend op kleur, voor alle vier statuscategorieën.
- De volledige flow (record selecteren, detail openen, terug navigeren) is met alleen toetsenbord (Tab/Enter/Shift+Tab/Escape) te doorlopen, geverifieerd via geautomatiseerde keyboard-navigatietest.

### Toegankelijkheid
- Elke statusbadge (Processable/Blocked/Unverified/License unknown) combineert tekstlabel en icoon/vorm, nooit alleen kleur — automatisch controleerbaar met axe-core 'color-contrast' en 'non-text-contrast' regels.
- Alle interactieve elementen (lijstitems, links, invoerveld, terug-knop) zijn volledig bereikbaar en bedienbaar met toetsenbord (Tab-volgorde, Enter/Spatie activeert), zonder muisafhankelijkheid.
- Focusindicator is zichtbaar op elk interactief element (minimaal 3:1 contrast t.o.v. achtergrond), automatisch te toetsen met een focus-visible/contrast-checktool.
- Tekst- en interface-elementen voldoen aan minimaal 4.5:1 contrastratio, geverifieerd met geautomatiseerde contrastanalyse.
- Externe links naar archieven.nl hebben een aria-label dat aankondigt dat de link een externe bron in een nieuw tabblad opent, zodat schermlezergebruikers dit vooraf weten.
- Detailpaneel verplaatst focus programmatisch naar de paneltitel bij openen, en terug naar het uitgangselement bij sluiten, zodat schermlezergebruikers de contextwissel niet missen.
- Foutmeldingen en statusreden (bijv. 'Geen match gevonden') worden als tekst binnen de DOM aangeboden (niet alleen als tooltip/hover), zodat schermlezers ze kunnen voorlezen.

### Privacy
- Pas de AVG-uitzondering voor overleden personen (Overweging 27 AVG) toe als vaste, deterministische regel; verwerk persoonsgegevens van een overledene alleen automatisch als 'Processable' wanneer het record geen identificeerbare gegevens van nog levende nabestaanden bevat.
- Sla van het externe archieven.nl-record alleen de minimale velden op die nodig zijn voor de verificatiekoppeling (URI, gematchte naam/datum, licentiestatus, controletijdstip) — geen volledige duplicatie van externe brondata, conform doelbinding en minimale gegevensverwerking.
- Bouw geen automatische intake van HKH's eigen collecties (beeldbank, archief, bidprentjes-cgi): deze blijven technisch geblokkeerd (403) en vereisen eerst eigenaarsactie (exportkanaal of volledige privacyreglement-tekst) voordat enige persoonsgegevensverwerking plaatsvindt.
- Behandel hergebruikslicenties op archieven.nl-content per record/pagina als apart te verifiëren gegeven; sla geen generieke 'CC0 voor hele collectie'-aanname op, om onbewezen hergebruikclaims te voorkomen.
- Records geclassificeerd als 'Blocked' (levende nabestaande gedetecteerd) worden nooit gepubliceerd of extern blootgesteld; er is geen menselijke overrule-stap ingebouwd, dus 'Blocked' blijft blijvend geblokkeerd totdat de geautomatiseerde regel zelf een andere uitkomst geeft.
- Een eventueel extern toegangstoken voor het archief-endpoint wordt uitsluitend versleuteld opgeslagen (secret storage), nooit in leesbare vorm getoond in UI, logs of foutmeldingen, en is de enige toegestane niet-volledig-geautomatiseerde invoerstap.
- Onverifieerbare of licentie-onbekende records worden gemarkeerd als 'Not published' en nooit stilzwijgend als verwerkbaar behandeld, om te voorkomen dat ontbrekende data leidt tot ongeoorloofde verwerking of publicatie.

## Kritische beoordeling

**Oordeel:** ACCEPT

Alle drie kandidaten adresseren direct de blokkerende kritiek uit iteratie 16 (onderbouwd niet-JWT extern toegangspad, deterministische privacyregel i.p.v. ad-hoc mensoordeel) met citeerbare bronnen (AVG Overweging 27, AP-bevestiging, archieven.nl open-data-documentatie). Geen van de drie vereist een handmatige test, productbesluit of andere eigenaarsactie buiten het expliciet toegestane optionele externe token in kandidaat 1; classificatie- en publicatielogica is volledig fail-closed en agent-testbaar via fixtures. Toegankelijkheidscriteria (axe-core, tekstlabel+icoon, contrast, focusbeheer, aria-labels) zijn concreet en automatisch verifieerbaar. Privacyverwerking is minimaal en doelgebonden (alleen verificatievelden, geen volledige duplicatie van bronnen). Geen BLOCKING-issues gevonden; wel twee WARNING-punten die aandacht verdienen bij verdere uitwerking: het ontbrekende detectiemechanisme voor 'levende nabestaande'-gegevens in kandidaat 0, en mogelijke overlap tussen kandidaat 1 en de reeds gepubliceerde kandidaat #15 over interne koppelingsvalidatie.
- **WARNING · SCOPE** — Kandidaat 0 specificeert niet welk veld/mechanisme bepaalt of een record 'identificeerbare gegevens van nog levende nabestaanden' bevat. De acceptatiecriteria testen alleen de uitkomst (Processable/Blocked), niet hoe de detectie zelf werkt. De fail-closed default op onbekende status beperkt het risico, maar dit moet bij uitwerking alsnog concreet worden gemaakt (bestaand veld vs. inferentie) om agent-uitvoerbaar te blijven zonder mensoordeel per record.
- **WARNING · CONSISTENCY** — Kandidaat 1 ('Extern verificatie-anker via archieven.nl') overlapt inhoudelijk met de reeds gepubliceerde kandidaat #15 ('Valideer een intern koppelingsdossier fail-closed'), die ook interne-externe recordverificatie en publiceerbaarheidsstatus behandelt. De dependsOn-lijst van kandidaat 1 vermeldt alleen #16, niet #15, waardoor het risico op dubbele of tegenstrijdige implementatielogica bestaat.
- **INFO · SOURCE** — De licentievermelding op de specifieke Heemskerk-archiefpagina kon deze onderzoeksiteratie niet worden herbevestigd; kandidaat 2 mitigeert dit correct door per-record verificatie i.p.v. een collectiebrede aanname, maar de onderliggende onzekerheid blijft zichtbaar en moet zo blijven gedocumenteerd.
- **INFO · PRIVACY** — Kandidaat 0 beperkt scope terecht tot het overlijdenscriterium van Overweging 27 AVG; andere grondslagen (bv. bijzondere persoonsgegevens zoals religieuze aanduiding op bidprentjes) vallen expliciet buiten scope. Dit is correct benoemd als risico en vereist geen actie nu, maar moet bewaakt blijven bij toekomstige uitbreiding.

## Geaccepteerde storykandidaten

### Deterministische AVG-classificatie voor overleden personen in genealogische records

Als privacy-classificatiemotor van hkh-autopilot wil ik elk lokaal genealogisch/bidprentje-record automatisch en fail-closed classificeren als 'Processable' of 'Blocked', op basis van de vaste, citeerbare AVG-uitzondering voor overleden personen (Overweging 27 AVG: de AVG is niet van toepassing op gegevens van overleden personen). Een record wordt alleen automatisch als 'Processable' geclassificeerd wanneer het onderwerp overleden is EN het record geen identificeerbare gegevens van nog levende nabestaanden bevat; in alle andere gevallen (onbekende status, levend onderwerp, of gedetecteerde levende nabestaande) is de uitkomst 'Blocked'. Dit vervangt ad-hoc mensbeoordeling door een reproduceerbare, agent-uitvoerbare beslisregel en staat los van de externe archiefkoppeling.

**Acceptatiecriteria**
- Gegeven een fixture-record met overleden=true en geen velden die een levende nabestaande identificeren, classificeert het systeem het record automatisch als 'Processable', geverifieerd via een geautomatiseerde unit test.
- Gegeven een fixture-record met overleden=true en een veld dat een nog levende nabestaande identificeert, classificeert het systeem het record als 'Blocked' met reden 'Bevat gegevens van levende nabestaande', getest met minimaal 3 verschillende fixture-varianten.
- Gegeven een fixture-record zonder bekende overlijdensstatus (onbekend of levend), classificeert het systeem het record standaard als 'Blocked' (fail-closed default), automatisch getest.
- De classificatiereden wordt als leesbare tekst bij het record opgeslagen (niet uitsluitend een interne code), gecontroleerd via een geautomatiseerde test op aanwezige tekstuele uitleg.
- Records met status 'Blocked' worden automatisch uitgesloten van elke publicatie-actie; een geautomatiseerde testsuite verifieert dat geen publish-functie kan worden aangeroepen voor 'Blocked'-records.
- Een geautomatiseerde toegankelijkheidsaudit (bijv. axe-core) bevestigt dat de classificatiestatus in de UI wordt getoond met zowel tekstlabel als icoon (niet uitsluitend kleur) en een contrastratio van minimaal 4.5:1.

Bronnen: [https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens](https://autoriteitpersoonsgegevens.nl/nl/over-privacy/persoonsgegevens/wat-zijn-persoonsgegevens), [https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen](https://www.security.nl/posting/588822/Minister:+privacywet+AVG+geldt+niet+voor+overleden+personen)

Afhankelijkheden: Bouwt voort op het lokale recordmodel dat door bestaande kandidaten over recordvalidatie (bijv. #15, #16) wordt geleverd; introduceert geen nieuw recordmodel.

Risico's: Onvolledige detectie van 'levende nabestaande'-velden kan leiden tot onterechte 'Processable'-classificatie; fail-closed default op onbekende status beperkt dit risico., De regel behandelt alleen het overlijdenscriterium; andere AVG-grondslagen (bijv. bijzondere persoonsgegevens) vallen buiten deze scope en moeten apart geadresseerd worden.

### Extern verificatie-anker via archieven.nl open data zonder autorisatietoken

Als verificatiecomponent van hkh-autopilot wil ik een lokaal genealogisch record automatisch koppelen aan het gedocumenteerde, autorisatievrije open-datapad van archieven.nl/Noord-Hollands Archief door de resolvebare URI (http://opendata.archieven.nl/id/<adtid>/<guid>) te bevragen met content-negotiation naar JSON-LD, kernvelden (naam, geboorte-/overlijdensdatum) te matchen, en het record te markeren als 'Verified' of 'Unverified'. Er wordt geen HKH-specifiek tokenprotocol gebouwd, omdat het onderzochte platform geen autorisatie vereist; alleen wanneer het endpoint zelf ooit expliciet een token eist, toont het systeem één enkel invoerveld hiervoor als de enige toegestane niet-volledig-geautomatiseerde stap.

**Acceptatiecriteria**
- Gegeven een lokaal record met een gekoppelde archieven.nl-identifier, bevraagt het systeem de resolvebare URI met Accept: application/ld+json zonder autorisatietoken, geverifieerd via een geautomatiseerde integratietest tegen een fixture/mock-endpoint.
- Wanneer naam- en datumvelden van het lokale record overeenkomen met het opgehaalde externe JSON-LD-record, krijgt het record status 'Verified', getest met minstens 2 matching-fixtures.
- Wanneer geen match wordt gevonden (bijvoorbeeld bij een niet-bestaande guid), krijgt het record status 'Unverified' en wordt het automatisch uitgesloten van publicatie, getest met een fixture met een ongeldige guid.
- Het systeem slaat uitsluitend de minimale verificatievelden op (externe URI, gematchte velden, controletijdstip) en dupliceert geen volledige externe brondata, gecontroleerd via een geautomatiseerde test op de opgeslagen veldenset.
- Alleen wanneer het archief-endpoint expliciet een toegangstoken vereist toont het systeem één invoerveld hiervoor; het token wordt versleuteld opgeslagen en nooit in leesbare vorm getoond in UI of logs, geverifieerd met een geautomatiseerde test die logoutput controleert op afwezigheid van de tokenwaarde.
- Een geautomatiseerde toegankelijkheidsaudit bevestigt dat de externe link naar archieven.nl een aria-label heeft dat aankondigt dat een externe bron in een nieuw tabblad opent.

Bronnen: [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210)

Afhankelijkheden: Vereist een bestaand lokaal recordmodel met een koppelbaar identifier-veld, zoals opgeleverd door kandidaat #16 (token-geautoriseerd lokaal record)., Enige toegestane eigenaarsafhankelijkheid: een extern toegangstoken, uitsluitend indien het archief-endpoint dit ooit alsnog blijkt te vereisen.

Risico's: De structuur of beschikbaarheid van de archieven.nl open-data-API kan wijzigen zonder voorafgaande kennisgeving, wat de integratie kan breken., Naam-/datummatching kan fout-positieve of fout-negatieve koppelingen opleveren bij onvolledige of afwijkend geformatteerde brondata.

### Per-record hergebruikslicentieverificatie voor archieven.nl-koppelingen

Als licentiecontrolecomponent van hkh-autopilot wil ik voor elk extern geverifieerd archieven.nl-record de hergebruikslicentie afzonderlijk uit het opgehaalde brondocument controleren en vastleggen, in plaats van een collectiebrede aanname te hanteren. Ontbrekende licentie-informatie resulteert automatisch in status 'License unknown' en sluit het record uit van publicatie, omdat eerder onderzoek bevestigde dat niet elke pagina binnen dezelfde archiefcollectie een zichtbare licentievermelding toont.

**Acceptatiecriteria**
- Voor elk extern geverifieerd record haalt het systeem de hergebruikslicentie-informatie op uit het opgehaalde JSON-LD/RDF-antwoord van dát specifieke record, niet uit een eerder gecachte collectiebrede waarde, getest met twee fixtures: één met zichtbare licentie en één zonder.
- Wanneer geen licentie-informatie aanwezig is in het externe record, krijgt het record status 'License unknown' en wordt het automatisch uitgesloten van publicatie, geverifieerd via een geautomatiseerde test.
- Wanneer een licentie aanwezig is (bijvoorbeeld CC0), wordt deze samen met de controledatum bij het specifieke record opgeslagen, gecontroleerd via een geautomatiseerde test op de aanwezige velden.
- Het systeem hergebruikt nooit een eerder vastgestelde licentiestatus van een ander record binnen dezelfde archiefcollectie als aanname voor een nieuw record; dit wordt getest door twee records uit dezelfde collectie met verschillende licentie-uitkomsten te verifiëren.
- De licentiestatus wordt getoond als apart statusbadge (tekstlabel + icoon) naast de verificatie- en privacystatus, gecontroleerd via een geautomatiseerde toegankelijkheidsaudit (axe-core) op tekstlabel en contrastratio van minimaal 4.5:1.

Bronnen: [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

Afhankelijkheden: Vereist de ruwe externe recorddata die wordt opgehaald door de story 'Extern verificatie-anker via archieven.nl open data zonder autorisatietoken'.

Risico's: Licentievermeldingen kunnen per dataset inconsistent gestructureerd zijn in de RDF/JSON-LD-respons, waardoor parsing een aanwezige licentie kan missen; de conservatieve default 'License unknown' beperkt dit risico op onterechte publicatie., Bij toekomstige wijzigingen in het licentieschema van archieven.nl moet de parsinglogica worden bijgewerkt om vals-negatieve 'License unknown'-uitkomsten te voorkomen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
