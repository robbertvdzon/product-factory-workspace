---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0014
date: 2026-08-07
status: approved
sources:
  - https://www.historischekringheemskerk.nl/
  - https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html
  - https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
  - https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html
  - https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
  - https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
  - https://docs.flutter.dev/ui/accessibility/web-accessibility
  - https://docs.flutter.dev/testing/code-debugging
---
# Shadow-iteratie 14

**Focus:** Herstel de inhoudelijk geaccepteerde homepage-richting uit iteratie 13 na de technische workspace-publicatiefout. Lever precies één kleine direct bouwbare Flutter-implementatiestory voor een minder technische, duidelijkere publieke homepage. Vermijd rechtenbeheer, accounts, backendwijzigingen en losse onderzoeksstories. Behoud laden en foutafhandeling; maak interacties toegankelijk en leg concrete verificatie vast.

## Onderzoek

Onderzoek afgerond zonder productbesluit of story. De publieke HKH-site bevestigt een lokaal-historische, publieksgerichte context met onder meer nieuws, activiteiten en een wandeling, maar de daadwerkelijke hkh-autopilot-homepage, ontdekroute en laad-/foutimplementatie zijn niet publiek verifieerbaar aangetroffen. Die onderdelen blijven dus onbevestigd.

### Publieke HKH-context bevat meerdere ingangen naar lokale geschiedenis

De geraadpleegde HKH-homepage presenteert nieuws, evenementen en onder meer een wandeling door oud Heemskerk. Dit onderbouwt alleen de historische publiekscontext; het bevestigt niet dat hkh-autopilot dezelfde navigatie, tekst of route gebruikt.

