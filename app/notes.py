from app.models import Note, NoteUpdate

notes: dict[str,Note] = {}
next_id = 1

def get_all_notes() -> list[Note]:
    return list(notes.values())

def get_note_by_id(note_id: str) -> Note | None:
    return notes.get(note_id)

def create_note( text: str) -> Note:
    global next_id
    note = Note(id=str(next_id), text=text)
    notes[note.id] = note
    next_id += 1
    return note

def update_note(note_id: str, updated_note: NoteUpdate) -> Note | None:
    existing_note = notes.get(note_id)

    if existing_note is None:
        return None

    existing_note.text = updated_note.text
    return existing_note

def delete_note(note_id: str) -> bool:
    if note_id in notes:
        del notes[note_id]
        return True
    return False

