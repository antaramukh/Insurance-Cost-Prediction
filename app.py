import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv('insurance.csv')
pipe = pickle.load(open("MLRModel.pkl", 'rb'))


@app.route('/')
def index():
    smoker = data['smoker'].unique()
    sexs = data['sex'].unique()
    regions = data['region'].unique()
    return render_template('index.html', sexs=sexs, smoker=smoker, regions=regions)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = request.form.get('age')
        sex = request.form.get('sex')
        if sex == 'female':
            sex = 0
        else:
            sex = 1
        bmi = request.form.get('bmi')
        smoke = request.form.get('smoke')
        if smoke == 'no':
            smoke = 0
        else:
            smoke = 1
        dep = request.form.get('dep')
        region = request.form.get('region')
        if region == 'southeast':
            region = 0
        elif region == 'southwest':
            region = 1
        elif region == 'northwest':
            region = 2
        elif region == 'northeast':
            region = 3

        input_data = (int(age), int(sex), float(bmi), int(dep), int(smoke), int(region))
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        prediction = pipe.predict(input_data_reshaped)[0]
        return str(np.round(prediction, 2))

    except:
        return str("Sorry")


if __name__ == "__main__":
    app.run()
