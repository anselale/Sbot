from flask import Flask, request, jsonify
from agentforge.agents.SummarizationAgent import SummarizationAgent
import json

app = Flask(__name__)

summ_agent = SummarizationAgent()


@app.route('/summarize', methods=['POST'])
def summarize():
    # Debugging: Print the request method and headers
    print("Request Method: ", request.method)
    print("Request Headers: ", request.headers)

    # Get JSON data from request
    data = request.get_json()
    if data is None:
        print("No JSON received. Request data: ", request.data)
        return jsonify({"error": "No JSON data found"}), 400

    # Debugging: Print the received JSON data
    print("JSON received: ", json.dumps(data, indent=4))

    # Process the text
    text = data.get('text')
    if not text:
        print("No 'text' found in JSON data")
        return jsonify({"error": "No 'text' key in JSON data"}), 400

    # Perform summarization
    result = summ_agent.summarize(text=text)  # Replace with appropriate method call

    # Debugging: Print the result
    print("Summarization result: ", result)

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
