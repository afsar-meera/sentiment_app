import pickle

class sentimen_classifier:

    def read_model(self,file):
        with open(file, 'rb') as model_file:
            model = pickle.load(model_file)
            return model

    def predict_sentiment(self,text):
        model = self.read_model('text_classification_pipeline.pkl')
        return model.predict(text)



# if __name__ == "__main__":
#   obj = sentimen_classifier()
#   text = "input"
#   prediction = obj.predict_sentiment(text)

#   print ({"text":  text , "sentiment": prediction})