---
type: essay
name: Twee vragen, geen een — over Source-regime en Synthesis-regime
version: 1.2.0
date: 2026-07-20
status: current
---

# Twee begrippen uit de wereld van AI en LLM's (geen Entoli)

## Synthesis

**Begripstype:** extern (niet-canoniek)

### Definitie 📝

**Synthesis** is het proces waarbij een taalmodel informatie combineert, integreert of samenbrengt tot één samenhangende output, in tegenstelling tot het enkel opzoeken of overnemen ervan. De term wordt in het vakgebied losjes gebruikt — hij benoemt een *functie* die een model vervult, geen gestandaardiseerde API-parameter — maar komt terug in enkele gevestigde betekenissen:

- **Response synthesis** (retrieval-augmented generation): de pipelinestap waarin een of meer opgehaalde passages worden gecombineerd tot één antwoord. Frameworks die RAG-pipelines als discrete stappen blootleggen, benoemen deze stap doorgaans expliciet (bijvoorbeeld als een "response synthesizer"-component), gescheiden van retrieval en reranking.
- **Content synthesis** (generatieve modellering in het algemeen): het produceren van nieuwe output — tekst, beeld, spraak of audio — als tegenhanger van analyse, classificatie of discriminatie. "Speech synthesis" en "image synthesis" dateren van vóór LLM's en benoemen hetzelfde onderliggende idee in andere modaliteiten.
- **Program/data synthesis**: het genereren van code op basis van een specificatie of voorbeelden (program synthesis), of het genereren van kunstmatige trainingsvoorbeelden (data synthesis, "synthetic data").

## Bron

**Begripstype:** extern (niet-canoniek)

### Definitie 📝

Een **bron** (*source*) is, in de context van een taalmodel, materiaal van buiten het model zelf waarop een antwoord is gebaseerd of waaraan een antwoord kan worden getoetst. De term wordt in het vakgebied in twee, wezenlijk verschillende, betekenissen gebruikt:

- **Trainingsbron**: een document, webpagina, boek, code-repository of andere tekst die deel uitmaakte van de trainingsdata waarop het model is voorgetraind of fijngeafstemd. Deze bronnen liggen vast op het moment van training en zijn na afloop niet meer individueel herleidbaar uit het model — een taalmodel bevat geparametriseerde gewichten, geen doorzoekbare index van zijn trainingscorpus.
- **Runtime-bron** (ook wel *retrieved context*, *grounding document* of *citation source*): een document, passage of chunk die op het moment van de aanroep aan het model wordt aangeboden — via de prompt zelf, via retrieval-augmented generation (RAG), of via een tool-/function-call — en waarop het model zijn antwoord dient te baseren.

In dit essay wordt met Bron bedoeld een Runtime-bron.

# Essay over Source-regime, Synthesis-regime en Task Mode

## Probleemstelling: een samengestelde variabele

Elke classificatie die het gedrag van een agent vastlegt, moet op enig moment twee logisch onafhankelijke vragen beantwoorden. De eerste betreft het domein: welke verzameling bronnen is toegankelijk? De tweede betreft de bewerking: welke transformatie mag op dat domein worden toegepast? In een eerdere versie van het Entoli-model waren beide vragen in één classificatie-as ondergebracht. Dat is, in de terminologie van meetmodellen, een samengestelde of geconflateerde variabele: één indicator die twee onderliggende dimensies tegelijk probeert te dragen. Dit essay beschrijft eerst hoe die samenvoeging is opgelost door de as te splitsen in Source-regime en Synthesis-regime. Vervolgens wordt beschreven hoe diezelfde ontvlechting, eenmaal zichtbaar gemaakt, een tweede, onafhankelijke fout blootlegde: een as die toen nog Interpretation Mode heette, en die — naar later bleek — niet beschreef *hoe* een bron gelezen wordt, maar *wat ermee gedaan wordt*. Die as is om die reden hernoemd tot Task Mode.

>Deze vorm van differentiatie is niet uniek voor dit domein. De geschiedenis van meten kent vergelijkbare episodes: massa en gewicht bleven tot in de vroegmoderne mechanica één begrip totdat het onderscheid tussen invariante hoeveelheid materie en plaatsgebonden zwaartekracht dwong tot twee aparte grootheden. Temperatuur en warmte-inhoud ondergingen een vergelijkbare scheiding in de achttiende eeuw, toen bleek dat gelijke temperatuur niet gelijke hoeveelheid warmte impliceert. In beide gevallen was de aanleiding niet esthetisch maar diagnostisch: er deden zich waarnemingen voor die de samengestelde grootheid niet kon representeren zonder tegenspraak. Hetzelfde patroon doet zich hier voor, zij het op de schaal van een classificatiesysteem in plaats van een natuurwet.

