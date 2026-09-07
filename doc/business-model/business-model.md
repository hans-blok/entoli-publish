# Entoli Business Model

*Met Agents. Voor blijvende waarde.*

![Entoli business model — van klant en probleem, via waardepropositie en aanbod, naar waardelevering en verdienmechanisme](business-model-visual.png)

*Het businessmodel in één overzicht: klant en probleem leiden tot klantwaarde en waardepropositie, verpakt in een aanbod, geleverd via een vaste keten van diensten, en verzilverd via een verdienmechanisme. Zie de [Business Model Canvas](business-model-canvas.md) voor dezelfde inhoud in het Osterwalder-format.*

> Dit document redeneert vanuit de klant, niet vanuit wat Entoli heeft gebouwd: **Klant → Probleem/behoefte → Klantwaarde → Waardepropositie → Business Service → Product/aanbod → Waardelevering → Verdienmechanisme → Versterking**. De onderliggende businessarchitectuur (Producten, Business Services, Business Processes in `vision-business-architecture`) blijft leidend voor wát bestaat; dit document legt uit wélke klantwaarde dat rechtvaardigt en hoe Entoli daar economische waarde aan overhoudt. Eén uitzondering is expliciet gemarkeerd: de commerciële behandeling van `Configureer professionele uitvoering` als "Entoli SaaS" (§6.3) is een businessmodelkeuze die vooruitloopt op de architectuurbron, die daar nog geen apart Product vastlegt. Waar de bronnen verder geen bewijs leveren, is dat gelabeld als **Hypothese** of **Openstaande vraag** — niet als vaststaand feit.

## 1. Context en drijfveren

Drie waarnemingen liggen aan de basis van waarom Entoli bestaat **[Decision/Evidence — vastgelegd in de visie]**:

- **Behoefte aan reproduceerbare en overdraagbare systemen.** Werk dat eenmalig en persoonsgebonden tot stand komt, is niet herhaalbaar en niet overdraagbaar.
- **Toenemende complexiteit van kennis en architectuur.** Professioneel werk steunt op steeds meer impliciete kennis en onderlinge samenhang.
- **Afhankelijkheid van individuen maakt systemen kwetsbaar.** Kennis en werkwijze die alleen in hoofden van specifieke mensen zit, maakt een organisatie kwetsbaar en niet schaalbaar.

Deze waarnemingen zijn niet AI-specifiek; AI maakt ze urgenter, omdat het de kosten van kennis expliciteren verlaagt én tegelijk verleidt om kennis juist ímpliciet in een taalmodel te laten zitten.

Entoli onderscheidt daarbij twee soorten verandering: **tijdelijke technologieontwikkeling** (welk model, welk framework, welke leverancier op dit moment vooroploopt) versus een **blijvende verandering in hoe professioneel werk kan worden gedefinieerd, overgedragen, geconfigureerd en uitgevoerd**. Entoli's marktthese is dat een businessmodel op de tweede, structurele verandering moet worden gebouwd — niet op de eerste. **[Decision]** Dit document doet geen uitspraken over marktomvang, concurrentiepositie of adoptiesnelheid; daarvoor ontbreekt onderbouwing in de bronnen.

## 2. Klanten — voor wie creëert Entoli waarde?

Voordat er over Producten wordt gesproken: wie heeft er baat bij wat Entoli doet? Onderstaande rollen zijn een businessmodel-indeling, geen aparte personen per se — in een kleine organisatie vallen ze vaak samen.

| Rol | Wat probeert deze rol te bereiken | Waar loopt deze rol tegenaan | Aard van de rol |
|---|---|---|---|
| **Knowledge Authority** | Eén gezaghebbende, eenduidige vastlegging van domeinkennis en terminologie | Kennis is verspreid, impliciet, of afhankelijk van wie er toevallig is | Beslisser over inhoud; begunstigde |
| **Professional Capability Developer** | Herbruikbare professionele rollen en capaciteit ontwikkelen op basis van die kennis | Elke keer opnieuw beginnen per team of project; geen herbruikbare basis | Gebruiker; begunstigde |
| **Professional User** | Daadwerkelijk professioneel werk sneller en betrouwbaarder uitvoeren | Werk is niet reproduceerbaar, niet traceerbaar, of te afhankelijk van één persoon of tool | Gebruiker; directe begunstigde |
| **Organisational Buyer / Governor** | Verantwoord investeren in AI-ondersteund werk; risico, compliance en kosten beheersen | Onvoldoende zicht op en grip op welke kennis, regels en modellen AI-gebruik stuurt; vendor lock-in | Besluitvormer/koper; begunstigde |

