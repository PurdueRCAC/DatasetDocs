import requests
from config import load_secrets

secrets = load_secrets()
API_KEY = secrets["api_key"]
API_URL = secrets["chat_api_url"]

# You can also change the model parameter to match your deployment; here we use a placeholder.
MODEL = "llama3.1:latest"  

def get_chat_response(messages):
    """
    Sends the conversation history as a list of messages to the LLM API.
    
    Args:
        messages (list): A list of dicts that represents the conversation history.
                         Each dict should have 'role' (e.g., 'user' or 'assistant') and 'content'.
    
    Returns:
        The assistant's response as a string if successful, or None if there was an error.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print("Error during API request:", e)
        return None

    # The API response is assumed to follow the OpenAI API style,
    # where the generated message is in data["choices"][0]["message"]["content"]
    try:
        data = response.json()
        assistant_message = data["choices"][0]["message"]["content"]
        return assistant_message.strip()
    except (KeyError, ValueError) as e:
        print("Error parsing API response:", e)
        return None

def main():
    print("Welcome to the Dataset Search Chatbot Service!")
    print("Type your questions and press enter. Type 'exit' to quit.\n")

    # Initialize conversation history (a list of messages).
    conversation_history = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Append the user's message to the history.
        conversation_history.append({"role": "user", "content": user_input})

        # Get response from the chat API by sending the full conversation history.
        assistant_response = get_chat_response(conversation_history)
        if assistant_response is None:
            print("Failed to retrieve a response from the API.")
            continue

        # Print the assistant's reply.
        print("Bot:", assistant_response, "\n")

        # Append the assistant's reply to the conversation history.
        conversation_history.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()
