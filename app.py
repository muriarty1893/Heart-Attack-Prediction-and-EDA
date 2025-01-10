from flask import Flask, render_template, request, jsonify
import requests
import joblib
from pathlib import Path

app = Flask(__name__)
# scroll ile değer değişmesi 
# inputlar için dropdown menü
# 
# Google Maps API Key
GOOGLE_MAPS_KEY = "AIzaSyDbVk9SRUpOCbNH39nKN9cYRweWUqt3RtI"

# Model yükleme
try:
    logreg_model = joblib.load('logreg_model.pkl')
except FileNotFoundError:
    logreg_model = None  # Model yoksa bu değişken None olur


def search_hospitals(latitude, longitude):
    try:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=20000&type=hospital&key={GOOGLE_MAPS_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()

        hospitals = []
        if 'results' in data:
            for hospital in data['results']:
                hospitals.append({
                    'name': hospital.get('name'),
                    'address': hospital.get('vicinity'),
                    'lat': hospital['geometry']['location']['lat'],
                    'lon': hospital['geometry']['location']['lng']
                })
        return hospitals[:5]
    except requests.RequestException as e:
        print(f"Hospital Search Error: {e}")
        return []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', google_maps_key=GOOGLE_MAPS_KEY)


@app.route('/predict', methods=['POST'])
def predict():
    if logreg_model is None:
        return jsonify({"success": False, "error": "Model bulunamadı."}), 500

    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not latitude or not longitude:
        return jsonify({
            'success': False,
            'error': 'Konum bilgisi alınamadı. Lütfen konum izni verdiğinizden emin olun.'
        }), 400

    try:
        features = [
            float(data['age']),
            float(data['sex']),
            float(data['cp']),
            float(data['trestbps']),
            float(data['chol']),
            float(data['fbs']),
            float(data['restecg']),
            float(data['thalach']),
            float(data['exang']),
            float(data['oldpeak']),
            float(data['slope']),
            float(data['ca']),
            float(data['thal'])
        ]

        prediction = logreg_model.predict([features])
        probability = logreg_model.predict_proba([features])[0][1]  # İkincil sınıf olasılığı

        result = {
            "success": True,
            "prediction": "Pozitif" if prediction[0] == 1 else "Negatif",
            "probability": round(probability * 100, 3),
            "doctor_advice": "Risk bulunmamaktadır, ancak düzenli kontrol önerilir." if prediction[0] == 0 else "Acilen Kardiyoloji Hekimine Görünmeniz Tavsiye Edilir"
        }

        # Yakın hastaneleri arama
        hospitals = search_hospitals(latitude, longitude)
        result['hospitals'] = hospitals

        # Harita URL'si
        map_url = f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_KEY}&q={latitude},{longitude}&zoom=15"
        result['map_url'] = map_url

        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == '__main__':

    app.run(debug=True)
