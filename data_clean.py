import pandas as pd
import json
import re


def data_clean():
    shloka_corpus = ""
    with open("bhagavadgita.json", encoding="utf8") as file:
        data = json.load(file)

    for shloka in data:
        shloka_corpus += shloka["slok_sanskrit"]

    print(shloka_corpus)

    pattern = r"[\u0964\u0965\u0966-\u096F|]|\|\|-?\|\|"

    cleaned_shlokas = re.sub(pattern, "", shloka_corpus)

    print(cleaned_shlokas)
    
    
    


# def main():
#     data_clean()


# if __name__ == "__main__":
#     main()
