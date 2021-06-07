import random


def replacement_space(text):
    result = '%20'.join(text.split(' '))
    return result


def get_stiker_afte_scrining():
    stiker = ('CAACAgIAAxkBAAEBBGJgV6Y9EGqNzXQpj05iRCHGJxchjAACgQADO2AkFMiOHFrXze0mHgQ',
              'CAACAgIAAxkBAAEBBGVgV6ZDsxUy543YFCC_ky_8M22EywACTAMAAvPjvgurG4z64FjwsR4E',
              'CAACAgIAAxkBAAEBBGhgV6ZKOV3UHWNW77lqAAHV6uX8B94AAlEDAALz474LXbwOtwABxQjoHgQ',
              'CAACAgIAAxkBAAEBBGtgV6ZtA5FqOo_9c7RfCwLC1Y8XmAACfAMAAm2wQgMDz1WRVs9wTB4E',
              'CAACAgIAAxkBAAEBBG5gV6aFkTWYKILQ9cNToWLB42S4kgACFAADTlzSKXkxDTEpx2NDHgQ',
              'CAACAgIAAxkBAAEBBHFgV6aWJY_xb3fZ61XC-XZtDzUjbAACJAEAAjDUnRGjRHcouiC8Hh4E',
              'CAACAgIAAxkBAAEBBHRgV6ajt-kQdUHlNRVcPTxKn-GLuQACbwADpsrIDFLE6St_zL2jHgQ',
              'CAACAgIAAxkBAAEBBHpgV6bQ5ovEhTszrT6ekMhwpYOS8AACmgcAAkb7rARJ7b3-ZNx9eh4E',
              'CAACAgIAAxkBAAEBBH1gV6bgD4OEAmiiurLpO9jMQpq6VQACNgMAArVx2gYg7pUj85BANh4E',
              'CAACAgIAAxkBAAEBBIBgV6byYPrKjLEsskVJ81e4_Us9IQACKAMAArVx2gaQekqHXpVKbh4E',
              'CAACAgIAAxkBAAEBBINgV6cTe523CWKe4O43wD5HmAxhwwAC5wcAApb6EgW7Igl1gUuAFx4E',)
    get_stiker = random.choice(stiker)
    return get_stiker