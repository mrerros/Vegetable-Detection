from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="qmYKfYLbupIakl4hNQ5a"
)

result = CLIENT.infer('all/model.jpg', model_id="strawberry-detection-msf0m/3")

with open('result.txt', "w") as file:
    file.write(str(result))

print("Yazdırıldı")