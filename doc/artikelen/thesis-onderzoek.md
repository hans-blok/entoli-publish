# Kwaliteit, context en kosten: een onderzoeksvoorstel

*Hoeveel context heeft een AI-agent nodig om goed werk te leveren, en wanneer wordt meer context juist een probleem?*

## 1. Inleiding

### Wat is Entoli?

Entoli is een platform dat professionele kennis bruikbaar maakt voor AI. Het vertrekpunt is kennis uit bewezen frameworks en standaarden, zoals TOGAF voor enterprise-architectuur, ArchiMate voor architectuurmodellen en DAMA voor datamanagement. Die kennis ligt meestal verspreid over boeken, standaarden en de hoofden van ervaren professionals. Entoli brengt haar samen in één expliciete, gezaghebbende kennisbasis: de *canon*. Een canon legt vast welke begrippen er zijn, wat ze betekenen, hoe ze samenhangen en welke regels gelden.

Op die kennis bouwt Entoli herbruikbare professionele capaciteit in de vorm van *agents*. Een agent is een AI-gedreven functie met een afgebakende rol, zoals een informatieanalist of een logisch datamodelleur. Elke agent heeft omschreven taken en werkt volgens de regels uit de canon. Een agent krijgt een vraag en de bijbehorende context, voert een taak uit en levert een concreet werkproduct op: een *artefact*, zoals een datamodel, een analyse of een architectuurbeschrijving.

Voor elke taak stelt Entoli een pakket samen met alles wat het taalmodel moet weten: de relevante begrippen, de regels die gelden, eerdere werkproducten en de vraag van de gebruiker. Dat pakket is de *context* van de taak. Dit onderzoek gaat over die context.

### Waarom dit onderzoek?

Het ligt voor de hand om een agent zo veel mogelijk context mee te geven. Meer kennis en meer regels lijken tot beter werk te leiden. Dat is om twee redenen niet vanzelfsprekend.

De eerste reden is kosten. Taalmodellen rekenen in *tokens*: stukjes tekst van ongeveer driekwart woord. Aanbieders rekenen per token af, voor de invoer en voor de uitvoer. Elke extra pagina context kost dus geld, bij elke aanroep opnieuw. Daarnaast kost elke aanroep energie. Google rapporteert voor een doorsnee tekstvraag aan Gemini ongeveer 0,24 Wh (Elsworth e.a., 2025). Per vraag is dat weinig, maar een agent die de hele dag taken uitvoert met tienduizenden tokens context per taak, telt op. Onderzoek van Luccioni e.a. (2024) laat zien dat generatieve taken per aanroep aanzienlijk meer energie vragen dan gerichte taken zoals classificatie. Schwartz e.a. (2020) pleiten er daarom voor om efficiëntie een volwaardig evaluatiecriterium te maken naast nauwkeurigheid.

De tweede reden is kwaliteit. Meer context maakt het werk niet altijd beter, en soms zelfs slechter. Daarover gaat de volgende paragraaf.

## 2. Wat we al weten: meer context is niet altijd beter

Er is de afgelopen jaren veel onderzoek gedaan naar hoe taalmodellen met lange invoer omgaan. Het beeld is consistent: modellen gebruiken hun context niet gelijkmatig.

- **Informatie in het midden raakt uit beeld.** Liu e.a. (2024) lieten zien dat modellen informatie aan het begin en het eind van de context goed gebruiken, maar informatie in het midden duidelijk slechter. Dit staat bekend als het *lost in the middle*-effect.
- **Prestaties dalen lang voordat het contextvenster vol is.** Levy e.a. (2024) gaven modellen steeds dezelfde redeneertaak, aangevuld met irrelevante tekst van toenemende lengte. De prestaties daalden al bij een paar duizend tokens, ver onder het technische maximum. Hsieh e.a. (2024) vonden met de RULER-benchmark dat slechts de helft van de geteste modellen die 32.000 tokens of meer claimen, bij die lengte nog goed presteert. Onderzoekers van Chroma testten achttien recente modellen en kwamen tot dezelfde conclusie; zij noemen het verschijnsel *context rot* (Hong e.a., 2025).
- **Veel regels tegelijk worden slecht nageleefd.** Harada e.a. (2025) gaven modellen opdrachten met één tot tien controleerbare instructies. De kans dat álle instructies worden gevolgd, daalt ruwweg exponentieel met het aantal instructies. Volgt een model één instructie in 90% van de gevallen, dan volgt het tien instructies tegelijk nog maar in ongeveer 35% van de gevallen (0,9¹⁰ ≈ 0,35).

