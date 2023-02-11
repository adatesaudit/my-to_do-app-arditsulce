import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal9")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# todo képre cserélni a nyomógombot
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do-App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            print("Select an item first")
    elif event == "Complete":
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')
    elif event == "Exit":
        break
    elif event == "todos":
        window['todo'].update(value=values['todos'][0])
    elif event == sg.WIN_CLOSED:
        break

window.close()

# while True:
#     event, values = window.read()
#     print(1, event)
#     print(2, values)
#     print(3, values['todos'])
#     match event:
#         case "Add":
#             todos = functions.get_todos()
#             new_todo = values['falsetodo'] + "\n"
#             todos.append(new_todo)
#             functions.write_todos(todos)
#             window['todos'].update(values=todos)
#
#         case "Edit":
#             try:
#                 todo_to_edit = values['todos'][0]
#                 new_todo = values['falsetodo']
#
#                 todos = functions.get_todos()
#                 index = todos.index(todo_to_edit)
#                 todos[index] = new_todo
#                 functions.write_todos(todos)
#                 window['todos'].update(values=todos)
#             except IndexError:
#                 print("Select an item first")
#
#         case "Complete":
#             todo_to_complete = values['todos'][0]
#             todos = functions.get_todos()
#             todos.remove(todo_to_complete)
#             functions.write_todos(todos)
#             window['todos'].update(values=todos)
#             window['falsetodo'].update(value='')
#
#         case "Exit":
#             break
#
#         case "todos":
#             window['falsetodo'].update(value=values['todos'][0])
#
#         case sg.WIN_CLOSED:
#             break