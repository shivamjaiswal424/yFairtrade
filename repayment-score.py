import logging
import pickle
from flask import Flask, request, jsonify
from numpy import array

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_repayment_score(instance: dict):
    """Loads model and scalar, predicts repayment score."""
    with open("model.pkl", "rb") as file:
        pickle_model = pickle.load(file)
    with open("scalar.pkl", "rb") as file:
        scalar = pickle.load(file)

    if pickle_model is None or scalar is None:
        logger.warning("Classifier file missing!")
        return -1

    x = array(
        [
            instance["education"],
            instance["capital"],
            instance["income"],
            instance["debt"],
            instance["interest"],
            instance["credit_score"],
        ]
    )

    x_test = scalar.transform(x.reshape(1, -1))
    return pickle_model.predict(x_test)[0]


@app.route("/get_repayment_score", methods=["POST"])
def calculate_repayment_score():
    """Handles POST requests to calculate the score."""
    # Fetch data from the POST request
    data = request.get_json()

    # Create a temporary instance
    instance = dict(
        education=data["education"],
        capital=data["capital"],
        income=data["income"],
        debt=data["debt"],
        interest=data["interest"],
        credit_score=data["credit_score"],
    )

    # Calculate the score
    repayment_score = get_repayment_score(instance)
    # Return the score as JSON
    return jsonify({"repayment_score": repayment_score})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
