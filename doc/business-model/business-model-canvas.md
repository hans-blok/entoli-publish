# Entoli Business Model Canvas

## Purpose

Dit document structureert het bestaande businessmodel (`artefacten/business-model/business-model.md`) in het standaard Business Model Canvas-format (Osterwalder), zodat het in één oogopslag beoordeelbaar is door investeerders, partners en interne stakeholders. Het is **geen nieuw ontwerp** en voegt geen klantwaarde, propositie of verdienmechanisme toe die niet al in de bron staat.

Elk item is gelabeld:

- **Decision** — bewust vastgelegde keuze;
- **Evidence** — onderbouwd door de businessarchitectuur of vastgelegde visie;
- **Hypothesis** — causale aanname over klant-/marktgedrag, nog niet gevalideerd;
- **Unknown** — nog niet bepaald;
- **Future Option** — bewust (nog) buiten het huidige model.

Waar de bron onvoldoende antwoord geeft, is dat hier expliciet zichtbaar gemaakt — niet stilzwijgend ingevuld.

![Entoli Business Model Canvas — de negen Osterwalder-blokken ingevuld vanuit het Entoli-businessmodel](bmc-visual.png)

*Hetzelfde businessmodel als het [Entoli Business Model](business-model.md), gestructureerd in het negen-blokken Business Model Canvas-format.*

## Customer Problems and Needs

Overgenomen uit `business-model.md` §2–§4, als basis voor het hele canvas:

| Klantrol | Streeft naar | Loopt tegenaan | Waardevolle uitkomst |
|---|---|---|---|
| Knowledge Authority | Eén gezaghebbende, eenduidige kennisvastlegging | Kennis is verspreid, impliciet, persoonsgebonden | Overdraagbare, gezaghebbende kennis |
| Professional Capability Developer | Herbruikbare professionele rollen ontwikkelen | Elke keer opnieuw beginnen, wisselende kwaliteit | Reproduceerbare professionele capaciteit |
| Professional User | Werk sneller en betrouwbaarder uitvoeren | Werk niet reproduceerbaar of herleidbaar | Snel én herleidbaar werk |
| Organisational Buyer / Governor | Verantwoord investeren, risico beheersen | Onvoldoende grip op kennis/regels/modellen; vendor lock-in | Aantoonbare beheersing, modelonafhankelijkheid |

Deze vier rijen zijn de bron voor elk blok hieronder — elk canvasblok wordt vanuit deze klantrollen opgebouwd, niet vanuit Entoli's Producten.

## Business Model Canvas

### 1. Customer Segments

| Segment | Type | Gebruiker | Begunstigde | Beslisser | Koper | Belangrijkste behoefte |
|---|---|---|---|---|---|---|
| Organisaties met een eigen kennisdomein die AI-ondersteund professioneel werk willen professionaliseren | Organisatie (B2B) | Professional User | Professional User, Organisational Buyer | Organisational Buyer/Governor | Organisational Buyer/Governor | Werk sneller én herleidbaar |
| Organisaties met verspreide/impliciete domeinkennis | Organisatie (B2B) | Knowledge Authority | Hele organisatie | Knowledge Authority / Organisational Buyer | Organisational Buyer/Governor | Kennis expliciteren en beheersen |
| Organisaties die zelf geen semantisch fundament kunnen opzetten | Organisatie (B2B) | — | Knowledge Authority, Capability Developer | Organisational Buyer | Organisational Buyer/Governor | Begeleiding (`Bied consultancy`) |
| Organisaties die onafhankelijk willen worden van Entoli's mensen | Organisatie (B2B) | Capability Developer, Professional User | Organisatie zelf | Organisational Buyer | Organisational Buyer/Governor | Vaardigheidsoverdracht (`Bied training`) |

**Wie is de eerste plausibele betalende klant?** **[Unknown]** — `business-model.md` beschrijft klantrollen en waardevolle uitkomsten in algemene termen, maar prioriteert geen specifiek eerste segment (bijvoorbeeld naar sector, omvang, of urgentie). Dit document verbreedt het klantsegment daarom niet verder dan de bron toelaat, maar markeert dit expliciet als open vraag (zie "Questions to Validate").

### 2. Value Propositions

