from interactive import entry_interactive_crud
from interactive import file_interactive_crud
from ql import parser


def exec_query(query):
    try:
        query = parser.get_query_template(query)
    except parser.ParseValidationError as err:
        print(err)
        return

    try:
        command = query.pop('verb')
        if command == 'get':
            entry_interactive_crud.read(query)
        elif command == 'delete':
            entry_interactive_crud.delete(query)
        elif command == 'write':
            entry_interactive_crud.insert_or_update()
        elif command == 'edit':
            entry_interactive_crud.insert_or_update(query)
        elif command == 'write on file':
            entry_interactive_crud.insert_or_update(is_file_entry=True)
        elif command == 'display':
            entry_interactive_crud.display_setting = query['display']
        elif command == 'use':
            entry_interactive_crud.use_setting = query['use']
        elif command == 'open file':
            entry_interactive_crud.get_file_entries()
        elif command == 'new file':
            file_interactive_crud.insert()
        elif command == 'files':
            file_interactive_crud.get_files()
        elif command == 'categories':
            print(entry_interactive_crud.get_categories())
    except KeyboardInterrupt:
        return


def _help():
    print("Help typed")


def interactive():
    print("Welcome to pyLog!")
    print("Type 'help' to view command list")
    std_in = input('> ')
    while std_in != "exit":
        if std_in != '':
            exec_query(std_in)
        std_in = input("> ")
    print("Bye!")

