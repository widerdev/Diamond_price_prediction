from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app = Flask(__name__) # pass current module

# make routes

@app.route('/')
def home_page():
    return render_template("index.html") #returning this template (route)

# route for prediction
@app.route("/predict",methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        pass

app.run()
