from flask import Flask, request, jsonify
from agentforge.agents.SummarizationAgent import SummarizationAgent

app = Flask(__name__)

summ_agent = SummarizationAgent()


@app.route('/summarize', methods=['POST'])
def summarize():
    # Retrieve data from form
    text = request.form.get('text')

    # Optional: Debugging to print the received data
    print("Received text:", text)

    # Check if the text is provided
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Process the text (and context if needed)
    result = summ_agent.summarize(text=text)  # Adjust as per your requirement

    # Return the result
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