| Voor | Probleem | Gewenste uitkomst | Waarde die Entoli creëert | Waarom dit telt | Aanbod |
|---|---|---|---|---|---|
| Knowledge Authority | Kennis is impliciet en verspreid | Eén gezaghebbend fundament | Overdraagbare, herbruikbare kennis, onafhankelijk van wie haar vastlegde | Vermindert afhankelijkheid van individuen | Entoli Studio (`Ontwikkel canon`) |
| Professional Capability Developer | Rollen worden telkens opnieuw uitgevonden | Herbruikbare professionele capaciteit | Reproduceerbare, inzetbare professionele rollen zonder de oorspronkelijke bouwers | Schaalbaarheid en consistentie | Entoli Studio (`Ontwikkel professionele capaciteit`) |
| Professional User | Werk niet traceerbaar of te langzaam | Snel én herleidbaar werk | Productiviteit en schaalbaarheid zonder verlies van controle | Vertrouwen in AI-ondersteund werk | Entoli Workspace (`Voer professioneel werk uit`) |
| Organisational Buyer/Governor | Onvoldoende beheersing, vendor lock-in | Aantoonbare beheersing en modelonafhankelijkheid | Verminderde afhankelijkheid van één AI-leverancier of sleutelpersoon | Risicobeheersing, compliance | Entoli SaaS (`Configureer professionele uitvoering`) |

**Overkoepelende propositie** *(Evidence — visie)*:

> **Trusted AI-powered Professional Work** — professioneel kenniswerk sneller en schaalbaarder uitvoeren met AI, terwijl de gebruikte kennis, regels, context en uitvoering expliciet beheerst en herleidbaar blijven.

Waardedimensies die hierin samenkomen, zoals vastgelegd in de bron: overdraagbaarheid, reproduceerbaarheid, governance/traceerbaarheid, herbruikbaarheid, verminderde afhankelijkheid van individuen, en model-/technologieonafhankelijkheid. Geen van deze is hier toegevoegd zonder basis in `business-model.md` §4–§5.

### 3. Customer Relationships

| Relatievorm | Waar van toepassing | Status |
|---|---|---|
| Doorlopende SaaS-relatie (zelfbediening) | Entoli Studio, Entoli Workspace | **Decision** — Producten zijn SaaS |
| Begeleide/consultancy-relatie | `Bied consultancy` — voor klanten die zelf geen canon/fundament kunnen opzetten | **Decision** (architectuur) |
| Training/capaciteitsoverdracht | `Bied training` — expliciet gericht op het overbodig maken van doorlopende afhankelijkheid | **Decision** (architectuur) |
| Beheerde dienst met eigen implementatie-/ondersteuningsrelatie | Entoli SaaS (`Configureer professionele uitvoering`) — door Entoli beheerd en expliciet als dienst aangeboden, geen klant-zelfbediening | **Business Model Choice — herzien**; nog geen apart Product in de architectuurbron |

**Expliciete overgang**: het model beweegt in intentie van *"Entoli doet het werk voor de klant"* (consultancy, Entoli SaaS) naar *"Entoli stelt de klant in staat het zelf te doen"* (training, zelfstandig Studio/Workspace-gebruik). Dat deze overgang daadwerkelijk plaatsvindt — dat training en consultancy leiden tot blijvende zelfstandigheid in plaats van doorlopende afhankelijkheid van Entoli's mensen — is een **[Hypothesis]** (zie Hypothese-register, H3). Entoli SaaS blijft een structureel beheerde relatie, geen zelfbediening: dit is nu een expliciete commerciële keuze (§6.3 van de bron), niet louter een architecturale asymmetrie.

### 4. Channels

| Kanaal | Rol | Status |
|---|---|---|
| Open referentiecanons en groeiende community | Instapkanaal: verlaagt de drempel om kennis te maken met de Entoli-aanpak; Entoli communiceert dit expliciet als onderdeel van zijn groeithese | **Business Model Choice** (open publicatie) — dat dit adoptie versnelt blijft **[Hypothesis]** (H1) |
| Professional Services (consultancy/training) | Directe, persoonlijke ingang voor klanten die niet zelfstandig beginnen | **Decision** (architectuur) — vaak de eerste stap bij een nieuwe klant, zoals beschreven in de bron |
| Directe SaaS-toegang (Entoli Studio/Workspace) | Voor klanten die al bekend zijn met de aanpak of via Professional Services zijn ingestroomd | **Evidence** — Producten bestaan als zelfbedienings-SaaS |
| Communities rond referentiecanons (bijv. Edgy, BPMN, ArchiMate) | Ontdekkings- en geloofwaardigheidsbron, en volgens de gecommuniceerde groeithese de basis voor netwerkeffecten binnen het ecosysteem | **Business Model Choice** (strategie) — het adoptie-effect zelf blijft **[Hypothesis]** |

