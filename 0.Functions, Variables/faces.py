def main():
    texts = input()
    faces = convert(texts)
    print(faces)


def convert(emoctions):
    emoji = emoctions.replace(":)", "🙂").replace(":(", "🙁")
    return emoji


main()