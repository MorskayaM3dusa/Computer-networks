import csv

from ping3 import ping


websites = ["ya.ru", "mail.ru", "nsu.ru", "vk.com", "github.com", "nsuts.ru", "twitch.tv", "wikipedia.org", "ok.ru", "gosuslugi.ru"]
milliseconds = []
for website in websites:
    millisecond = round(ping(website, timeout=10) * 1000)
    milliseconds.append(millisecond)

FILENAME = "websites.csv"
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    for pair in (zip(websites, milliseconds)):
        writer.writerow(pair)