Daar komt een praktisch risico bij. Als de context groter is dan het model aankan, wordt de invoer afgekapt of geweigerd. Afkappen gebeurt vaak aan het eind, terwijl daar juist essentiële instructies kunnen staan, zoals de eigenlijke opdracht of de vorm van het gewenste resultaat. Een agent die zonder foutmelding verder werkt met een onvolledige opdracht, is gevaarlijker dan een agent die weigert.

Voor Entoli betekent dit dat er waarschijnlijk een optimum is. Te weinig context en de agent mist kennis of regels. Te veel context en de agent raakt kennis of regels kwijt, tegen hogere kosten. Het vakgebied spreekt tegenwoordig van *context engineering*: het zoeken naar de kleinste set tokens met de grootste kans op het gewenste resultaat (Anthropic, 2025).

## 3. Onderzoeksvraag

De hoofdvraag van dit onderzoek is:

> **Wat is het verband tussen de omvang en de kwaliteit van de context die een Entoli-agent meekrijgt, en de kwaliteit van het werkproduct dat de agent oplevert?**

Deelvragen zijn:

1. Hoe definiëren en meten we de kwaliteit van een uitgevoerde taak?
2. Wat is *kwaliteit van context*, los van de omvang ervan, en welke eigenschappen van de context doen ertoe?
3. Hoe verandert de taakkwaliteit als de context groeit, en is er een punt waarop meer context niets meer toevoegt of zelfs schaadt?
4. Hoe drukken we efficiëntie uit, zodat we de kwaliteit en de kosten van verschillende contextvarianten eerlijk kunnen vergelijken?

## 4. Een nieuw begrip: Task Quality

Om het verband tussen context en kwaliteit te onderzoeken, moeten we kwaliteit eerst meetbaar maken. We introduceren daarvoor het begrip *Task Quality*: de kwaliteit van het artefact dat een agent bij één taak oplevert.

### Vier dimensies

We onderscheiden vier dimensies. Twee ervan sluiten aan bij de kenmerken *functional correctness* en *functional completeness* uit de internationale kwaliteitsnorm ISO/IEC 25010 (ISO, 2023).

| Symbool | Dimensie | Vraag |
|---|---|---|
| \(C\) | Correctheid (*correctness*) | Is het resultaat inhoudelijk juist? |
| \(R\) | Regelnaleving (*rule compliance*) | Houdt het resultaat zich aan de regels uit de canon en de instructies van de taak? |
| \(S\) | Volledigheid (*completeness*) | Zijn alle vereiste onderdelen van de taak uitgevoerd? |
| \(K\) | Consistentie (*consistency*) | Is het resultaat intern consistent, en consistent met de meegegeven context? |

Elke dimensie krijgt een score tussen 0 en 1. Task Quality \(Q\) is dan een functie van die vier scores:

$$
Q = f(C, R, S, K)
$$

### Hoe combineren we de dimensies?

De eenvoudigste keuze is een gewogen som:

$$
Q = w_C C + w_R R + w_S S + w_K K, \qquad w_C + w_R + w_S + w_K = 1
$$

Die formule is makkelijk uit te leggen, maar heeft een belangrijk nadeel: dimensies compenseren elkaar volledig. Een artefact dat een cruciale regel schendt, kan toch hoog scoren als het verder correct en volledig is. Dat roept een principiële vraag op: **als een taak één heel belangrijke regel niet naleeft, is de kwaliteit dan nul?**

Er zijn drie redelijke antwoorden, en de keuze daartussen is zelf een onderzoeksvraag:


- **Een poort voor harde regels.** Regels krijgen een zwaarte. Wordt een harde regel geschonden, dan is \(Q = 0\); anders geldt een van de formules hierboven. Dit sluit aan bij Entoli zelf: de canon onderscheidt al gebod, verbod en toestemming, en zou daarnaast kunnen vastleggen welke regels een harde grens zijn.

### Hoe meten we elke dimensie?

Een formule is maar zo goed als de metingen die erin gaan. Per dimensie zien we deze mogelijkheden:

