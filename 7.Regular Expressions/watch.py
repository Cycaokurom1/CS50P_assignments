import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url_matches := re.search(r'src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"', s):
        if re.search(r'</iframe>$', s):
            shorter_url = 'https://youtu.be/' + url_matches.group(1)
            return shorter_url
    else:
        return None


if __name__ == "__main__":
    main()