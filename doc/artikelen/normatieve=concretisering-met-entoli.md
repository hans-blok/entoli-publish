# Van principe naar uitvoering: normatieve concretisering in Entoli

Een architectuurprincipe kan richting geven zonder precies te vertellen wat iemand morgen moet doen. Een canonieke regel kan inhoudelijk juist zijn zonder een goede instructie voor een Large Language Model te zijn.

Dat verschil wordt belangrijk zodra we AI niet alleen kennis willen meegeven, maar betrouwbaar werk willen laten uitvoeren.

Binnen Entoli gebruiken we daarom twee samenhangende ideeën: **normatieve concretisering** en **progressive concretization**. Samen beschrijven ze hoe algemene kennis, principes en regels stapsgewijs worden vertaald naar concrete instructies voor AI-gedreven functies.

## Het probleem met algemene regels

Veel professionele kennis begint op een hoog abstractieniveau.

Frameworks en standaarden zoals TOGAF, ArchiMate en DAMA bevatten concepten, principes, definities en regels. Ze vertellen ons bijvoorbeeld hoe we naar architectuur, informatie of datamodellering moeten kijken.

Dat is waardevol als ontwerpkennis.

Maar een regel die goed werkt in een canon of architectuur is niet automatisch een goede instructie voor een LLM.

Neem een abstract principe als:

> Data governance en data management zijn verschillende verantwoordelijkheden.

Dat onderscheid is belangrijk. Maar het vertelt een LLM dat op dit moment een Logical Data Model moet maken nog niet precies wat het moet doen.

Een concrete regel zoals:

> Als een definitie in het bronmodel ontbreekt, rapporteer dit en verzin geen definitie.

doet dat wel.

Het verschil zit niet noodzakelijk in de kwaliteit van beide regels. Ze hebben een ander doel en bevinden zich op een ander abstractieniveau.

Daarom moeten we voorkomen dat we algemene principes rechtstreeks als uitvoeringsinstructies behandelen.

## Normatieve concretisering

Met **normatieve concretisering** bedoelen we het vertalen van een algemene norm naar een concretere norm voor een specifieke verantwoordelijkheid of handeling.

Het uitgangspunt blijft behouden, maar de interpretatieruimte wordt kleiner.

Bijvoorbeeld:

**Algemeen principe**

> Een model introduceert geen betekenis die niet uit de bron kan worden verantwoord.

Dat kan voor een bepaalde professionele functie worden geconcretiseerd naar:

**Agent Rule**

> Een Logical Data Modeller voegt geen businessconcepten toe die niet traceerbaar zijn naar het bronmodel.

Voor een specifieke intent kan dat nog verder worden geconcretiseerd:

**Agent Intent Rule**

> Bij het afleiden van een Logical Data Model moet iedere Entity traceerbaar zijn naar een concept uit het bronmodel of naar een expliciete transformatieregel.

De betekenis verandert niet willekeurig. De regel wordt **specifieker ten opzichte van de verantwoordelijkheid die moet worden uitgevoerd**.

Dat is normatieve concretisering.

## Progressive concretization

Normatieve concretisering is onderdeel van een breder ontwerpprincipe: **progressive concretization**.

Progressive concretization betekent dat we niet proberen om in één stap van abstracte kennis naar een perfecte prompt te springen.

Iedere ontwerpstap heeft zijn eigen verantwoordelijkheid en reduceert een deel van de interpretatieruimte.

Conceptueel ontstaat:

**kennis → principes → functie → intent → instructie → uitvoering**

Of concreter:

**Framework → Canon → Agent Rule → Agent Intent Rule → Instruction Set → Execution**

Aan het begin van de keten willen we duurzame betekenis vastleggen.

Aan het einde willen we ondubbelzinnig uitvoerbaar gedrag.

Hoe dichter we bij Execution komen, hoe minder ontwerpbeslissingen we nog aan het uitvoerende LLM willen overlaten.

Dat is een belangrijk verschil met een aanpak waarbij tijdens iedere execution een grote hoeveelheid algemene documentatie, principes en regels aan het model wordt aangeboden met de impliciete opdracht:

> Bepaal zelf wat hiervan voor deze taak relevant is en hoe je dit moet toepassen.

Dat lijkt flexibel, maar verplaatst architectuurwerk naar runtime.

Progressive concretization probeert juist zoveel mogelijk van die interpretatie tijdens **design time** expliciet te maken.

## De ontwerpgrondslag

