# Smart-Irrigation-System-API
#
**INTRODUCTION<br>**
The API is used to predict for prediction of Soil Status.<br>
#
**ROUTES<br>**
| **Routes** | **Desc** |
|----------------|----------------|
| / | It is just the index of API that says, Welcome. |
| /dashboard | A small UI to see the details of the Smart Irrigation System. |
| /predict | Where POST request is sent for predictiion. |
#
/dashboard UI
<img src="https://i.imgur.com/TbgZTCR.png" title="source: imgur.com" /> <img src="https://i.imgur.com/cBcgHMk.png" title="source: imgur.com" />
#
**LANGUAGES**
> Python (3.11+).
#
**LIBRARIES**
> Flask.<br>
> Joblib.<br>
#
**MODEL**
> Random Forest Classifier.<br>
#
**DATASET<br>**
<b>No of Classes:</b> 4<br>
<b>Unique Vakues:</b> 4,688<br>
<b>Classes:</b> <br><br>

| **Classes** |
|----------------|
| Very Wet |
| Wet |
| Dry |
| Very Dry |
#
<hr>
