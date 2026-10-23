# Implementace A

Jednoduchá aplikace pro správu poznámek vytvořená v rámci experimentu zaměřeného na porovnání různých přístupů k vývoji softwaru.

## Funkce

Aplikace poskytuje HTTP API pro:
- kontrolu dostupnosti aplikace,
- zobrazení všech poznámek a konkrétní poznámky,
- vytváření nových poznámek,
- úpravu a odstraňování existujících poznámek.

Vstupní data jsou validována a API vrací odpovídající HTTP stavové kódy při úspěšných operacích i chybových situacích.

## Technologie

- Python
- FastAPI
- Pydantic
- pytest

## Spuštění

Nainstalujte závislosti:

    pip install -r requirements.txt

Spusťte aplikaci z kořenové složky projektu:

    uvicorn app.main:app --reload

Interaktivní dokumentace API je dostupná na `http://127.0.0.1:8000/docs`.

## Testování

Automatizované testy lze spustit příkazem:

    pytest -v

Data poznámek jsou uchovávána pouze v paměti aplikace. Po restartování aplikace se uložené poznámky odstraní.

Projekt slouží k experimentálnímu porovnání implementací a není určen jako produkční systém.