import cognitive_face as CF

KEY = 'b5305d275700491eb82c5ff82573eab4'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = './white_new.jpg'
result = CF.face.detect(img_url)
print result
