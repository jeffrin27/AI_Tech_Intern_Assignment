import streamlit as st

# Page setup
st.set_page_config(page_title="To-Do App", page_icon="✅", layout="centered")
st.title("✅ Simple To-Do Manager (EdTech Version)")

# Initialize tasks (preloaded EdTech-related tasks)
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        "Attend online class",
        "Submit feedback form",
        "Prepare for weekly quiz",
        "Review leadership notes"
    ]

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("➕ Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task)
        st.success("Task added!")

# Show tasks
st.subheader("📋 Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([6, 2, 2])

        with col1:
            st.write(f"- {task}")

        with col2:
            # Done button removes the task
            if st.button("✔️ Done", key=f"done_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

        with col3:
            # Delete button removes the task
            if st.button("🗑️ Delete", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

    # Clear All Tasks button
    if st.button("🧹 Clear All Tasks"):
        st.session_state.tasks = []
        st.success("All tasks cleared!")
        st.rerun()
else:
    st.info("No tasks yet. Add one above ⬆️")
