import streamlit as st
# Streamlit is a popular library, as it is easy to create web apps and easy to integrate
# with graphs and widgets and deploy your apps
import functions
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    st.session_state["new_todo"] = ""
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase productivity")

# st.checkbox("Buy grocery")
# st.checkbox("Throw the trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo..",
              on_change=add_todo, key='new_todo')

# st.session_state
