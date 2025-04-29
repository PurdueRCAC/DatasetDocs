import os
import shutil
from knowledge_manager import upload_file, add_file_to_knowledge, get_all_documents

def find_datasets_kb_id():
    """Finds the knowledge base ID for the 'Datasets' KB (case-insensitive)."""
    docs = get_all_documents()
    for doc in docs:
        if doc.get('name', '').strip().lower() == 'datasets':
            return doc['id']
    raise RuntimeError("No knowledge base named 'Datasets' found.")

def upload_rst_files(docs_dir):
    """
    Finds all .rst files in docs_dir, uploads them as their parent folder name .rst, and adds them to the Datasets KB.
    """
    kb_id = find_datasets_kb_id()
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.rst') and file != 'index.rst':
                # Compute relative path from docs_dir
                rel_path = os.path.relpath(os.path.join(root, file), docs_dir)
                parts = rel_path.split(os.sep)
                if len(parts) >= 3:
                    top_level = parts[0]
                    parent = parts[-2]
                    new_name = f"{top_level}-{parent}.rst"
                elif len(parts) == 2:
                    # e.g. docs/a/10.rst → a-a.rst
                    top_level = parts[0]
                    new_name = f"{top_level}-{top_level}.rst"
                else:
                    # e.g. docs/10.rst → 10.rst
                    new_name = parts[-1]
                src_path = os.path.join(root, file)
                tmp_path = os.path.join('/tmp', new_name)
                shutil.copy2(src_path, tmp_path)
                print(f"Uploading {tmp_path} (original: {src_path}) ...")
                file_obj = upload_file(tmp_path)
                if file_obj and 'id' in file_obj:
                    file_id = file_obj['id']
                    add_result = add_file_to_knowledge(kb_id, file_id)
                    print(f"Added {new_name} to knowledge base. Result: {add_result}")
                else:
                    print(f"Failed to upload {src_path}")
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass

if __name__ == "__main__":
    upload_rst_files("../docs")