- **Regelnaleving (\(R\))** is het best meetbaar. Veel regels zijn controleerbaar te formuleren, zoals "elke entiteit heeft een definitie" of "verzin geen definities die niet in de bron staan". De IFEval-benchmark (Zhou e.a., 2023) laat zien hoe je naleving automatisch kunt toetsen. Het is nuttig om twee cijfers te rapporteren: het aandeel nageleefde regels, en of *alle* regels zijn nageleefd.
- **Volledigheid (\(S\))** is te meten tegen een checklist van verplichte onderdelen. In Entoli volgt die checklist uit het template dat bij het artefacttype hoort.
- **Correctheid (\(C\))** is het lastigst. Opties zijn een referentie-artefact dat een expert heeft gemaakt, beoordeling door experts, of beoordeling door een tweede taalmodel (*LLM-as-a-judge*). Die laatste methode komt vaak goed overeen met menselijke beoordelaars, maar heeft bekende vertekeningen, zoals een voorkeur voor langere antwoorden (Zheng e.a., 2023).
- **Consistentie (\(K\))** is deels automatisch te controleren, bijvoorbeeld of elke verwijzing in een datamodel naar een bestaand element wijst. De consistentie met de context vraagt om een vergelijking tussen het artefact en de meegegeven bronnen.

Een overweging hierbij: meten kost zelf ook tokens. Een beoordeling door een tweede model kan duurder zijn dan de taak zelf. Voor het onderzoek is dat acceptabel; voor gebruik in productie moet de meetmethode zelf ook efficiënt zijn.

## 5. Kwaliteit van context

Naast de omvang van de context kijken we naar de kwaliteit ervan. Twee contexten van even veel tokens kunnen heel verschillend presteren. Eigenschappen die er volgens de literatuur toe doen, zijn:

- **Relevantie:** hoeveel van de context is nodig voor deze taak? Irrelevante tekst verlaagt de prestaties, ook als die tekst verder onschuldig is (Levy e.a., 2024).
- **Positie:** staan de cruciale regels en de opdracht aan het begin of eind, of verstopt in het midden (Liu e.a., 2024)?
- **Aantal regels:** hoeveel instructies moet het model tegelijk naleven (Harada e.a., 2025)?
- **Redundantie en tegenstrijdigheid:** herhaalt de context zichzelf, of bevat hij regels die elkaar tegenspreken?

Entoli heeft hier een voordeel. Omdat de context van een taak expliciet wordt samengesteld uit benoemde begrippen, regels en eerdere werkproducten, is precies vast te stellen wat er in de context zat. Dat maakt het mogelijk om de context systematisch te variëren en het effect te meten.

Bekende manieren om context kleiner en beter te maken zijn:

- **Selecteren:** alleen de relevante kennis ophalen, zoals bij *retrieval-augmented generation* (Lewis e.a., 2020).
- **Ordenen:** cruciale regels en de opdracht op plekken zetten waar het model ze goed gebruikt.
- **Comprimeren:** de tekst inkorten zonder de betekenis te verliezen. LLMLingua comprimeert prompts tot twintig keer met beperkt kwaliteitsverlies (Jiang e.a., 2023).
- **Opsplitsen:** een grote taak verdelen over kleinere taken met elk minder regels.

## 6. Efficiëntie

Het uiteindelijke doel is niet de hoogste kwaliteit, maar de beste verhouding tussen kwaliteit en kosten. We definiëren de efficiëntie van een taak als een functie van de kwaliteit en het aantal invoertokens:

$$
E_{task} = f(Q_{task}, \text{InputTokens})
$$

Een eenvoudige invulling is kwaliteit per duizend tokens. Die maat heeft een zwakte: een bijna lege context met een matig resultaat kan dan efficiënter lijken dan een goede context met een uitstekend resultaat. Twee alternatieven zijn beter bruikbaar:

- **Een drempel:** wat is het kleinste aantal tokens waarmee de kwaliteit boven een vooraf gekozen minimum blijft?
- **Een afwegingscurve:** zet voor elke contextvariant de kwaliteit uit tegen de kosten. Varianten die op beide assen door een andere variant worden verslagen, vallen af. Wat overblijft, is de verzameling redelijke keuzes.

Overwegingen bij deze definitie:

- Ook uitvoertokens kosten geld, en zijn per token vaak duurder dan invoertokens. Een volledige kostenmaat neemt beide mee.
- De keuze van het model beïnvloedt kosten en kwaliteit sterk. FrugalGPT liet zien dat een slimme keuze tussen modellen de kosten tot 98% kan verlagen bij vergelijkbare kwaliteit (Chen e.a., 2023). Dit onderzoek houdt het model constant, maar de resultaten kunnen per model verschillen.
- Euro's en energie zijn verschillende kosten. De prijs per token zegt niet direct iets over het energieverbruik, dus het is zinvol beide te rapporteren.

## 7. Voorgestelde aanpak

Het onderzoek is een reeks gecontroleerde experimenten met Entoli-agents:

