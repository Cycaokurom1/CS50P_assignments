import emoji

words = input('Input: ')

emo = emoji.emojize(emoji.emojize(words), language='alias')

print('Output:', emo)