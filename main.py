from sentimen_classifier import sentimen_classifier
from flask import Flask, jsonify, request


app = Flask(__name__)


obj = sentimen_classifier()

@app.route('/predict', methods=['POST'])

def predict():

  data = request.get_json()
  text = data.get("text","")
  print (text)
  if not text:
    return jsonify({"error": "no text provided"}), 400
  
  prediction = obj.predict_sentiment([text])
  print (prediction)
  result = {"text": text, "sentiment": prediction.tolist() if hasattr(prediction, 'tolist') else prediction}

  return jsonify(result)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5007)
