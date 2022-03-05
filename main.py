from my_chrome_history import *
from my_morph import *
from my_wordcloud import *

import cv2
import re

"""
texts = ["12", "34*56", "PC-8801", "", "ABC12-34def"]
for text in texts:
    nums = re.sub(r"d", "", text)
    result = re.sub(r"\d", "", text)
    print(text, "->", result)



"""
words = get_history()

#filename = "hasire.txt"
#with open(filename, mode="r", encoding="utf_8") as f:
#    words = f.read()

words = morph(words)
words = ' '.join(words)
print(words)

image = make_wordcloud(words)

cv2.imshow("", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