Het businessmodel moet voor elke rol een herkenbare reden geven om Entoli te gebruiken of te steunen — niet alleen voor de rol die uiteindelijk betaalt.

## 3. Klantproblemen en -behoeften

Per rol, afgeleid uit de drijfveren in §1 — dit zijn klantproblemen, geen Entoli-architectuurproblemen:

- **Knowledge Authority**: professionele kennis blijft impliciet, verspreid over documenten, mensen en gewoontes, en is daardoor niet controleerbaar of overdraagbaar naar nieuwe mensen of systemen.
- **Professional Capability Developer**: zonder een expliciete kennisbasis moet elke professionele rol of werkwijze opnieuw worden "uitgevonden," met wisselende kwaliteit en geen garantie dat twee toepassingen consistent zijn.
- **Professional User**: AI-ondersteund werk is vaak niet reproduceerbaar en niet herleidbaar — onduidelijk op basis van welke kennis, regels of context een resultaat tot stand kwam, en het werk hangt af van wie het heeft opgezet.
- **Organisational Buyer / Governor**: het is moeilijk te beheersen en te verantwoorden welke kennis, regels en modellen AI-gebruik in de organisatie stuurt, en organisaties willen niet structureel afhankelijk worden van één AI-leverancier of van individuele sleutelpersonen.

Daarnaast signaleert Entoli een verschuivend knelpunt: **software maken wordt met AI en tooling steeds makkelijker, maar de definitiefase (architectuur, requirements, datamodellering) blijft daarbij achter.** Dit is geen uitspraak uit `vision-business-architecture` of eerdere versies van dit document, maar een toevoeging op basis van recente marketingcommunicatie. **[Businessmodelkeuze — nieuw, nog niet in de architectuurbronnen onderbouwd]** Zolang dit niet in de canonieke visie is teruggelegd, moet het hier gelezen worden als een aanvullend, extern gecommuniceerd inzicht, niet als een architecturaal vastgestelde driver.

Gemeenschappelijke noemer: professionele kennis en werkwijze zijn onvoldoende **expliciet, overdraagbaar en beheersbaar** gemaakt om onafhankelijk van specifieke mensen, modellen of leveranciers te kunnen bestaan.

## 4. Klantwaarde

Voor elk probleem de waardevolle uitkomst — als resultaat voor de klant, niet als Entoli-artefact:

| Probleem | Waardevolle uitkomst voor de klant |
|---|---|
| Kennis is impliciet en persoonsgebonden | Kennis wordt **overdraagbaar en herbruikbaar**, onafhankelijk van wie haar heeft vastgelegd |
| Professionele rollen worden telkens opnieuw uitgevonden | Professionele capaciteit wordt **reproduceerbaar en inzetbaar** zonder de oorspronkelijke bouwers |
| AI-werk is niet herleidbaar | Werk wordt **traceerbaar en beheersbaar**: aantoonbaar op basis van welke kennis, regels en context een resultaat ontstond |
| Afhankelijkheid van één leverancier of individu | **Verminderde afhankelijkheid** van specifieke modellen, leveranciers of sleutelpersonen |
| AI-werk moet sneller en op meer schaal, zonder controle te verliezen | **Productiviteit en schaalbaarheid mét vertrouwen** — niet het een ten koste van het ander |

Deze vijf uitkomsten — overdraagbaarheid, reproduceerbaarheid, traceerbaarheid/beheersing, verminderde afhankelijkheid, en productiviteit-met-vertrouwen — zijn de kern van elke waardepropositie die hierna volgt.

## 5. Waardepropositie

Niet: *"Wij bouwen een AI-platform."*

Voor elke rol afzonderlijk:

- **Voor de Knowledge Authority**: een gezaghebbend, expliciet vastgelegd semantisch fundament, los van individuele medewerkers.
- **Voor de Professional Capability Developer**: het vermogen om professionele rollen en werkwijzen één keer goed te definiëren en daarna herhaald in te zetten.
- **Voor de Professional User**: werk dat sneller gaat én herleidbaar blijft — geen keuze tussen snelheid en controle.
- **Voor de Organisational Buyer/Governor**: aantoonbare beheersing over welke kennis, regels en modellen AI-gebruik sturen, zonder structurele afhankelijkheid van één leverancier.

