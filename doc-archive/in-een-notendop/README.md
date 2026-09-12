# In een notendop — herkomst

De pagina `doc/in-een-notendop.md` is op 2026-09-12 gemigreerd vanuit een
Claude Artifact:

    https://claude.ai/code/artifact/aa438e42-f91f-44e6-a867-2bdf6e999881

Dat Artifact was een losse indexpagina die naar de vijf ArchiMate-weergaven
op deze site linkte. De site hoeft er niet meer naar te verwijzen; het
Artifact blijft bestaan op bovenstaande URL, maar is geen onderdeel meer van
de navigatie.

## Wat is overgenomen

De redactionele laag — de titels en de zin per weergave — is de eigenlijke
waarde van het origineel en staat vrijwel ongewijzigd in de gepubliceerde
pagina. De presentatie is vervangen door de Entoli-huisstijl.

Originele lede:

> Vijf ArchiMate-weergaven, in de volgorde waarin ze samen het verhaal
> vertellen — van de losse bedrijfsobjecten tot de belofte aan het eind van
> de waardestroom. Elke titel opent de live weergave in Archi.

## De vijf weergaven

De volgorde is ongewijzigd. De ID's verwijzen naar views in
`model/entoli-architecture-model.archimate`.

| # | Titel | View-ID | Naam in het model |
|---|---|---|---|
| 1 | Het semantisch fundament | `id-cbd780d82d40493fa36ca540fd74bf41` | logical-instances-bedrijfsobjecten |
| 2 | Van canon tot toewijzing | `id-d44db71136d542fcb71799bc56ee686a` | logical-instances-processen-en-diensten |
| 3 | Wat Entoli daadwerkelijk levert | `id-809e5a10fbb54d2d84dea2d84d44146a` | bedrijfsprocessen-dienten-en-producten |
| 4 | De grammatica achter alles hierboven | `id-e370b29df1904e7aa3dff365806a402d` | entoli-conceptueel-datamodel |
| 5 | Waarom dit alles bestaat | `id-60706a63f1ca4b3cb3ddb02d1161c408` | waardestroom |

**Let op:** het Artifact noemde bij weergave 4 en 5 nog de oude modelnamen
`entoli-conceptual` en `capabilities`. Die zijn in het model inmiddels
hernoemd; de ID's zijn wél stabiel gebleven. De gepubliceerde pagina toont
daarom geen modelnamen, alleen de redactionele titels.

## Wat is weggelaten

Presentatie-elementen uit het Artifact die geen begrip toevoegen en botsen
met de Entoli-huisstijl:

- de serif-kop en het ruitjespatroon in de achtergrond;
- de eyebrow "Architectuurmodel · entoli-publish";
- de laagaanduidingen ("c. information-systems", "b. business-architecture");
- de afgekorte view-ID's en de modelnamen per kaart;
- de telling "5 vensters" en de voettekst met het domein.
