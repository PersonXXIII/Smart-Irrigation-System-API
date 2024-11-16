# Smart-Irrigation-System-API
#
**INTRODUCTION<br>**
The API is used to predict for prediction of Soil Status. The Training model for this is <a href="https://github.com/PersonXXIII/Smart-Irrigation-System-Training">here.</a> and for the IoT system, you can visit the repo <a href="https://github.com/PersonXXIII/Smart-Irrigation-System-IoT">here.</a><br>
#
**ROUTES<br>**
| **Routes** | **Desc** |
|----------------|----------------|
| / | It is just the index of API that says, Welcome. |
| /dashboard | A small UI to see the details of the Smart Irrigation System. |
| /predict | Where POST request is sent for predictiion. |
#
**/dashboard UI Media<br>**
<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
  <img src="https://i.imgur.com/TbgZTCR.png" alt="Dashboard UI 1" style="width: 500px; height: 400px;">
  <img src="https://i.imgur.com/cBcgHMk.png" alt="Dashboard UI 2" style="width: 500px; height: 400px;">
</div>

[![Watch the video](https://img.youtube.com/vi/4a8zPJVXBd0/0.jpg)](https://youtu.be/4a8zPJVXBd0)

Click the thumbnail above to watch the video.<br><br>
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
