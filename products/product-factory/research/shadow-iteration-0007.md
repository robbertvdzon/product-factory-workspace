---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0007
date: 2026-08-09
status: approved
sources:
  - https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
  - https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow
  - https://docs.gitlab.com/ci/yaml/needs/
  - https://docs.gitlab.com/ci/jobs/
  - https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies
  - https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on
  - https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987
  - https://github.com/sqlalchemy/sqlalchemy/discussions/10698
  - https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/
  - https://community.atlassian.com/forums/Jira-questions/Importing-subtasks-for-an-existing-issue-from-an-excel-file/qaq-p/882077
---
# Productcyclus 7

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoeksfocus: uit iteratie 5 signaleerden twee onafhankelijke critics een concreet, nog onopgelost risico in hoe Product Factory zelf story-kandidaten binnen één batch aan elkaar koppelt: kandidaat 1 verwees in zijn dependsOn naar "Kandidaat 0" — een batch-relatief, nulgebaseerd reviewindexnummer — terwijl die kandidaat na publicatie een heel ander, doorlopend backlog-ID krijgt. Zodra dat gebeurt resolveert de verwijzing niet meer. Dit is een generiek probleem: hoe verwijs je betrouwbaar naar een item dat nog geen definitief/persistent ID heeft? Vergelijkend onderzoek bij vijf gevestigde systemen (GitHub Actions, GitLab CI/CD, Terraform, relationele databases, Jira-bulkimport) laat een consistent patroon zien: al deze systemen lossen dit op met een stabiele, door de auteur zelf gekozen symbolische naam/sleutel die vanaf het moment van aanmaken vaststaat — nooit met een positie- of volgordeafhankelijk (runtime- of batch-)nummer. GitHub Actions gebruikt de YAML-sleutel job_id als interne referentie voor needs:, niet een runtime run-ID. GitLab CI's needs:-keyword verwijst naar jobs via hun jobnaam. Terraform's impliciete dependency-mechanisme werkt via het resource-adres (type.naam), niet via de cloud-provider-ID die pas na apply bestaat. Databases lossen het "ID nog niet bekend vóór insert"-probleem structureel op met client-gegenereerde UUID's. En Jira's eigen CSV-bulkimport kent een expliciet "ID Field" waarmee je binnen hetzelfde importbatch naar nog-niet-aangemaakte issues kunt verwijzen, los van de uiteindelijke issue-key. Conclusie: het is een breed gedragen, beproefd patroon om binnen-batch-referenties te baseren op een stabiele, zelfgekozen symbolische sleutel (naam/slug/UUID) in plaats van op een positie- of reviewvolgordenummer — direct toepasbaar op het door de critics gesignaleerde dependsOn-risico. Beperking: dit is zuiver extern webonderzoek naar precedenten; of en hoe Product Factory's eigen datamodel voor backlog-items en dependsOn-velden dit al dan niet ondersteunt, is niet geverifieerd omdat in deze sessie geen toegang tot de eigen broncode beschikbaar was — dat blijft de noodzakelijke volgende verificatiestap vóór er een productbesluit of stories over dit onderwerp volgen.

### Vijf gevestigde systemen lossen "verwijzen naar een nog niet definitief-ge-ID'd item" op met een stabiele, zelfgekozen symbolische sleutel, nooit met een positie-/volgordenummer

Over CI/CD (GitHub Actions, GitLab CI), infrastructure-as-code (Terraform), databases en issue-tracking (Jira) heen is het consistente patroon: de maker van een item kent er zelf, op het moment van aanmaken, een stabiele naam/sleutel/ID aan toe die niet verandert wanneer het systeem later een eigen (runtime- of database-)ID toekent. Verwijzingen tussen items in dezelfde batch gebeuren via die zelfgekozen sleutel, niet via een tijdelijk positienummer zoals een reviewvolgorde-index. Dit is direct relevant voor het door de critics in iteratie 5 gesignaleerde risico dat kandidaat 1 verwees naar "Kandidaat 0", een batchpositie die na publicatie niet meer bestaat.

