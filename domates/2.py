import cv2
import ast, os


with open('result.txt', 'r') as file:
    result_str = file.read()

result_dict = ast.literal_eval(result_str)


image = cv2.imread('all/model.jpg')


for prediction in result_dict['predictions']:
    class_name = prediction['class']
    x = int(prediction['x'])
    y = int(prediction['y'])
    width = int(prediction['width'])
    height = int(prediction['height'])
    
    
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    cv2.putText(image, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imwrite('output.jpg', image)

os.remove('result.txt')
os.remove('all/model.jpg')
print("İşlem tamamlandı")