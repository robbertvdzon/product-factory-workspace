# Product Factory Workspace

Deze repository is het leesbare, versieerbare productdossier van de Product Factory. De database
van de runtime bevat alleen operationele toestand. Goedgekeurde research, UX, beslissingen,
roadmaps, storyvoorstellen en evaluaties komen hier terecht.

- `products/hkh` wordt door de eigenaar beheerd.
- `products/hkh-autopilot` wordt na de gezamenlijke baseline door Product Factory beheerd.
- een agent schrijft nooit rechtstreeks naar Git; alleen de workspace-publisher publiceert;
- iedere publicatie heeft metadata, een unieke run-ID en herleidbare bronnen;
- deze repository bouwt of deployt geen applicatie.

Voer lokaal `python3 tools/validate_workspace.py` uit voor dezelfde snelle controle als in CI.
