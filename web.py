import streamlit as st
import function

todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("Aplikasi ini memudahkan produktivitas anda")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        st.legacy_caching.clear_cache(todo)
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')

