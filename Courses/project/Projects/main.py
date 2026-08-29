from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model for a note
class Note(BaseModel):
    title: str
    content: str

# In-memory storage
notes = []

# CREATE — add a note
@app.post("/notes")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note added", "note": note}

# READ — get all notes
@app.get("/notes")
def get_notes():
    return {"notes": notes}

# READ — get one note by ID
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        return {"error": "Note not found"}
    return {"note": notes[note_id]}

# DELETE — remove a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        return {"error": "Note not found"}
    removed = notes.pop(note_id)
    return {"message": "Note deleted", "note": removed}