Bronnen: [https://www.historischekringheemskerk.nl/](https://www.historischekringheemskerk.nl/)

### De bestaande app-homepage en toestanden zijn niet vastgesteld

De geraadpleegde publieke HKH-pagina beschrijft geen hkh-autopilot-Flutterapp, concrete primaire ontdekroute, of zichtbare laad-, succes- en foutweergave. Daarom is niet vastgesteld of een toekomstige wijziging een bestaande route of statuspresentatie behoudt; dit moet uit de feitelijke app-implementatie of een publieke live-versie worden geverifieerd.

Bronnen: [https://www.historischekringheemskerk.nl/](https://www.historischekringheemskerk.nl/), [https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html)

### FutureBuilder is hoogstens een voorwaardelijke technische referentie

Als de app FutureBuilder gebruikt, kan de builder een waiting-snapshot en daarna een done-snapshot met data of fout ontvangen. De Flutter-documentatie bewijst echter niet dat HKH deze widget gebruikt; er kan geen feitelijke toestandsmatrix voor de app uit worden afgeleid.

Bronnen: [https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html)

### Zichtbare dynamische status vraagt programmatische waarneembaarheid

WCAG 2.2 SC 4.1.3 vereist voor statusmeldingen die zonder focus verschijnen een programmatisch bepaalbare rol of eigenschap. De toelichting noemt wachtstatus en fouten expliciet als mogelijke statusmeldingen en waarschuwt dat te veel live updates schermlezers te spraakzaam kunnen maken. Flutter kan een semantische live region markeren, maar aankondiging blijft platformafhankelijk.

Bronnen: [https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html](https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html)

### Concrete toegankelijkheidsdrempels voor latere verificatie

Voor normale tekst geldt WCAG 2.2 AA minimaal 4,5:1 contrast; voor grote tekst minimaal 3:1. Voor pointerdoelen geldt minimaal 24×24 CSS-pixels, tenzij een expliciete uitzondering zoals voldoende tussenruimte van toepassing is. Een eis van 48×48 is dus geen WCAG-AA-minimum zonder afzonderlijke productrichtlijn.

Bronnen: [https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

### Flutter-websemantiek moet in de doelomgeving worden gecontroleerd

Flutter web zet de interne Semantics-boom om naar een toegankelijke HTML-DOM, maar toegankelijkheid staat volgens de Flutter-documentatie niet standaard aan wegens prestaties. Een toekomstige handmatige browser-/schermlezercontrole is daarom nodig naast widget- of semantische tests; uit de documentatie volgt geen bewijs van feitelijke HKH-ondersteuning of testdekking.

Bronnen: [https://docs.flutter.dev/ui/accessibility/web-accessibility](https://docs.flutter.dev/ui/accessibility/web-accessibility), [https://docs.flutter.dev/testing/code-debugging](https://docs.flutter.dev/testing/code-debugging)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://www.historischekringheemskerk.nl/) | 2026-08-07 | Onbekend; bij de geraadpleegde openbare zoekweergave is geen licentie- of rechtenverklaring vastgesteld. | Primaire publieke bron voor de actuele, door HKH gepresenteerde historische publiekscontext en zichtbare soorten ingangen. |
| [bron](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html) | 2026-08-07 | Onbekend; op de geraadpleegde API-pagina is geen licentie- of rechtenverklaring vastgesteld. | Officiële API-referentie voor mogelijke waiting-, succes- en fout-snapshots, uitsluitend voorwaardelijk gebruikt. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | 2026-08-07 | W3C Document License; de geraadpleegde W3C Understanding-pagina is informatief, niet zelf normatief. | Legt de betekenis en programmatische waarneembaarheid van statusmeldingen uit. |
| [bron](https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html) | 2026-08-07 | Onbekend; op de geraadpleegde API-pagina is geen licentie- of rechtenverklaring vastgesteld. | Officiële Flutter-API-beschrijving van live regions en de mogelijke beleefde aankondiging. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | 2026-08-07 | W3C Document License; de geraadpleegde W3C Understanding-pagina is informatief, niet zelf normatief. | Geeft de concrete WCAG-AA-contrastdrempels voor tekst. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | 2026-08-07 | W3C Document License; de geraadpleegde W3C Understanding-pagina is informatief, niet zelf normatief. | Geeft de concrete WCAG-AA-minimummaat en uitzonderingen voor pointerdoelen. |
| [bron](https://docs.flutter.dev/ui/accessibility/web-accessibility) | 2026-08-07 | Creative Commons Attribution 4.0 voor documentatie; codevoorbeelden BSD 3-Clause, zoals op de geraadpleegde pagina vermeld. | Officiële Flutter-documentatie over Semantics, toegankelijke HTML-DOM en het inschakelen van webtoegankelijkheid. |
| [bron](https://docs.flutter.dev/testing/code-debugging) | 2026-08-07 | Creative Commons Attribution 4.0 voor documentatie; codevoorbeelden BSD 3-Clause, volgens de licentieverklaring van Flutter Docs. | Officiële Flutter-documentatie over het inspecteren van de Semantics-boom bij verificatie. |

## Productbeslissing

Maak de eerste, nog te verifiëren ontdekingang naar lokale geschiedenis robuust toegankelijk: geef laden, beschikbare inhoud en fouten als korte, begrijpelijke statusmeldingen weer, zonder de bestaande route of inhoudsstructuur te wijzigen voordat die is vastgesteld.

**Waarom:** Dit is een kleine, toetsbare verbetering die de missie ondersteunt: bezoekers mogen niet vastlopen voordat zij lokale verhalen, activiteiten of een wandeling kunnen ontdekken. De publieke HKH-context bevestigt zulke publieksingangen, maar niet de feitelijke app-route of huidige toestanden. Daarom is routebehoud een expliciete aanname en start uitvoering pas na verificatie in de app of live-versie. Statusmeldingen zijn relevant voor toegankelijke voortgang en fouten; live-aankondigingen moeten beperkt blijven.

### Prioriteiten
- Verifieer eerst welke homepage- of ontdekroute daadwerkelijk inhoud laadt en welke huidige laad-, succes- en fouttoestanden bestaan.
- Definieer per geverifieerde toestand één korte, zichtbare en programmatisch waarneembare statusmelding.
- Toets de aangepaste toestand handmatig in de Flutter-webdoelomgeving, inclusief semantiek en schermlezerervaring.
- Controleer tekstcontrast en interactiedoelen tegen de genoemde WCAG-AA-drempels; voeg geen strengere maatregel toe zonder productbesluit.

### Besluiten
- **Kies statushelderheid in de eerste ontdekervaring als enige productrichting.** — Dit verlaagt een directe drempel naar historische inhoud zonder onbevestigde navigatie of nieuwe content te introduceren.
- **Behoud route en inhoudsopbouw totdat de feitelijke app is geverifieerd.** — De beschikbare bronnen bevestigen geen hkh-autopilot-homepage, primaire route of bestaande toestandspresentatie.
- **Beperk live-statussen tot betekenisvolle laad- en foutmomenten en verifieer semantiek in de doelbrowser.** — Statusmeldingen moeten programmatisch bepaalbaar zijn, terwijl overmatige live-updates hinderlijk kunnen zijn; Flutter-websemantiek en aankondigingen vragen praktijkcontrole.

## UX-voorstel: MVP: toegankelijke status in de eerste geverifieerde ontdekroute

**Gebruikersdoel:** Als bezoeker wil ik begrijpen of lokale historische inhoud wordt geladen, beschikbaar is of niet kan worden opgehaald, zodat ik niet vastloop vóór ik de inhoud kan ontdekken.

### Flow
1. Open de feitelijk geverifieerde homepage of ontdekroute; behoud bestaande navigatie en inhoudsvolgorde.
2. Toon bij het starten één korte zichtbare status: ‘Inhoud wordt geladen.’
3. Kondig deze laadstatus programmatisch aan zonder focus te verplaatsen.
4. Bij succes verdwijnt de laadstatus en verschijnt de bestaande inhoud ongewijzigd; kondig alleen aan: ‘Inhoud geladen.’
5. Bij een fout toon je een duidelijke foutmelding met een actie ‘Opnieuw proberen’.
6. Na ‘Opnieuw proberen’ krijgt de gebruiker opnieuw één laadstatus, gevolgd door inhoud of dezelfde foutmelding.
7. Verifieer de volledige flow met toetsenbord, schermlezer en in de daadwerkelijke Flutter-webdoelomgeving.

### Wireframe

[Bestaande paginakop en navigatie]\n\n[Hoofdinhoud / bestaande ontdekroute]\n  Statusgebied (altijd op dezelfde plek)\n  - Laden: ‘Inhoud wordt geladen.’\n  - Succes: ‘Inhoud geladen.’ (kort, daarna verborgen)\n  - Fout: ‘De inhoud kan nu niet worden geladen.’\n          [Opnieuw proberen]\n\n[Bestaande inhoud verschijnt uitsluitend bij succes; structuur en route blijven behouden]

### Interactiehypotheses
- Minstens 90% van de testdeelnemers kan na een laad- of fouttoestand correct benoemen wat er gebeurt en wat de volgende actie is.
- Toetsenbordgebruikers bereiken ‘Opnieuw proberen’ in de natuurlijke leesvolgorde, activeren de knop met Enter of spatie, en behouden een voorspelbare focuspositie.
- Schermlezergebruikers ontvangen precies één relevante aankondiging per toestandsovergang, zonder herhaalde of storende meldingen.
- De foutactie verlaagt het aandeel sessies dat na een mislukte laadpoging zonder vervolgstap stopt, vergeleken met de huidige geverifieerde ervaring.

### Toegankelijkheid
- Gebruik semantisch en programmatisch waarneembaar statusgebied voor laden en fout; verplaats focus niet automatisch naar statusmeldingen.
- Zorg dat ‘Opnieuw proberen’ een echte, benoemde knop is, volledig bedienbaar met toetsenbord en zichtbaar gefocust.
- Houd lees- en focusvolgorde gelijk aan de visuele volgorde; laat bestaande navigatie en inhoudsstructuur intact.
- Toets normale tekst op minimaal 4,5:1 contrast en grote tekst op minimaal 3:1.
- Controleer interactieve doelen op minimaal 24×24 CSS-pixels of op een geldige WCAG-uitzondering.
- Test in de doelbrowser met ten minste één schermlezer, omdat Flutter-websemantiek en live-aankondigingen praktijkvalidatie vragen.

### Privacy
- De statusflow verzamelt of toont geen persoonsgegevens.
- Meet hypothesen bij voorkeur geaggregeerd en zonder account-, apparaat- of exacte locatiegegevens.
- Als foutdiagnostiek nodig is, beperk deze tot technische foutcategorie en tijdstip; vermijd inhoud van invoervelden, IP-adressen en unieke identifiers tenzij doel, grondslag, bewaartermijn en toegang expliciet zijn vastgesteld.
- Maak geen nieuwe tracking of profielvorming onderdeel van deze MVP zonder afzonderlijk product- en privacybesluit.

## Kritische beoordeling

**Oordeel:** ACCEPT

Kandidaat 0 is afgebakend als verificatiestory, behoudt bestaande structuur en bevat toetsbare toegankelijkheidscriteria. Afhankelijkheid van kandidaat 13 is expliciet gemaakt.

## Geaccepteerde storykandidaten

### Valideer Flutter-websemantiek voor statussen in de bestaande ontdekroute

Als kwaliteitsverantwoordelijke wil ik de geverifieerde laad-, succes- en foutovergangen van de bestaande ontdekroute handmatig in de Flutter-webdoelomgeving kunnen toetsen, zodat statusfeedback voor schermlezer- en toetsenbordgebruikers aantoonbaar bruikbaar is zonder route of inhoudsstructuur te wijzigen.

**Acceptatiecriteria**
- De feitelijke ontdekroute en de bestaande laad-, succes- en foutovergangen zijn vóór de test vastgelegd als testscenario’s.
- In de doelbrowser wordt per toestandsovergang precies één relevante programmatisch waarneembare statusmelding vastgesteld; focus verplaatst niet automatisch naar het statusgebied.
- De foutactie ‘Opnieuw proberen’ is in de natuurlijke lees- en focusvolgorde bereikbaar, heeft een zichtbare focusindicator en is te activeren met Enter en spatie.
- Een handmatige toets met ten minste één schermlezer documenteert per scenario de gehoorde aankondiging en eventuele afwijkingen of dubbelmeldingen.
- De wijziging van route, navigatie en bestaande inhoudsvolgorde valt buiten deze story en wordt niet aangebracht.

Bronnen: [https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html](https://api.flutter.dev/flutter/semantics/SemanticsProperties/liveRegion.html), [https://docs.flutter.dev/ui/accessibility/web-accessibility](https://docs.flutter.dev/ui/accessibility/web-accessibility), [https://docs.flutter.dev/testing/code-debugging](https://docs.flutter.dev/testing/code-debugging)

Afhankelijkheden: 13 | Maak de bestaande primaire ontdekactie toegankelijk met toetsbare statusfeedback

Risico's: De feitelijke homepage, ontdekroute en statusimplementatie zijn nog niet publiek bevestigd., Flutter-websemantiek en live-aankondigingen kunnen per browser en schermlezer verschillen., Deze story levert verificatie op; geconstateerde toegankelijkheidsproblemen kunnen vervolgwerk vereisen.

_Dit dossier is in shadow mode gemaakt. Er is geen story naar Software Factory gestuurd._