Daarmee ontstaat een belangrijk begrip binnen Entoli: de **ontwerpgrondslag**.

Een ontwerpgrondslag is de autoritatieve semantische en normatieve basis waartegen een professionele functie wordt ontworpen.

Die grondslag hoeft niet in iedere Ecosystem Context hetzelfde te zijn.

Binnen Entoli zelf is de **Canon** de ontwerpgrondslag.

Binnen een Tenant Workspace is de **Architecture** de ontwerpgrondslag.

| Ecosystem Context | Ontwerpgrondslag | Concretisering    | Uitvoerbaar resultaat            |
| ----------------- | ---------------- | ----------------- | -------------------------------- |
| Entoli            | Canon            | Agent Development | Agent Rules + Agent Intent Rules |
| Tenant            | Architecture     | Agent Development | Agent Rules + Agent Intent Rules |

Dat onderscheid is essentieel.

Entoli en een tenant hoeven niet dezelfde inhoudelijke ontwerpgrondslag te hebben om hetzelfde ontwikkelprincipe toe te passen.

## De Canon als ontwerpgrondslag voor Entoli

Entoli ontwikkelt zijn eigen professionele functies vanuit zijn Canon.

Die Canon ontstaat op zijn beurt niet uit het niets. Frameworks, standaarden, vakkennis en expliciete ontwerpbeslissingen worden geïnterpreteerd en gecanoniseerd.

Bijvoorbeeld:

**TOGAF / ArchiMate / DAMA → Entoli Canon → Agent Development → Agent Rules → Agent Intent Rules**

De Canon legt vast wat binnen Entoli als betekenisvol, normatief en duurzaam wordt beschouwd.

Dat betekent niet dat iedere Canon Rule letterlijk in iedere Instruction Set terecht moet komen.

Integendeel.

Een Canon Rule mag relatief fundamenteel zijn. Tijdens Agent Development wordt vervolgens bepaald wat die regel betekent voor een specifieke professionele functie.

De Canon hoeft dus niet zelf de uitvoeringsinstructie te zijn.

De Canon is de **ontwerpgrondslag waaruit uitvoeringsinstructies verantwoord kunnen worden afgeleid**.

## Architectuur als ontwerpgrondslag voor een tenant

Hetzelfde patroon kunnen we toepassen binnen een Tenant Workspace.

Daar is niet de Entoli Canon de primaire inhoudelijke beschrijving van de organisatie. De tenant heeft een eigen werkelijkheid, eigen principes en een eigen architectuur.

De **Business Architecture** beschrijft bijvoorbeeld relevante businessconcepten, capabilities, processen en samenhangen. Waar relevant kan ook de **Application Architecture** onderdeel van die ontwerpgrondslag zijn.

Een Conceptual Data Model kan belangrijke concepten en relaties uit die architectuur expliciet en machineleesbaar maken. Architectuurprincipes leggen daarnaast normatieve uitspraken over die werkelijkheid vast.

Samen vormen die de ontwerpgrondslag voor het ontwikkelen van functies binnen de tenant.

De keten wordt dan bijvoorbeeld:

**Tenant Architecture → Agent Development → Agent Rules → Agent Intent Rules**

Een relatief algemeen architectuurprincipe kan daardoor worden vertaald naar concreet gedrag voor een specifieke functie.

De architectuur hoeft niet tijdens iedere execution opnieuw volledig geïnterpreteerd te worden.

Die interpretatie vindt al plaats tijdens Agent Development.

## Twee verschillende grondslagen, hetzelfde patroon

Daarmee ontstaat een interessante symmetrie.

Voor Entoli:

**Canon → concretisering → uitvoerbare functie**

Voor een tenant:

**Architecture → concretisering → uitvoerbare functie**

De Canon en de Architecture zijn niet hetzelfde soort inhoud. We moeten die begrippen daarom niet samenvoegen.

Ze vervullen echter wel een vergelijkbare **architectonische rol**.

Beide zijn een ontwerpgrondslag.

Dat levert een generieker patroon op:

**Ecosystem Context → Ontwerpgrondslag → Agent Development → Agent Rules → Agent Intent Rules → Execution**

De Ecosystem Context bepaalt daarmee mede vanuit welke autoritatieve grondslag functies worden ontwikkeld.

## Van vaag naar specifiek is geen verlies van architectuur

Een mogelijke zorg bij concretisering is dat de oorspronkelijke principes verdwijnen.