Samengevat in één overkoepelende propositie:

> **Trusted AI-powered Professional Work** — professioneel kenniswerk sneller en schaalbaarder uitvoeren met AI, terwijl de gebruikte kennis, regels, context en uitvoering expliciet beheerst en herleidbaar blijven.

Kort samengevat wat dit uniek maakt: **expliciete kennis als fundament voor professionele AI-capaciteit**.

- Domeinkennis expliciet en canoniek vastgelegd.
- Professionele functies als herbruikbare Agents.
- Onafhankelijk van specifieke AI-modellen en tooling.
- Traceerbaar en beheersbaar.
- Open kennisbasis, professionele toepassing.

Deze belofte blijft geldig ook als de onderliggende AI-technologie of Entoli's huidige Producten veranderen: hij gaat over overdraagbare, beheersbare professionele capaciteit, niet over een specifiek stuk software. Positionering: Entoli is niet nóg een agentframework, maar de **semantische infrastructuur** waarop organisaties hun eigen betrouwbare professionele AI-capaciteit ontwikkelen, configureren en inzetten.

## 6. Aanbod — hoe Entoli die waarde verpakt

Nu pas volgen de Producten en Business Services, elk teruggeredeneerd naar de klantwaarde uit §4–§5. Voor volledige architecturale definities is `business-processes-services-and-products.md` leidend; hier volgt alleen de koppeling naar klantwaarde. **[Decision/Evidence — architectuur]**

### 6.1 Entoli Studio — voor de Knowledge Authority en Professional Capability Developer

Klantwaarde eerst: een organisatie moet professionele kennis expliciet en gezaghebbend kunnen vastleggen (overdraagbaarheid, §4), en op basis daarvan herbruikbare professionele rollen kunnen ontwikkelen (reproduceerbaarheid, §4) — zónder daarvoor afhankelijk te zijn van de oorspronkelijke experts.

**Entoli Studio** is het Product waarmee Entoli die waarde levert: het klantgerichte SaaS-product dat `Ontwikkel canon` (kennis expliciteren tot een Canon) en `Ontwikkel professionele capaciteit` (professionele rollen definiëren en bundelen tot inzetbare pakketten) aggregeert. Een **Canon** is hierbij het architecturale mechanisme waarmee die waarde wordt gerealiseerd — niet de klantwaarde zelf: een klant koopt geen Canon, hij koopt het vermogen om kennis te expliciteren, te beheersen en daarop voort te bouwen.

Concreet biedt Entoli Studio: canons modelleren; Agents en intents definiëren; organisatiekennis configureren; herbruikbare professionele capaciteit ontwikkelen; gebaseerd op open standaarden.

Elke klant ontwikkelt in zijn eigen Entoli Studio-omgeving zijn eigen, klant-specifieke canon, voortbouwend op een open referentiecanon (zie §7). Entoli gebruikt Entoli Studio ook zelf om die referentiecanons te bouwen.

### 6.2 Entoli Workspace — voor de Professional User

Klantwaarde eerst: een professional moet daadwerkelijk werk kunnen uitvoeren dat sneller en schaalbaarder gaat, zonder herleidbaarheid en beheersing te verliezen (traceerbaarheid en productiviteit-met-vertrouwen, §4).

**Entoli Workspace** is het Product waarmee die waarde wordt geleverd: het klantgerichte SaaS-product dat `Voer professioneel werk uit` aggregeert — instructies samenstellen, het werk uitvoeren, overdragen naar vervolgwerk, en het resultaat opleveren, op een traceerbare en beheerste manier.

Concreet biedt Entoli Workspace: Agents inzetten voor professioneel werk; werken binnen eigen context; community-canons gebruiken; traceerbare resultaten; van vraag naar werkresultaat.

