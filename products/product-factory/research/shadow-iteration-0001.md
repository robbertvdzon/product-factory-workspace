---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0001
date: 2026-08-08
status: approved
sources:
  - https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows
  - https://redis.io/blog/ai-human-in-the-loop/
  - https://air-governance-framework.finos.org/mitigations/mi-21_agent-decision-audit-and-explainability.html
  - https://agentic-design.ai/patterns/ui-ux-patterns
---
# Productcyclus 1

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoeksvraag voor deze eerste iteratie: hoe moet een dashboard/orchestratielaag voor autonome AI-agent-cycli (zoals Product Factory's eigen sturing van haar autonome iteraties) worden ingericht zodat menselijke gebruikers het prettig blijven vinden, het begrijpen en er controle over houden? Er zijn nog geen eerdere beoordeelde iteraties, dus deze vraag is autonoom afgeleid uit de productmissie ("prettig, begrijpelijk, aansluitend bij daadwerkelijk gebruik") toegepast op een zelfsturend orchestratieproduct. Vier publieke bronnen zijn geraadpleegd (webzoekopdrachten + volledige paginafetch) over dashboardarchitectuur voor agent-orchestratie, human-in-the-loop (HITL) versus human-on-the-loop (HOTL) besturingspatronen, uitlegbaarheid/auditability voor meerdere doelgroepen, en UI/UX-patronen voor transparantie en foutherstel in agentische systemen. Deze bevindingen leveren geen productbesluit, maar bouwen het feitendossier op waarmee een volgende stap onderbouwd kan worden. Belangrijk: alle bevindingen komen uit externe marketing-/kennisbronnen van derde partijen; ze zijn richtinggevend, niet normatief, en moeten in een volgende iteratie getoetst worden tegen Product Factory's eigen broncode, documentatie, gitgeschiedenis en productiedata, wat in deze researchstap niet is gedaan omdat de taak uitdrukkelijk vroeg om onafhankelijk webonderzoek.

### "Observability first, control second" als kernprincipe voor agent-orchestratiedashboards

Een dashboard voor het orchestreren van meerdere autonome agents heeft pas waarde als de status van alle lopende/afgeronde runs accuraat en binnen enkele seconden zichtbaar is; controlemogelijkheden (retry, pauzeren, goedkeuren) zijn pas bruikbaar als die observability klopt. Aanbevolen kernonderdelen: een 'fleet status overview' (status/laatste run/resultaat per agent, kleurcodering), een executietijdlijn om faalpatronen te herkennen, een foutenlog met classificatie (bijv. rate-limit, tool-auth-failure, timeout) in plaats van alleen een foutenteller, kostenanalyse per agent, en een 'human-in-the-loop inbox' met een wachtrij van acties die goedkeuring nodig hebben inclusief beslissingscontext. Foutclassificatie wordt expliciet belangrijker genoemd dan foutentelling, omdat het de juiste interventie stuurt.

Bronnen: [https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows](https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows)

### Drie besturingsmodellen: human-in-the-loop, human-on-the-loop, human-out-of-the-loop

Voor productie-AI-systemen die zelfstandig acties uitvoeren worden drie te onderscheiden oversight-modellen beschreven. Bij human-in-the-loop (HITL) neemt de mens de beslissing en wacht het systeem (synchroon interrupt-and-resume); bij human-on-the-loop (HOTL) werkt het systeem zelfstandig terwijl mensen monitoren en veto kunnen uitoefenen (asynchroon, leunt op monitoringdashboards en override-mogelijkheden); bij human-out-of-the-loop opereert het systeem volledig binnen vooraf gedefinieerde grenzen zonder tussenkomst tijdens uitvoering. De keuze bepaalt of de uitvoeringsarchitectuur synchroon of asynchroon moet zijn, met gevolgen voor state-persistentie (checkpoints) om een workflow te kunnen pauzeren en hervatten.

Bronnen: [https://redis.io/blog/ai-human-in-the-loop/](https://redis.io/blog/ai-human-in-the-loop/)

### Confidence-based escalation en gestructureerde review-wachtrijen als risicogetrapte interventie

In plaats van elke actie door een mens te laten beoordelen, wordt aangeraden alleen laag-vertrouwen-uitkomsten te escaleren. Een enkele confidence-score is onbetrouwbaar (een model kan hoog vertrouwen tonen bij een incorrecte voorspelling); een combinatie van een geaggregeerde trust-score en aparte risk-scores (die specifieke probleemcategorieën signaleren) vangt meer faalmodi. Reviewbeslissingen worden vastgelegd als workflow-status (pending/approved/rejected) die downstream-automatisering aanstuurt, en menselijke interventies kunnen als actief-leren-feedback teruggevoerd worden om toekomstige escalaties te verminderen.

Bronnen: [https://redis.io/blog/ai-human-in-the-loop/](https://redis.io/blog/ai-human-in-the-loop/)

### Uitlegbaarheid moet per doelgroep verschillen: gebruiker, technisch team, auditor

Het FINOS AIR Governance Framework (open source) beveelt aan om beslissingsverklaringen te laten verschillen per publiek: voor zakelijke/eindgebruikers natuurlijke-taal-samenvattingen van de agentredenering; voor technische teams gedetailleerde beslislogica inclusief confidence-scores en overwogen alternatieven; voor auditors/toezichthouders geformatteerde, manipulatiebestendige audit trails die voldoen aan compliance-kaders. Het raamwerk beschrijft ook een getrapt implementatiemodel (tiers 0-3) waarbij de auditintensiteit wordt afgestemd op het risiconiveau van de actie, van geen retentie bij laag risico tot uitgebreide, real-time gemonitorde trails bij hoog risico.

Bronnen: [https://air-governance-framework.finos.org/mitigations/mi-21_agent-decision-audit-and-explainability.html](https://air-governance-framework.finos.org/mitigations/mi-21_agent-decision-audit-and-explainability.html)

### Progressive disclosure en zichtbare redenering om cognitieve overbelasting te voorkomen

UI/UX-patronen voor mens-AI-interactie bij autonome agents benadrukken dat agentautonomie zichtbaar moet zijn in plaats van verborgen: real-time status van 'denken' en operationele activiteit, visualisatie van onzekerheid/betrouwbaarheid, en 'visual reasoning'-patronen die het besluitvormingsproces transparant tonen. Tegelijk wordt 'progressive disclosure' aangeraden om mogelijkheden en redenering geleidelijk te onthullen zodat gebruikers niet overspoeld raken. Foutherstel wordt het best ondersteund met graduele disclosure, concrete hersteladviezen en behoud van context, en met goedkeuringswachtrijen/escalatie die onderscheid maken tussen omkeerbare en onomkeerbare acties.

Bronnen: [https://agentic-design.ai/patterns/ui-ux-patterns](https://agentic-design.ai/patterns/ui-ux-patterns)

### Regelgevingsdruk (EU AI Act) verschuift audit-logging van best practice naar architectuurvereiste

De EU AI Act (Artikel 14) vereist effectief menselijk toezicht op hoog-risico AI-systemen, inclusief het kunnen interpreteren van uitkomsten, overrulen van beslissingen en stopzetten van de werking; Artikel 12 vereist dat aanbieders automatische logging inbouwen op ontwerpniveau, en Artikel 26 vereist dat toepassers die logs bewaren. Ook het NIST AI Risk Management Framework noemt human-in-the-loop als veelgebruikte risicomanagementstrategie en vraagt om gedefinieerde, beoordeelde en gedocumenteerde toezichtprocessen. Dit is relevante externe context voor het ontwerp van een audit-/logginglaag, ook al valt Product Factory zelf mogelijk niet onder deze regelgeving.

Bronnen: [https://redis.io/blog/ai-human-in-the-loop/](https://redis.io/blog/ai-human-in-the-loop/)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows) | 2026-08-08 | © 2012–2026 LowCode Agency. All Rights Reserved (paginafooter); geen expliciete open licentie gevonden — alleen als informatieve referentie te gebruiken, niet te hergebruiken zonder toestemming. | Concreet, recent (juli 2026) artikel met specifieke, bruikbare dashboardcomponenten (fleet status, foutclassificatie, HITL-inbox) direct relevant voor Product Factory's eigen orchestratiedashboard. |
| [bron](https://redis.io/blog/ai-human-in-the-loop/) | 2026-08-08 | Corporate blogpost (Redis), impliciet alle rechten voorbehouden; geen open licentie zichtbaar op de pagina — alleen als informatieve referentie te gebruiken. | Diepgaand, recent (april 2026) overzicht van HITL/HOTL-besturingspatronen, escalatiepatronen en regelgeving (EU AI Act, NIST AI RMF), direct toepasbaar op de vraag hoe menselijke controle over een autonome productcyclus in te richten. |
| [bron](https://air-governance-framework.finos.org/mitigations/mi-21_agent-decision-audit-and-explainability.html) | 2026-08-08 | CC-BY-4.0 gelicenseerd (FINOS / Fintech Open Source Foundation) — hergebruik met naamsvermelding toegestaan. | Open-source governanceraamwerk met concrete, doelgroep-specifieke richtlijnen voor uitlegbaarheid en auditability van agentbeslissingen, relevant voor de begrijpelijkheid-doelstelling van Product Factory's eigen orchestratie. |
| [bron](https://agentic-design.ai/patterns/ui-ux-patterns) | 2026-08-08 | © 2026 KORTEXYA SAS. All rights reserved (paginafooter); geen open licentie gevonden — alleen als informatieve referentie te gebruiken. | Gestructureerd overzicht van UI/UX-patronen specifiek voor transparantie, controle, statuscommunicatie en foutherstel bij autonome AI-agents, direct relevant voor de 'prettig en begrijpelijk'-doelstelling van het dashboard. |

## Productbeslissing

Voor deze eerste iteratie richt Product Factory zich uitsluitend op de observability-basis van haar eigen autonome cyclusrapportage, niet op nieuwe controlemechanismen. Concreet: bestaande statusrapportage van iteraties wordt uitgebreid met een gestructureerde uitkomstclassificatie (bijv. onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen) in plaats van alleen geslaagd/mislukt, en elke iteratie toont standaard een korte 'waarom'-samenvatting met de volledige redenering optioneel uitklapbaar (progressive disclosure). Het toezichtmodel blijft human-on-the-loop voor de doorlopende cyclus (de eigenaar monitort en kan ingrijpen) gecombineerd met het bestaande human-in-the-loop-moment waarbij de eigenaar elke voorgestelde richting/wijziging expliciet goedkeurt voordat deze wordt doorgevoerd. Er wordt in deze iteratie geen confidence-scoring, geen auto-escalatie, geen doelgroep-gedifferentieerde (auditor-grade) uitleglaag en geen nieuwe authenticatie- of Software Factory-koppeling gebouwd; dat wordt pas overwogen zodra een volgende iteratie met echte gebruiksdata aantoont dat de behoefte er is. Deze richting is bewust klein en incrementeel: ze raakt alleen de rapportage-/weergavelaag van bestaande statusdata, vereist geen extern toegangstoken, is in isolatie te beoordelen door de eigenaar en volledig terug te draaien zonder gevolgen voor hkh, hkh-autopilot of de Software Factory-uitvoeringspaden.

**Waarom:** De missie vraagt continue zelftoetsing op prettig-in-gebruik, begrijpelijkheid en aansluiting bij daadwerkelijk gebruik. Omdat dit de eerste iteratie is zonder eerdere beoordeelde cycli en zonder gevalideerde gebruiksdata over Product Factory's eigen orchestratielaag, is de veiligste en meest onderbouwde stap er één die klein, omkeerbaar en puur op de rapportagelaag gericht is — precies wat de bronnen aanraden ('observability first, control second') en wat de kwaliteitsregel vereist (uitleg van huidig gedrag, isoleerbaar, terugdraaibaar). Zwaardere patronen uit het onderzoek (confidence-based escalatie, auditor-grade audit trails, doelgroep-tiers) zijn waardevol maar prematuur: ze vergroten de blast radius, veronderstellen gebruiksbehoeften die nog niet zijn getoetst, en raken sneller aan de guardrails rond authenticatie en Software Factory-koppeling. Door nu alleen classificatie en zichtbare, uitklapbare redenering toe te voegen, blijft het bestaande human-in-the-loop-goedkeuringsmoment intact terwijl de eigenaar via monitoring (human-on-the-loop) beter zicht krijgt op patronen — een stap die zichzelf kan bewijzen voordat er verder wordt geïnvesteerd.

### Prioriteiten
- Observability vóór control: eerst gestructureerde uitkomstclassificatie, geen nieuwe interventieknoppen
- Human-on-the-loop monitoring voor de doorlopende cyclus, met behoud van het bestaande human-in-the-loop-goedkeuringsmoment per wijziging
- Progressive disclosure: korte 'waarom'-samenvatting standaard zichtbaar, volledige redenering optioneel
- Geen nieuwe authenticatie, Software Factory-koppeling of aanraking van andere producten in deze iteratie
- Confidence-scoring, risicoscores en auditor-grade audit trails pas bouwen als gebruik dat rechtvaardigt

### Besluiten
- **Prioriteer voor de eerste iteratie observability boven control: voeg aan Product Factory's eigen iteratie-/statusrapportage een gestructureerde uitkomstclassificatie toe (bijv. 'onderzoek-onvoldoende', 'guardrail-conflict', 'richting-gekozen', 'richting-verworpen') in plaats van alleen een geslaagd/mislukt-teller, vóórdat enige nieuwe controlefunctionaliteit (goedkeuringsknoppen, escalatie) wordt gebouwd.** — De bron stelt expliciet dat een orchestratiedashboard pas waarde heeft als de status van runs accuraat zichtbaar is, en dat foutclassificatie belangrijker is dan foutentelling omdat het de juiste interventie stuurt. Dit is de kleinste, direct terug te draaien wijziging (alleen rapportagelaag, geen gedragswijziging van de cyclus zelf) en voldoet aan de kwaliteitsregel dat een wijziging in isolatie beoordeelbaar moet zijn.
- **Hanteer human-on-the-loop (monitoren + veto) als standaard toezichtmodel voor de doorlopende autonome cyclus van Product Factory zelf, terwijl het bestaande human-in-the-loop-moment (eigenaar beoordeelt elke voorgestelde richting/PR) behouden blijft als synchrone goedkeuringsstap voor daadwerkelijke wijzigingen.** — De bron onderscheidt HITL (synchroon, blokkerend) van HOTL (asynchroon, monitoren met veto). Product Factory draait al autonoom tussen goedkeuringsmomenten door (shadow-taken); volledige HITL op elke tussenstap zou de missie van 'continue zelftoetsing' vertragen zonder aantoonbare meerwaarde, terwijl volledig loslaten (human-out-of-the-loop) ingaat tegen de eis dat de eigenaar controle houdt.
- **Pas progressive disclosure toe op de weergave van redenering: elke iteratie toont standaard een korte 'waarom'-samenvatting (aansluitend bij de kwaliteitsregel dat een wijziging moet uitleggen waarom het huidige gedrag zo was), met de volledige redeneerketen optioneel uitklapbaar — niet standaard getoond.** — De bron benadrukt dat agentredenering zichtbaar moet zijn zonder gebruikers te overspoelen; progressive disclosure voorkomt cognitieve overbelasting terwijl het toch aan de bestaande kwaliteitsregel voldoet. Dit is een presentatiekeuze, geen architectuurwijziging, dus laag risico en makkelijk terug te draaien.
- **Stel de bouw van confidence-/risk-scoregebaseerde auto-escalatie en van doelgroep-gedifferentieerde uitlegniveaus (zakelijk versus technisch versus auditor-grade audit trail) uit tot een latere iteratie, tot echt gebruik aantoont dat de eigenaar meerdere uitlegniveaus nodig heeft.** — Beide bronnen beschrijven waardevolle patronen, maar ze introduceren aanzienlijke complexiteit (scoringmodellen, gemanipuleerbestendige audittrails) zonder dat er nu gebruiksdata is die de behoefte bevestigt. Dit past bij de missie om te toetsen aan 'hoe hij daadwerkelijk gebruikt wordt' vóór uitbreiding, en voorkomt overbouw die niet in isolatie te rechtvaardigen is.
- **Beperk deze iteratie expliciet tot de rapportage-/weergavelaag van Product Factory's eigen orchestratie; raak geen authenticatie, geen koppeling met de Software Factory-uitvoeringspaden en geen data van andere producten aan.** — De guardrails vragen extra terughoudendheid bij migraties, authenticatie en de Software Factory-koppeling. Een wijziging beperkt tot classificatie en weergave van reeds bestaande statusdata is functioneel geïsoleerd, vereist geen nieuwe externe toegang en is dus zonder token-actie van de eigenaar uitvoerbaar en terug te draaien.

## UX-voorstel: Iteratie-uitkomstclassificatie & uitklapbare "waarom"-redenering in het Product Factory dashboard

**Gebruikersdoel:** Als eigenaar van Product Factory wil ik in het bestaande iteratieoverzicht in één oogopslag zien wélk type uitkomst elke autonome iteratie had (niet enkel geslaagd/mislukt) en waarom, zodat ik de doorlopende cyclus comfortabel kan monitoren (human-on-the-loop) zonder overspoeld te raken, terwijl het bestaande goedkeuringsmoment per voorgestelde wijziging (human-in-the-loop) ongewijzigd blijft.

### Flow
1. Eigenaar opent het bestaande Product Factory iteratieoverzicht (geen nieuwe route, geen nieuwe authenticatie).
2. Overzicht toont per iteratierij een classificatiebadge met vaste waarden: onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen (in plaats van alleen geslaagd/mislukt).
3. Naast elke badge staat standaard een korte 'waarom'-samenvatting van 1-2 zinnen, zichtbaar zonder extra klik.
4. Eigenaar kan per rij een 'toon volledige redenering'-toggle (button met aria-expanded) activeren om de volledige onderzoeks-/besluitketen uit te klappen (progressive disclosure); dit is puur client-side weergave van reeds bestaande data.
5. Eigenaar kan de lijst filteren op classificatiewaarde om patronen te herkennen (bv. herhaalde guardrail-conflict-uitkomsten).
6. Als een iteratie een concrete wijziging voorstelt, blijft de bestaande link/knop naar de PR-goedkeuringsflow ongewijzigd zichtbaar in de uitgeklapte detailweergave.
7. Eigenaar klapt de redenering weer in of navigeert terug naar het overzicht; filterstatus blijft behouden binnen de sessie.

### Wireframe

[Product Factory · Iteratieoverzicht]
--------------------------------------------------------------
Filter: ( Alle ) ( Onderzoek-onvoldoende ) ( Guardrail-conflict ) ( Richting-gekozen ) ( Richting-verworpen )
--------------------------------------------------------------
Rij 1
  [Badge: RICHTING-GEKOZEN] iteratie-hkh-autopilot-0023 · 2026-08-08
  Waarom: "Observability vóór control gekozen; classificatielaag toegevoegd zonder nieuwe interventie."
  [ Toon volledige redenering ▾ ]  [ Bekijk voorgestelde wijziging → bestaande PR-goedkeuringsflow ]
--------------------------------------------------------------
Rij 2
  [Badge: GUARDRAIL-CONFLICT] iteratie-hkh-autopilot-0022 · 2026-08-05
  Waarom: "Voorstel raakte authenticatielaag; geblokkeerd door guardrail, geen wijziging voorgesteld."
  [ Toon volledige redenering ▾ ]
--------------------------------------------------------------
Rij 3 (uitgeklapt voorbeeld)
  [Badge: ONDERZOEK-ONVOLDOENDE] iteratie-x-0021 · 2026-08-01
  Waarom: "Onvoldoende bronnen om richting te onderbouwen."
  [ Verberg volledige redenering ▴ ]
    > Onderzoeksvraag: ...
    > Geraadpleegde bronnen (met licentie-indicatie): ...
    > Overwogen opties en waarom verworpen: ...
    > Besluit: geen richting gekozen, volgende iteratie herhaalt onderzoek met scherpere vraag.
--------------------------------------------------------------
(Geen wijzigingen aan bestaande navigatie, koppen of PR-goedkeuringsscherm; alleen badge, samenvatting, toggle en filter zijn nieuw.)

### Interactiehypotheses
- H1 (herkenbaarheid): Classificatiebadges (4 vaste waarden) i.p.v. alleen geslaagd/mislukt zijn voor elke iteratie-rij aanwezig en tekstueel onderscheidend gerenderd — toetsbaar met een geautomatiseerde DOM/snapshot-test die controleert dat elke iteratierij precies één van de vier badge-teksten bevat en dat badge-tekst nooit alleen via kleur wordt gecommuniceerd.
- H2 (progressive disclosure werkt): Bij initial page load bevat de DOM per iteratie alleen de korte 'waarom'-samenvatting (meetbaar: samenvattingslengte ≤ vaste karaktergrens, bv. 280 tekens) en verschijnt de volledige redenering pas in de DOM ná een klik/toets-activatie op de toggle — toetsbaar via geautomatiseerde e2e-test die DOM-inhoud vóór en na toggle-interactie vergelijkt.
- H3 (filter reduceert scan-inspanning): Filteren op één classificatiewaarde retourneert uitsluitend rijen met die badge-waarde en een kleiner aantal zichtbare rijen dan de ongefilterde lijst — toetsbaar via geautomatiseerde test die filter toepast en asserts dat alle getoonde rijen de gekozen classificatie hebben.
- H4 (geen regressie op bestaand goedkeuringspad): De bestaande link/knop naar de PR-goedkeuringsflow blijft voor iteraties met een voorgestelde wijziging exact naar dezelfde bestemming verwijzen als vóór deze wijziging — toetsbaar via geautomatiseerde e2e-test die de href/route vergelijkt met een vastgelegde baseline.
- H5 (toetsenbord- en screenreader-bruikbaarheid van de toggle): De 'toon volledige redenering'-toggle is bereikbaar en bedienbaar met uitsluitend het toetsenbord (Tab + Enter/Space) en communiceert zijn staat via aria-expanded — toetsbaar via geautomatiseerde toegankelijkheidstest (bv. axe-core) die aria-expanded-attribuut en toetsenbordfocus-volgorde valideert.

### Toegankelijkheid
- Classificatie mag nooit uitsluitend via kleur worden gecommuniceerd; elke badge heeft een tekstlabel zodat schermlezers en kleurenblinde gebruikers de classificatie kunnen onderscheiden.
- De 'toon volledige redenering'-toggle is een echt <button>-element met aria-expanded={true|false} en een aria-controls-koppeling naar het uitklapbare tekstblok, volledig bedienbaar met toetsenbord (Tab-volgorde, Enter/Space) zonder muis.
- Kleurcontrast van badge-tekst en achtergrond voldoet aan WCAG 2.1 AA (minimaal 4.5:1 voor normale tekst), geverifieerd met een geautomatiseerde contrastcheck (bv. axe-core) in plaats van handmatige visuele controle.
- Filterknoppen zijn als toggle-buttons met aria-pressed geïmplementeerd zodat schermlezergebruikers de actieve filterstatus horen.
- Focusvolgorde blijft logisch na uitklappen: focus verplaatst niet onverwacht weg van de geactiveerde toggle, zodat toetsenbordgebruikers niet de context verliezen.

### Privacy
- Uitsluitend operationele metadata van Product Factory zelf (iteratie-ID, classificatie, samenvatting, tijdstip, bronvermeldingen) wordt getoond; geen persoonsgegevens en geen gebruikersdata van hkh, hkh-autopilot of andere producten worden verwerkt of weergegeven.
- De volledige redenering die via progressive disclosure uitklapt bevat alleen reeds bestaande, niet-persoonlijke onderzoeks- en besluitdata (bronnen, overwegingen); er wordt geen nieuwe dataverzameling of externe koppeling toegevoegd om deze weergave te realiseren.
- Er wordt geen nieuwe authenticatie, toegangstoken of Software Factory-koppeling geïntroduceerd voor deze functionaliteit; de weergave hergebruikt uitsluitend data die al beschikbaar is binnen het bestaande, reeds beveiligde iteratieoverzicht.
- Bronvermeldingen in de redenering tonen alleen URL en licentie-indicatie van geraadpleegde publieke bronnen, geen herpublicatie van volledige externe content, om rechten van derden te respecteren.
- Filtervoorkeuren worden alleen lokaal/sessiegebonden onthouden, niet gekoppeld aan een identificeerbaar gebruikersprofiel buiten de reeds bestaande eigenaarsessie.

## Kritische beoordeling

**Oordeel:** ACCEPT

Eén kandidaat beoordeeld: het toevoegen van vier vaste uitkomstclassificatie-badges aan het bestaande iteratieoverzicht, ter vervanging van een impliciete geslaagd/mislukt-status. De kandidaat is klein, geïsoleerd tot de rapportagelaag, raakt geen authenticatie/Software Factory-koppeling, is volledig agent-uitvoerbaar (geen handmatige test, accountaanmaak, betaling of andere eigenaarsactie vereist) en heeft sterke, geautomatiseerd verifieerbare acceptatiecriteria voor toegankelijkheid (WCAG AA-contrast, aria-expanded/aria-pressed, geen kleur-only signalering) en regressiebescherming van de bestaande PR-goedkeuringsflow. Privacy is in orde: uitsluitend operationele metadata van Product Factory zelf, geen persoonsgegevens. Er zijn twee niet-blokkerende aandachtspunten: (1) de onderliggende productrichting is volledig afgeleid uit externe, deels rechtenbeperkte webbronnen zonder toetsing aan Product Factory's eigen broncode/data — de researchsamenvatting erkent dit zelf expliciet; (2) de factische aanname dat het huidige overzicht slechts een impliciete geslaagd/mislukt-status toont is niet aantoonbaar geverifieerd tegen de actuele broncode. Beide worden voldoende ondervangen doordat de kandidaat expliciet vereist dat de mapping-logica getest en met een expliciet fallback-gedrag wordt geïmplementeerd, wat de implementerende agent dwingt de werkelijke databron te inspecteren in plaats van aannames te doen. Geen BLOCKING issues gevonden; kandidaat is vrijgegeven voor levering.
- **WARNING · SOURCE** — De productrichting en prioriteiten (decisions/priorities/productDirection) zijn volledig afgeleid uit vier externe webbronnen (LowCode Agency, Redis, FINOS, agentic-design.ai) en expliciet nog niet getoetst aan Product Factory's eigen broncode, documentatie, gitgeschiedenis of productiedata, zoals de researchsamenvatting zelf erkent. De 'bronnen'-regel vereist onderbouwing met eigen bronnen, niet aannames. Dit blokkeert de huidige kandidaat niet omdat de acceptatiecriteria de implementerende agent dwingen de eigen databron te verifiëren, maar een volgende iteratie moet deze externe bevindingen alsnog expliciet toetsen aan het eigen systeem.
- **WARNING · SOURCE** — De kandidaat stelt als feitelijke premisse dat het bestaande iteratieoverzicht 'momenteel alleen een impliciete geslaagd/mislukt-status' toont, zonder dat dit blijkt te zijn geverifieerd tegen de actuele broncode van het dashboard. Dit is een aanname over bestaand gedrag die volgens de 'bronnen'-regel eigenlijk eerst in eigen code bevestigd moet worden.
- **INFO · RIGHTS** — Twee van de vier geraadpleegde bronnen (LowCode Agency, agentic-design.ai) hebben expliciet geen open licentie ('alleen als informatieve referentie, niet te hergebruiken zonder toestemming'). De kandidaat zelf republiceert geen externe content in de UI, dus dit vormt geen risico voor déze kandidaat, maar moet bewaakt blijven als latere iteraties bronvermeldingen/redenering in de UI tonen.
- **INFO · CONSISTENCY** — De kandidaat legt niet uit waarom het huidige geslaagd/mislukt-gedrag oorspronkelijk zo was ontworpen (kwaliteitsregel vereist uitleg van bestaand gedrag). Dit is een kleine omissie die de isoleerbaarheid en terugdraaibaarheid niet aantast, maar bij implementatie kan worden meegenomen in de PR-beschrijving.
- **INFO · SCOPE** — Het risico dat bestaande iteratiedata onvoldoende structuur biedt om betrouwbaar tussen de vier classificatiewaarden te onderscheiden is correct benoemd in de kandidaat zelf en wordt ondervangen door een vereiste unit-test met expliciet fallback-gedrag. Dit is een goed voorbeeld van adequate risicomitigatie zonder aannames.

## Geaccepteerde storykandidaten

### Vervang geslaagd/mislukt-indicator door vaste uitkomstclassificatie-badges in het iteratieoverzicht

In het bestaande Product Factory iteratieoverzicht toont elke iteratierij momenteel alleen een impliciete geslaagd/mislukt-status. Voeg een classificatiebadge toe met exact één van vier vaste waarden — onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen — afgeleid uit reeds bestaande iteratie-uitkomstdata (geen nieuwe dataverzameling). Dit is uitsluitend een wijziging in de rapportage-/weergavelaag van het bestaande overzicht: geen nieuwe route, geen nieuwe authenticatie, geen koppeling met Software Factory-uitvoeringspaden en geen aanpassing van de bestaande PR-goedkeuringsflow. Doel is dat de eigenaar in één oogopslag het type uitkomst van elke autonome iteratie herkent (observability vóór control), zonder dat er nieuwe interventiemogelijkheden worden toegevoegd.

**Acceptatiecriteria**
- Elke iteratierij in het bestaande overzicht toont exact één classificatiebadge met een van de vier vaste tekstwaarden: onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen.
- Een geautomatiseerde DOM/snapshot-test bevestigt dat elke gerenderde iteratierij precies één van de vier toegestane badge-teksten bevat en geen vrije tekst of andere waarden.
- De badge communiceert de classificatie via een tekstlabel dat programmatisch leesbaar is (bijv. in de accessible name), niet uitsluitend via kleur; dit is geautomatiseerd geverifieerd (bijv. met axe-core of een DOM-inhoudscontrole).
- Kleurcontrast tussen badge-tekst en badge-achtergrond voldoet voor elk van de vier badge-varianten aan WCAG 2.1 AA (minimaal 4.5:1 voor normale tekst), geverifieerd met een geautomatiseerde contrastcheck (bijv. axe-core) in de testsuite.
- De bestaande link/knop naar de PR-goedkeuringsflow blijft voor iteraties met een voorgestelde wijziging exact naar dezelfde bestemming (href/route) verwijzen als vóór deze wijziging, bevestigd met een geautomatiseerde regressietest tegen een vastgelegde baseline.
- De mapping-logica die bestaande iteratie-uitkomstdata omzet naar een van de vier classificatiewaarden is met unit tests gedekt, inclusief een expliciet gedrag (bijv. fallback-waarde of build-fout) voor het geval bestaande data niet ondubbelzinnig op een van de vier waarden te mappen is.
- Geen enkele test of codewijziging raakt authenticatie, nieuwe routes, of de koppeling met Software Factory-uitvoeringspaden; bestaande end-to-end tests voor het iteratieoverzicht blijven slagen zonder aanpassing van hun verwachte navigatiepaden.

Bronnen: [https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows](https://www.lowcode.agency/blog/how-to-build-an-ai-agent-orchestration-dashboard-for-complex-workflows), [https://agentic-design.ai/patterns/ui-ux-patterns](https://agentic-design.ai/patterns/ui-ux-patterns)

Afhankelijkheden: Bestaande iteratiedata moet voldoende informatie bevatten om ondubbelzinnig te mappen naar een van de vier classificatiewaarden (onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen); indien dit ontbreekt moet de mapping-logica dit expliciet en getest afvangen.

Risico's: Bestaande iteratiedata bevat mogelijk niet genoeg structuur om betrouwbaar te onderscheiden tussen 'onderzoek-onvoldoende' en 'guardrail-conflict', wat tot foutieve classificatie kan leiden., Vervangen van de impliciete geslaagd/mislukt-weergave door vier nieuwe waarden kan bestaande automatiseringen of tests die op de oude status vertrouwen laten breken als deze niet zijn meegenomen in de regressietests., Vaste badge-waarden zijn mogelijk niet toereikend voor toekomstige, nog onbekende uitkomsttypen, wat een latere uitbreiding van de classificatieset noodzakelijk kan maken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
