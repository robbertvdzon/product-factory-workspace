---
product: hkh-autopilot
artifact_type: meeting
run_id: meeting-hkh-autopilot-0002
date: 2026-08-12
status: closed
---
# Overleg 2

**Initiator:** de eigenaar

## Samenvatting

Besluit: de goedgekeurde productvisie van hkh-autopilot blijft ongewijzigd. De 100/75/50-termijnen gelden uitsluitend als openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten; zij zijn geen algemene privacy-, AVG- of publicatieregel. De FamilySearch 110/95-regel blijft een niet-wettelijke, conservatieve heuristiek. Alleen concrete, materiële en aantoonbare privacy-, security- of rechtenrisico’s zijn BLOCKING; ontbrekende beleidsinformatie, optimalisaties, verbeteringen en hypothetische toekomstige risico’s zijn WARNING. Bij ontbrekend beleid wordt waar mogelijk een kleinere veilige scope gekozen, zoals herleidbare metadata en externe bronlinks, zonder lokale media of gevoelige persoonsgegevens. Historische dossiers blijven herkenbaar als historisch of achterhaald.

Correctie roadmapthema 0003: “De Nederlandse termijnen 100/75/50 jaar mogen uitsluitend worden gebruikt als openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten. Zij zijn geen algemene privacy-, AVG- of publicatieregel voor andere gegevens, bronnen of collecties binnen hkh-autopilot. De FamilySearch 110/95-regel is uitsluitend een niet-wettelijke, conservatieve heuristiek. Privacy- en rechtenonzekerheid wordt fail-closed behandeld wanneer sprake is van een concreet, materieel en aantoonbaar risico. Ontbrekende beleidsinformatie, optimalisaties en hypothetische toekomstige risico’s zijn WARNING en niet automatisch BLOCKING. De veilige uitvoeringsscope mag daarom waar mogelijk worden beperkt tot herleidbare metadata en externe bronlinks, zonder lokale media of gevoelige persoonsgegevens.” Dit vereist een afzonderlijke roadmapsessie.

Correctie voor onderzoeksvraag 6: “Deze correctie vervangt en supersedeert onderzoeksvraag 6 en iedere eerdere beantwoording daarvan: de Nederlandse 100/75/50-termijnen zijn uitsluitend openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten. Ze vormen geen algemene privacy-, AVG- of publicatieregel voor alle gegevens en bronnen in hkh-autopilot. De FamilySearch 110/95-regel blijft een niet-wettelijke, conservatieve heuristiek. Alleen concrete, materiële en aantoonbare privacy-, security- of rechtenrisico’s zijn BLOCKING; ontbrekende beleidsinformatie, verbeteringen, optimalisaties en hypothetische toekomstige risico’s zijn WARNING.” Omdat de huidige tooling vraag 6 niet kan wijzigen of supersederen, moet deze correctie onmiddellijk afzonderlijk worden toegevoegd; dit is een aparte roadmap- of Product Factory-actie.

Eerstvolgende HKH-documentatiestory — Titel: “Corrigeer en centraliseer privacy- en rechtenbeleid voor hkh-autopilot”. Beschrijving: “Leg één canonieke privacy- en rechtenpolicy vast in de hkh-autopilot-repository. Corrigeer strijdige functionele en technische documentatie, waaronder formuleringen die de 100/75/50-termijnen als algemene regel beschrijven of de FamilySearch 110/95-regel als wettelijke norm presenteren. Markeer in de repository relevante historische of achterhaalde documentatie herkenbaar. Beperk de uitvoerbare scope waar nodig tot herleidbare metadata en externe bronlinks; lokale media en gevoelige persoonsgegevens vallen buiten scope.” Acceptatiecriteria: één canonieke policy met verwijzingen vanuit relevante documentatie; 100/75/50 uitsluitend gekoppeld aan bedoelde burgerlijke-standakten; 110/95 expliciet als niet-wettelijke heuristiek; BLOCKING/WARNING volgens materialiteit; strijdige formuleringen gecorrigeerd of verwijderd; geen lokale media en geen verwerking/publicatie van gevoelige persoonsgegevens. Deze HKH-story wijzigt uitsluitend de canonieke policy en relevante functionele/technische repositorydocumentatie. Zij wijzigt niet roadmapthema 0003, supersedeert onderzoeksvraag 6 niet en markeert geen dossiers in product-factory-workspace.

Benodigde Product Factory-systeemwijzigingen: (1) afgehandelde onderzoeksvragen corrigeerbaar of supersedeerbaar maken, met expliciete verwijzing van de oude vraag naar de geldende correctie en behoud van auditgeschiedenis