**Studio–Workspace relatie**: Entoli Studio ontwikkelt professionele capaciteit; Entoli Workspace past die capaciteit toe in daadwerkelijk werk. **[Evidence — architectuur]** Dit opent een mogelijk sterker mechanisme: *ontwikkel capaciteit (Studio) → pas haar toe in werk (Workspace) → leer waar zij tekortschiet → verbeter haar (terug naar Studio) → vergroot de herbruikbare waarde.* Dit is een **Hypothese**: het veronderstelt dat Workspace-gebruik daadwerkelijk aanleiding geeft tot herziening in Studio, en dat dit voor een klant meetbaar meer oplevert dan de twee producten los. Dat vraagt validatie in de praktijk (zie §10).

### 6.3 Entoli SaaS — hosting, configuratie en beheer als zichtbare laag

Klantwaarde eerst: voordat werk kan worden uitgevoerd, moet er een werkende, beheerste operationele omgeving zijn — inclusief de mogelijkheid om van AI-leverancier te wisselen zonder de professionele rollen te hoeven aanpassen (verminderde afhankelijkheid, §4) — en die omgeving moet gehost, geconfigureerd, beheerd en actueel gehouden worden.

`Configureer professionele uitvoering` is de Business Service die dit levert: de operationele omgeving, providertoegang, orchestratie en modelkeuze inrichten. Dit is waar **modelonafhankelijkheid** zit. Deze Business Service wordt geleverd via **Entoli SaaS**: de hostings-, configuratie- en beheerlaag die zowel Entoli Studio als Entoli Workspace operationeel draagt, en die daarnaast als zichtbare, expliciet aangeboden implementatie- en ondersteuningsdienst aan klanten wordt gepresenteerd (inrichting, doorlopende ondersteuning, updates). **[Businessmodelkeuze — herzien]**

Concreet biedt Entoli SaaS: veilige en betrouwbare hosting; configuratie en tenant-setup; beheer en monitoring; regelmatige updates; schaalbaar en zorgeloos in gebruik.

Dit is een bewuste herziening ten opzichte van de eerdere positie in dit document: eerder werd deze Business Service uitsluitend als intern, niet-gecommercialiseerd mechanisme beschreven, zonder eigen omzetregel. Die aanname is nu losgelaten. Belangrijk om vast te houden: de canonieke businessarchitectuur (`business-processes-services-and-products.md`) legt voor `Configureer professionele uitvoering` nog geen eigen, klantgericht **Product** vast — deze herziening is dus vooralsnog een **businessmodelkeuze die vooruitloopt op** de architectuur, niet een architecturale vaststelling. Zolang de architectuurbron dit niet zelf bijwerkt, moet "Entoli SaaS" hier gelezen worden als de commerciële presentatie van een bestaande Business Service, niet als een nieuw canoniek Product-element (zie §14 en §15).

De strategische vraag is nu specifieker dan voorheen:

> Blijft Entoli SaaS een door Entoli beheerde, impliciete laag onder Studio en Workspace met een eigen implementatie-/ondersteuningsomzet (huidige koers), of groeit dit door naar een volwaardig, door de klant zelf bedienbaar Product? **[Toekomstoptie — niet besloten]**

### 6.4 Professional Services — voor wie het zelf (nog) niet kan

Klantwaarde eerst: niet elke organisatie heeft de expertise of capaciteit om zelfstandig een semantisch fundament en professionele capaciteit op te bouwen, en veel organisaties willen hun eigen mensen daar juist onafhankelijk in maken.

- **`Bied consultancy`** — deskundige begeleiding voor organisaties die niet zelfstandig een canon en semantisch fundament kunnen of willen opzetten.
- **`Bied training`** — het overdragen van vaardigheden aan klantmedewerkers, zodat zij Entoli Studio en Entoli Workspace zelfstandig kunnen gebruiken — een directe uitwerking van "verminderde afhankelijkheid" (§4), nu gericht op afhankelijkheid van Entoli zelf.

Beide zijn **gelijkwaardige** Business Services, niet ondergeschikt aan de SaaS-producten: voor een nieuwe klant zijn ze vaak de eerste stap, en voor bestaande klanten blijven ze relevant bij verdieping of maatwerk.

## 7. Waardelevering — hoe Entoli de belofte structureel waarmaakt

Op business-modelniveau, niet als volledige procescatalogus:

De architectuur beschrijft één doorlopende keten van kennis vastleggen tot resultaat opleveren; elk Product/Business Service hierboven is een schakel daarin: **[Evidence — architectuur]**

