import argparse
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import requests


def extract_from_link(link):
    link_parts = urlparse(link)
    return f"{link_parts.netloc}{link_parts.path}"


def shorten_link(token, link):
    shortener_url = "https://api-ssl.bitly.com/v4/shorten"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    payload = {
        "long_url": link,
    }

    response = requests.post(
        url=shortener_url,
        headers=headers,
        json=payload,
    )
    response.raise_for_status()

    short_link = response.json()['id']

    return short_link


def count_clicks(token, bitlink):
    bitlink = extract_from_link(bitlink)
    summary_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    payload = {
        "unit": "day",
        "units": -1,
    }

    response = requests.get(
        url=summary_url,
        headers=headers,
        params=payload,
    )
    response.raise_for_status()

    clicks_count = response.json()["total_clicks"]

    return clicks_count


def is_bitlink(token, link):
    formatted_link = extract_from_link(link)
    bitlink_info_url = f"https://api-ssl.bitly.com/v4/bitlinks/{formatted_link}"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(
        url=bitlink_info_url,
        headers=headers,
    )

    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_API_TOKEN')
    parser = argparse.ArgumentParser(
        description="Программа выдает ссылки bit.ly и статистику кликов по ним"
    )
    parser.add_argument("link", help="Ваша ссылка")
    args = parser.parse_args()

    url = args.link

    try:
        if is_bitlink(bitly_token, url):
            clicks_count = count_clicks(bitly_token, url)
            print("Количество кликов:", clicks_count)
        else:
            bitlink = shorten_link(bitly_token, url)
            print("Битлинк:", bitlink)
    except requests.exceptions.HTTPError as error:
        print(f"Не удалось обработать ссылку \"{url}\". Ответ от bit.ly:\n",
               error)


if __name__ == '__main__':
    main()
