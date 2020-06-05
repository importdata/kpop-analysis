# use flask to host the model

import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'model.pkl', 'rb') as f:
    model = pickle.load(f)

# initialize the flask app
app = flask.Flask(__name__, template_folder='templates')


'''
# open the pickle file in the read mode
model = pickle.load(open('model.pkl', 'rb'))



# root node for API URL
@app.route('/')
def home():
    return render_template('index.html') # rewrite to the index.html file


# create another API
@app.route('/predict', methods=['POST'])
def predict():
   
    #For rendering results on HTML GUI
  
    # int value of dependent variables
    int_features = [int(x) for x in request.form.values()]
    
    # convert the above to the array
    final_features = [np.array(int_features)]
    #final_features = np.array(int_features)[:, np.newaxis]
    #final_features = np.array(int_features)
    #print(final_features, flush=True)
    
    # perform prediction
    prediction = model.predict(final_features)
    
    # get the prediction
    output = round(prediction[0], 2)
    print(output)

    return render_template('index.html', prediction_text='The predicted number of hours you listen to K-Pop is {} hours'.format(output))
'''    


# set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        yr_listened = flask.request.form['yr_listened']
        daily_MV_hr = flask.request.form['daily_MV_hr']
        yr_merch_spent = flask.request.form['yr_merch_spent']
        age = flask.request.form['age']
        num_gr_like = flask.request.form['num_gr_like']
        
        # Make DataFrame for model
        input_variables = pd.DataFrame([[yr_listened, daily_MV_hr, yr_merch_spent, age, num_gr_like]],
                                       columns=['yr_listened', 'daily_MV_hr', 'yr_merch_spent', 'age', 'num_gr_like'],
                                       dtype=float,
                                       index=['input'])
        
        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
        output = float(round(prediction, 2))
        
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('index.html',
                                     original_input={'yr_listened':yr_listened,
                                                     'daily_MV_hr':daily_MV_hr,
                                                     'yr_merch_spent':yr_merch_spent,
                                                     'age':age,
                                                     'num_gr_like':num_gr_like},
                                     result=float(output)
                                     )
        
if __name__ == "__main__":
    app.run(debug=True)