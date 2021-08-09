import airtable
def getairdata():
    aird=airtable.Airtable('appTrXBmiYXmKyLLj','bot','keybPU0bpOGwuAwRA')
    at1=aird.get_all(view='anstable', maxRecords=20)
    print()
    return at1

# airo2=list(airdata.getairdata())
# >>> airo2[0].get('fields').get('ответ')
# 'Здравствуйте!'
# >>> airo2[0].get('fields').get('вопрос')
# 'привет'