from turtle import width
from wordcloud import WordCloud
import os


def make_wordcloud(words, background_color="white", width=800, height=600, font_file = "UDDigiKyokashoN-R.ttc", min_font_size=15):
    font_path = os.environ["SYSTEMROOT"] + r"/Fonts/" + font_file
    wordcloud = WordCloud(background_color = background_color,
                          font_path = font_path,
                          width = width, 
                          height = height,
                          min_font_size = min_font_size)

    wordcloud.generate(words)
    image = wordcloud.to_array()
    return image

if __name__ == "__main__":
    filename = "hasire.txt"
    with open(filename, mode="r", encoding="utf_8") as f:
        words = f.read()

    image = make_wordcloud(words)
    import cv2
    cv2.imshow("", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()