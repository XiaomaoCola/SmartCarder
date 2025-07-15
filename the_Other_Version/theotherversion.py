from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="japan")
# lang可选'en', 'ch', 'japan'等

result = (ocr.predict("/Users/a111/Downloads/001351960.png"))
# 开始识别，括号里的参数是图片的系统位置。
# 可以多图片一起识别。

print(result)
print(type(result))
# 这里result的数据类型是list，每一个element都是一张图。
# 每一个element是一个dictionary。

texts = result[0]['rec_texts']
print(texts)
# 这边'rec_texts'是dictionary里面的key，所以上面打印出来的是value。
# 这个value的数据类型是list，所以下面可以一行一行打印出来。

for line in texts:
    print(line)
