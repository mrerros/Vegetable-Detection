from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://outline.roboflow.com",
    api_key="qmYKfYLbupIakl4hNQ5a"
)

result = CLIENT.infer('all/model.jpg', model_id="carrot-test/3")

with open('result.txt', "w") as file:
    file.write(str(result))
    print("Yazdırıldı")