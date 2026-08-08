---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0022
date: 2026-08-08
status: approved
sources:
  - https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased
  - https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree
  - https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf
  - https://www.openarchieven.nl/api/docs/uri.php
  - https://www.archieven.nl/nl/algemene-voorwaarden
  - https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210
  - https://opendata.archieven.nl/nl/over-open-data
---
# Productcyclus 22

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Focus van deze iteratie: de WARNING van de critic in iteratie 21 dat kandidaat 0 (AVG-classificatie voor overleden personen) geen concreet detectiemechanisme specificeerde voor "identificeerbare gegevens van nog levende nabestaanden" in een record. Onderzoek naar bestaande genealogische privacystandaarden levert twee citeerbare, machinaal toepasbare bronnen: (1) FamilySearch's officieel gedocumenteerde regel om "levend" vs "overleden" te bepalen (geboorte ≤110 jaar geleden, of huwelijk/kind ≤95 jaar geleden, én geen overlijdensgegevens ingevuld), en (2) de GEDCOM 7.0 RESN-tag (Confidential/Locked/Privacy) als gestandaardiseerd veld om privacygevoelige (sub-)records te markeren. Beide zijn direct bruikbaar als deterministische, testbare bouwstenen voor het ontbrekende detectiemechanisme. Daarnaast is de eerdere aanname over een collectiebrede CC0-licentie op archieven.nl opnieuw getoetst: de centrale 'Algemene voorwaarden'-pagina bevat geen auteursrechten- of hergebruikbepalingen, wat bevestigt dat licentie-informatie niet centraal is vastgelegd en dus per record/dataset geverifieerd moet blijven — dit onderbouwt het eerdere productbesluit voor per-record verificatie. Tot slot is de technische documentatie van archieven.nl's open-data-URI's en content-negotiation preciezer bevestigd via aanvullende openarchieven.nl API-documentatie (profielen A2A/CIV/PiCo; formaten incl. GEDCOM 7.0, JSON, XML naast RDF-serialisaties), zonder authenticatievereiste.

### FamilySearch's gedocumenteerde 110/95-jaarregel als concreet detectiemechanisme voor "levend vs. overleden"

FamilySearch's officiële Help Center legt een exacte, machinaal toepasbare regel vast om te bepalen of een persoon in een genealogisch record als "levend" moet worden behandeld: een persoon wordt als levend beschouwd als (a) de geboortedatum 110 jaar of minder geleden valt, óf een huwelijk of de geboorte van een kind 95 jaar of minder geleden plaatsvond, ÉN (b) er geen overlijdensgegevens (datum/plaats van overlijden of begrafenis) zijn ingevuld. Zodra tekst in een overlijdens- of begrafenisveld staat, neemt het systeem overlijden aan. Het systeem werkt fail-closed in de zin dat er geen automatische statusverandering naar 'overleden' plaatsvindt na het verstrijken van de termijn zonder expliciete overlijdensinformatie. Dit is direct bruikbaar als het ontbrekende detectiemechanisme dat de critic in iteratie 21 aanmerkte als WARNING bij kandidaat 0: pas dezelfde 110/95-jaarregel toe op elk gekoppeld persoonsveld in een HKH-record (hoofdpersoon én genoemde familieleden) om te bepalen of een genoemde nabestaande vermoedelijk nog leeft, en behandel elk zo gedetecteerd 'vermoedelijk levend' veld fail-closed als blokkerend voor automatische classificatie.

Bronnen: [https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased](https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased), [https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree](https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree)

### GEDCOM 7.0 RESN-tag als gestandaardiseerd, machineleesbaar privacylabel in genealogische recordformaten

De officiële FamilySearch GEDCOM 7.0.18-specificatie definieert de RESN (restriction)-structuur met drie mogelijke waarden: CONFIDENTIAL, LOCKED en PRIVACY. RESN kan op het niveau van een volledig record (persoon, familie, bron) of op het niveau van een individueel feit/gebeurtenis worden toegepast, en de specificatie beveelt aan dat toepassingen bij export in staat zijn om met RESN gemarkeerde data te verwijderen. Dit is relevant omdat het een reeds bestaande, industriestandaard datastructuur is voor het markeren van privacygevoelige (sub-)velden binnen een genealogisch record — en dus, als een lokaal of extern record al in GEDCOM-vorm beschikbaar is (archieven.nl biedt GEDCOM 7.0 als exportformaat aan), een direct herbruikbaar signaal kan zijn naast de zelf te bouwen 110/95-jaarregel voor het detecteren van gevoelige nabestaande-gegevens.

Bronnen: [https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf)

### Archieven.nl's centrale 'Algemene voorwaarden' bevat geen auteursrechten- of hergebruikbepalingen

