import requests
from config import load_secrets

secrets = load_secrets()
API_KEY = secrets["api_key"]
KNOWLEDGE_API_URL = secrets["knowledge_api_url"]

def get_all_documents():
    """
    Retrieves all documents from the knowledge base.
    
    Returns:
        A list of document dictionaries if successful, or an empty list on failure.
    """
    url = f"{KNOWLEDGE_API_URL}/knowledge/list"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        if isinstance(data, dict):
            documents = data.get("data", [])
        elif isinstance(data, list):
            documents = data
        else:
            print("Unexpected response format:", data)
            documents = []
        print(f"Found {len(documents)} documents in the knowledge base.")
        return documents
    except requests.RequestException as e:
        print("Error retrieving documents:", e)
        return []


def upload_file(file_path):
    """
    Uploads a file to the OpenWebUI/AnvilGPT instance.
    Returns the file object (including its 'id') if successful, else None.
    Prints detailed error info if upload fails.
    """
    url = f"{KNOWLEDGE_API_URL}/files/"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, headers=headers, files=files)
            if response.ok:
                data = response.json()
                # Accept either top-level 'id' or in 'data'
                if "id" in data:
                    return data
                elif "data" in data and "id" in data["data"]:
                    return data["data"]
                else:
                    return None
            else:
                print(f"File upload failed with status code {response.status_code}")
                return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Unexpected error opening file: {e}")
        return None

def add_file_to_knowledge(kb_id, file_id):
    """
    Adds a file (by file_id) to a knowledge base (by kb_id).
    Returns the API response.
    Prints debug info if request fails.
    """
    url = f"{KNOWLEDGE_API_URL}/knowledge/{kb_id}/file/add"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {"file_id": file_id}
    print(f"[DEBUG] POST {url} with payload: {data}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"[DEBUG] Error response content: {response.content}")
        print(f"Error adding file to knowledge base: {e}")
        return None



def tag_document(file_id, tags):
    """
    Adds or updates tags for a file/document in the knowledge base.

    Args:
        file_id (str): The ID of the file to tag.
        tags (list of str): Tags to associate with the file.

    Returns:
        dict: The API response as a dictionary.
    """
    url = f"{KNOWLEDGE_API_URL}/files/{file_id}/update"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "tags": tags
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error tagging file: {e}")
        return None

def delete_document(doc_id):
    """
    Deletes a document from the knowledge base by its ID.
    
    Args:
        doc_id (str): The identifier of the document to delete.
    
    Returns:
        True if deletion was successful, False otherwise.
    """
    url = f"{KNOWLEDGE_API_URL}/files/{doc_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print(f"Deleted document {doc_id}.")
        return True
    except requests.RequestException as e:
        print(f"Failed to delete document {doc_id}:", e)
        return False

def delete_all_documents():
    """
    Deletes all documents in the knowledge base.
    
    Iterates over the list of documents retrieved from the API and attempts to delete each one.
    """
    documents = get_all_documents()
    if not documents:
        print("No documents to delete or error retrieving documents.")
        return

    deleted_count = 0
    for doc in documents:
        file_ids = []
        # Option 1: from data['file_ids']
        if doc.get('data') and doc['data'].get('file_ids'):
            file_ids.extend(doc['data']['file_ids'])
        # Option 2: from files array
        if doc.get('files'):
            file_ids.extend([f['id'] for f in doc['files'] if 'id' in f])
        if not file_ids:
            print(f"No file IDs found for knowledge base '{doc.get('name')}' (ID: {doc.get('id')}), skipping.")
        
        # Deletion of files
        for file_id in file_ids:
            if delete_document(file_id):
                print(f"Deleted file {file_id} from knowledge base '{doc.get('name')}' (ID: {doc.get('id')})")
                deleted_count += 1
    total_files = sum(
        len(doc.get('data', {}).get('file_ids', [])) + len(doc.get('files', []))
        for doc in documents
    )
    print(f"Deletion complete: {deleted_count} file(s) deleted out of {total_files} total. Knowledge bases were not deleted.")

if __name__ == "__main__":
    # Example: Upload a file and add it to the 'Datasets' knowledge base
    documents = get_all_documents()
    dataset_kb = next((doc for doc in documents if doc.get('name', '').strip().lower() == 'datasets'), None)
    if dataset_kb:
        kb_id = dataset_kb['id']
        file_path = "../README.md"  # Change to your actual file path
        print(f"Uploading {file_path} ...")
        file_obj = upload_file(file_path)
        if file_obj and 'id' in file_obj:
            file_id = file_obj['id']
            print(f"File uploaded with ID: {file_id}. Adding to knowledge base '{dataset_kb['name']}' (ID: {kb_id})...")
            add_result = add_file_to_knowledge(kb_id, file_id)
            print("Add to knowledge base result:", add_result)
        else:
            print("File upload failed.")
    else:
        print("No knowledge base named 'Datasets' found.")
    # delete_all_documents() 
