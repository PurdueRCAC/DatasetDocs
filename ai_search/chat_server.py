from flask import Flask, request, jsonify
from chat import get_chat_response

app = Flask(__name__)

# In-memory conversation history per session (for demo; use persistent store for production)
conversation_histories = {}

@app.route('/chat', methods=['GET'])
def chat():
    session_id = request.args.get('session_id', 'default')
    user_message = request.args.get('message')
    if not user_message:
        return jsonify({'error': 'Missing required GET parameter: message'}), 400

    # Get or initialize conversation history for this session
    history = conversation_histories.setdefault(session_id, [])
    history.append({'role': 'user', 'content': user_message})

    assistant_response = get_chat_response(history)
    if assistant_response is None:
        return jsonify({'error': 'Failed to retrieve a response from the API.'}), 500

    history.append({'role': 'assistant', 'content': assistant_response})
    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