---

## Eerste as: Source-regime als domeinvariabele

In de oorspronkelijke, samengevoegde as moest één classificatie tegelijk uitdrukken *waar* een agent mocht kijken — uitsluitend de expliciet aangeleverde input, uitsluitend de canon, canon plus met naam genoemde externe bronnen, of een onbegrensde ruimte — én *wat* de agent met die bronnen mocht doen. De spanning werd het scherpst zichtbaar bij de ruimste positie, Open. Die positie codeerde niet alleen "de bronruimte is niet vooraf afgebakend," maar ook een bepaling als "aannames mogen expliciet worden gemaakt." Dat laatste is geen uitspraak over de omvang van het domein; het is een uitspraak over wat er met betekenis gebeurt nadat een bron is geraadpleegd.

Het identificatieprobleem wordt expliciet zodra men de volgende vraag stelt: kan een agent met een ruim bronbereik niettemin verplicht zijn strikt bij de letter van de bron te blijven? Het antwoord is bevestigend — een agent kan vrij zoeken door een omvangrijk corpus, tot en met het hele internet toe (Source-regime = Open), en toch onder de eis staan niets toe te voegen dat niet letterlijk in het gevondene voorkomt (Task Mode = Extracting). Onder de samengevoegde as was deze combinatie alleen weer te geven door een aparte, hybride positie te definiëren. Het optreden van zulke hybriden is in de praktijk het diagnostische signaal dat een as niet fijnmaziger moet worden gemaakt, maar gesplitst.

Source-regime is vervolgens teruggebracht tot precies één vraag: onder welke bronbeperking opereert dit agent-contract, en welke mate van herleidbaarheid volgt daaruit? Vier posities — Input-bound, Canon-bound, External-source-bound, Open — beantwoorden uitsluitend de domeinvraag. De vraag naar de toegestane bewerking is elders ondergebracht.

## Tweede as: Synthesis-regime als transformatievariabele

De tweede as, Synthesis-regime, stelt een onafhankelijke vraag: welke betekenistransformatie is toegestaan zodra de bronnen zijn geraadpleegd? Drie posities vormen een geordende schaal van toenemende vrijheid. Bij Preserving zijn herformulering en samenvatting toegestaan, maar geen toevoeging: elke bewering blijft herleidbaar tot een reeds aantoonbaar gegeven. Bij Relating blijft de betekenis ongewijzigd, maar is reorganisatie toegestaan — relaties expliciet maken, structuur blootleggen — zonder introductie van nieuwe entiteiten of claims. Bij Generating is nieuwe betekenis toegestaan — hypothesen, aannames, alternatieve framingen — mits gemarkeerd, aangezien deze nieuwe betekenis geen epistemische garantie draagt totdat ze is gevalideerd en gecanoniseerd.

Synthesis-regime is daarmee de as waar het begrip epistemische garantie zijn plaats heeft. Preserving en Relating laten die garantie ongemoeid voor elke bewering die zij aanraken; Generating schort haar expliciet op voor het nieuw geïntroduceerde deel. Dit verklaart waarom de as niet kon blijven bestaan als onderdeel van Source-regime: een garantie over betekenis is een andere grootheid dan een begrenzing van een domein. Een ruim domein en een strenge garantie zijn onafhankelijk combineerbaar, en precies die combinatie kon de samengevoegde as niet zonder verlies van precisie weergeven — het equivalent van multicollineariteit tussen twee regressoren die vervolgens niet meer afzonderlijk te schatten zijn.

## Derde as: dezelfde ontvlechting, gevonden via een naamfout in Task Mode

