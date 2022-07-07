import csv
import json
import requests, time

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

def get_json():
    count = 1
    for i in range(0, 241, 40):
        url = f"https://www.olx.pl/api/v1/offers/?offset={i}&limit=40&category_id=1554&filter_refiners=&sl=18114005058x5b939de8"

        r = requests.get(url, headers)

        with open(f'data/{count}.json', 'w', encoding='utf-8') as file:
            json.dump(r.json(), file, indent=4, ensure_ascii=False)

        count += 1
        time.sleep(3)

def get_data():
    full_data = []
    count = 1

    with open('main.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
                    'id',
                    'href',
                    'title',
                    'location',
                    'price',
                    'vin',
                    'model',
                    'year',
                    'enginesize',
                    'enginepower',
                    'petrol',
                    'car_body',
                    'milage',
                    'color',
                    'condition',
                    'transmission',
                    'country_origin'
                    'righthanddrive'
        ])

    for index in range(1, 8):
        with open('data/1.json', encoding='utf-8') as file:
            data = json.load(file)

        for info in data['data']:
            id = info['id']
            href = info['url'].strip()
            title = info['title'].strip()
            # description = info['description'].strip()
            location = f"{info['location']['city']['name']}, {info['location']['region']['name']}".strip()

            try:
                for i in range(0, 14):
                    if info['params'][i]['key'] == "price":
                        price = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "model":
                        model = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "year":
                        year = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "enginesize":
                        enginesize = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "enginepower":
                        enginepower = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "petrol":
                        petrol = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "car_body":
                        car_body = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "milage":
                        milage = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "color":
                        color = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "condition":
                        condition = info['params'][i]['value']['label'].strip()
                    if info['params'][i]['key'] == "transmission":
                        transmission = info['params'][i]['value']['label'].strip()
                    try:
                        if info['params'][i]['key'] == "country_origin":
                            country_origin = info['params'][i]['value']['label'].strip()
                    except Exception:
                        country_origin = None
                    try:
                        if info['params'][i]['key'] == "righthanddrive":
                            righthanddrive = info['params'][i]['value']['label'].strip()
                    except Exception:
                        righthanddrive = None
                    try:
                        if info['params'][i]['key'] == "vin":
                            vin = info['params'][i]['value']['label'].strip()
                    except Exception:
                        vin = None
            except Exception as ex:
                print(ex)

            full_data.append(
                {
                    'id': id,
                    'href': href,
                    'title': title,
                    'location': location,
                    'price': price,
                    'vin': vin,
                    'model': model,
                    'year': year,
                    'enginesize': enginesize,
                    'enginepower': enginepower,
                    'petrol': petrol,
                    'car_body': car_body,
                    'milage': milage,
                    'color': color,
                    'condition': condition,
                    'transmission': transmission,
                    'country_origin': country_origin,
                    'righthanddrive': righthanddrive
                }
            )

            with open('main.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((
                    id,
                    href,
                    title,
                    location,
                    price,
                    vin,
                    model,
                    year,
                    enginesize,
                    enginepower,
                    petrol,
                    car_body,
                    milage,
                    color,
                    condition,
                    transmission,
                    country_origin,
                    righthanddrive
                ))

            print(count)
            count += 1

    with open('main.json', 'w', encoding='utf-8') as file:
        json.dump(full_data, file, indent=4, ensure_ascii=False)

def main():
    # get_json()
    get_data()

if __name__ == '__main__':
    main()
