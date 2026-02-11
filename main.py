from note_manager import Note, save_notes, load_notes

def add_note(notes):
    title = input("Title: ")
    content = input("Content: ")
    tags = input("Tags (comma separated): ").split(",")
    tags = [tag.strip() for tag in tags if tag.strip()]

    notes.append(Note(title, content, tags))
    save_notes(notes)
    print("Note added!\n")

def view_notes(notes):
    if not notes:
        print("No notes found.\n")
        return

    for i, note in enumerate(notes, start=1):
        print(f"Note #{i}")
        note.display()

def search_notes(notes):
    term = input("Search keyword: ")
    results = [n for n in notes if n.matches_search(term)]

    if not results:
        print("No matches.\n")
        return

    for note in results:
        note.display()

def delete_note(notes):
    view_notes(notes)
    if not notes:
        return

    try:
        index = int(input("Delete which note #: ")) - 1
        notes.pop(index)
        save_notes(notes)
        print("Note deleted.\n")
    except:
        print("Invalid choice.\n")

def filter_by_tag(notes):
    tag = input("Enter tag: ").lower()
    filtered = [n for n in notes if tag in [t.lower() for t in n.tags]]

    if not filtered:
        print("No notes with that tag.\n")
        return

    for note in filtered:
        note.display()

def main():
    notes = load_notes()

    while True:
        print("""
1. Add Note
2. View Notes
3. Search Notes
4. Delete Note
5. Filter by Tag
6. Exit
""")
        choice = input("Choose: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            filter_by_tag(notes)
        elif choice == "6":
            save_notes(notes)
            print("Bye!")
            break
        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()