De ontvlechting van Source-regime en Synthesis-regime bleef niet zonder gevolg voor de rest van het model. Zij leverde een onderscheidingscriterium op — domein versus bewerking — dat vervolgens kon worden toegepast op een as die op dat moment nog Interpretation Mode heette en zeven posities telde: Exploratory, Explanatory, Structural, Normative, Realising, Evaluative, Validating. Onder dat criterium bleek de naam zelf onjuist. "Interpretation" suggereert een vraag over lezen of duiden van de bron; de as beschreef in werkelijkheid iets anders, namelijk welk gedrag op de bron wordt losgelaten. Dat is niet een kwestie van interpreteren maar van handelen — precies het type vraag dat inmiddels, dankzij Synthesis-regime, als aparte categorie herkenbaar was geworden. De as is om die reden hernoemd tot Task Mode. Bij nadere analyse bleek de as bovendien, net als de oorspronkelijke Source/Synthesis-as, twee vragen tegelijk te dragen.

In de eerste correctiestap is de taal over betekenistransformatie verwijderd — dezelfde taal die hierboven al is aangetroffen in de oude Open-positie van Source-regime. Wat resteerde, betrof niet uitsluitend de vorm van de taak; er bleek een tijdsdimensie in verborgen te zitten. Exploratory beschreef niet het resultaat van één stap, maar een werkwijze over meerdere stappen heen: meerdere sporen parallel volgen zonder vooraf te weten welk spoor productief blijkt. Dat is geen eigenschap van een enkele, deterministische stap, maar van de ordening van stappen door de agent. Deze dimensie is daarom afgesplitst tot een eigen as, Execution Strategy, met de posities Linear, Exploratory en Convergent Execution — niet langer het label van een stap, maar een kenmerk van de sequentiële organisatie ervan.

Na deze twee correcties kon de resterende as worden teruggebracht tot één vraag: welk type operatie voert deze stap uit, en welke outputstructuur volgt daaruit? Onder die vraag zijn de resterende zeven posities samengevoegd tot vijf:

| Oude positie(s) | Nieuwe positie | Reden van samenvoeging |
|---|---|---|
| Explanatory, Normative, Realising | **Transforming** | alle drie leveren output die strikt is afgeleid van de bron |
| Evaluative, Validating | **Evaluating** | beide beoordelen tegen criteria |
| Structural | **Structuring** | hernoeming, uitsluitend voor morfologische consistentie |
| Extracting | **Extracting** | ongewijzigd — isoleert uitsluitend wat al in het geraadpleegde materiaal aanwezig is, ongeacht hoe breed het doorzochte domein is (Source-regime = Open kan dus samengaan met Task Mode = Extracting, bijvoorbeeld: vrij zoeken over het hele internet, maar niets toevoegen dat niet letterlijk gevonden is) |
| Generating | **Originating** | ongewijzigd — produceert inhoud die niet in de bron voorkomt; hernoemd ten opzichte van Synthesis-regime, ter vermijding van naamgevingsambiguïteit met de gelijknamige Synthesis-regime-positie — zie hieronder |

Extracting en Originating vormen samen de twee uiterste posities van de schaal.

De onderliggende regel is in alle drie de gevallen dezelfde: een classificatie-as beantwoordt precies één vraag; zodra een tweede vraag insluipt — een tijdsdimensie, een betekenisvrijheid, een handhavingsmoment — vereist die vraag een eigen as, niet een extra positie op de bestaande. Source-regime, Synthesis-regime en Task Mode zijn drie opeenvolgende toepassingen van hetzelfde ontvlechtingsprincipe op drie verschillende conflaties: de eerste toepassing legde het criterium vast, de tweede en derde as werden er vervolgens mee getoetst en gecorrigeerd.

Deze opeenvolgende ontstaansgeschiedenis verklaarde ook een naamgevingscollisie. Toen de meest vrije positie van Synthesis-regime werd hernoemd van Generative naar Generating — een zuiver morfologische correctie, ter aansluiting bij de gerundiumvorm van de overige posities — bleek Task Mode, via een onafhankelijke correctie, reeds een positie met exact dezelfde naam te bevatten. Twee assen, elk afzonderlijk teruggebracht tot één scherpe vraag, deelden sindsdien het label van hun meest open positie. Deze collisie is inmiddels opgeheven door de Task Mode-positie te hernoemen tot Originating (zie de tabel hierboven en de motivering hieronder).

