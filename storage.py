import json
from note_manager.note import Note

FILE_NAME = "notes.json"

def save_notes(notes_list):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([note.save() for note in notes_list], file, indent=2)

def load_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [
                Note(
                    title=item["title"],
                    content=item["content"],
                    tags=item["tags"],
                    timestamp=item["timestamp"]
                )
                for item in data
            ]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
