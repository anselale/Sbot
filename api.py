from flask import Flask, request, jsonify
# from agentforge.agents.SummarizationAgent import SummarizationAgent
from CustomAgents.SummaryAgent import SummaryAgent
from CustomAgents.DraftAgent import DraftAgent

app = Flask(__name__)

# summ_agent = SummarizationAgent()
cip_summ_agent = SummaryAgent()
draft_agent = DraftAgent()


# @app.route('/summarize', methods=['POST'])
# def summarize():
#     # Retrieve data from form
#     text = request.form.get('text')
#
#     # Optional: Debugging to print the received data
#     print("\n\nReceived text:\n\n", text)
#
#     # Check if the text is provided
#     if not text:
#         return jsonify({"error": "No text provided"}), 400
#
#     # Process the text (and context if needed)
#     result = summ_agent.summarize(text=text)  # Adjust as per your requirement
#
#     print(f"\n\nModel Response:\n\n{result}")
#
#     # Return the result
#     return jsonify(result=result)


@app.route('/summary', methods=['POST'])
def summary():
    # Retrieve data from form
    ticket = request.form.get('ticket_content')

    # Optional: Debugging to print the received data
    # print("\n\nReceived text:\n\n", text)

    # Check if the text is provided
    if not ticket:
        return jsonify({"error": "No text provided"}), 400

    feedback = request.form.get('feedback')

    # Check if the text is provided
    if not feedback:
        feedback = ""

    # Process the text (and context if needed)
    result = cip_summ_agent.run(ticket_content=ticket, feedback=feedback)  # Adjust as per your requirement

    print(f"\n\nModel Response:\n\n{result}")

    # Return the result
    return jsonify(result=result)


@app.route('/draft', methods=['POST'])
def draft():
    # Retrieve data from form
    ticket = request.form.get('ticket_content')

    # Optional: Debugging to print the received data
    # print("\n\nReceived text:\n\n", text)

    # Check if the text is provided
    if not ticket:
        return jsonify({"error": "No text provided"}), 400

    feedback = request.form.get('feedback')

    # Check if the text is provided
    if not feedback:
        feedback = ""

    # Process the text (and context if needed)
    result = draft_agent.run(ticket_content=ticket, feedback=feedback)  # Adjust as per your requirement

    print(f"\n\nModel Response:\n\n{result}")

    # Return the result
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
