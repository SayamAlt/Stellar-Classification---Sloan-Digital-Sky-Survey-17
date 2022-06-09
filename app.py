#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


scaler = joblib.load('scaler.bin')
scaler


# In[4]:


app = Flask(__name__)


# In[5]:


@app.route("/")
def home():
    return render_template('home.html')


# In[6]:


@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        alpha = request.form['alpha'] #range: (0.005,359.999)
        delta = request.form['delta'] #range: (-18.785,83.000)
        u = request.form['u'] #range: (15.349,28.690)
        r = request.form['r'] #range: (13.772,25.408)
        run_id = request.form['run_id'] #range: (109.0,8162.0)
        cam_col = request.form['cam_col'] #range: (1.0,6.0)
        field_id = request.form['field_id'] #range: (11.0,479.5)
        redshift = request.form['redshift'] #range: (-0.009,1.678)
        plate = request.form['plate'] #range: (266.0,12547.0)
        fiber_id = request.form['fiber_id'] #range: (1.0,1000.0)
        mjy = request.form['mjy'] #range: (141.39,161.45)

        X_test = scaler.transform([[
            alpha,
            delta,
            u,
            r,
            run_id,
            cam_col,
            field_id,
            redshift,
            plate,
            fiber_id,
            mjy
        ]])
        
        predictions = model.predict(X_test)
        output = predictions[0]
        if output == "GALAXY":
            return render_template('home.html',prediction_text="The stellar class based on the specified spectral characteristics is a galaxy.")
        elif output == "QSO":
            return render_template('home.html',prediction_text="The stellar class based on the specified spectral characteristics is a quasar.")
        elif output == "STAR":
            return render_template('home.html',prediction_text="The stellar class based on the specified spectral characteristics is a star.")


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

