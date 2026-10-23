
from fastapi.testclient import TestClient

from app.main import app
from app import notes

client = TestClient(app)


def setup_function():
    """Vyčistí úložiště před každým testem."""
    notes.notes.clear()
    notes.next_id = 1


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_note():
    response = client.post("/notes", json={"text": "Testovací poznámka"})

    assert response.status_code == 201
    note = response.json()

    fetched = client.get(f"/notes/{note['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["text"] == "Testovací poznámka"


def test_get_all_notes():
    client.post("/notes", json={"text": "První"})
    client.post("/notes", json={"text": "Druhá"})

    response = client.get("/notes")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_create_note_with_empty_text():
    response = client.post("/notes", json={"text": ""})

    assert response.status_code == 422


def test_get_nonexistent_note():
    response = client.get("/notes/999")

    assert response.status_code == 404


def test_update_note():
    created = client.post("/notes", json={"text": "Původní text"})
    note_id = created.json()["id"]

    response = client.put(
        f"/notes/{note_id}",
        json={"text": "Nový text"},
    )

    assert response.status_code == 200
    assert response.json()["text"] == "Nový text"


def test_update_nonexistent_note():
    response = client.put("/notes/999", json={"text": "Nový text"})

    assert response.status_code == 404


def test_delete_note():
    created = client.post("/notes", json={"text": "Smazat mě"})
    note_id = created.json()["id"]

    response = client.delete(f"/notes/{note_id}")

    assert response.status_code == 200
    assert client.get(f"/notes/{note_id}").status_code == 404


def test_delete_nonexistent_note():
    response = client.delete("/notes/999")

    assert response.status_code == 404


def test_unknown_endpoint():
    response = client.get("/unknown")

    assert response.status_code == 404