| Schakel | Business Service | Geleverd via |
|---|---|---|
| Kennis vastleggen | `Ontwikkel canon` | Entoli Studio |
| Capaciteit voorbereiden | `Ontwikkel professionele capaciteit` | Entoli Studio |
| Uitvoering configureren | `Configureer professionele uitvoering` | Entoli SaaS (§6.3) |
| Werk voorbereiden, uitvoeren, overdragen en opleveren | `Voer professioneel werk uit` | Entoli Workspace |

Als doorlopende cyclus vanuit klantperspectief bestaat waardelevering uit vijf stappen, die zich herhalen: **1. Behoefte (klantvraag) → 2. Kennis en capaciteit configureren → 3. Werk uitvoeren met Agents → 4. Traceerbaar werkresultaat → 5. Leren en verbeteren** — waarna inzichten uit stap 5 teruglopen naar stap 2, zodat de kennis en capaciteit in Entoli Studio verder verbeteren. Dit is de continue waardecreatie die de Studio–Workspace-relatie (§6.2) op procesniveau concretiseert.

Twee mechanismen ondersteunen deze levering, elk met een eigen rol:

- **Open referentiecanons** (Edgy, BPMN, ArchiMate, Agent Development e.a.) — door Entoli zelf ontwikkeld en waar mogelijk open gepubliceerd, geven een klant een startpunt voor zijn eigen canon in plaats van bij nul te beginnen. **[Decision]** Klant-specifieke canons — uitbreidingen op een referentiecanon met eigen elementen, relaties, regels en context — blijven privé-IP van de klant.
- **Interne configuratie** (§6.3) zorgt dat wat in Studio is ontwikkeld ook daadwerkelijk operationeel bruikbaar is in Workspace, zonder dat de klant dit zelf hoeft in te richten.

Onderscheid klantgerichte waarde versus interne mechanismen: de klant ervaart "mijn kennis en capaciteit zijn herbruikbaar" en "mijn werk is traceerbaar en snel," niet de onderliggende orchestratie- of modelconfiguratie — die is een intern mechanisme dat deze waarde mogelijk maakt, geen zelfstandige klantpropositie.

## 8. Waardevangst — wie betaalt Entoli, waarvoor?

Entoli onderscheidt hierin vier verdienmechanismen:

| Verdienmechanisme | Aanbod | Wie betaalt | Waarvoor | Mechaniek |
|---|---|---|---|---|
| **SaaS-abonnementen** | Entoli Studio | Organisatie (via Knowledge Authority/Capability Developer) | Toegang tot Entoli Studio — kennis en capaciteit ontwikkelen | Terugkerende SaaS-omzet — precieze eenheid/abonnementsvorm **[Toekomstoptie, niet besloten]** |
| **SaaS-abonnementen** | Entoli Workspace | Organisatie (via Professional User/budgethouder) | Toegang tot Entoli Workspace — professioneel werk uitvoeren | Terugkerende SaaS-omzet; abonnement, gebruik, of hybride **[Toekomstoptie, niet besloten]** |
| **Configuratie en begeleiding** | Entoli SaaS (`Configureer professionele uitvoering`) | Organisatie (via Organisational Buyer/Governor) | Implementatie, inrichting en doorlopende ondersteuning: hosting, configuratie, beheer en updates van de operationele omgeving | Implementatie- en ondersteuningsomzet, naast/onder Studio en Workspace **[Businessmodelkeuze — herzien, prijsvorm nog niet besloten]** |
| **Consultancy** | `Bied consultancy` | Organisatie die begeleiding inkoopt | Advies en maatwerktrajecten bij canon-/kennisontwikkeling | Professional-services-omzet |
| **Opleiding** | `Bied training` | Organisatie die capaciteit wil overdragen | Geven van trainingen, vaardigheden om zelfstandig te werken | Training-/services-omzet |
| *(geen verdienmechanisme)* | Open referentiecanons | Niemand | Lagere instapdrempel, ecosysteem | Geen omzet; investering (zie §9) |

**Verdienmechanisme versus prijs**: dit document legt vast *waarom* en *waarvoor* betaald zou worden (mechanisme), niet de prijseenheid, het tarief of het abonnementsmodel (prijs) — dat laatste is voor Entoli Studio en Entoli Workspace nog niet besloten.

## 9. Structurele economie