**Wat de bron niet beschrijft**: een expliciete sales-, marketing-, of partnerkanaalstrategie (advertenties, directe verkoop, wederverkopers, marktplaatsen) komt in `business-model.md` niet voor. Dit is hier dus **[Unknown]**, niet ingevuld met een aanname.

### 5. Revenue Streams

| Aanbod | Wie betaalt | Voor welke klantwaarde | Mechanisme | Terugkerend? | Status |
|---|---|---|---|---|---|
| Entoli Studio | Organisatie (Knowledge Authority/Capability Developer) | Kennis en capaciteit ontwikkelen | SaaS-omzet | Ja | **Decision** (Product); prijseenheid **Unknown** |
| Entoli Workspace | Organisatie (Professional User/budgethouder) | Professioneel werk uitvoeren | SaaS-omzet | Ja | **Decision** (Product); abonnement/gebruik/hybride **[Future Option, niet besloten]** |
| Entoli SaaS (`Configureer professionele uitvoering`) | Organisatie (Organisational Buyer/Governor) | Hosting, configuratie, beheer en updates van de uitvoeringsomgeving | Implementatie-/ondersteuningsomzet | Deels (doorlopende ondersteuning) | **Business Model Choice — herzien**; loopt vooruit op de architectuurbron (nog geen apart Product); prijsvorm **Unknown** |
| `Bied consultancy` | Organisatie die begeleiding inkoopt | Deskundige hulp bij canon-/kennisontwikkeling | Professional-services-omzet | Nee (doorgaans projectmatig) | **Decision** |
| `Bied training` | Organisatie die capaciteit wil overdragen | Vaardigheden om zelfstandig te werken | Training-/services-omzet | Nee (doorgaans projectmatig) | **Decision** |
| Open referentiecanons | Niemand | Lagere instapdrempel, ecosysteem | Geen omzet; investering | N.v.t. | **Decision** (open publicatie); economisch effect **[Hypothesis]** |

**Verdienmechanisme versus prijsmodel**: dit canvas legt vast *wie betaalt en waarvoor*, niet het tarief of de precieze eenheid — die zijn voor Entoli Studio en Entoli Workspace nog niet besloten.

**Dominante economische motor**: de bron identificeert geen vastgestelde dominante omzetbron. Gegeven dat Entoli Studio, Entoli Workspace én nu ook Entoli SaaS als (deels) terugkerende omzet zijn bedoeld, en Professional Services doorgaans projectmatig is, ligt een SaaS-zwaartepunt voor de hand zodra de Producten volwassen zijn — maar dit is een **[Hypothesis]**, niet een conclusie die de bron zelf trekt. Aanvankelijk kan Professional Services juist de eerste en grootste omzetbron zijn, zoals de bron zelf aangeeft voor nieuwe klanten.

### 6. Key Activities

| Activiteit | Waarom structureel belangrijk | Onderscheidend of operationeel |
|---|---|---|
| Ontwikkelen en onderhouden van Entoli Studio en Entoli Workspace (software) | Dit zíjn de terugkerende commerciële Producten | Onderscheidend |
| Ontwikkelen van open referentiecanons (Edgy, BPMN, ArchiMate, Agent Development) | Voedt het ecosysteem en verlaagt de instapdrempel (§7, §10 van de bron) | Onderscheidend |
| Leveren van Entoli SaaS: hosting, configureren en beheren van professionele uitvoering (`Configureer professionele uitvoering`) | Noodzakelijk om Entoli Workspace operationeel te laten werken, én nu een expliciet aangeboden dienst met eigen omzet | Operationeel én onderscheidend (herzien) |
| Leveren van consultancy en training | Eerste omzetbron en toegang tot klanten die niet zelfstandig beginnen | Onderscheidend én operationeel |
| Onderhouden van de semantische methodologie/architectuurprincipes | Onderbouwt de belofte van herleidbaarheid en beheersing die de propositie draagt | Onderscheidend |

Dit is geen volledige Business Process-catalogus; voor de canonieke procesindeling is `business-processes-services-and-products.md` leidend, niet dit canvas.