## Volledig gesprek

**Eigenaar:** De goedgekeurde productvisie blijft ongewijzigd. Ik wil met hoogste prioriteit een correctie aanbrengen in het privacy- en rechtenbeleid.
De termijnen 100/75/50 jaar mogen uitsluitend worden beschreven als openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten. Ze zijn geen algemene privacy-, AVG- of publicatieregel voor alle gegevens en bronnen in hkh-autopilot.
Behandel de huidige roadmaptekst “Nederlandse wachttermijnen zijn de primaire privacytoets” en afgehandelde onderzoeksvraag 6 daarom als achterhaald en te breed geformuleerd.
Totdat expliciet een ander beleid is goedgekeurd, blijft de bestaande repositorydocumentatie leidend: de FamilySearch 110/95-regel is een niet-wettelijke, conservatieve heuristiek; privacy- en rechtenonzekerheid wordt fail-closed behandeld. Verzin geen aanvullende wettelijke regels, curatorbesluiten of menselijke goedkeuringsstappen.
Ontbrekende beleidsinformatie mag niet automatisch iedere productverbetering blokkeren. Kies waar mogelijk een kleinere veilige scope, bijvoorbeeld alleen herleidbare metadata en externe bronlinks, zonder lokale media of gevoelige persoonsgegevens. Alleen een concreet en materieel privacy-, security- of rechtenrisico is BLOCKING; verbeteringen en toekomstige verfijningen zijn WARNING.
Maak hiervan de eerstvolgende prioriteit. Ik wil:
correctie van roadmapthema theme-hkh-autopilot-0003;
expliciete supersessie van afgehandelde onderzoeksvraag 6;
één canonieke privacy- en rechtenpolicy in de HKH-repository;
controle en correctie van functionele en technische documentatie die daarmee strijdig is;
een kleine, direct uitvoerbare documentatiestory als eerstvolgende story.
De productvisie zelf hoeft niet te veranderen. Historische onderzoeksdossiers hoeven ook niet herschreven te worden, maar moeten als historisch en waar nodig achterhaald herkenbaar blijven.
Vertel mij concreet welke onderdelen je zelf kunt aanpassen, welke pas in een roadmapsessie worden gewijzigd en welke een Product Factory-systeemwijziging vereisen.

**AI:** Ik kan in dit overleg de prioriteit vastleggen, de veilige scope en acceptatiecriteria formuleren, en de eerstvolgende documentatiestory klaarzetten als voorstel. Ik wijzig hier zelf geen bestanden.

Een roadmapsessie is nodig voor:
- correctie van theme-hkh-autopilot-0003;
- expliciete supersessie van onderzoeksvraag 6;
- vastleggen dat 100/75/50 uitsluitend over bedoelde burgerlijke-standakten gaat;
- bevestiging van fail-closed bij concrete privacy-, security- of rechtenrisico’s, met WARNING voor ontbrekende maar niet-materiële beleidsinformatie.

Een repositorywijziging is nodig voor één canonieke privacy- en rechtenpolicy, correctie van strijdige functionele en technische documentatie, en het herkenbaar markeren van historische of achterhaalde onderzoeksdossiers. De eerste story kan beperkt blijven tot documentatie, herleidbare metadata en externe bronlinks; lokale media en gevoelige persoonsgegevens vallen buiten scope.

Op basis van dit verzoek is geen Product Factory-systeemwijziging nodig. Dat wordt pas nodig als de huidige tooling supersessie, canonieke policyverwijzing of BLOCKING/WARNING-classificatie niet kan vastleggen. De eerstvolgende story moet daarom zijn: ‘Corrigeer en centraliseer privacy- en rechtenbeleid voor hkh-autopilot’, met controle op de genoemde roadmap- en documentatieformuleringen.