- **Schaalbaar digitaal**: Entoli Studio en Entoli Workspace zijn software; eenmaal ontwikkeld, kunnen ze door meerdere klanten worden gebruikt tegen relatief lage marginale kosten per extra klant.
- **Mensafhankelijke capaciteit**: `Bied consultancy` en `Bied training` schalen met de beschikbare tijd van Entoli's mensen — omzet groeit hier niet automatisch mee met het aantal klanten zoals bij SaaS.
- **Vooraf-investering in open activa**: de open referentiecanons vergen investering van Entoli zelf (tijd, expertise) vóórdat er sprake is van klantomzet — een bewuste kost om het kip-ei-probleem te doorbreken (zie §10), niet een kostenpost die met gebruik meegroeit.
- **Variabele uitvoeringskosten**: het daadwerkelijk uitvoeren van werk in Entoli Workspace hangt af van AI-modelgebruik, waarvan de kosten meegroeien met gebruiksvolume. Modelonafhankelijkheid (§6.3) is hier ook economisch relevant: het maakt het mogelijk om leverancier of model te kiezen op basis van kosten en geschiktheid, zonder de professionele rollen te hoeven aanpassen.
- **Hosting- en beheerkosten (Entoli SaaS)**: het draaiend houden van de operationele omgeving — hosting, configuratie, beheer en updates — kent zowel een relatief vaste component (platformbeheer) als een component die meegroeit met het aantal klantomgevingen. Nu dit expliciet als eigen implementatie-/ondersteuningsdienst wordt aangeboden (§6.3, §8), staat hier voor het eerst een eigen omzet tegenover, naast de bijbehorende kosten.

Dit is geen financieel model met bedragen, maar maakt zichtbaar welke delen van het aanbod digitaal schalen, welke aan mensen gebonden zijn, welke vooraf worden geïnvesteerd, en welke met gebruik meebewegen.

## 10. Versterking en groei

Entoli communiceert inmiddels expliciet een **groeithese**: dat het ecosysteem van herbruikbare canons en capaciteit, gecombineerd met het Studio–Workspace-mechanisme, op termijn tot netwerkeffecten, grotere adoptie en een sterkere marktpositie leidt. **[Businessmodelkeuze — herzien]** Dit document benoemt deze keten daarom niet langer alleen als losse, ongevalideerde hypothesen, maar als de groeithese die Entoli extern uitdraagt. Tegelijk blijft vastgelegd wélke causale schakels daarbinnen nog om validatie in de praktijk vragen, zodat de these navolgbaar en falsifieerbaar blijft — dat onderscheid is niet losgelaten, alleen de presentatie ervan.

**De groeithese, stap voor stap:**

1. **Groeiende community** — open referentiecanons *(Decision)* en herbruikbare agent-templates trekken gebruikers en bijdragers aan rond gedeelde semantische fundamenten.
2. **Netwerkeffecten** — meer herbruikbare canons, agent-templates en klantervaring vergroten de waarde van het ecosysteem voor iedere volgende gebruiker: meer klant-specifieke canons en Workspace-gebruik leveren signalen op die referentiecanons en professionele capaciteit in Entoli Studio verbeteren, wat het aanbod voor nieuwe en bestaande klanten waardevoller maakt.
3. **Grotere adoptie** — een waardevoller ecosysteem en een sterkere Studio–Workspace-cyclus (ontwikkelen → toepassen → leren → verbeteren → herbruiken) verlagen de drempel voor nieuwe klanten en vergroten het gebruik bij bestaande klanten.
4. **Sterkere marktpositie** — grotere adoptie, opgebouwd via een moeilijk te kopiëren combinatie van open referentiecanons, semantische methodologie en opgebouwde klantrelaties, versterkt Entoli's positie ten opzichte van alternatieven zonder expliciete canon of modelonafhankelijkheid.

**Wat nog validatie vraagt** (ongewijzigd ten opzichte van de eerdere, voorzichtiger formulering): dat open referentiecanons daadwerkelijk tot meetbare adoptie leiden; dat Workspace-gebruik daadwerkelijk en systematisch terugvloeit naar verbetering in Studio; en dat Professional Services daadwerkelijk tot blijvende zelfstandigheid leidt in plaats van doorlopende afhankelijkheid van Entoli's mensen. Deze drie schakels blijven gelabeld in §13 als **Hypothese**, ook nu de keten als geheel als groeithese wordt gepresenteerd.

## 11. Businessmodel in één overzicht

