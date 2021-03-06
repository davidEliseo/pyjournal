from utils import interactiveutils
from pymongo.errors import ConnectionFailure
from persistence.file_collection import FileCollection
from persistence.entry_collection import EntryCollection

try:
    file_collection = FileCollection()
    entry_collection = EntryCollection()
except ConnectionFailure:
    print("We couldn't find a mongod instance.")


def insert():
    print("Enter the name of the new file")
    file_name = interactiveutils.not_empty_input("Name cannot be empty", "file > ")
    new_file = file_collection.insert({'file_name': file_name})
    print("New file:\n{} ({})".format(file_name, new_file['_id']))


def get_files():
    print("\nFiles:\n-------")
    files = file_collection.get_all_files()
    for index, file in enumerate(files):
        qty = get_file_entries_qty(file['_id'])
        if qty > 1:
            print("{}: {} ({} entries)".format(index, file['file_name'], qty))
        else:
            print("{}: {}".format(index, file['file_name'], qty))
    print("")


def get_file_entries_qty(file_id):
    query = {'file_id': file_id}
    return entry_collection.find_with_projection(query, ['_id']).count()


