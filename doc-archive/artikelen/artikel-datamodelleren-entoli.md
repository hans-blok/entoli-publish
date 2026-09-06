# Datamodelleren met Entoli

## Van bron naar structuur via betekenis

Datamodelleren wordt in veel organisaties benaderd als een technische activiteit: het ontwerpen van tabellen, attributen en relaties. Binnen Entoli wordt dat radicaal anders gepositioneerd. Datamodelleren is geen technisch startpunt, maar het resultaat van een **keten van betekenisvorming** die begint bij bronnen en eindigt bij implementatie.

Dit artikel beschrijft hoe datamodelleren met Entoli werkt, en hoe het zich onderscheidt door een strikte scheiding tussen betekenis, structuur en implementatie.

---

# 1. Het fundament: betekenis vóór structuur

De kern van Entoli is eenvoudig maar streng:

> **Structuur volgt betekenis.**

Dat betekent dat een logisch datamodel (LDM) nooit direct uit requirements of bronnen wordt afgeleid. Tussen deze lagen zit een cruciale stap: **NIAM-analyse**.

De volledige keten ziet er als volgt uit:

SOURCE
→ SOURCE_SECTION
→ REQUIREMENT
→ NIAM ANALYSIS
→ INFORMATION MODEL
→ LOGICAL DATA MODEL
→ TECHNICAL DATA MODEL

Elke stap heeft een eigen functie en mag niet worden overgeslagen.

---

# 2. Bronnen en requirements: de normatieve basis

Alles begint bij een bron:

* wetgeving
* beleid
* contract
* standaard

Deze bron wordt opgesplitst in **SOURCE_SECTIONs** (bijvoorbeeld artikelen of paragrafen). Vanuit deze secties worden **REQUIREMENTS** afgeleid.

Een requirement is:

* normatief (wat moet gelden)
* herleidbaar naar een bron
* geformuleerd in natuurlijke taal

Belangrijk is dat requirements nog **geen structuur bevatten**. Ze beschrijven alleen wat waar moet zijn.

---

# 3. NIAM: de vertaallaag van taal naar betekenis

De NIAM-analyse is de brug tussen tekst en model.

Hier gebeurt het echte werk:

* ontleden van zinnen
* identificeren van feiten
* expliciteren van impliciete concepten

Bijvoorbeeld:

> “Een vergunning heeft een geldigheidsdatum”

wordt vertaald naar:

* INFORMATION_ELEMENT: Vergunning
* CHARACTERISTIC: geldigheidsdatum

NIAM is geen model, maar een **methode**. Het resultaat is een set van:

* feiten
* kandidaat-concepten
* kandidaat-eigenschappen

---

# 4. Het informatiemodel: het vastleggen van betekenis

Het **Information Model (IM)** is het eerste echte model.

Het bevat:

* **INFORMATION_ELEMENT** (concepten)
* **CHARACTERISTIC** (eigenschappen)
* relaties tussen elementen
* koppelingen naar REQUIREMENTS

Hier wordt betekenis **vastgelegd**, niet ontworpen.

Een belangrijk principe:

> Elk element en elke characteristic moet herleidbaar zijn tot een requirement.

---

# 5. CHARACTERISTIC: de sleutel tussen lagen

Een **Characteristic** is een eigenschap van een concept.

Binnen Entoli heeft dit begrip een dubbele rol:

* generiek: eigenschap van een concept
* in IM: eigenschap van een information element

En:

> Een characteristic kan worden gerealiseerd als een attribute in het LDM.

Dit maakt CHARACTERISTIC de brug tussen:

* betekenis (IM)
* structuur (LDM)

---

# 6. Het logisch datamodel: structuur toevoegen

Het **Logical Data Model (LDM)** is niet simpelweg een vertaling van het informatiemodel.

Het voegt iets toe:

* structuur
* tijd
* proces
* systeemlogica

Hier ontstaat een belangrijke asymmetrie:

> Niet elk attribute komt uit een characteristic.

We onderscheiden:

### 1. Semantische attributen

* afgeleid van characteristics
* representeren betekenis

### 2. Structurele attributen

* toegevoegd in LDM
* voor:

  * tijd (validiteit, historie)
  * proces (statussen)
  * systeem (identifiers)

Dit betekent:

> LDM = IM + structuur

---

# 7. Normalisatie en conventies

Binnen Entoli gelden strikte regels voor het LDM:

* modellen zijn minimaal in **vierde normaalvorm (4NF)**
* referentietabellen:

  * prefix `ref_`
  * kolommen:

    * `<table_name>_id`
    * `code`
    * `description`

Deze regels zorgen voor:

* consistentie
* herbruikbaarheid
* voorspelbaarheid

---

# 8. Grenzen in het LDM: een architectuurvraagstuk

Een van de lastigste vragen is:

> Waar leg je de grenzen van je datamodel?

Binnen Entoli is het antwoord:

> **Niet op basis van data, maar op basis van architectuur.**

Een LDM is geen monolithisch model, maar een **set van modellen**, bijvoorbeeld:

* execution
* coordination

Deze indeling volgt:

* verantwoordelijkheden
* processen
* systeemgrenzen

Niet:

* tabellen
* entiteiten
* of bronstructuur

---

# 9. Requirements en datamodelleren: een iteratieve relatie

De relatie tussen requirements en datamodellen is niet lineair.

Er is een continue wisselwerking:

### Voorwaartse richting

* requirements → NIAM → IM → LDM

### Terugkoppeling

* model onthult:

  * ambiguïteiten
  * ontbrekende regels
  * inconsistenties

→ requirements worden aangescherpt

Belangrijk onderscheid:

* **toegestaan**: verduidelijking
* **niet toegestaan**: structurele details in requirements

---

# 10. De rol van semantic scopes

Om het systeem schaalbaar te houden, werkt Entoli met **semantic scopes**:

* subsets van de ontology
* gericht op een specifieke context (bijv. datamodelleren)

Dit voorkomt:

* overbodige context
* hoge tokenkosten
* verwarring in agents

De ontology blijft generiek; selectie gebeurt via scopes.

---

# 11. Conclusie: datamodelleren als keten van betekenis

Datamodelleren met Entoli is geen geïsoleerde activiteit.

Het is een gecontroleerde keten:

1. bron
2. interpretatie
3. betekenis
4. structuur
5. implementatie

De kracht zit in de scheiding:

* NIAM → methode
* IM → betekenis
* LDM → structuur
* TDM → implementatie

En in het principe:

> **Elke stap heeft een eigen verantwoordelijkheid — en die mag niet vervagen.**

---

# Slot

Wie deze aanpak volgt, krijgt geen “sneller model”, maar een **betrouwbaarder model**:

* volledig herleidbaar
* semantisch correct
* architectonisch consistent

En dat is precies waar datamodelleren in complexe domeinen om draait.