Bronnen: [https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions), [https://docs.gitlab.com/ci/yaml/needs/](https://docs.gitlab.com/ci/yaml/needs/), [https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies), [https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987](https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987), [https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/](https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/)

### GitHub Actions: needs: verwijst naar de YAML-sleutel job_id, een auteurgedefinieerde stabiele identifier, niet naar een runtime-ID

In GitHub Actions workflows geeft jobs.<job_id> een job een unieke, door de auteur gekozen identifier. Die job_id (de YAML-sleutel zelf) is de interne referentie die wordt gebruikt in jobs.<job_id>.needs, voor outputs en voor API-verwijzingen — expliciet onderscheiden van eventuele runtime-identifiers die GitHub tijdens uitvoering toekent. De referentie is dus vanaf het moment van schrijven vast, ongeacht in welke volgorde of met welk intern ID de job later wordt uitgevoerd.

Bronnen: [https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions), [https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow](https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow)

### GitLab CI/CD: needs: refereert altijd aan de jobnaam, nooit aan een intern job-ID

GitLab CI's needs-keyword bouwt een directed acyclic graph van jobafhankelijkheden op basis van jobnamen zoals gedefinieerd in de .gitlab-ci.yml. Ook bij geparallelliseerde jobs wordt naar de naam verwezen om van alle instanties afhankelijk te zijn. Dit bevestigt hetzelfde patroon: een mensleesbare, door de auteur bepaalde naam als stabiele koppelsleutel, niet een systeemgegenereerd volgnummer.

Bronnen: [https://docs.gitlab.com/ci/yaml/needs/](https://docs.gitlab.com/ci/yaml/needs/), [https://docs.gitlab.com/ci/jobs/](https://docs.gitlab.com/ci/jobs/)

### Terraform: impliciete dependencies verwijzen naar het resource-adres (type.naam), niet naar het cloud-ID dat pas na apply bestaat

Terraform leidt afhankelijkheden tussen resources automatisch af doordat het ene resource-blok een attribuut van een ander resource-blok noemt via diens resource-adres (bijv. aws_instance.foo.id). Dat adres is een door de auteur gekozen naam die al bestaat vóórdat de daadwerkelijke cloud-provider-ID is toegekend; Terraform gebruikt dat adres om de juiste aanmaakvolgorde te bepalen, ook als de onderliggende waarde pas "known after apply" is.

Bronnen: [https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies), [https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on)

### Databases: client-gegenereerde UUID's bestaan specifiek om foreign-key-verwijzingen niet te laten wachten op een pas-na-insert-bekend auto-increment-ID

Een expliciet genoemd voordeel van client-gegenereerde UUID's (in tegenstelling tot database-gegenereerde auto-increment-ID's) is dat de identifier al bekend is vóórdat de rij daadwerkelijk is opgeslagen, zodat gerelateerde records met foreign-key-verwijzingen niet hoeven te wachten tot de rij is aangemaakt en het systeem een ID heeft toegekend. Dit is exact het patroon dat het "batchpositie bestaat straks niet meer"-probleem structureel voorkomt.

Bronnen: [https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987](https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987), [https://github.com/sqlalchemy/sqlalchemy/discussions/10698](https://github.com/sqlalchemy/sqlalchemy/discussions/10698)

### Jira's eigen CSV-bulkimport gebruikt een expliciet "ID Field" om binnen één importbatch naar nog niet aangemaakte issues te verwijzen

Bij het in bulk aanmaken van issues (inclusief subtasks) via CSV-import kent Jira een apart "ID Field" toe waarmee je binnen hetzelfde importbestand naar andere, nog-niet-aangemaakte issues kunt verwijzen (bijvoorbeeld voor parent-/subtask-koppelingen), losstaand van de uiteindelijke, door Jira toegekende issue-key. Dit is vrijwel identiek aan het scenario van Product Factory's story-batches: meerdere nieuwe items worden tegelijk voorgesteld, onderling gekoppeld, en pas later krijgt elk item zijn definitieve backlog-ID.

Bronnen: [https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/](https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/), [https://community.atlassian.com/forums/Jira-questions/Importing-subtasks-for-an-existing-issue-from-an-excel-file/qaq-p/882077](https://community.atlassian.com/forums/Jira-questions/Importing-subtasks-for-an-existing-issue-from-an-excel-file/qaq-p/882077)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) | 2026-08-09 | Officiële GitHub-documentatie; publiek toegankelijk, auteursrecht GitHub Inc., gangbaar om als technische referentie te citeren (geen expliciete open licentie geverifieerd). | Primaire, officiële bron voor hoe GitHub Actions job_id als stabiele referentie voor needs: gebruikt, ter vergelijking met Product Factory's fragiele batch-index-verwijzing. |
| [bron](https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow) | 2026-08-09 | Officiële GitHub-documentatie; publiek toegankelijk, auteursrecht GitHub Inc. | Aanvullende officiële uitleg over job_id als unieke, auteurgedefinieerde identifier los van runtime-uitvoering. |
| [bron](https://docs.gitlab.com/ci/yaml/needs/) | 2026-08-09 | Officiële GitLab-documentatie; publiek toegankelijk, auteursrecht GitLab B.V. (delen onder CC BY-SA volgens GitLab's algemene docs-licentiebeleid, niet per pagina geverifieerd). | Primaire bron voor hoe GitLab CI's needs-keyword jobs uitsluitend via naam koppelt, als tweede onafhankelijke CI/CD-precedent naast GitHub Actions. |
| [bron](https://docs.gitlab.com/ci/jobs/) | 2026-08-09 | Officiële GitLab-documentatie; publiek toegankelijk, auteursrecht GitLab B.V. | Ondersteunende context over hoe GitLab-jobs en hun namen als eersteklas identifiers functioneren binnen een pipeline. |
| [bron](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies) | 2026-08-09 | Officiële HashiCorp-documentatie; publiek toegankelijk, auteursrecht HashiCorp; tutorialtekst onder HashiCorp's docs-voorwaarden (geen losse open licentie geverifieerd). | Toont een derde, ander soort systeem (infrastructure-as-code) met hetzelfde patroon: verwijzen via een stabiel, auteurgekozen adres in plaats van een systeemtoegekend ID. |
| [bron](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on) | 2026-08-09 | Officiële HashiCorp-referentiedocumentatie; publiek toegankelijk, auteursrecht HashiCorp. | Formele referentie voor hoe expliciete en impliciete Terraform-dependencies via resource-adressen werken, ter onderbouwing van het gevonden patroon. |
| [bron](https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987) | 2026-08-09 | Publiek technisch blogartikel op DEV Community; auteursrecht bij de individuele auteur, vrij toegankelijk voor lezen; uitsluitend als informatieve referentie gebruikt. | Legt het algemene databasepatroon uit waarom client-gegenereerde UUID's het "ID nog niet bekend vóór insert"-probleem voorkomen, als generiek technisch precedent buiten CI/CD-context. |
| [bron](https://github.com/sqlalchemy/sqlalchemy/discussions/10698) | 2026-08-09 | Publieke GitHub Discussions-thread; content valt onder GitHub's gebruikersvoorwaarden, auteursrecht bij individuele bijdragers; uitsluitend geraadpleegd als praktijkvoorbeeld, niet overgenomen. | Praktijkvoorbeeld/discussie uit een concreet ORM-project dat het client-side UUID-generatiepatroon bevestigt en de afweging ervan toelicht. |
| [bron](https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/) | 2026-08-09 | Publiek technisch blogartikel; auteursrecht bij de auteur ("The Jira Guy"), vrij toegankelijk voor lezen; uitsluitend als informatieve referentie gebruikt. | Beschrijft Jira's eigen "ID Field"-mechanisme voor onderlinge verwijzingen tussen nog-niet-aangemaakte issues binnen één bulkimportbatch — het meest directe precedent voor Product Factory's eigen story-batchprobleem. |
| [bron](https://community.atlassian.com/forums/Jira-questions/Importing-subtasks-for-an-existing-issue-from-an-excel-file/qaq-p/882077) | 2026-08-09 | Publiek Atlassian Community-forum; content onder Atlassian Community-gebruikersvoorwaarden, auteursrecht bij individuele forumleden; uitsluitend als aanvullende bevestiging geraadpleegd. | Aanvullende community-bevestiging van hoe parent-/subtask-koppelingen tijdens bulk-imports worden gelegd voordat definitieve issue-keys bestaan. |

## Productbeslissing

Vervang in Product Factory's story-batchvoorstellen de huidige batch-relatieve reviewindex (bijv. \"Kandidaat 0\") als basis voor dependsOn-verwijzingen door een stabiele, bij aanmaak toegekende, mensleesbare symbolische sleutel per kandidaat. Voeg bij publicatie een expliciete resolve-stap toe die deze sleutel vertaalt naar het definitieve, doorlopende backlog-ID — zodat het koppelmechanisme zelf verandert, maar het uiteindelijke ID-formaat dat de rest van het systeem en de Software Factory al verwachten, ongemoeid blijft. Dit is een gerichte, kleine wijziging aan één specifiek, al aangetoond risico (gesignaleerd door twee onafhankelijke critics in iteratie 5), beperkt tot Product Factory's eigen story-batch-contract — niet aan hkh of hkh-autopilot. Eerste stap is verificatie van het bestaande datamodel voor backlog-items en dependsOn, omdat dat in dit onderzoek nog niet is gecontroleerd.

**Waarom:** De missie vraagt dat Product Factory zichzelf continu toetst, ook zonder gemelde klacht van de eigenaar — het dependsOn-risico is precies zo'n zelf-gesignaleerd probleem, door critics in iteratie 5 al aangetoond maar nog niet opgelost. Het vergelijkend onderzoek naar vijf gevestigde systemen (GitHub Actions, GitLab CI, Terraform, databases, Jira) laat een consistent, breed gedragen patroon zien: verwijs binnen een batch naar een stabiele, auteurgekozen sleutel, nooit naar een positie- of volgordenummer. Dat is direct toepasbaar en sluit aan bij \"klein en toetsbaar\" (het raakt alleen het koppelmechanisme, niet het bredere datamodel) en bij \"onomkeerbaarheid weegt zwaarder dan gemak\" (de wijziging blijft binnen Product Factory's eigen contract, weg van authenticatie, migraties of de koppeling met andere producten). Omdat het onderzoek zelf aangeeft dat de eigen broncode niet is geverifieerd, wordt die verificatie als eerste, noodzakelijke stap in de richting opgenomen — conform \"eerst begrijpen, dan wijzigen\" en \"transparant over eigen twijfel\".

### Prioriteiten
- Voorkom dat dependsOn-verwijzingen binnen een story-batch silently falen nadat kandidaten hun definitieve backlog-ID krijgen
- Baseer de oplossing op een breed beproefd patroon (stabiele auteurssleutel) in plaats van een nieuw, zelfbedacht mechanisme
- Verifieer eerst hoe het huidige datamodel voor backlog-items en dependsOn is opgebouwd, vóór gedrag wordt gewijzigd
- Houd de wijziging klein, in isolatie beoordeelbaar en terug te draaien, beperkt tot Product Factory's eigen story-batch-contract
- Wees expliciet over de resterende onzekerheid: dit is nog niet tegen de eigen broncode geverifieerd

### Besluiten
- **Verwijzingen tussen story-kandidaten binnen één batch (dependsOn) worden gebaseerd op een stabiele, bij aanmaak toegekende symbolische sleutel (bijv. een korte, mensleesbare naam of slug per kandidaat), in plaats van op het huidige batch-relatieve reviewvolgordenummer ("Kandidaat 0").** — Vijf onafhankelijke, gevestigde systemen (CI/CD, infrastructure-as-code, databases, issue-tracking) lossen exact dit probleem — verwijzen naar een item dat nog geen definitief systeem-ID heeft — consistent op met een auteurgekozen sleutel die vaststaat vanaf aanmaak. Een positienummer is per definitie instabiel zodra de volgorde of samenstelling van de batch verandert of items een definitief ID krijgen; dat is precies het faalpad dat critics in iteratie 5 signaleerden.
- **Bij publicatie van een batch wordt een expliciete resolve-stap toegevoegd die elke symbolische sleutel vertaalt naar het definitieve, doorlopende backlog-ID, analoog aan hoe databases client-gegenereerde UUID's koppelen vóór insert en hoe Jira's CSV-bulkimport een apart "ID Field" gebruikt om binnen één import naar nog-niet-aangemaakte issues te verwijzen.** — De sleutel zelf is bedoeld voor mensen en voor koppeling binnen de batch; het definitieve backlog-ID blijft de vorm die de rest van het systeem (en de Software Factory) al verwacht. Een losse resolve-stap houdt de wijziging klein en isoleerbaar: alleen het koppelmechanisme verandert, niet het uiteindelijke ID-formaat.
- **De sleutel blijft mensleesbaar (naam/slug) in plaats van een ondoorzichtige UUID, en het mechanisme wordt beperkt tot het story-batch-contract dat Product Factory zelf produceert en consumeert — geen wijziging aan hoe hkh of hkh-autopilot hun eigen data of gedrag beheren.** — GitHub Actions' job_id en GitLab CI's jobnaam zijn beide bewust leesbare, betekenisvolle sleutels — geen ondoorzichtige runtime-ID's — wat aansluit bij het principe dat bedienbaarheid beoordeeld wordt vanuit de eigenaar, niet vanuit wat intern het makkelijkst is. Beperking tot Product Factory's eigen contract respecteert de guardrail om nooit data of gedrag van andere producten te wijzigen.
- **Voordat dit gedrag daadwerkelijk wordt gewijzigd, wordt eerst geverifieerd hoe het bestaande datamodel voor backlog-items en dependsOn-velden in Product Factory nu al is opgebouwd (bijv. of er al een naam/slug-achtig veld bestaat dat hergebruikt kan worden).** — Dit onderzoek is zuiver extern precedentenonderzoek gebleven; er is in deze sessie geen toegang tot of verificatie van de eigen broncode geweest. Conform het principe "eerst begrijpen, dan wijzigen" mag een voorstel niet worden doorgezet zonder eerst uit te leggen waarom het huidige batch-index-gedrag zo is en of het datamodel de nieuwe sleutel al dan niet al ondersteunt.

## UX-voorstel: Story-batch review met stabiele kandidaatsleutels

**Gebruikersdoel:** Als Product Factory-reviewer (mens of agent) een voorgestelde story-batch beoordelen en publiceren zonder dat dependsOn-verwijzingen tussen kandidaten breken doordat ze nu gebaseerd zijn op een stabiele, bij aanmaak toegekende sleutel in plaats van een batch-relatief reviewvolgordenummer.

### Flow
1. Reviewer opent het Story-batch Review Dashboard en ziet een lijst van kandidaten; elke rij toont een stabiele, mensleesbare kandidaatsleutel (bv. candidate-depends-on-fix) naast de titel, in plaats van een positienummer zoals 'Kandidaat 0'.
2. Reviewer scant de lijst; elke kandidaat met een dependsOn-veld toont de verwezen sleutel(s) plus een inline resolutiestatus-badge (Resolved binnen batch / Onbekende sleutel).
3. Reviewer opent een kandidaat-detailweergave en ziet de volledige dependsOn-keten uitgeschreven met sleutels en, indien al bekend, het bijbehorende definitieve backlog-ID.
4. Reviewer of geautomatiseerde validatie-agent controleert vóór publicatie of alle dependsOn-sleutels binnen dezelfde batch aanwezig zijn; niet-gevonden sleutels blokkeren publicatie en worden gemarkeerd met een foutindicator op de betreffende rij.
5. Reviewer triggert de actie 'Publiceer batch'.
6. Systeem voert een expliciete resolve-stap uit: elke symbolische sleutel wordt vertaald naar het definitieve, doorlopende backlog-ID; een preview-paneel toont de volledige sleutel-naar-ID-mapping vóór definitieve opslag.
7. Reviewer bevestigt de resolve-preview (of geautomatiseerde agent bevestigt op basis van een vooraf gedefinieerde acceptatieregel, bv. 100% van de sleutels gemapt).
8. Na publicatie toont het dashboard elke kandidaatrij met zowel de oorspronkelijke sleutel als het toegewezen backlog-ID, zodat traceerbaarheid behouden blijft voor latere audits.

### Wireframe

[Story-batch Review Dashboard]
─────────────────────────────────────────────
Header: "Batch #2026-08-09-a — 4 kandidaten"   [Publiceer batch ▶]

Lijst (toetsenbord-navigeerbaar, elke rij is een focusbaar element):
┌─────────────────────────────────────────────────────────┐
│ ● sleutel: fix-dependson-refs        status: ✔ resolved │
│   titel: "Vervang batch-index door stabiele sleutel"     │
│   dependsOn: (geen)                                       │
├─────────────────────────────────────────────────────────┤
│ ● sleutel: resolve-step-publish      status: ✔ resolved │
│   titel: "Voeg resolve-stap toe bij publicatie"           │
│   dependsOn: [fix-dependson-refs]  → gevonden in batch    │
├─────────────────────────────────────────────────────────┤
│ ● sleutel: validate-unresolved-key   status: ⚠ unresolved│
│   titel: "Blokkeer publicatie bij onbekende sleutel"      │
│   dependsOn: [oude-kandidaat-2]  → NIET gevonden in batch │
└─────────────────────────────────────────────────────────┘

[Detailweergave kandidaat: resolve-step-publish]
─────────────────────────────────────────────
sleutel:        resolve-step-publish
titel:          Voeg resolve-stap toe bij publicatie
dependsOn-keten:
   1. fix-dependson-refs  (status: resolved, backlog-ID: nog niet toegewezen)
status:         klaar voor publicatie
[Sluiten]  [Volgende kandidaat ▶]

[Publicatie-preview modal — verschijnt na klik op "Publiceer batch"]
─────────────────────────────────────────────
Titel: "Resolve-preview: sleutel → backlog-ID"
Waarschuwing (indien van toepassing):
  ⚠ 1 kandidaat geblokkeerd: validate-unresolved-key
    → dependsOn-sleutel "oude-kandidaat-2" niet gevonden in deze batch.
    Publicatie van deze kandidaat is uitgeschakeld tot de sleutel bestaat
    of het dependsOn-veld is aangepast.

Mapping-tabel (alleen resolvebare kandidaten):
| sleutel                | definitief backlog-ID |
|-------------------------|------------------------|
| fix-dependson-refs      | PF-1042                |
| resolve-step-publish    | PF-1043                |

[Annuleer]   [Bevestig publicatie van 2/3 kandidaten]

[Na publicatie — bijgewerkte rij]
┌─────────────────────────────────────────────────────────┐
│ sleutel: fix-dependson-refs  →  backlog-ID: PF-1042      │
│ status: gepubliceerd                                      │
└─────────────────────────────────────────────────────────┘

### Interactiehypotheses
- Door dependsOn-verwijzingen te baseren op een stabiele sleutel in plaats van een batch-relatief volgordenummer daalt het aantal onopgeloste (unresolved) dependsOn-referenties na publicatie tot 0%, meetbaar via een geautomatiseerde regressietest die batches met gewijzigde review-volgorde simuleert.
- De expliciete resolve-preview vóór publicatie voorkomt dat kandidaten met een niet-bestaande dependsOn-sleutel alsnog gepubliceerd worden; te toetsen met een geautomatiseerde testcase die een batch met een opzettelijk kapotte sleutel aanbiedt en verifieert dat publicatie van die kandidaat geblokkeerd wordt.
- Een geautomatiseerde validatie-agent kan, zonder menselijke tussenkomst, voor elke batch controleren dat elke dependsOn-sleutel binnen dezelfde batch voorkomt vóórdat publicatie wordt toegestaan; te toetsen door de validatiestap te draaien tegen een corpus van historische en synthetische batches en het percentage correct gedetecteerde fouten te meten.
- Na publicatie blijft de sleutel-naar-backlog-ID-mapping volledig en consistent traceerbaar (elke gepubliceerde kandidaat toont zowel sleutel als backlog-ID); te toetsen met een geautomatiseerde schemavalidatietest op het publicatie-uitvoerbestand/-record.

### Toegankelijkheid
- Alle kandidaatrijen, statusbadges en de resolve-preview-modal zijn volledig bedienbaar met alleen het toetsenbord (Tab/Shift+Tab, Enter om te openen, Esc om modals te sluiten), zonder muisafhankelijke acties.
- Statusindicatoren (resolved/unresolved, geblokkeerd/gepubliceerd) worden niet uitsluitend met kleur gecommuniceerd maar ook met tekst en icoon (bv. ✔/⚠), zodat ze bruikbaar zijn zonder kleurperceptie.
- Alle interactieve elementen en statuswijzigingen hebben correcte ARIA-labels/roles; de resolve-preview-modal gebruikt aria-live voor dynamische mapping-updates zodat schermlezers wijzigingen aankondigen.
- Contrastverhoudingen van tekst, statusbadges en focus-indicatoren voldoen minimaal aan WCAG 2.1 AA (4,5:1 voor normale tekst, 3:1 voor grote tekst/iconen).
- Focus wordt bij openen van de detailweergave of publicatie-modal automatisch en zichtbaar verplaatst naar het eerste interactieve element, en bij sluiten teruggezet naar het element dat de actie triggerde.

### Privacy
- Kandidaatsleutels, titels en dependsOn-verwijzingen bevatten uitsluitend operationele metadata van Product Factory zelf (story-batchstructuur), geen persoonsgegevens of gebruikersdata van hkh, hkh-autopilot of andere producten.
- De resolve-stap en publicatie-preview tonen alleen sleutel→backlog-ID-mappings binnen Product Factory's eigen contract; er wordt geen data uit andere producten gelezen, gecombineerd of gepubliceerd.
- Toegang tot het review-dashboard en de publicatieactie wordt beperkt tot geautoriseerde Product Factory-reviewers/agents; een eventueel benodigd extern toegangstoken wordt alleen gebruikt voor authenticatie en nooit in kandidaatsleutels, logs of de mapping-tabel opgeslagen.
- Foutmeldingen over niet-gevonden dependsOn-sleutels tonen alleen de sleutelnaam zelf (geen onderliggende systeem- of gebruikersdetails), om te voorkomen dat interne implementatiedetails onnodig worden blootgesteld.

## Kritische beoordeling

**Oordeel:** ACCEPT

Drie kandidaten pakken het in iteratie 5 gesignaleerde dependsOn-risico (batch-relatieve reviewindex vs. definitief backlog-ID) gefaseerd aan: eerst een zuivere, agent-uitvoerbare inspectie van het bestaande datamodel (kandidaat 0), dan een voorwaardelijke implementatie van een stabiele sleutel (kandidaat 1), dan een voorwaardelijke resolve-stap bij publicatie met expliciet legacy-fallbackpad (kandidaat 2). Alle drie zijn volledig agent-uitvoerbaar zonder menselijk besluitmoment, betaling, accountaanmaak of apparaatcontrole; conditionaliteit is gebaseerd op machineleesbare velden die kandidaat 0 zelf vastlegt. Scope blijft correct beperkt tot Product Factory's eigen story-batch-contract (geen wijziging aan hkh/hkh-autopilot), en er is geen persoonsgegevensverwerking. De onderliggende onderzoeksbron is expliciet en eerlijk gemarkeerd als zuiver extern precedentenonderzoek zonder eigen-broncode-verificatie — maar kandidaat 0 is precies ontworpen om dat gat te dichten vóórdat er functioneel gewijzigd wordt, wat in lijn is met 'eerst begrijpen, dan wijzigen'. Geen blokkerende problemen gevonden; twee niet-blokkerende aandachtspunten (zelfreferentiële dependsOn-robuustheid in kandidaat 1, en een in het onderzoek geschetste UI/accessibility-dashboard dat door geen van de drie kandidaten wordt gebouwd) worden hieronder genoteerd.
- **WARNING · CONSISTENCY** — Kandidaat 1 verwijst in zijn eigen dependsOn naar de sleutel 'verify-dependson-datamodel' van kandidaat 0, binnen dezelfde batch die nu juist onderzoekt of het publicatiemechanisme zulke symbolische sleutels al kan resolveren. Als kandidaat 0 vaststelt dat dit nog niet zo is, loopt deze specifieke batchkoppeling het risico op precies hetzelfde faalpad dat het onderzoek beschrijft. De acceptatiecriteria documenteren dit expliciet als bekende beperking in plaats van het te verdoezelen, wat voldoende is om niet te blokkeren, maar reviewers moeten dit bewust meenemen bij publicatie van deze batch.
- **INFO · SCOPE** — Het onderzoeksdocument bevat een uitgewerkte flow, wireframe en uitgebreide toegankelijkheidseisen voor een 'Story-batch Review Dashboard' (badges, resolve-preview modal, ARIA-live, contrast), maar geen van de drie kandidaten implementeert deze UI. Dat is een bewuste, correcte klein-en-isoleerbaar-scoping (backend/datamodel eerst), maar de discrepantie tussen onderzoek en geleverde kandidaten is het vermelden waard zodat een toekomstige batch dit weloverwogen oppakt of het onderzoek als aspirational markeert.
- **INFO · SOURCE** — De onderliggende research is uitsluitend gebaseerd op extern precedentenonderzoek (GitHub Actions, GitLab CI, Terraform, database-patronen, Jira) en expliciet niet geverifieerd tegen Product Factory's eigen broncode/datamodel, wat strikt genomen tegen de bronnenregel ingaat. Dit wordt echter direct gemitigeerd doordat kandidaat 0 als eerste, verplichte stap precies die eigen-broncode-verificatie uitvoert vóórdat kandidaat 1/2 functioneel iets wijzigen.

## Geaccepteerde storykandidaten

### Verifieer of dependsOn-verwijzingen binnen een story-batch nu op een batch-relatieve positie-index of op een stabiele sleutel zijn gebaseerd

Twee onafhankelijke critics signaleerden in iteratie 5 dat kandidaat 1 in zijn dependsOn-veld verwees naar "Kandidaat 0" — een batch-relatief, nulgebaseerd reviewindexnummer dat na publicatie niet meer bestaat omdat het kandidaat dan een doorlopend backlog-ID krijgt. Vergelijkend onderzoek bij vijf gevestigde systemen (GitHub Actions job_id, GitLab CI needs:-jobnaam, Terraform resource-adres, database client-UUID's, Jira CSV-bulkimport ID Field) laat zien dat dit generieke probleem — verwijzen naar een item zonder definitief ID — consistent wordt opgelost met een stabiele, bij aanmaak toegekende symbolische sleutel in plaats van een positienummer. Voordat dat patroon in Product Factory wordt toegepast, moet eerst geverifieerd worden hoe het bestaande datamodel voor story-batchkandidaten en het dependsOn-veld daadwerkelijk is opgebouwd, aangezien dit in het voorafgaande onderzoek uitsluitend extern precedentenonderzoek was zonder toegang tot de eigen broncode. Deze story is een zuivere, geautomatiseerde inspectie- en documentatiestap zonder functionele wijziging. Deze story's eigen batchsleutel (voor gebruik door afhankelijke stories in deze batch) is: verify-dependson-datamodel.

**Acceptatiecriteria**
- Een geautomatiseerde inspectie van de broncode/het datamodel dat story-batchkandidaten en hun dependsOn-veld genereert en verwerkt wordt uitgevoerd door de implementerende agent, zonder menselijke tussenkomst.
- De inspectie resulteert in een gedocumenteerde, machineleesbare uitkomst met exact één van de volgende vier waarden: 'uses-positional-index', 'uses-stable-key-already', 'uses-persistent-id-only', 'inconclusive'.
- Indien de uitkomst 'uses-positional-index' is, bevat de documentatie een concreet voorbeeld uit de bestaande code/het bestaande gedrag dat aantoont dat een dependsOn-verwijzing zoals "Kandidaat 0" een batch-relatieve positie is en geen stabiele sleutel.
- De documentatie wordt toegevoegd als een op zichzelf staand, doorzoekbaar artefact (bijv. een bestand) binnen de Product Factory-codebase, zodat afhankelijke stories deze uitkomst kunnen inlezen zonder opnieuw te hoeven inspecteren.
- De inspectie stelt tevens vast en documenteert of het huidige publicatiemechanisme al in staat is een dependsOn-waarde te resolveren die géén positionele index maar een vrije symbolische sleutel (string) is; dit wordt vastgelegd als aparte machineleesbare boolean 'publish-mechanism-supports-symbolic-keys'.
- Er wordt geen functioneel gedrag gewijzigd; dit is uitsluitend een inspectie- en documentatiestap.
- Als de broncode/het datamodel niet binnen deze story ondubbelzinnig te doorgronden is (bijv. door verspreide of asynchrone verwerking), wordt in plaats van een aanname de uitkomst 'inconclusive' vastgelegd.

Bronnen: [https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions), [https://docs.gitlab.com/ci/yaml/needs/](https://docs.gitlab.com/ci/yaml/needs/), [https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies), [https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/](https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/)

Risico's: Als het datamodel complexer is dan verwacht (bijv. dependsOn wordt op meerdere plekken in de codebase verwerkt), kan de inspectie onvolledig zijn en tot een foutieve classificatie leiden., Deze story raakt Product Factory's eigen kernmechanisme voor story-batches; een onjuiste documentatie kan afhankelijke stories op het verkeerde been zetten.

### Vervang batch-relatieve reviewindex door een stabiele, auteurgekozen sleutel voor dependsOn-verwijzingen, indien bevestigd nodig

Deze story bouwt voort op de verificatie-story (sleutel: verify-dependson-datamodel) en wordt alleen daadwerkelijk uitgevoerd als die story bevestigt dat dependsOn-verwijzingen nu op een batch-relatieve positie-index rusten. Analoog aan GitHub Actions' job_id, GitLab CI's needs:-jobnaam en Terraform's resource-adres krijgt elk story-kandidaat binnen een batch bij aanmaak een stabiele, mensleesbare symbolische sleutel (kebab-case-slug) die vaststaat ongeacht latere review- of publicatievolgorde. Het dependsOn-veld wordt vanaf dan gevalideerd op basis van deze sleutel in plaats van een positienummer. De wijziging blijft beperkt tot Product Factory's eigen story-batch-generatie- en validatiecode en introduceert geen nieuw persistent backlog-ID-formaat. Deze story gebruikt zelf al de sleutel 'verify-dependson-datamodel' om naar de voorgaande kandidaat te verwijzen; omdat kandidaat 0 tegelijk vaststelt of het huidige publicatiemechanisme dat soort sleutels al kan resolveren, wordt deze eigen verwijzing pas als betrouwbaar koppelmechanisme voor déze batch beschouwd zodra dat bevestigd is (zie acceptatiecriteria). Deze story's eigen batchsleutel is: stable-candidate-key.

**Acceptatiecriteria**
- Deze story wordt alleen uitgevoerd indien de gedocumenteerde uitkomst van de voorgaande verificatie-story (verify-dependson-datamodel) 'uses-positional-index' is; bij elke andere uitkomst levert deze story uitsluitend een gedocumenteerde 'skipped-precondition-not-met'-bevinding op en wordt geen code gewijzigd.
- Vóór verdere uitvoering leest de implementerende agent het door verify-dependson-datamodel vastgelegde 'publish-mechanism-supports-symbolic-keys'-veld; is dat false of ontbreekt het, dan implementeert deze story het nieuwe sleutelmechanisme zoals gepland, maar documenteert de agent expliciet dat de eigen dependsOn-verwijzing van deze kandidaat naar 'verify-dependson-datamodel' in déze batch mogelijk nog niet resolveert via het bestaande publicatiepad, en meldt dit als bekende beperking zonder de story te blokkeren.
- Bij bevestigde precondition krijgt elk story-kandidaat dat binnen een batch wordt gegenereerd bij aanmaak een stabiele, mensleesbare symbolische sleutel die niet verandert wanneer de batch- of reviewvolgorde wijzigt.
- Het dependsOn-veld van elk kandidaat wordt gevalideerd op verwijzing via deze sleutel in plaats van via een batch-relatief volgnummer zoals "Kandidaat 0".
- Een geautomatiseerde regressietest simuleert een batch waarin twee kandidaten via hun sleutel naar elkaar verwijzen en bevestigt dat de dependsOn-referentie correct resolveert, ongeacht de volgorde waarin de kandidaten zijn gegenereerd of gereviewed.
- Er wordt geen bestaand persistent backlog-ID-veld verwijderd of van formaat veranderd; de sleutel wordt uitsluitend gebruikt voor koppelingen binnen een nog niet gepubliceerde batch.
- De wijziging is beperkt tot Product Factory's eigen story-batch-generatie- en validatiecode; er wordt geen data of gedrag van hkh, hkh-autopilot of andere producten gewijzigd.

Bronnen: [https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow](https://docs.github.com/actions/using-jobs/using-jobs-in-a-workflow), [https://docs.gitlab.com/ci/jobs/](https://docs.gitlab.com/ci/jobs/), [https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on](https://developer.hashicorp.com/terraform/language/meta-arguments/depends_on)

Afhankelijkheden: verify-dependson-datamodel

Risico's: Als de precondition-story een andere uitkomst oplevert dan 'uses-positional-index', is deze story een no-op; dat is gewenst gedrag maar moet expliciet als zodanig herkenbaar zijn in de rapportage., Wijziging aan het kernmechanisme van story-batchgeneratie kan onbedoeld bestaande, al gepubliceerde batches beïnvloeden als de wijziging niet zorgvuldig geïsoleerd blijft tot nieuwe, nog niet gepubliceerde batches., Als het publicatiemechanisme symbolische sleutels nog niet ondersteunt, kan de eigen dependsOn-verwijzing van deze kandidaat naar 'verify-dependson-datamodel' binnen deze specifieke batch niet resolveren; dit wordt als bekende beperking gedocumenteerd in plaats van stilzwijgend genegeerd.

### Voeg expliciete resolve-stap toe bij batchpublicatie die sleutels naar definitieve backlog-ID's vertaalt, met gedefinieerd fallbackgedrag voor bestaande legacy-batches

Deze story bouwt voort op de introductie van de stabiele kandidaatsleutel (sleutel: stable-candidate-key) en voegt, analoog aan Jira's CSV-bulkimport "ID Field" en het databasepatroon van client-gegenereerde UUID's die vóór insert al bekend zijn, een expliciete resolve-stap toe aan het publiceren van een story-batch. Elke gebruikte dependsOn-sleutel wordt bij publicatie automatisch vertaald naar het definitieve, doorlopende backlog-ID van de betreffende kandidaat. Als een sleutel niet binnen dezelfde batch gevonden wordt, wordt publicatie van die kandidaat geblokkeerd in plaats van stilzwijgend een niet-resolverende verwijzing te publiceren. Om te voorkomen dat deze nieuwe blokkade bestaande, nog niet gepubliceerde batches met het oude positionele dependsOn-formaat ('Kandidaat N') onbedoeld laat falen, wordt een volledig geautomatiseerd, agent-uitvoerbaar fallbackpad gedefinieerd (zie acceptatiecriteria) zodat hiervoor geen menselijk besluitmoment tijdens implementatie nodig is. De wijziging blijft beperkt tot Product Factory's eigen publicatiepad.

**Acceptatiecriteria**
- Deze story wordt alleen uitgevoerd indien de voorgaande story (stable-candidate-key) daadwerkelijk is geïmplementeerd (d.w.z. niet is afgesloten met 'skipped-precondition-not-met'); anders levert deze story eveneens alleen een gedocumenteerde skip-bevinding op.
- Bij het publiceren van een story-batch voert het systeem een geautomatiseerde resolve-stap uit die elke gebruikte dependsOn-sleutel binnen de batch vertaalt naar het definitieve, doorlopende backlog-ID van de betreffende kandidaat.
- Een dependsOn-waarde die matcht met het oude positionele legacy-patroon (een string die overeenkomt met 'Kandidaat' gevolgd door een geheel getal, bijv. 'Kandidaat 0') wordt automatisch, zonder menselijke tussenkomst, herkend als legacy-verwijzing in plaats van direct als onbekende sleutel behandeld.
- Voor een herkende legacy-verwijzing probeert de resolve-stap deze automatisch te vertalen door het batch-item te identificeren dat op de betreffende (nulgebaseerde) reviewpositie binnen dezelfde batch staat; lukt dit, dan wordt de kandidaat normaal gepubliceerd en wordt in de mapping expliciet gelogd dat resolutie via het legacy positionele fallbackpad is verlopen.
- Lukt de automatische legacy-vertaling niet (bijv. de gerefereerde positie bestaat niet meer binnen de batch), dan wordt publicatie van die specifieke kandidaat geblokkeerd en als fout gelogd, op dezelfde manier als bij een onbekende symbolische sleutel; overige, wel-resolverende kandidaten worden normaal gepubliceerd.
- Twee geautomatiseerde tests tonen aan: (1) een batch met een opzettelijk niet-bestaande dependsOn-sleutel blokkeert publicatie van de afhankelijke kandidaat terwijl overige kandidaten normaal publiceren, en (2) een batch met een dependsOn-waarde in het oude 'Kandidaat N'-formaat resolveert correct via het legacy-fallbackpad en wordt als zodanig in de mapping-log gemarkeerd.
- Na publicatie is de volledige sleutel-naar-backlog-ID-mapping (inclusief eventuele legacy-resoluties) traceerbaar vastgelegd, zodat achteraf geverifieerd kan worden welke sleutel of legacy-index tot welk definitief ID heeft geleid.
- De wijziging blijft beperkt tot Product Factory's eigen publicatiepad voor story-batches; er wordt geen wijziging aangebracht aan Software Factory, hkh, hkh-autopilot of aan authenticatie-/PR-goedkeuringsflows.

Bronnen: [https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/](https://thejiraguy.com/2021/05/26/csv-imports-the-secrets-of-bulk-jira-issue-creation/), [https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987](https://dev.to/arctype/uuids-vs-auto-incrementing-primary-keys-in-sql-2987), [https://github.com/sqlalchemy/sqlalchemy/discussions/10698](https://github.com/sqlalchemy/sqlalchemy/discussions/10698)

Afhankelijkheden: stable-candidate-key

Risico's: Als de publicatiecode meerdere entry-points heeft (bijv. handmatige publicatie versus geautomatiseerde orchestrator), kan de resolve-stap gemist worden in één van de paden tenzij expliciet op alle paden toegepast., Het legacy-fallbackpad interpreteert een positioneel patroon; als een toekomstige, legitieme symbolische sleutel toevallig hetzelfde patroon volgt (bijv. een sleutel die letterlijk 'Kandidaat 3' heet), kan deze onbedoeld als legacy-verwijzing worden behandeld in plaats van als reguliere sleutel. Dit wordt beperkt doordat nieuwe sleutels per acceptatiecriterium van kandidaat 'stable-candidate-key' kebab-case zijn en dus niet met dit patroon overeenkomen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
