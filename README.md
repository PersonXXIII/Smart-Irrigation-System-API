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
**/dashboard UI<br>**
1. Images:<br>
<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
  <img src="https://i.imgur.com/TbgZTCR.png" alt="Dashboard UI 1" style="width: 300px; height: auto;">
  <img src="https://i.imgur.com/cBcgHMk.png" alt="Dashboard UI 2" style="width: 300px; height: auto;">
</div>
2. Video:<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/4a8zPJVXBd0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> <br>
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