### 7. Key Resources

| Resource | Waarom economisch/strategisch belangrijk |
|---|---|
| Entoli Studio en Entoli Workspace (software/platform) | De dragers van de terugkerende SaaS-omzet |
| Open referentiecanons | Het "content"-fundament dat het ecosysteem aantrekkelijk maakt; zonder canons is een lege omgeving weinig waard |
| Semantische methodologie (hoe kennis wordt gecanoniseerd, capaciteit wordt opgebouwd) | De basis van de waardepropositie (herleidbaarheid, beheersing); niet triviaal te kopiëren |
| Expertise van Entoli's mensen (consultancy/training) | Draagt de Professional Services-omzet en de eerste klantrelaties |
| Klantrelaties en vertrouwen bij vroege klanten | Nodig om van consultancy naar zelfstandig SaaS-gebruik te bewegen (Hypothesis H3) |

Niet elk architecturaal Business Object is hier opgenomen als Key Resource — alleen wat economisch of strategisch zwaarwegend is, conform de bron.

### 8. Key Partners

| Partnercategorie | Wat Entoli nodig heeft | Aard van de afhankelijkheid | Bewust verminderen? |
|---|---|---|---|
| AI/modelleveranciers (OpenAI, Anthropic, Google, lokale modellen) | Toegang tot LLM's om professioneel werk daadwerkelijk uit te voeren | Structureel — zonder modeltoegang geen uitvoering | Ja — modelonafhankelijkheid is expliciet architectuurprincipe (§6.3 van de bron) |
| Standaardorganisaties/kenniscommunities (bijv. rond Edgy, BPMN, ArchiMate) | Bron van gezaghebbende kennis voor referentiecanons; geloofwaardigheid | Matig — Entoli wil zelf geen inhoudelijke autoriteit zijn, dus is mede afhankelijk van erkenning door deze communities | Nee, dit is juist gewenste samenwerking |
| Content-/IP-eigenaren met beperkingen (bijv. DAMA) | Toegang tot of gebruiksrecht op specifieke raamwerken | Beperkt en concreet (specifiek IP-vraagstuk, zie bron §14.2/§15) | Ja, waar IP-beperkingen open publicatie in de weg staan |

De bron noemt geen concrete cloud-/infrastructuurpartner, implementatiepartner, of naam van een specifieke samenwerking; dit is dus niet ingevuld met een aanname. Een technologieleverancier wordt hier alleen als Key Partner behandeld wanneer de bron een structurele afhankelijkheid benoemt (zoals modelleveranciers) — niet automatisch omdat SaaS-producten doorgaans op cloudinfrastructuur draaien.

### 9. Cost Structure

| Kostentype | Voorbeeld | Karakter |
|---|---|---|
| Softwareontwikkeling | Entoli Studio, Entoli Workspace | Relatief vast; investering vooraf, marginale kosten per klant laag |
| Ontwikkeling/onderhoud open referentiecanons | Edgy, BPMN, ArchiMate, Agent Development | Vooraf-investering, niet gebruiksafhankelijk |
| AI-modeluitvoering | Modelgebruik binnen Entoli Workspace | Gebruiksafhankelijk — groeit mee met uitvoeringsvolume |
| Professional Services-capaciteit | Consultancy en training | Mensafhankelijk — schaalt met beschikbare tijd van Entoli's mensen, niet automatisch met klantaantal |
| Entoli SaaS: hosting, configuratie en beheer (`Configureer professionele uitvoering`) | Operationele omgeving inrichten en onderhouden namens de klant | Deels vast (platformbeheer), deels meegroeiend met aantal klantomgevingen; staat nu tegenover een eigen omzetregel |