Anders dan bij Source-regime en Synthesis-regime is de relatie tussen deze twee posities echter geen zuivere onafhankelijkheid. Task Mode = Originating is een *beschrijvende* classificatie: zij typeert, achteraf, wat een stap feitelijk heeft opgeleverd — output die niet in de bron voorkwam. Synthesis-regime = Generating is een *normatieve* classificatie: zij bepaalt, vooraf, wat een contract mag opleveren. Tussen beide bestaat een eenzijdige logische afhankelijkheid, geen correlatie: een stap kan alleen als Task Mode = Originating geclassificeerd worden wanneer het onderliggende contract Synthesis-regime = Generating toestaat, want Preserving en Relating sluiten per definitie uit dat er niet-herleidbare betekenis ontstaat. Het omgekeerde geldt niet — een contract met Synthesis-regime = Generating laat toe dat een individuele stap toch niet meer dan Extracting doet. Task Mode = Originating impliceert dus Synthesis-regime = Generating, maar niet andersom. Dat is een striktere relatie dan de eerdere formulering ("een sterke empirische correlatie, geen definitorische identiteit") suggereerde, en zij is precies de reden waarom het voorheen gedeelde label niet onschuldig was: twee assen die voor alle overige waarden vrij composeerbaar zijn, kennen op dit ene punt een noodzakelijk verband, dat door een toevallig identiek label werd gemaskeerd.

### Resolutie: de twee posities lopen uiteen in naam

Om deze ambiguïteit weg te nemen, lag het voor de hand niet de Synthesis-regime-positie te hernoemen, maar de Task Mode-positie. Preserving–Relating–Generating vormt op de Synthesis-regime-as een inhoudelijk samenhangende, oplopende schaal van epistemische vrijheid; Generating is daar de natuurlijke afsluiting van die schaal. Op de Task Mode-as was Generating daarentegen één van vijf posities die toch al recent waren samengevoegd of hernoemd (zie de tabel hierboven) — een hernoeming past in diezelfde consolidatieslag.

Besluit: de Task Mode-positie Generating is hernoemd tot **Originating**. Deze naam:

- blijft in de gerundiumvorm, consistent met Extracting, Structuring, Transforming, Evaluating;
- vormt een natuurlijk contrasterend paar met Extracting — isoleren van wat er al is, tegenover laten ontstaan van wat er nog niet was;
- draagt geen normatieve lading (in tegenstelling tot Generating, dat op de Synthesis-regime-as juist een vrijheid *toekent*): Originating beschrijft alleen wat de stap heeft gedaan, niet wat zij mocht doen.

Overwogen, maar niet gekozen: **Authoring** (legt nadruk op het creatieve karakter van de output, maar kan associaties oproepen met documentauteurschap) en **Composing** (sluit aan bij "samenstellen", maar ligt inhoudelijk te dicht bij Structuring/Relating, wat een nieuwe verwarring zou introduceren). Originating had van de drie de kleinste overlap met bestaande termen op beide assen.

Met deze hernoeming vervalt het gedeelde label; de eenzijdige afhankelijkheid (Task Mode = Originating ⟹ Synthesis-regime = Generating) blijft bestaan — dat is een inhoudelijke eigenschap van het model, geen naamgevingsfout — maar wordt niet langer gemaskeerd door een toevallige gelijkenis in naam.

## Conclusie: winst in identificeerbaarheid, niet in expressief bereik

De ontvlechting voegt geen combinatie van bron en gedrag toe die voorheen onbereikbaar was; het bereik van het systeem is ongewijzigd. De winst zit in identificeerbaarheid. Doordat elke as precies één vraag beantwoordt, is aan drie voorwaarden tegelijk voldaan: elke waarde van Source-regime kan met elke waarde van Synthesis-regime worden gecombineerd zonder verlies van precisie in de classificatie; de twee vormen van handhaving — vóór de aanroep tegen het domein, tijdens de redenering tegen de transformatie — interfereren niet met elkaar; en een afwijking in de output is altijd aan precies één as toe te schrijven, niet aan een niet nader te ontleden mengsel van beide.

Dit is in essentie een identificatievraagstuk: zolang twee dimensies in één indicator zijn samengevoegd, is geen van beide afzonderlijk schatbaar of toetsbaar, en is een afwijking in de uitkomst niet ondubbelzinnig aan een oorzaak toe te wijzen. Orthogonalisering van de assen lost dat op. De resterende naamgevingscollisie tussen de twee "Generating"-posities bleek bij nadere analyse geen toevallige gelijkenis, maar het zichtbare symptoom van een eenzijdige logische afhankelijkheid tussen Task Mode en Synthesis-regime. De hernoeming van de Task Mode-positie tot Originating maskeert die afhankelijkheid niet langer achter een gedeeld label, zonder de afhankelijkheid zelf — die inhoudelijk terecht is — weg te nemen.