Dat zou inderdaad problematisch zijn.

Normatieve concretisering betekent daarom niet dat een Agent Rule simpelweg een nieuwe, losstaande regel is.

De afleiding moet traceerbaar blijven.

Bijvoorbeeld:

**Architecture Principle**
↓ concretiseert naar
**Agent Rule**
↓ concretiseert naar
**Agent Intent Rule**

Of binnen Entoli:

**Framework / Specification**
↓ geïnterpreteerd in
**Canon Rule**
↓ concretiseert naar
**Agent Rule**
↓ concretiseert naar
**Agent Intent Rule**

Daardoor kunnen we bij een concrete uitvoeringsregel uiteindelijk terugredeneren:

> Waarom moet deze functie zich eigenlijk zo gedragen?

Dat antwoord moet niet zijn:

> Omdat het zo in de prompt staat.

Het antwoord moet terug te voeren zijn op de ontwerpgrondslag.

## Concretisering is geen kopiëren

Dat betekent ook dat we algemene regels niet simpelweg naar beneden kopiëren.

Als dezelfde Canon Rule letterlijk terugkomt als Agent Rule en vervolgens opnieuw als Agent Intent Rule, hebben we weinig geconcretiseerd.

Iedere stap moet iets toevoegen: **context en specificiteit**.

Een Canon Rule zegt wat normatief geldt.

Een Agent Rule zegt wat dat betekent voor de verantwoordelijkheid van een professionele functie.

Een Agent Intent Rule zegt wat dat betekent bij een specifieke handeling van die functie.

Het doel is dus niet meer regels produceren.

Het doel is de interpretatieruimte gecontroleerd verkleinen.

## Design time versus runtime

Hieruit volgt een belangrijke architecturale keuze voor Entoli.

We willen zoveel mogelijk semantische en normatieve interpretatie uitvoeren tijdens **design time**.

Tijdens **runtime** willen we vooral selecteren, assembleren en uitvoeren.

Dat geeft grofweg twee werelden.

**Agent Development** interpreteert en concretiseert:

**Ontwerpgrondslag → verantwoordelijkheid → intent → concrete regels**

**Agent Execution** selecteert en assembleert:

**Agent + Intent + Rules + relevante context + input → Instruction Set → Execution**

Hierdoor hoeft Instruction Assembly niet telkens opnieuw te bedenken wat een abstract architectuurprincipe betekent.

Dat werk is eerder gedaan.

Instruction Assembly kan daardoor eenvoudiger worden.

En eenvoud op dat punt is waardevol: het verkleint de hoeveelheid interpretatie die we tijdens iedere afzonderlijke LLM-execution opnieuw moeten vertrouwen.

## De interessante recursie van Entoli

Daarmee ontstaat uiteindelijk een interessante structuur.

Entoli gebruikt externe frameworks en professionele kennis om zijn Canon op te bouwen.

Vervolgens gebruikt Entoli die Canon als ontwerpgrondslag om functies te ontwikkelen.

Een aantal van die functies helpt een organisatie om haar eigen architectuur expliciet te maken.

Die tenantarchitectuur wordt vervolgens de ontwerpgrondslag voor het ontwikkelen van functies binnen die Tenant Workspace.

Dus:

**Frameworks → Entoli Canon → Entoli-functies → Tenant Architecture → Tenant-functies**

Hetzelfde ontwerpprincipe herhaalt zich op een ander niveau.

Niet omdat Canon en Architecture hetzelfde zijn, maar omdat beide de rol van **ontwerpgrondslag** vervullen binnen hun eigen Ecosystem Context.

## Van betekenis naar betrouwbaar gedrag

De kern van progressive concretization is uiteindelijk eenvoudig:

> **Hoe dichter we bij uitvoering komen, hoe minder fundamentele interpretatie we aan het uitvoerende model overlaten.**

Aan het begin van de keten willen we rijke concepten, principes en samenhang.

Aan het einde willen we concrete verantwoordelijkheid, expliciete grenzen en toepasbare regels.

Normatieve concretisering vormt de brug tussen die twee.

Daarmee wordt een Canon of Architecture meer dan documentatie. Het wordt een grondslag waaruit gedrag systematisch kan worden ontworpen.

En Agent Development wordt meer dan het schrijven van prompts.

Het wordt het proces waarin we algemene betekenis en normen stap voor stap transformeren tot **traceerbaar, contextgebonden en uitvoerbaar AI-gedrag**.