**Wat de schaalbaarheid kan beperken**: de gebruiksafhankelijke AI-uitvoeringskosten (marge onder druk bij groeiend Workspace-gebruik zonder prijsaanpassing) en de mensafhankelijke Professional Services- en Entoli SaaS-capaciteit (omzet schaalt niet vanzelf met meer klanten zolang deze diensten door Entoli's mensen worden geleverd). De bron bevat geen cijfers; dit blijft kwalitatief.

## Business Model Canvas — samenvattend overzicht

| Blok | Kern |
|---|---|
| **1. Customer Segments** | Organisaties met een kennisdomein die AI-werk willen professionaliseren; eerste betalend segment **[Unknown]** |
| **2. Value Propositions** | Trusted AI-powered Professional Work: overdraagbaarheid, reproduceerbaarheid, traceerbaarheid, verminderde afhankelijkheid, productiviteit-met-vertrouwen |
| **3. Customer Relationships** | SaaS-zelfbediening (Studio/Workspace) + begeleiding (consultancy/training) + beheerde configuratie (intern) |
| **4. Channels** | Open referentiecanons/community (Business Model Choice, adoptie-effect **[Hypothesis]**), Professional Services (Decision), directe SaaS-toegang; sales-/partnerkanaal **[Unknown]** |
| **5. Revenue Streams** | SaaS-omzet Studio/Workspace (prijsvorm **Unknown/Future Option**), implementatie-/ondersteuningsomzet Entoli SaaS (herzien), Professional-services-omzet |
| **6. Key Activities** | Studio/Workspace ontwikkelen, referentiecanons ontwikkelen, Entoli SaaS leveren (hosting/configuratie/beheer), consultancy/training, methodologie onderhouden |
| **7. Key Resources** | Studio/Workspace, open referentiecanons, semantische methodologie, expertise, klantrelaties |
| **8. Key Partners** | AI-modelleveranciers (afhankelijkheid bewust verminderd), kenniscommunities, specifieke content-/IP-eigenaren |
| **9. Cost Structure** | Vast (softwareontwikkeling, canon-investering), gebruiksafhankelijk (modeluitvoering, hosting), mensafhankelijk (Professional Services, Entoli SaaS-levering) |

## Business Model Reinforcement

Entoli communiceert inmiddels expliciet een **groeithese** (`business-model.md` §10): dat een groeiende community rond open referentiecanons, netwerkeffecten binnen het ecosysteem, en de Studio–Workspace-cyclus samen tot grotere adoptie en een sterkere marktpositie leiden. **[Business Model Choice — herzien]** Dit canvas benoemt de keten daarom als groeithese, en houdt tegelijk vast welke afzonderlijke schakels daarbinnen nog niet gevalideerd zijn:

1. **Groeiende community** — open referentiecanons *(Decision)* trekken gebruikers en bijdragers aan rond gedeelde semantische fundamenten *(Hypothesis dat dit daadwerkelijk optreedt, H1)*.
2. **Netwerkeffecten** — **Entoli Studio ontwikkelt professionele capaciteit** *(Evidence — architectuur)* → **Entoli Workspace past die capaciteit toe in werk** *(Evidence)* → uitvoering in Workspace kan tekortkomingen of verbetermogelijkheden blootleggen en zo referentiecanons/capaciteit verbeteren *(Hypothesis, H2 — geen vastgelegd terugkoppelmechanisme)*, wat het ecosysteem waardevoller maakt voor iedere volgende gebruiker.
3. **Grotere adoptie** — een waardevoller ecosysteem en een sterkere Studio–Workspace-cyclus verlagen de drempel voor nieuwe klanten en vergroten gebruik bij bestaande klanten *(Hypothesis, samenstelling van H1+H2)*. Professional Services dragen hieraan bij: zij bouwen kennis en vertrouwen op bij een klant *(Decision)* → de klant wordt mogelijk zelfstandiger in het gebruik van Entoli Studio/Workspace *(Hypothesis, H3)*.
4. **Sterkere marktpositie** — grotere adoptie, opgebouwd via een moeilijk te kopiëren combinatie van open referentiecanons, semantische methodologie en klantrelaties, versterkt Entoli's positie *(Hypothesis, afhankelijk van 1–3)*.

Geen van de onderliggende schakels is in de bron gevalideerd; ze zijn hier zichtbaar gemaakt als de gecommuniceerde richting, niet als bewezen mechanisme. Zie het Hypothese-register hieronder voor wat concreet nog getoetst moet worden.

## Business Model Hypotheses

| ID | Businessmodel-hypothese | Waarom het ertoe doet | Huidig bewijs | Validatie nodig |
|---|---|---|---|---|
| H1 | Open referentiecanons verlagen daadwerkelijk de drempel tot adoptie van Entoli Studio, Entoli Workspace of Professional Services | Onderbouwt de open-source-strategie als acquisitiekanaal (Blok 4) en investering (Blok 9) | Strategische analogie met andere open-source-ecosystemen; geen eigen marktdata | Meten of gebruikers van open canons daadwerkelijk doorstromen naar betaalde Producten/diensten |
| H2 | Gebruik van professionele capaciteit in Entoli Workspace levert signalen op die de ontwikkeling in Entoli Studio verbeteren, met meetbaar meer waarde dan de twee Producten los | Bepaalt of Studio–Workspace een structureel versterkingsmechanisme is of "slechts" twee SaaS-producten | Architecturale relatie (ontwikkelen → toepassen) staat vast; het terugkoppelmechanisme zelf niet | Vaststellen of en hoe Workspace-inzichten daadwerkelijk tot Studio-verbetering leiden, en dit meten bij echte klanten |
| H3 | Professional Services (consultancy/training) leiden tot blijvend zelfstandig SaaS-gebruik in plaats van doorlopende afhankelijkheid van Entoli's mensen | Bepaalt of Professional Services een tijdelijke krukfunctie of een structurele adoptiemotor is | Training is architecturaal bedoeld om afhankelijkheid te verminderen; geen bewijs dat dit in de praktijk gebeurt | Volgen van klanten na een consultancy-/trainingstraject: gaan zij zelfstandig door met Studio/Workspace? |
| H4 | Organisaties zijn bereid te betalen voor Entoli SaaS (hosting/configuratie/beheer, incl. aantoonbare modelonafhankelijkheid) als aparte implementatie-/ondersteuningsdienst | Bepaalt de commerciële relevantie van de herziening in §6.3 en of dit ooit doorgroeit naar een zelfstandig Product | Genoemd als onderscheidend verhaal richting gereguleerde sectoren; nu ook expliciet als omzetlijn gepositioneerd, maar betalingsbereidheid nog niet getoetst | Gesprekken met potentiële kopers (met name gereguleerde sectoren) over expliciete betalingsbereidheid voor Entoli SaaS |
| H5 | Er is een specifiek eerste klantsegment met voldoende urgentie om als eerste betalend te worden | Bepaalt focus voor go-to-market; de bron laat dit open | Geen — de bron beschrijft rollen generiek, geen geprioriteerd segment | Expliciete keuze en toetsing van een eerste doelsegment |
| H6 | SaaS-omzet (Studio/Workspace) kan op termijn groeien zonder proportionele groei van Professional Services-capaciteit | Bepaalt of het model op termijn schaalbaar wordt of mensafhankelijk blijft | Architecturaal is SaaS schaalbaar, Professional Services mensafhankelijk (Blok 9); geen data over daadwerkelijke verhouding | Volgen van de omzetmix na verloop van tijd |

## Questions to Validate

1. Wie is het eerste klantsegment dat daadwerkelijk zou betalen, en waarom is de behoefte daar urgent genoeg voor een koopbeslissing? *(H5)*
2. Wie beheert het budget voor Entoli Studio/Workspace binnen een klantorganisatie — de Knowledge Authority, de Professional User, of de Organisational Buyer/Governor?
3. Waarom zou een klant voor Entoli kiezen boven het huidige alternatief (bijvoorbeeld: impliciete kennis en losse AI-tools zonder canon)?
4. Wat is de eerste realistische route naar de markt, gegeven dat de bron geen sales-/partnerkanaal beschrijft? *(Blok 4)*
5. Dragen open referentiecanons daadwerkelijk bij aan commerciële adoptie van Studio, Workspace of Professional Services? *(H1)*
6. Leidt gebruik van Entoli Studio daadwerkelijk tot (meer) gebruik van Entoli Workspace, en andersom? *(H2)*
7. Leiden consultancy en training daadwerkelijk tot zelfstandig, blijvend SaaS-gebruik — of blijft de klant afhankelijk van Entoli's mensen? *(H3)*
8. Welk verdienmechanisme (abonnement, gebruik, hybride) sluit voor Entoli Workspace het beste aan bij hoe klanten waarde ervaren?
9. Kan SaaS-omzet groeien zonder dat Professional Services-capaciteit evenredig meegroeit? *(H6)*
10. Is er daadwerkelijk betalingsbereidheid voor modelonafhankelijkheid en beheersing, los van de vraag of dit ooit een apart Product wordt? *(H4)*
11. Welk onderdeel van het model is het moeilijkst voor concurrenten te reproduceren: de open referentiecanons, de semantische methodologie, of de opgebouwde klantrelaties?
12. Welke van bovenstaande aannames moeten zijn gevalideerd vóór een investering in significante schaalvergroting?
