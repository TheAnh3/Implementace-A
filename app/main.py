from fastapi import FastAPI, HTTPException
from app.models import Note, NoteUpdate, NoteCreate, NoteResponse
from app import notes

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/notes", response_model=list[NoteResponse])
def get_notes():
    return notes.get_all_notes()


@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: str):
    note = notes.get_note_by_id(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Poznámka s tímto ID nebyla nalezena.")
    return note

@app.post("/notes", response_model=NoteResponse, status_code=201)
def create_note(note_create: NoteCreate):
    note = notes.create_note(note_create.text)
    return NoteResponse(id=note.id, text=note.text)

@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, note_update: NoteUpdate):
    updated_note = notes.update_note(note_id, note_update)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Poznámka s tímto ID nebyla nalezena.")
    return NoteResponse(id=updated_note.id, text=updated_note.text)

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    success = notes.delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Poznámka s tímto ID nebyla nalezena.")
    return {"message": "Poznámka byla úspěšně smazána."}