import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:/Users/HP-PC/PycharmProjects/application/static/models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction==1:
        output="Nominal interest rate"
    elif prediction==2:
        output="effective rate"
    else :
        output="real interest rate"

    return render_template('index.html', prediction_text='Interest category is {}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)