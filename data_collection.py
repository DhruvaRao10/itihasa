import requests
import json

base_url = "https://vedicscriptures.github.io/slok/{ch}/{sl}"
output_file = "bhagavadgita.json"


def collect_gita_data():
    gita_data = []
    total_chapters = 18

    for i in range(1, total_chapters + 1):
        for j in range(1, 80):
            url = base_url.format(ch=i, sl=j)
            response = requests.get(url)
            if response.status_code != 200:
                break

            data = response.json()
            entry = {
                "id": data.get("_id"),
                "chapter": data.get("chapter"),
                "verse": data.get("verse"),
                "slok_sanskrit": data.get("slok"),
                "transliteration": data.get("transliteration"),
            }
            gita_data.append(entry)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(gita_data, f, indent=4, ensure_ascii=False)

    print(f"Shlokas saved to {output_file}")


def main():
    collect_gita_data()


if __name__ == "__main__":
    main()
    