**Eigenaar:** Dit antwoord is nog niet volledig en bevat twee belangrijke correcties.
Een overleg maakt niet daadwerkelijk een story aan; formuleer daarom nu een exact storyvoorstel met titel, beschrijving en acceptatiecriteria, zodat dit volledig in de afsluitende samenvatting terechtkomt.
Daarnaast kan de huidige tooling afgehandelde onderzoeksvraag 6 niet echt wijzigen of supersederen. Leg daarom vast dat onmiddellijk een nieuwe correctie moet worden toegevoegd met de expliciete tekst dat deze vraag 6 vervangt, maar erken ook dat een Product Factory-systeemwijziging nodig is om afgehandelde onderzoeksvragen duurzaam corrigeerbaar of supersedeerbaar te maken.
Ook is een Product Factory-systeemwijziging nodig om de algemene criticusregel structureel aan te passen: alleen concrete, materiële en aantoonbare risico’s mogen BLOCKING zijn; optimalisaties, ontbrekende verfijningen en hypothetische toekomstige risico’s zijn WARNING.
Herhaal nu mijn besluit in je eigen woorden en geef daarna exact:
de gewenste correctie voor roadmapthema 0003;
de correctietekst die onderzoeksvraag 6 expliciet vervangt;
titel, beschrijving en acceptatiecriteria van de eerstvolgende HKH-documentatiestory;
de afzonderlijke benodigde Product Factory-systeemwijzigingen.
Neem al deze punten letterlijk en ondubbelzinnig op in de afsluitende overlegs­samenvatting.

**AI:** Je besluit: de productvisie blijft ongewijzigd. De 100/75/50-termijnen gelden uitsluitend als openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten, niet als algemene privacy-, AVG- of publicatieregel. De FamilySearch 110/95-regel blijft een niet-wettelijke, conservatieve heuristiek. Privacy-, security- en rechtenonzekerheid wordt fail-closed behandeld bij concrete materiële risico’s; ontbrekende of toekomstige verfijningen zijn WARNING en blokkeren niet automatisch een kleinere veilige scope. De bestaande documentatie en historische dossiers moeten hiermee in lijn worden gebracht, waarbij achterhaalde dossiers herkenbaar blijven.

Gewenste correctie voor roadmapthema 0003:
“De Nederlandse termijnen 100/75/50 jaar mogen uitsluitend worden gebruikt als openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten. Zij zijn geen algemene privacy-, AVG- of publicatieregel voor andere gegevens, bronnen of collecties binnen hkh-autopilot. De FamilySearch 110/95-regel is uitsluitend een niet-wettelijke, conservatieve heuristiek. Privacy- en rechtenonzekerheid wordt fail-closed behandeld wanneer sprake is van een concreet, materieel en aantoonbaar risico. Ontbrekende beleidsinformatie, optimalisaties en hypothetische toekomstige risico’s zijn WARNING en niet automatisch BLOCKING. De veilige uitvoeringsscope mag daarom waar mogelijk worden beperkt tot herleidbare metadata en externe bronlinks, zonder lokale media of gevoelige persoonsgegevens.”

Correctietekst die onderzoeksvraag 6 expliciet vervangt:
“Deze correctie vervangt en supersedeert onderzoeksvraag 6 en iedere eerdere beantwoording daarvan: de Nederlandse 100/75/50-termijnen zijn uitsluitend openbaarheidstermijnen voor daarvoor bedoelde burgerlijke-standakten. Ze vormen geen algemene privacy-, AVG- of publicatieregel voor alle gegevens en bronnen in hkh-autopilot. De FamilySearch 110/95-regel blijft een niet-wettelijke, conservatieve heuristiek. Alleen concrete, materiële en aantoonbare privacy-, security- of rechtenrisico’s zijn BLOCKING; ontbrekende beleidsinformatie, verbeteringen, optimalisaties en hypothetische toekomstige risico’s zijn WARNING.”

Eerstvolgende HKH-documentatiestory
Titel: “Corrigeer en centraliseer privacy- en rechtenbeleid voor hkh-autopilot”

Beschrijving: “Leg één canonieke privacy- en rechtenpolicy vast in de HKH-repository. Corrigeer roadmap- en functionele/technische documentatie die de 100/75/50-termijnen als algemene regel beschrijft of de FamilySearch 110/95-regel als wettelijke norm presenteert. Markeer historische of achterhaalde onderzoeksdossiers herkenbaar, zonder deze volledig te herschrijven. Beperk de uitvoerbare scope waar nodig tot herleidbare metadata en externe bronlinks; lokale media en gevoelige persoonsgegevens vallen buiten scope.”

Acceptatiecriteria:
1. Er is één canonieke privacy- en rechtenpolicy met verwijzingen vanuit relevante functionele en technische documentatie.
2. De 100/75/50-termijnen worden uitsluitend gekoppeld aan openbaarheid van daarvoor bedoelde burgerlijke-standakten.
3. De FamilySearch 110/95-regel wordt expliciet als niet-wettelijke, conservatieve heuristiek beschreven.
4. Concrete, materiële en aantoonbare privacy-, security- of rechtenrisico’s zijn BLOCKING; ontbrekende beleidsinformatie, optimalisaties en hypothetische toekomstige risico’s zijn WARNING.
5. Strijdige formuleringen, waaronder “Nederlandse wachttermijnen zijn de primaire privacytoets”, zijn gecorrigeerd of verwijderd.
6. Onderzoeksvraag 6 is in de huidige tooling niet wijzigbaar; de bovenstaande correctietekst wordt daarom onmiddellijk als afzonderlijke correctie toegevoegd en vermeldt expliciet dat zij vraag 6 vervangt.
7. Historische of achterhaalde onderzoeksdossiers zijn als zodanig herkenbaar.
8. De story wijzigt geen lokale media en introduceert geen verwerking of publicatie van gevoelige persoonsgegevens.