| Klant/rol | Probleem/behoefte | Klantwaarde | Aanbod | Economisch mechanisme |
|---|---|---|---|---|
| Knowledge Authority | Kennis is impliciet en verspreid | Overdraagbare, gezaghebbende kennis | Entoli Studio (`Ontwikkel canon`) | SaaS-omzet, prijseenheid TBD |
| Professional Capability Developer | Rollen worden telkens opnieuw uitgevonden | Reproduceerbare professionele capaciteit | Entoli Studio (`Ontwikkel professionele capaciteit`) | SaaS-omzet, prijseenheid TBD |
| Professional User | Werk is niet traceerbaar of te langzaam | Snel én herleidbaar werk | Entoli Workspace (`Voer professioneel werk uit`) | SaaS-omzet, model TBD (abonnement/gebruik/hybride) |
| Organisational Buyer/Governor | Onvoldoende beheersing, vendor lock-in | Aantoonbare beheersing, modelonafhankelijkheid | Entoli SaaS (`Configureer professionele uitvoering`) | Implementatie-/ondersteuningsomzet, prijsvorm TBD |
| Organisatie zonder eigen capaciteit | Kan zelf geen canon/capaciteit opzetten | Deskundige begeleiding | `Bied consultancy` | Professional-services-omzet |
| Organisatie die zelfstandig wil worden | Wil onafhankelijk worden van Entoli's mensen | Overgedragen vaardigheid | `Bied training` | Training-/services-omzet |
| Ecosysteem/nieuwe klanten (breed) | Hoge instapdrempel om te beginnen | Herbruikbaar startpunt | Open referentiecanons | Geen omzet; investering (Hypothese: verlaagt drempel) |

Onbekende cellen zijn hierboven niet ingevuld met verzonnen antwoorden; waar een mechanisme nog niet vastligt, staat dat expliciet als TBD.

## 12. Besluiten en bewijs (Decisions & Evidence)

Vastgelegd in de businessarchitectuur of expliciet besloten, niet ter discussie in dit document:

- Entoli Studio en Entoli Workspace zijn losstaande Producten; een Product aggregeert Business Services en realiseert zelf niets.
- Business Processes realiseren Business Services.
- `Ontwikkel canon` en `Ontwikkel professionele capaciteit` worden aangeboden via Entoli Studio; `Voer professioneel werk uit` via Entoli Workspace.
- `Configureer professionele uitvoering` heeft vandaag geen klantgericht **Product** in de canonieke businessarchitectuur; de architectuurbron legt hier nog steeds interne levering vast.
- `Bied consultancy` en `Bied training` zijn Professional Services, gelijkwaardig aan de Core Services.
- Entoli publiceert zelf een beperkte set open referentiecanons; klant-specifieke canons blijven privé-IP van de klant.
- Entoli presenteert `Configureer professionele uitvoering` als "Entoli SaaS" — een zichtbare hosting-, configuratie- en beheerlaag met een eigen implementatie-/ondersteuningsomzet, naast Studio en Workspace. **[Businessmodelkeuze — herzien; loopt vooruit op de architectuurbron, zie §6.3]**
- De groei van open referentiecanons, netwerkeffecten, adoptie en marktpositie wordt door Entoli extern gecommuniceerd als samenhangende groeithese (§10). **[Businessmodelkeuze — herzien]**

## 13. Businesshypothesen

Causale aannames over klant- of marktgedrag die nog validatie vragen:

- Open referentiecanons verlagen daadwerkelijk de drempel tot adoptie van Entoli Studio, Entoli Workspace of Professional Services.
- Gebruik van professionele capaciteit in Entoli Workspace levert bruikbare signalen op die de ontwikkeling in Entoli Studio verbeteren, en dit levert meetbaar meer waarde op dan de twee Producten los.
- Professional Services (consultancy/training) leiden tot blijvend, zelfstandig SaaS-gebruik in plaats van doorlopende afhankelijkheid van Entoli's mensen.
- Organisaties zijn bereid te betalen voor aantoonbare modelonafhankelijkheid en beheersing, los van de vraag of dit ooit een apart geprijsd onderdeel wordt.

## 14. Toekomstopties (bewust nog geen onderdeel van het huidige model)

