
import pytest

from app import notes
from app.models import NoteUpdate


@pytest.fixture(autouse=True)
def reset_notes():
    notes.notes.clear()
    notes.next_id = 1


def test_create_note():
    note = notes.create_note("Testovací text")

    assert note.id == "1"
    assert note.text == "Testovací text"
    assert notes.get_note_by_id("1") == note


def test_get_all_notes():
    notes.create_note("První poznámka")
    notes.create_note("Druhá poznámka")

    result = notes.get_all_notes()

    assert len(result) == 2


def test_get_missing_note():
    assert notes.get_note_by_id("999") is None


def test_update_note():
    note = notes.create_note("Původní text")

    updated = notes.update_note(
        note.id,
        NoteUpdate(text="Nový text"),
    )

    assert updated is not None
    assert updated.text == "Nový text"


def test_update_missing_note():
    result = notes.update_note(
        "999",
        NoteUpdate(text="Nový text"),
    )

    assert result is None


def test_delete_note():
    note = notes.create_note("Smazat mě")

    result = notes.delete_note(note.id)

    assert result is True
    assert notes.get_note_by_id(note.id) is None


def test_delete_missing_note():
    assert notes.delete_note("999") is False
