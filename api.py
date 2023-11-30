from flask import Flask, request, jsonify
from agentforge.agents.SummarizationAgent import SummarizationAgent

app = Flask(__name__)

summ_agent = SummarizationAgent()


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text')
    result = summ_agent.summarize(text=text)  # Replace with appropriate method call
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
