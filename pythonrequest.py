# import requests

# # API'nin URL'si
# url = "https://educationwebapimanagement-dev002.azure-api.net/api/CafeteriaCard"

# # Abonelik anahtarı
# subscription_key = "5e11bd7709744923a4f9afea26b8b24d"

# # Başlıklar (headers) sözlüğü oluşturun
# headers = {
#     "Ocp-Apim-Subscription-Key": subscription_key
# }

# # GET isteği gönderin
# response = requests.get(url, headers=headers)

# # Yanıtı kontrol edin
# if response.status_code == 200:
#     print("İstek başarılı, yanıt:", response.text)
# else:
#     print("İstek başarısız, hata kodu:", response.status_code)


#     https.addHeader("Content-Type", "application/json");
# https.addHeader("Ocp-Apim-Subscription-Key", "b6e696976de349e5be3c0cff0e782ec2");

# // JSON verisini hazırla
# String jsonData = "{"
#                   "\"title\": \"Deneme Esp32\","
#                   "\"content\": \"Bu bir uyarı duyurusudur.\","
#                   "\"date\": \"2024-05-05T16:36:56.968Z\","
#                   "\"typeID\": 1,"
#                   "\"status\": true"
#                   "}";

# // HTTP POST isteği gönder
# int httpResponseCode = https.POST(jsonData);

import requests

# API'nin URL'si
url = "https://localhost:44373/api/CafeteriaCard/DeductBalance"

# Abonelik anahtarı
subscription_key = "5e11bd7709744923a4f9afea26b8b24d"

# Başlıklar (headers) sözlüğü oluşturun
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"  # İstek gövdesinin JSON formatında olduğunu belirtin
}

# Güncellenecek veri
data = {
    "cardNumber": "19216821",
    "amount": 30
}

# PUT isteği gönderin
response = requests.put(url, headers=headers, json=data)

# Yanıtı kontrol edin
if response.status_code == 200:
    print("İstek başarılı, yanıt:", response.text)
else:
    print("İstek başarısız, hata kodu:", response.status_code)
