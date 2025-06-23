import json

DB_File = "tag.json"

def load_db():
    try:
        with open(DB_File,'r') as f:
            return json.load(f)
    except(json.JSONDecodeError, FileNotFoundError):
        return {}

def save_db(data):
    with open(DB_File, 'w') as f:
        json.dump(data,f)

def ingest_file(tag, file_path):
    db = load_db()
    if tag in db:
        if file_path not in db[tag]:
            db[tag].append(file_path)
            print(f"Ingested: {file_path}")
        else:
            print("File already exist")
    else:
        db[tag] = []
        db[tag].append(file_path)
        print(f"Ingested: {file_path}")
    save_db(db)

def assign_tag(tag):
    db = load_db()
    if tag not in db:
        db[tag] = []
        print(f"Ingested: {tag}")
    else:
        print("Tag already exist")
    save_db(db)

def remove_tag(tag):
    db = load_db()
    if tag in db:
        db.pop(tag)
        print(f"Removed tag: {tag}")
    else:
        print("Tag does not exist")
    save_db(db)

def search(tag):
    db = load_db()
    if tag in db:
        return db[tag]
    else:
        return "does not exist"

def print_dic():
    db = load_db()
    if not db:
        print("Dictionary is empty\n")
    else:
        for k,v in db.items():
            print(f"{k} = {v}")

j = 1
while(j != 0):
    i = int(input("Enter\n1. for ingest_file\n2. for assign tag\n3. remove tag\n4. search\n5. Print all tags and their files\n"))
    if i == 1:
        file_path = input("Enter file path: ")
        tag = input("Enter tag for file: ")
        ingest_file(tag, file_path)
    elif i == 2:
        tag = input("Enter tag: ")
        assign_tag(tag)
    elif i == 3:
        tag = input("Enter tag: ")
        remove_tag(tag)
    elif i == 4:
        tag = input("Enter tag: ")
        l = search(tag)
        print(f"file path related to tag : {l} ")
    elif i == 5:
        print_dic()
    else:
        print("You entered a wrong choice")
    j = int(input("press 0 to exit and any num to continue: "))