- Een eigen, klantgericht, zelfbedienbaar **Product** voor `Configureer professionele uitvoering`/Entoli SaaS (de bronarchitectuur noemt een werktitel, `entoli control`, zonder verdere scope — hier niet als bestaand Product geïntroduceerd). Entoli SaaS blijft vooralsnog een door Entoli beheerde laag met een eigen implementatie-/ondersteuningsomzet, geen door de klant zelf te bedienen Product.
- Canon-curatie/certificatie: Entoli als vertrouwens-/governancelaag rondom een ecosysteem van canons (versiebeheer, kwaliteitskeurmerk, compatibiliteitsgarantie). Geen prijsvorm of mechaniek hiervoor uitgewerkt; pas relevant zodra er meerdere referentiecanons bestaan.
- Het exacte verdienmodel voor Entoli Workspace (abonnement, gebruik, of hybride), voor Entoli Studio (prijseenheid), en voor Entoli SaaS (implementatie-/ondersteuningstarief).

## 15. Openstaande vragen

- **Entoli SaaS versus de canonieke architectuur**: de businessarchitectuur (`business-processes-services-and-products.md`) legt voor `Configureer professionele uitvoering` nog geen klantgericht Product vast; dit document commercialiseert deze Business Service inmiddels wel als "Entoli SaaS." Deze architectuurbron zelf moet nog worden bijgewerkt of expliciet bevestigen dat dit een bewuste, blijvende asymmetrie is (Business Service met commerciële behandeling, zonder formeel Product-element).
- **Configuratie als toekomstig zelfbedienbaar Product**: blijft Entoli SaaS een door Entoli beheerde laag, of groeit dit door naar een door de klant zelf bediende capaciteit met een eigen Product? Niet besloten.
- **DAMA/DMBOK** (specifiek content-/IP-vraagstuk, geen fundamentele businessmodelvraag): blijft een `Bied consultancy`-opdracht zolang de IP-verhouding met DAMA niet is opgehelderd (overleg NL-Meta Data Werkgroep).
- **Naamgeving en volgorde in de ArchiMate-bronmodellen** bevatten nog open punten (zie `business-processes-services-and-products.md` §10) die de terminologie in dit document kunnen raken zodra ze worden opgelost.
- **Canon-curatie/certificatie**: of, en zo ja wanneer, dit een reële commerciële laag wordt is niet vastgesteld.

Geen van deze punten is hier stilzwijgend opgelost; ze vragen een aparte architecturale of commerciële beslissing.

## 16. Businessmodel-verklaring

> Voor organisaties die professioneel kenniswerk willen versnellen met AI zonder de kennis, regels en herleidbaarheid van dat werk te verliezen — vertegenwoordigd door een Knowledge Authority, een Professional Capability Developer, Professional Users, en een Organisational Buyer/Governor — maakt Entoli professionele kennis en capaciteit expliciet, overdraagbaar en herbruikbaar, en past deze vervolgens traceerbaar toe in daadwerkelijk werk. Entoli levert dit via Entoli Studio (kennis en capaciteit ontwikkelen), Entoli Workspace (capaciteit toepassen in werk) en Entoli SaaS (hosting, configuratie en beheer van de uitvoeringsomgeving), ondersteund door Professional Services voor organisaties die dat niet zelfstandig kunnen of willen, en verlaagt de instapdrempel via een beperkte set open referentiecanons. Entoli verdient hieraan via terugkerende SaaS-omzet uit Studio en Workspace, implementatie-/ondersteuningsomzet uit Entoli SaaS (exacte prijsvormen nog te bepalen), en via Professional Services-omzet uit consultancy en training. Entoli's gecommuniceerde groeithese is dat een groeiende community rond open referentiecanons, netwerkeffecten binnen het ecosysteem, en de Studio–Workspace-cyclus samen tot grotere adoptie en een sterkere marktpositie leiden.

Wat nog onbekend is: de exacte verdienvorm van Entoli Workspace, Entoli Studio en Entoli SaaS (§8, §14); of de afzonderlijke schakels van de groeithese — het open-source-effect en de Studio–Workspace-terugkoppeling — in de praktijk daadwerkelijk optreden zoals gecommuniceerd (§10, §13); en of Entoli SaaS ooit doorgroeit naar een volwaardig, zelfbedienbaar Product, en of de architectuurbron zelf wordt bijgewerkt om de huidige commerciële behandeling te weerspiegelen (§6.3, §15).
