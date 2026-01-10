# Requirements

Repository centralizzato per la gestione delle dipendenze Python comuni utilizzate nei progetti dell'organizzazione DLRSP.

## 📋 Descrizione

Questo repository contiene file di requirements Python compilati per diverse versioni di Python, utilizzati come dipendenze comuni in tutti i progetti dell'organizzazione.

## 📦 File Disponibili

### Requirements per sviluppo
- `py38-dev.txt` - Python 3.8
- `py39-dev.txt` - Python 3.9
- `py310-dev.txt` - Python 3.10
- `py311-dev.txt` - Python 3.11

### Requirements per documentazione
- `py-docs.txt` - Dipendenze per la generazione della documentazione (MkDocs)

### File sorgente
- `dev.in` - File sorgente per i requirements di sviluppo
- `docs.in` - File sorgente per i requirements di documentazione

## 🚀 Utilizzo

### Installazione tramite URL GitHub

Per utilizzare questi requirements in un progetto, puoi installarli direttamente da GitHub:

```bash
# For Python 3.10
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt

# For Python 3.11
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py311-dev.txt

# For documentation
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py-docs.txt
```

### Utilizzo in GitHub Actions

Esempio di utilizzo in un workflow GitHub Actions:

```yaml
- name: Install dependencies
  run: |
    pip install -r https://raw.githubusercontent.com/DLRSP/requirements/main/py310-dev.txt
```

### Utilizzo con tag/versioni

Per utilizzare una versione specifica, puoi fare riferimento a un tag:

```bash
pip install -r https://raw.githubusercontent.com/DLRSP/requirements/v1.0.0/py310-dev.txt
```

## 🔄 Aggiornamento dei Requirements

I file `.txt` sono generati automaticamente dai file `.in` usando `pip-compile`:

```bash
# For Python 3.10
pip-compile --allow-unsafe --generate-hashes --output-file=py310-dev.txt dev.in

# For Python 3.11
pip-compile --allow-unsafe --generate-hashes --output-file=py311-dev.txt dev.in

# For documentation
pip-compile --allow-unsafe --generate-hashes --output-file=py-docs.txt docs.in
```

## 📝 Dipendenze Incluse

### Requirements di sviluppo (`dev.in`)
- `pip`, `setuptools`, `wheel` - Strumenti base
- `tox`, `tox-py` - Testing e automazione
- `coverage` - Code coverage
- `pytest`, `pytest-django`, `pytest-randomly` - Framework di testing

### Requirements di documentazione (`docs.in`)
- `mkdocs`, `mkdocs-material` - Generazione documentazione
- `mkdocs-git-revision-date-plugin` - Plugin per date di revisione

## 🔧 Workflow Automatici

Questo repository utilizza workflow centralizzati da `DLRSP/workflows`:
- **CI/CD**: Esegue test automatici su push e PR
- **Upgrade Dependencies**: Aggiorna automaticamente le dipendenze comuni
- **PR Rebase**: Esegue rebase automatico delle PR quando viene fatto push su main

## 📚 Note

- I file requirements sono generati con `--generate-hashes` per garantire sicurezza e riproducibilità
- I pacchetti `pip`, `setuptools` e `wheel` sono marcati come `--allow-unsafe` in quanto necessari per l'installazione
- Questo repository non è un package Python installabile, ma un repository di file requirements

## 🤝 Contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida su come contribuire.

## 📄 Licenza

MIT License - Vedi [LICENSE](LICENSE) per i dettagli.