Afzonderlijk benodigde Product Factory-systeemwijzigingen:
- Ondersteuning om afgehandelde onderzoeksvraag

**Eigenaar:** Bijna, maar nog niet afsluiten. Het antwoord is in de database exact bij 4.000 tekens afgekapt, midden in:
“Ondersteuning om afgehandelde onderzoeksvraag…”

Daardoor ontbreken juist de Product Factory-systeemwijzigingen in het opgeslagen antwoord.
Er zit ook nog een scopefout in de voorgestelde HKH-story:
Een HKH-repositorystory kan de roadmapdatabase niet aanpassen.
Die story kan onderzoeksvraag 6 niet supersederen.
Historische onderzoeksdossiers staan voornamelijk in product-factory-workspace; de HKH-story kan die niet zomaar bijwerken.
Deze onderdelen moeten dus aparte roadmap- of Product Factory-acties blijven.
Stuur nog dit korte vervolgbericht:
Je antwoord is door de maximale berichtlengte afgekapt. Vul daarom uitsluitend het ontbrekende slot compact aan.
Corrigeer daarbij de scope: de HKH-documentatiestory wijzigt alleen de canonieke policy en relevante functionele/technische documentatie in de hkh-autopilot-repository. Correctie van roadmapthema 0003, toevoeging van de vervangende onderzoeksvraag en markering van historische dossiers in product-factory-workspace zijn afzonderlijke acties en geen acceptatiecriteria van die HKH-story.
Leg de benodigde Product Factory-systeemwijzigingen als volgt vast:
Afgehandelde onderzoeksvragen moeten corrigeerbaar of supersedeerbaar worden, met een expliciete verwijzing van de oude naar de geldende correctie en behoud van auditgeschiedenis.
De criticus moet bronhiërarchie en materialiteit toepassen: alleen concrete, materiële en aantoonbare risico’s zijn BLOCKING; optimalisaties, ontbrekende verfijningen en hypothetische risico’s zijn WARNING. Bij ontbrekend beleid kiest hij waar mogelijk een kleinere veilige scope.
Historische productgeheugen- en onderzoeksartefacten moeten als achterhaald/superseded gemarkeerd kunnen worden zonder hun auditgeschiedenis te herschrijven.
Bevestig ten slotte dat het overleg alleen besluiten en voorstellen vastlegt en deze wijzigingen nog niet werkelijk uitvoert. Neem dit compacte slot samen met alle eerdere teksten op in de afsluitende samenvatting.

**AI:** Aanvulling op het afgekaptte slot:

Afzonderlijk benodigde Product Factory-systeemwijzigingen:
- Afgehandelde onderzoeksvragen moeten corrigeerbaar of supersedeerbaar worden, met expliciete verwijzing van de oude vraag naar de geldende correctie en behoud van de auditgeschiedenis.
- De criticus moet bronhiërarchie en materialiteit toepassen: alleen concrete, materiële en aantoonbare privacy-, security- of rechtenrisico’s zijn BLOCKING. Optimalisaties, ontbrekende verfijningen en hypothetische toekomstige risico’s zijn WARNING. Bij ontbrekend beleid kiest de criticus waar mogelijk een kleinere veilige scope.
- Historische productgeheugen- en onderzoeksartefacten moeten als achterhaald of superseded kunnen worden gemarkeerd zonder hun auditgeschiedenis te herschrijven.

Scopecorrectie voor de HKH-documentatiestory:
De story wijzigt uitsluitend de canonieke privacy- en rechtenpolicy en relevante functionele en technische documentatie in de hkh-autopilot-repository. Correctie van roadmapthema 0003, toevoeging van de vervangende onderzoeksvraag en markering van historische dossiers in product-factory-workspace zijn afzonderlijke roadmap- of Product Factory-acties en geen acceptatiecriteria van deze HKH-story.

Dit overleg legt alleen besluiten en voorstellen vast. De genoemde repository-, roadmap- en Product Factory-systeemwijzigingen worden hier nog niet daadwerkelijk uitgevoerd.