1. Kies een klein aantal representatieve taken, bijvoorbeeld het afleiden van een logisch datamodel uit een conceptueel model.
2. Maak per taak een referentie-artefact en een lijst met controleerbare regels en verplichte onderdelen.
3. Varieer de context langs één dimensie tegelijk: omvang, relevantie, positie van cruciale regels en aantal regels. Dit volgt de opzet van Levy e.a. (2024), die dezelfde taak in steeds andere verpakking aanbieden.
4. Voer elke variant meerdere keren uit, omdat taalmodellen niet deterministisch zijn.
5. Meet per uitvoering de vier dimensies van Task Quality, het aantal invoer- en uitvoertokens, en waar mogelijk het energieverbruik.
6. Analyseer het verband tussen context en kwaliteit, en bepaal per taak de efficiënte contextvarianten.

## 8. Overwegingen en beperkingen

- **Modelafhankelijkheid.** Resultaten gelden voor de geteste modellen en versies. Nieuwe modellen gaan beter om met lange context, al blijft de daling bestaan (Hong e.a., 2025).
- **Gewichten zijn keuzes.** Hoe zwaar correctheid telt ten opzichte van regelnaleving, is geen natuurwet maar een afweging. Het onderzoek moet die gewichten expliciet maken en laten zien hoe gevoelig de uitkomsten ervoor zijn.
- **Beoordelaarsbias.** Als een taalmodel de correctheid beoordeelt, moet een deel van de beoordelingen door mensen worden gecontroleerd.
- **Generaliseerbaarheid.** Entoli-taken zijn gestructureerd en regelgebonden. Of de conclusies ook gelden voor vrijere taken, zoals tekstschrijven, is niet vanzelfsprekend.

## Bijlage A. Bronnen

1. **Anthropic (2025).** *Effective context engineering for AI agents.* Anthropic Engineering. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
2. **Chen, L., Zaharia, M. & Zou, J. (2023).** *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance.* arXiv:2305.05176. <https://arxiv.org/abs/2305.05176>
3. **Elsworth, C. e.a. (2025).** *Measuring the environmental impact of delivering AI at Google Scale.* arXiv:2508.15734. <https://arxiv.org/abs/2508.15734>
4. **Harada, K. e.a. (2025).** *Curse of Instructions: Large Language Models Cannot Follow Multiple Instructions at Once.* ICLR 2025 (OpenReview). <https://openreview.net/forum?id=R6q67CDBCH>
5. **Hong, K., Troynikov, A. & Huber, J. (2025).** *Context Rot: How Increasing Input Tokens Impacts LLM Performance.* Chroma Technical Report. <https://www.trychroma.com/research/context-rot>
6. **Hsieh, C.-P. e.a. (2024).** *RULER: What's the Real Context Size of Your Long-Context Language Models?* COLM 2024. <https://arxiv.org/abs/2404.06654>
7. **ISO (2023).** *ISO/IEC 25010:2023 — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model.* <https://www.iso.org/standard/78176.html>
8. **Jiang, H., Wu, Q., Lin, C.-Y., Yang, Y. & Qiu, L. (2023).** *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models.* EMNLP 2023, 13358–13376. <https://aclanthology.org/2023.emnlp-main.825/>
9. **Levy, M., Jacoby, A. & Goldberg, Y. (2024).** *Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models.* ACL 2024, 15339–15353. <https://aclanthology.org/2024.acl-long.818/>
10. **Lewis, P. e.a. (2020).** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS 2020. <https://arxiv.org/abs/2005.11401>
11. **Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P. (2024).** *Lost in the Middle: How Language Models Use Long Contexts.* Transactions of the ACL, 12, 157–173. <https://aclanthology.org/2024.tacl-1.9/>
12. **Luccioni, S., Jernite, Y. & Strubell, E. (2024).** *Power Hungry Processing: Watts Driving the Cost of AI Deployment?* FAccT 2024. <https://doi.org/10.1145/3630106.3658542>
13. **Schwartz, R., Dodge, J., Smith, N. A. & Etzioni, O. (2020).** *Green AI.* Communications of the ACM, 63(12), 54–63. <https://doi.org/10.1145/3381831>
14. **UNDP (2010).** *Human Development Report 2010*, technische toelichting bij de overstap naar het meetkundig gemiddelde in de Human Development Index. <https://hdr.undp.org/content/improving-measurement-human-development>
15. **Zheng, L. e.a. (2023).** *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* NeurIPS 2023 Datasets and Benchmarks. <https://arxiv.org/abs/2306.05685>
16. **Zhou, J. e.a. (2023).** *Instruction-Following Evaluation for Large Language Models.* arXiv:2311.07911. <https://arxiv.org/abs/2311.07911>