Bij directe raadpleging van de centrale gebruiksvoorwaardenpagina van archieven.nl (www.archieven.nl/nl/algemene-voorwaarden) bleek deze uitsluitend algemene contractvoorwaarden te bevatten (registratie, betaling, klachten, geschillen) en geen enkele bepaling over auteursrecht, hergebruik of licenties (zoals CC0) van getoonde archiefstukken of records. Dit bevestigt en verzwaart het eerdere productbesluit uit iteratie 21 om hergebruikslicenties per pagina/dataset te verifiëren in plaats van een collectiebrede aanname te doen: er bestaat kennelijk geen platformbreed, centraal vastgelegd licentiebeleid dat automatisch op elk record van toepassing is, dus licentiestatus moet per opgehaald record (via de open-data-koppeling) worden meegenomen als apart, mogelijk onbekend/onzeker veld.

Bronnen: [https://www.archieven.nl/nl/algemene-voorwaarden](https://www.archieven.nl/nl/algemene-voorwaarden)

### Verfijnde technische documentatie van open-data-toegang: bredere profielen en formaten, nog steeds zonder authenticatie

Aanvullende officiële API-documentatie op openarchieven.nl (URI and Content Negotiation) specificeert een preciezer URI-patroon (https://www.openarchieven.nl/{archiefcode}:{uuid}[/{token}]) en content-onderhandeling via zowel querystring-parameters (_profile, _mediatype) als HTTP-headers (Accept, Accept-Profile), volgens de W3C 'Content Negotiation by Profile'-specificatie. Er zijn drie gedocumenteerde datamodel-profielen (A2A als standaard, CIV voor burgerlijke stand, PiCo voor 'Persons in Context') en een breder formaatpalet dan eerder vastgesteld: naast Turtle/JSON-LD/N-Triples/RDF-XML/N3 ook JSON, XML, GEDCOM 7.0 en HTML. Nergens in deze documentatie wordt een authenticatievereiste genoemd, wat het eerdere besluit bevestigt dat voor dit externe verificatie-anker geen HKH-specifiek token nodig is. De GEDCOM 7.0-uitvoeroptie is relevant in combinatie met de RESN-bevinding: een extern opgehaald record kan al gestandaardiseerde privacylabels bevatten.

Bronnen: [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

### Specifieke Heemskerk-archieftoegangspagina blijft zonder zichtbare individuele licentievermelding

Herhaalde raadpleging van de eerder aangehaalde archieftoegangspagina 'Ambachts- en Gemeentebestuur van Heemskerk' (inv.nr. 1032, archieven.nl) toont geen expliciete CC0- of andere rechtenvermelding in de zichtbare paginatekst; de pagina verwijst wel naar de open-data-portal en algemene footerlinks (Algemene voorwaarden, Privacy, Disclaimer), maar geen van deze bevat blijkens eerdere en huidige verificatie een direct voor deze pagina geldende licentietekst. Dit bevestigt voor de derde keer (na iteratie 21) dat een collectiebrede CC0-aanname voor Heemskerk-archiefdata niet kan worden onderbouwd en per record/dataset apart geverifieerd moet worden op het moment van ophalen.

Bronnen: [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased) | 2026-08-08 | Officiële help-documentatie van FamilySearch (The Church of Jesus Christ of Latter-day Saints); auteursrechtelijk beschermd, hier uitsluitend geciteerd/samengevat als feitelijke bron, geen herpublicatie van broncontent. | Levert de exacte, citeerbare drempelwaarden (110/95 jaar + afwezigheid overlijdensgegevens) die het door de critic in iteratie 21 gevraagde concrete detectiemechanisme voor 'levende nabestaanden' onderbouwen. |
| [bron](https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree) | 2026-08-08 | Officiële help-documentatie van FamilySearch; auteursrechtelijk beschermd, hier feitelijk samengevat. | Aanvullende bevestiging en context van de living/deceased-regel en het privacydoel ervan binnen een grootschalig, vergelijkbaar genealogisch platform. |
| [bron](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf) | 2026-08-08 | Publiek gepubliceerde technische standaardspecificatie (FamilySearch GEDCOM 7.0.18), vrij toegankelijk als referentiedocumentatie voor implementatoren; licentie voor hergebruik van de spec zelf niet expliciet geverifieerd. | Bevestigt het bestaan van een gestandaardiseerd machineleesbaar privacylabel (RESN-tag) in het GEDCOM-formaat, relevant als aanvullend of alternatief detectiesignaal naast de leeftijdsregel. |
| [bron](https://www.openarchieven.nl/api/docs/uri.php) | 2026-08-08 | Publieke technische API-documentatie van Open Archieven; geen expliciete licentievermelding op de documentatiepagina zelf aangetroffen, functioneert als vrij toegankelijke ontwikkelaarsdocumentatie. | Preciseert het URI-patroon, content-negotiation-mechanisme en de beschikbare datamodel-profielen/formaten voor het externe verificatie-anker, en bevestigt opnieuw de afwezigheid van een authenticatievereiste. |
| [bron](https://www.archieven.nl/nl/algemene-voorwaarden) | 2026-08-08 | Officiële juridische voorwaardenpagina van archieven.nl; publiek toegankelijk, geen herpublicatie van de volledige tekst, alleen feitelijke constatering van afwezige auteursrechtbepalingen. | Directe verificatie of er een collectiebreed, centraal vastgelegd hergebruik-/licentiebeleid bestaat op archieven.nl; bevestigt dat dit niet het geval is en dat per-record verificatie nodig blijft. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210) | 2026-08-08 | Publieke archiefbeschrijvingspagina van het Noord-Hollands Archief via archieven.nl; rechtenstatus van de onderliggende archiefstukken en van de paginatekst zelf blijft bij herhaalde raadpleging onbevestigd/onbekend. | Derde verificatiepoging van de eerder aangenomen maar niet-reproduceerbare CC0-licentievermelding op de specifieke Heemskerk-archieftoegangspagina; bevestigt aanhoudende onzekerheid die zichtbaar moet blijven in het product. |
| [bron](https://opendata.archieven.nl/nl/over-open-data) | 2026-08-08 | Officiële uitlegpagina van archieven.nl over het open-dataprogramma; publiek toegankelijk als beleidsdocumentatie. | Aanvullende bevestiging van het bestaande externe verificatie-anker (resolvebare URI's, content negotiation) uit iteratie 21, gebruikt als kruisverwijzing bij de nieuwe openarchieven.nl API-documentatie. |

## Productbeslissing

Werk de AVG-classificatiefunctie voor overleden personen in HKH-autopilot uit met een concreet, deterministisch en fail-closed detectiemechanisme voor 'vermoedelijk levende nabestaanden', in plaats van de door de critic afgekeurde impliciete aanname. Het mechanisme bestaat uit twee gelaagde, machinaal toepasbare bouwstenen: (1) de FamilySearch 110/95-jaarregel als primaire test per genoemde persoon in een record (hoofdpersoon én familieleden), en (2) de GEDCOM 7.0 RESN-tag als secundair signaal wanneer het brongegeven als GEDCOM beschikbaar is via archieven.nl/openarchieven.nl. Alle onzekere of ontbrekende gevallen worden fail-closed behandeld (geblokkeerd, niet automatisch vrijgegeven). Tegelijk wordt het eerdere besluit over per-record licentieverificatie herbevestigd en technisch verankerd in dezelfde open-data-URI/content-negotiation-koppeling, zonder dat hiervoor authenticatie nodig is: geen enkel record krijgt een licentiestatus toegekend zonder expliciete verificatie.

**Waarom:** De missie vraagt om Heemskerkse geschiedenis toegankelijk én betekenisvol te maken door lokale bronnen te koppelen aan externe collecties — dit vereist automatische, schaalbare AVG-classificatie, maar de critic wees terecht op het ontbreken van een concreet detectiemechanisme voor privacyrisico's bij nog levende nabestaanden. Het onderzoek levert twee bestaande, citeerbare industriestandaarden (FamilySearch-leeftijdsregel, GEDCOM RESN-tag) die dit gat dichten zonder dat HKH-autopilot een eigen, onderbouwde privacyregel hoeft te verzinnen. Beide mechanismen zijn machinaal en fail-closed toepasbaar, wat aansluit bij de KWALITEITSREGEL om in kleine, toetsbare stappen te werken en aannames expliciet te maken. De herbevestiging van per-record licentieverificatie (in plaats van een collectiebrede CC0-aanname) voorkomt een ander, eerder gesignaleerd risico: onterechte hergebruikclaims op archiefmateriaal. Beide bouwstenen zijn met dezelfde open-data-API (geen authenticatie nodig) technisch te realiseren, waardoor de richting volledig autonoom uitvoerbaar blijft voor Product Factory- en Software Factory-agents.

### Prioriteiten
- Implementeer de 110/95-jaarregel als primair, fail-closed detectiemechanisme voor vermoedelijk levende nabestaanden in elk HKH-record (hoofdpersoon + genoemde familieleden).
- Voeg GEDCOM 7.0 RESN-tagherkenning toe als secundair privacysignaal wanneer een bron in GEDCOM-formaat beschikbaar is.
- Maak elke classificatiebeslissing testbaar: definieer unit-testbare voorbeeldcases (met/zonder overlijdensdatum, net onder/boven de 110/95-jaargrens, met/zonder RESN-tag).
- Verwijder elke resterende aanname van een collectiebrede CC0-licentie; licentiestatus is per record 'onbekend' totdat via de open-data-URI geverifieerd.
- Documenteer beide mechanismen (leeftijdsregel + RESN) en het licentieverificatieproces expliciet zodat Software Factory-agents ze zonder verdere interpretatie kunnen implementeren.

### Besluiten
- **Los de WARNING van de critic (iteratie 21, kandidaat 0) op door de FamilySearch 110/95-jaarregel als primair, deterministisch detectiemechanisme te specificeren voor 'vermoedelijk levende nabestaanden' in een HKH-record: een genoemde persoon geldt als vermoedelijk levend als (geboortedatum ≤110 jaar geleden, of huwelijk/geboorte-van-kind ≤95 jaar geleden) EN geen overlijdens-/begrafenisgegevens zijn ingevuld. Dit geldt zowel voor de hoofdpersoon als voor elk genoemd familielid in het record. Bij twijfel of ontbrekende datumvelden wordt fail-closed geclassificeerd (behandeld als vermoedelijk levend, dus geblokkeerd voor automatische AVG-vrijgave).** — Dit is de exacte, citeerbare en machinaal toepasbare regel die de kern van de WARNING wegneemt: er is nu een concreet, testbaar criterium in plaats van een impliciete aanname. Fail-closed gedrag sluit aan bij de KWALITEITSREGEL om aannames expliciet te maken en risico's richting privacyschending te vermijden.
- **Voeg de GEDCOM 7.0 RESN-tag (CONFIDENTIAL/LOCKED/PRIVACY) toe als aanvullend, secundair detectiesignaal: wanneer een brongegeven in GEDCOM 7.0-formaat wordt opgehaald (archieven.nl/openarchieven.nl bieden dit formaat aan), wordt een aanwezige RESN-markering op record- of feitniveau overgenomen als extra blokkerend privacysignaal, naast de leeftijdsregel.** — RESN is een bestaande industriestandaard voor privacylabeling en direct herbruikbaar zonder eigen ontwerpwerk; het versterkt het detectiemechanisme met een tweede, onafhankelijke bron zonder de scope te vergroten.
- **Handhaaf en verscherp het eerdere besluit dat licentiestatus (bijv. CC0) per record/dataset apart wordt geverifieerd via de open-data-URI met content negotiation, en nooit collectiebreed wordt aangenomen. Een record zonder expliciet geverifieerde licentie krijgt het veld licentie="onbekend" totdat verificatie via de open-data-koppeling is uitgevoerd.** — Herhaalde raadpleging van zowel de centrale 'Algemene voorwaarden'-pagina als de specifieke Heemskerk-archiefpagina bevestigt voor de derde keer dat er geen platformbreed licentiebeleid vastligt; een default 'onbekend' voorkomt onterechte hergebruikclaims en is in lijn met fail-closed werken.
- **Gebruik voor zowel het ophalen van GEDCOM-gegevens (voor RESN-detectie) als voor licentieverificatie hetzelfde technische verificatie-anker: de openarchieven.nl URI-structuur (https://www.openarchieven.nl/{archiefcode}:{uuid}[/{token}]) met content negotiation (_profile/_mediatype of Accept/Accept-Profile headers), zonder dat hiervoor authenticatie of een extern toegangstoken nodig is.** — De API-documentatie bevestigt expliciet geen authenticatievereiste; dit maakt de richting volledig autonoom uitvoerbaar door Product Factory- en Software Factory-agents zonder menselijke tussenkomst voor toegangstokens.

## UX-voorstel: Record Privacy Status Panel — AVG-classificatie voor overleden personen (HKH-autopilot)

**Gebruikersdoel:** Een agent of geautomatiseerde test moet, gegeven één HKH-record, direct en machinaal kunnen verifiëren of het record correct als 'vrijgegeven' of 'geblokkeerd (fail-closed)' is geclassificeerd, inclusief de onderliggende signalen (110/95-jaarregel per genoemde persoon, GEDCOM RESN-tag, licentiestatus), zonder dat er persoonsgegevens van vermoedelijk levende personen onnodig zichtbaar worden.

### Flow
1. Systeem haalt brongegeven op via de openarchieven.nl open-data-URI (content negotiation naar GEDCOM 7.0/JSON) voor het te classificeren record.
2. Systeem past de 110/95-jaarregel toe op elke genoemde persoon in het record (hoofdpersoon en familieleden): geboorte ≤110 jaar of huwelijk/kind ≤95 jaar EN geen overlijdens-/begrafenisgegevens ⇒ 'vermoedelijk levend'.
3. Indien het brongegeven in GEDCOM-vorm beschikbaar is, leest systeem eventuele RESN-tag (CONFIDENTIAL/LOCKED/PRIVACY) als secundair blokkerend signaal.
4. Systeem bepaalt licentiestatus per record via dezelfde open-data-koppeling; ontbreekt expliciete verificatie, dan wordt licentie='onbekend' gezet (nooit een collectiebrede aanname).
5. Systeem berekent totaaloordeel: 'Geblokkeerd' zodra minstens één persoon 'vermoedelijk levend' is of RESN aanwezig is; anders 'Vrijgegeven'. Bij ontbrekende/onduidelijke datumvelden: fail-closed ⇒ 'Geblokkeerd'.
6. UI-panel toont per record: totaaloordeel-badge, per-persoon regel met leeftijdsregel-uitkomst, RESN-indicator (indien van toepassing), licentiebadge en machineleesbare status-attributen (data-status, aria-live) voor geautomatiseerde tests.
7. Geautomatiseerde testsuite voert synthetische voorbeeldrecords in (met/zonder overlijdensdatum, net onder/boven 110/95-jaargrens, met/zonder RESN-tag, met/zonder licentieverificatie) en controleert of het panel de verwachte status en signalen toont.
8. Bij afwijking tussen verwachte en getoonde classificatie logt de test een falend scenario met recordreferentie (géén opslag van persoonsgegevens van geblokkeerde personen) voor verdere iteratie door agents.

### Wireframe

[Record Privacy Status Panel] (leesbaar via toetsenbord-tab-volgorde: header → per-persoon-lijst → licentie → footer-acties)

┌─────────────────────────────────────────────────────────────┐
│ HKH-record: {archiefcode}:{uuid}                              │
│ Totaaloordeel: [BADGE: GEBLOKKEERD ⛔ | VRIJGEGEVEN ✅]        │
│  role="status" aria-live="polite" data-status="blocked|released"│
├─────────────────────────────────────────────────────────────┤
│ Genoemde personen (lijst, elk item focusbaar, <ul><li>)       │
│  1) Hoofdpersoon — {naam-placeholder}                          │
│     Leeftijdsregel: [icoon+tekst] "Vermoedelijk levend"        │
│       (geboorte ≤110j OF huwelijk/kind ≤95j; geen overl.datum) │
│     data-age-rule="likely_living|deceased|unknown_failclosed"  │
│  2) Familielid — {rol-placeholder, bv. "kind"}                 │
│     Leeftijdsregel: [icoon+tekst] "Overleden (overl.datum aanw.)"│
│     data-age-rule="deceased"                                   │
│  …                                                              │
├─────────────────────────────────────────────────────────────┤
│ RESN-signaal (alleen tonen indien GEDCOM-bron beschikbaar)     │
│  [icoon+tekst] "RESN: CONFIDENTIAL aanwezig op recordniveau"   │
│  data-resn="confidential|locked|privacy|none|not_applicable"   │
├─────────────────────────────────────────────────────────────┤
│ Licentiestatus                                                  │
│  [BADGE] "Onbekend — nog niet geverifieerd" (default)           │
│  of  [BADGE] "Geverifieerd: CC0" / "Geverifieerd: overig"       │
│  data-license="unknown|verified_cc0|verified_other"             │
├─────────────────────────────────────────────────────────────┤
│ Testhaken (verborgen voor eindgebruiker, wel in DOM):           │
│  <div data-testid="privacy-panel" data-status data-age-rule    │
│       data-resn data-license> — door geautomatiseerde tests     │
│       en agents uit te lezen zonder menselijke tussenkomst.     │
└─────────────────────────────────────────────────────────────┘

Kleur nooit als enige signaaldrager: elke badge combineert icoon + tekstlabel + kleur (bv. ⛔ rood "Geblokkeerd", ✅ groen "Vrijgegeven"). Alle interactieve/informatieve elementen zijn bereikbaar via Tab en voorzien van aria-label die de status in platte tekst herhaalt.

### Interactiehypotheses
- Als een genoemd familielid een geboortejaar ≤110 jaar geleden heeft en geen overlijdensdatum, toont het panel voor dat item data-age-rule='likely_living' en het totaaloordeel data-status='blocked' — verifieerbaar door een geautomatiseerde test die een synthetisch record met bekende leeftijd invoert en het DOM-attribuut uitleest.
- Als alle genoemde personen een overlijdensdatum hebben én er geen RESN-tag aanwezig is én de licentie geverifieerd is, toont het panel data-status='released' — getest met een synthetisch 'volledig vrij' record.
- Als het brongegeven een RESN-tag CONFIDENTIAL bevat op recordniveau, blokkeert het panel het record ongeacht de uitkomst van de leeftijdsregel — getest door twee synthetische records te vergelijken die identiek zijn behalve de RESN-tag.
- Als een datumveld ontbreekt of onleesbaar is (bv. onvolledige datum), classificeert het panel dat item fail-closed als 'vermoedelijk levend' — getest met synthetische records met lege/corrupte datumvelden.
- Als de licentiestatus niet expliciet geverifieerd kon worden via de open-data-koppeling, toont het panel altijd data-license='unknown' en nooit een aangenomen 'verified_cc0' — getest door de open-data-call te mocken zodat deze geen licentie-informatie teruggeeft.

### Toegankelijkheid
- Alle statusbadges en per-persoon regels zijn volledig bereikbaar en bedienbaar via toetsenbord (Tab/Shift+Tab), zonder muis-afhankelijke interacties.
- Totaaloordeel-badge gebruikt role='status' met aria-live='polite' zodat schermlezers wijzigingen automatisch aankondigen zonder focusverlies.
- Geen enkel statussignaal (geblokkeerd/vrijgegeven/RESN/licentie) steunt uitsluitend op kleur; elk badge combineert icoon + expliciete tekstlabel die door schermlezers wordt voorgelezen.
- Kleurcontrast van tekst en iconen ten opzichte van achtergrond voldoet aan WCAG 2.1 AA (minimaal 4.5:1 voor normale tekst, 3:1 voor grote tekst/iconen).
- Alle data-testid/data-status attributen zijn ook als aria-label of visueel-verborgen tekst beschikbaar, zodat zowel geautomatiseerde tests als schermlezergebruikers dezelfde informatie ontvangen.

### Privacy
- Toon nooit volledige persoonsgegevens (namen, geboortedata) van personen die als 'vermoedelijk levend' zijn geclassificeerd in logs of testrapportages; gebruik alleen recordreferenties (archiefcode:uuid) bij falende testscenario's.
- Pas het fail-closed principe strikt toe: bij twijfel, ontbrekende of onleesbare datumvelden wordt een persoon standaard als 'vermoedelijk levend' behandeld en het record geblokkeerd, nooit automatisch vrijgegeven.
- Sla geen kopie van herleidbare persoonsgegevens van levende nabestaanden op buiten wat strikt nodig is voor de classificatiebeslissing zelf; bewaar bij voorkeur alleen het classificatieresultaat (booleans/enums), niet de brondata.
- Behandel de GEDCOM RESN-markering (CONFIDENTIAL/LOCKED/PRIVACY) als bindend blokkerend signaal en respecteer deze ongeacht de uitkomst van de leeftijdsregel.
- Ken nooit standaard een licentie (bv. CC0) toe aan een record; licentiestatus is 'onbekend' totdat expliciete verificatie via de open-data-URI met content negotiation heeft plaatsgevonden.
- Voor het gebruik van de openarchieven.nl open-data-koppeling is geen authenticatie of extern toegangstoken vereist volgens de API-documentatie; er hoeft dus geen menselijk te verstrekken token in dit ontwerp te worden opgenomen.
- Alle classificatie- en verificatiestappen moeten door agents en geautomatiseerde tests herhaalbaar en controleerbaar zijn (synthetische testcases), zodat geen handmatige menselijke goedkeuring nodig is in de flow.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten (0: 110/95-jaarregel voor levend-detectie; 1: GEDCOM 7.0 RESN-tag als secundair signaal) leveren een concreet, deterministisch en fail-closed detectiemechanisme dat de eerder gesignaleerde WARNING over ontbrekende detectielogica voor "levende nabestaanden" adresseert. Beide zijn volledig agent-uitvoerbaar en testbaar via synthetische fixtures, vereisen geen menselijke actie, account, betaling of token (bevestigd: openarchieven.nl vereist geen authenticatie), en bouwen consistent voort op reeds gepubliceerde kandidaten (17, 18) zonder scope-verbreding of duplicatie met andere gepubliceerde/afgewezen kandidaten. Privacyontwerp is behoudend (fail-closed bij onzekerheid, geen opslag van herleidbare gegevens, alleen classificatie-enums). Geen van beide kent blokkerende issues; er zijn wel enkele WARNING-punten over brongezag en randgevallen die in de uitwerking/documentatie expliciet gemaakt moeten worden, maar deze vereisen geen nieuwe iteratie.
- **WARNING · SOURCE** — De FamilySearch 110/95-jaarregel is een intern productbeleid van een commerciële partij, geen wettelijke AVG-norm of erkende industriestandaard. De candidate erkent dit al als risico, maar er is geen acceptatiecriterium dat afdwingt dat de documentatie deze regel expliciet als heuristische aanname (los van de wettelijke grondslag in kandidaat 17) labelt.
- **WARNING · SOURCE** — De acceptatiecriteria classificeren ontbrekende/onleesbare datumvelden als 'unknown_failclosed', wat afwijkt van de letterlijk geciteerde FamilySearch-bronregel (die bij afwezigheid van elk datumveld conditie (a) niet laat gelden). Deze bewuste, privacy-versterkende afwijking van de bron moet expliciet als zodanig gedocumenteerd worden, niet als rechtstreekse toepassing van de bron.
- **WARNING · CONSISTENCY** — De 95-jaar-subregel (huwelijk/geboorte kind) veronderstelt dat het brondatamodel deze gebeurtenissen als aparte, gestructureerde velden blootstelt. Als archieven.nl/HKH-bronrecords deze granulariteit niet uniform bieden, is de subregel mogelijk onbruikbaar; er ontbreekt een expliciet fallbackgedrag hiervoor in de acceptatiecriteria (risico wordt wel genoemd, maar niet opgelost).
- **WARNING · SOURCE** — RESN-detectie is specifiek aan GEDCOM 7.0 gekoppeld; oudere, veelgebruikte GEDCOM 5.5.1-exports kennen een andere of ontbrekende RESN-structuur. Risico is benoemd, maar er is geen acceptatiecriterium voor versiedetectie of expliciete fallback wanneer een oudere GEDCOM-versie wordt aangeleverd.
- **INFO · SCOPE** — Het RESN-signaal dekt per ontwerp slechts het deel van de records dat als GEDCOM ophaalbaar is; dit gedeeltelijke bereik is correct benoemd als risico en moet in documentatie duidelijk worden onderscheiden van volledige dekking, om verkeerde verwachtingen bij vervolgiteraties te voorkomen.

## Geaccepteerde storykandidaten

### Persoonsniveau levend-detectie via de FamilySearch 110/95-jaarregel voor AVG-classificatie

Als privacy-classificatiemotor van hkh-autopilot wil ik de bestaande fail-closed AVG-classificatie (kandidaat 17) uitbreiden met een concreet, deterministisch detectiemechanisme voor 'vermoedelijk levende nabestaanden': voor elke in een record genoemde persoon (hoofdpersoon én familieleden) bepaal ik of deze 'vermoedelijk levend' is aan de hand van de gedocumenteerde FamilySearch-regel — geboortedatum ≤110 jaar geleden, of een geregistreerd huwelijk of de geboorte van een kind ≤95 jaar geleden, ÉN geen ingevulde overlijdens- of begrafenisgegevens. Zodra minstens één genoemde persoon als 'vermoedelijk levend' wordt gedetecteerd, blijft het totaaloordeel van het record 'Blocked'. Ontbrekende, onvolledige of onleesbare datumvelden worden fail-closed als 'vermoedelijk levend' behandeld, zodat er nooit een onterechte automatische vrijgave plaatsvindt. Dit vult het concrete detectiemechanisme in dat in kandidaat 17 nog impliciet was.

**Acceptatiecriteria**
- Gegeven een record met een genoemd familielid met geboortedatum ≤110 jaar geleden en zonder overlijdens-/begrafenisdatum, wanneer de classificatiefunctie draait, dan is de leeftijdsregel-uitkomst voor die persoon 'likely_living' en is het totaaloordeel van het record 'Blocked'.
- Gegeven een record met een genoemd familielid waarvan alleen een huwelijk of de geboorte van een kind ≤95 jaar geleden is geregistreerd en geen overlijdensdatum aanwezig is, dan is de uitkomst voor die persoon 'likely_living' en het record 'Blocked'.
- Gegeven een record waarin alle genoemde personen (hoofdpersoon en familieleden) een ingevulde overlijdens- of begrafenisdatum hebben, dan is de leeftijdsregel-uitkomst voor elk van hen 'deceased', en is het record — bij afwezigheid van andere blokkerende signalen — 'Processable'.
- Gegeven een record waarin voor een genoemde persoon het geboorte-, huwelijks- of overlijdensdatumveld ontbreekt of niet als geldige datum te parsen is, dan is de leeftijdsregel-uitkomst voor die persoon 'unknown_failclosed' en is het totaaloordeel van het record 'Blocked'.
- Een geautomatiseerde unit-testsuite voert minimaal de volgende synthetische recordvarianten in en verifieert de deterministische functie-uitvoer zonder menselijke tussenkomst: net onder de 110-jaargrens, net boven de 110-jaargrens, net onder/boven de 95-jaargrens voor huwelijk/kind, met overlijdensdatum aanwezig, met ontbrekend datumveld, met meerdere genoemde personen waarvan er één 'likely_living' is.
- De classificatiefunctie retourneert voor elk genoemd persoon een machineleesbaar resultaat (bijv. enum-waarde likely_living | deceased | unknown_failclosed) dat door een geautomatiseerde test kan worden uitgelezen zonder visuele inspectie.

Bronnen: [https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased](https://www.familysearch.org/en/help/helpcenter/article/how-does-family-tree-determine-whether-a-person-is-living-or-deceased), [https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree](https://www.familysearch.org/en/help/helpcenter/article/living-and-confidential-people-in-family-tree)

Afhankelijkheden: kandidaat 17: Deterministische AVG-classificatie voor overleden personen in genealogische records

Risico's: Interpretatieruimte bij het herkennen van 'huwelijk' of 'geboorte van een kind' als apart gebeurtenisveld wanneer het brondatamodel deze niet uniform structureert, wat tot inconsistente toepassing van de 95-jaargrens kan leiden., Fail-closed gedrag kan leiden tot een hoog aantal vals-positieve blokkades (over-blocking) bij onvolledige historische bronrecords, wat de bruikbaarheid van de dataset vermindert; dit is een bewuste privacyafweging maar moet gemonitord worden., Datumvelden met alleen een jaartal of onvolledige datums (bv. alleen maand/jaar) vereisen expliciete parseerregels; inconsistente parsing kan tot verkeerde classificatie leiden., De 110/95-jaarregel is een externe, niet-juridisch bindende praktijkregel van FamilySearch en geen wettelijke AVG-norm; dit moet in documentatie duidelijk worden onderscheiden van de wettelijke basis uit kandidaat 17.

### GEDCOM 7.0 RESN-tag als aanvullend blokkerend privacysignaal in de AVG-classificatie

Als privacy-classificatiemotor van hkh-autopilot wil ik, wanneer een brongegeven via de bestaande open-data-koppeling (kandidaat 18) in GEDCOM 7.0-formaat wordt opgehaald, de aanwezigheid van een RESN-structuur (CONFIDENTIAL, LOCKED of PRIVACY) op record- of feitniveau herkennen en als onafhankelijk, bindend blokkerend signaal meewegen in de classificatie uit kandidaat 17 — ongeacht de uitkomst van de leeftijdsregel. Is geen GEDCOM-bron beschikbaar, dan wordt het RESN-signaal expliciet als 'niet van toepassing' vastgelegd en blijft de classificatie afhankelijk van de overige, reeds bestaande signalen. Dit voegt een tweede, industriestandaard detectiesignaal toe zonder de scope van bestaande kandidaten te verbreden.

**Acceptatiecriteria**
- Gegeven een opgehaald GEDCOM 7.0-record met een RESN-waarde CONFIDENTIAL, LOCKED of PRIVACY op recordniveau, wanneer de classificatiefunctie draait, dan is het totaaloordeel van het record 'Blocked', ongeacht de leeftijdsregel-uitkomst van de genoemde personen.
- Gegeven een opgehaald GEDCOM 7.0-record met een RESN-waarde op het niveau van een individueel feit/gebeurtenis (niet op recordniveau), dan wordt dit eveneens als blokkerend signaal voor het gehele record herkend en resulteert in 'Blocked'.
- Gegeven een opgehaald GEDCOM 7.0-record zonder enige RESN-structuur en waarbij alle personen volgens de leeftijdsregel 'deceased' zijn, dan is het RESN-signaal 'none' en blokkeert dit signaal het record niet.
- Gegeven een brongegeven dat niet in GEDCOM-formaat beschikbaar is (bv. alleen JSON of RDF), dan wordt het RESN-signaal vastgelegd als 'not_applicable' en beïnvloedt het de classificatie-uitkomst niet.
- Een geautomatiseerde testsuite gebruikt minimaal vier synthetische GEDCOM-fixtures (zonder RESN, met RESN op recordniveau, met RESN op feitniveau, met een niet-GEDCOM bron) en verifieert per fixture de deterministische RESN-signaalwaarde en het resulterende totaaloordeel zonder menselijke tussenkomst.
- De functie die het GEDCOM-bestand parseert doorzoekt geneste structuren recursief op RESN-tags, zodat een RESN-markering op een subniveau (bv. binnen een specifieke gebeurtenis) niet wordt gemist.

Bronnen: [https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf](https://gedcom.io/specifications/FamilySearchGEDCOMv7.pdf), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php)

Afhankelijkheden: kandidaat 17: Deterministische AVG-classificatie voor overleden personen in genealogische records, kandidaat 18: Extern verificatie-anker via archieven.nl open data zonder autorisatietoken

Risico's: GEDCOM 7.0-parsing vereist correcte implementatie van de specificatie (versie 7.0.18); afwijkende of oudere GEDCOM-versies (bv. 5.5.1) kunnen een andere of ontbrekende RESN-structuur hebben, wat foutieve 'none'-classificaties kan veroorzaken als hier geen rekening mee wordt gehouden., Niet elk record is beschikbaar in GEDCOM-formaat, waardoor dit signaal slechts voor een deelverzameling van records daadwerkelijk toegevoegde waarde biedt; de aanvullende dekking moet niet worden verward met volledige dekking., Content negotiation naar GEDCOM 7.0 bij openarchieven.nl moet stabiel en reproduceerbaar zijn; wijzigingen in de externe API kunnen de beschikbaarheid van dit formaat beïnvloeden zonder dat hkh-autopilot dit controleert.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
