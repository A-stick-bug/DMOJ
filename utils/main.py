from bs4 import BeautifulSoup
import requests


def format_table(data):
    max_title_length = max(len(title) for title, _, _ in data)
    max_url_length = max(len(url) for _, url, _ in data)

    print(f"\n{'Problems':<{max_title_length}} | Points | URL")
    print(f"{'-' * max_title_length}-+--------+-{'-' * max_url_length}")

    for title, url, points in data:
        print(f"{title:<{max_title_length}} | {points:>6} | {url}")


with open("questions.txt", "r") as questions:
    data = []

    qs = questions.readlines()
    for q in qs:
        q = q.strip()
        found = False

        url = f"https://dmoj.ca/problems/?search={q}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            problem_table = soup.find('table', id='problem-table')
            if problem_table:
                rows = problem_table.find_all('tr')

                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) >= 3:
                        link = cells[0].find('a')

                        if link:
                            title = link.text.strip()
                            url = link['href']
                            points = cells[2].text.strip()

                            if title == q:
                                found = True
                                data.append((title, f"dmoj.ca{url}", points))

            if not found:
                print(f"No problems were found for '{q}' on DMOJ")

        else:
            print(f"An error occurred while searching for '{q}' on DMOJ: {response.status_code}")

if __name__ == '__main__':
    format_table(data)
