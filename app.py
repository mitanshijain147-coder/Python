
import streamlit as st
from pathlib import Path
import shutil

# Main workspace
BASE = Path("file_manager_workspace").resolve()
BASE.mkdir(exist_ok=True)

st.set_page_config(
    page_title="File Manager",
    page_icon="📁",
    layout="wide"
)

# ---------- Helper Functions ----------

def get_path(name):
    p = (BASE / name).resolve()

    if not p.is_relative_to(BASE) or p == BASE:
        raise ValueError("Invalid file or folder path")

    return p


def get_items():
    return sorted(
        [p for p in BASE.rglob("*")],
        key=lambda p: str(p).lower()
    )


def get_files():
    return [p for p in get_items() if p.is_file()]


def get_folders():
    return [p for p in get_items() if p.is_dir()]


def relative_name(p):
    return str(p.relative_to(BASE))


# ---------- Sidebar ----------

st.sidebar.title("📁 File Manager")
st.sidebar.write("Manage your files and folders")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "Dashboard",
        "Create Folder",
        "View Folders",
        "Update Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Python + Streamlit Project")


# ---------- Dashboard ----------

if menu == "Dashboard":

    st.title("📁 File & Folder Management System")
    st.write("Welcome! Manage all your files and folders here.")

    folders = get_folders()
    files = get_files()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Folders", len(folders))

    with col2:
        st.metric("Total Files", len(files))

    st.divider()

    st.subheader("Your Workspace")

    if not get_items():
        st.info("Your workspace is empty. Create a folder or file to get started.")
    else:
        for item in get_items():
            if item.is_dir():
                st.write("📁", relative_name(item))
            else:
                st.write("📄", relative_name(item))


# ---------- Create Folder ----------

elif menu == "Create Folder":

    st.title("📁 Create New Folder")

    name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        if not name.strip():
            st.error("Please enter a folder name.")

        else:
            try:
                p = get_path(name.strip())

                if p.exists():
                    st.warning("This folder or file already exists.")

                else:
                    p.mkdir(parents=True)
                    st.success("Folder created successfully!")

            except (ValueError, OSError) as e:
                st.error(f"Unable to create folder: {e}")


# ---------- View Folders ----------

elif menu == "View Folders":

    st.title("📂 View All Folders")

    folders = get_folders()

    if folders:
        for folder in folders:
            st.write("📁", relative_name(folder))
    else:
        st.info("No folders found.")


# ---------- Update Folder ----------

elif menu == "Update Folder":

    st.title("✏️ Rename Folder")

    folders = get_folders()
    options = [relative_name(p) for p in folders]

    if options:

        selected = st.selectbox("Select folder", options)
        new_name = st.text_input("Enter new folder name")

        if st.button("Rename Folder"):

            if not new_name.strip():
                st.error("Enter a new folder name.")

            else:
                try:
                    old_path = get_path(selected)
                    new_path = get_path(new_name.strip())

                    if new_path.exists():
                        st.warning("A file or folder with this name already exists.")
                    else:
                        old_path.rename(new_path)
                        st.success("Folder renamed successfully!")
                        st.rerun()

                except (ValueError, OSError) as e:
                    st.error(f"Unable to rename folder: {e}")

    else:
        st.info("No folders available to rename.")


# ---------- Delete Folder ----------

elif menu == "Delete Folder":

    st.title("🗑️ Delete Folder")

    folders = get_folders()
    options = [relative_name(p) for p in folders]

    if options:

        selected = st.selectbox("Select folder to delete", options)

        st.warning("Deleting a folder also deletes all files and subfolders inside it.")

        confirm = st.checkbox("I understand and want to delete this folder.")

        if st.button("Delete Folder", disabled=not confirm):

            try:
                p = get_path(selected)

                if p.is_dir():
                    shutil.rmtree(p)
                    st.success("Folder deleted successfully!")
                    st.rerun()
                else:
                    st.error("Folder not found.")

            except (ValueError, OSError) as e:
                st.error(f"Unable to delete folder: {e}")

    else:
        st.info("No folders available to delete.")


# ---------- Create File ----------

elif menu == "Create File":

    st.title("📄 Create New File")

    name = st.text_input("Enter file name with extension")
    data = st.text_area("Enter content of your file")

    if st.button("Create File"):

        if not name.strip():
            st.error("Please enter a file name.")

        else:
            try:
                p = get_path(name.strip())

                if p.exists():
                    st.warning("File or folder already exists.")

                else:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(data, encoding="utf-8")
                    st.success("File created successfully!")

            except (ValueError, OSError) as e:
                st.error(f"Unable to create file: {e}")


# ---------- Read File ----------

elif menu == "Read File":

    st.title("📖 Read File")

    files = get_files()
    options = [relative_name(p) for p in files]

    if options:

        selected = st.selectbox("Select a file", options)

        if st.button("Read File"):

            try:
                p = get_path(selected)
                data = p.read_text(encoding="utf-8")

                st.subheader("File Content")
                st.code(data, language="text")

            except (ValueError, OSError, UnicodeError) as e:
                st.error(f"Unable to read file: {e}")

    else:
        st.info("No files found.")


# ---------- Update File ----------

elif menu == "Update File":

    st.title("✏️ Update File")

    files = get_files()
    options = [relative_name(p) for p in files]

    if options:

        selected = st.selectbox("Select file", options)

        action = st.radio(
            "Choose operation",
            ["Rename File", "Overwrite File", "Append Content"]
        )

        if action == "Rename File":

            new_name = st.text_input("Enter new file name")

            if st.button("Rename"):
                try:
                    old_path = get_path(selected)
                    new_path = get_path(new_name.strip())

                    if not new_name.strip():
                        st.error("Enter a new file name.")
                    elif new_path.exists():
                        st.warning("This name already exists.")
                    else:
                        old_path.rename(new_path)
                        st.success("File renamed successfully!")
                        st.rerun()

                except (ValueError, OSError) as e:
                    st.error(f"Unable to rename file: {e}")

        elif action == "Overwrite File":

            data = st.text_area("Enter new content")

            if st.button("Overwrite"):
                try:
                    p = get_path(selected)
                    p.write_text(data, encoding="utf-8")
                    st.success("File overwritten successfully!")

                except (ValueError, OSError) as e:
                    st.error(f"Unable to update file: {e}")

        elif action == "Append Content":

            data = st.text_area("Enter content to append")

            if st.button("Append"):
                try:
                    p = get_path(selected)

                    with open(p, "a", encoding="utf-8") as file:
                        file.write(data)

                    st.success("Content appended successfully!")

                except (ValueError, OSError) as e:
                    st.error(f"Unable to update file: {e}")

    else:
        st.info("No files available to update.")


# ---------- Delete File ----------

elif menu == "Delete File":

    st.title("🗑️ Delete File")

    files = get_files()
    options = [relative_name(p) for p in files]

    if options:

        selected = st.selectbox("Select file to delete", options)

        confirm = st.checkbox("I want to permanently delete this file.")

        if st.button("Delete File", disabled=not confirm):

            try:
                p = get_path(selected)

                if p.is_file():
                    p.unlink()
                    st.success("File deleted successfully!")
                    st.rerun()
                else:
                    st.error("File not found.")

            except (ValueError, OSError) as e:
                st.error(f"Unable to delete file: {e}")

    else:
        st.info("No files available to delete.")
