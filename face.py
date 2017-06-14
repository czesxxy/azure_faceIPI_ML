import cognitive_face as CF

KEY = 'a7f1241ed0b34a91a420a16d56dde6c3'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = './white_new.jpg'
result = CF.face.detect(img_url)
print result
