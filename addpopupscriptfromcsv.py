import csv

def atr_change(request):
    with open('addpopup/popuplist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if (row[1]):#указать уникальное поле таблицы, по которому искать в БД
                csvslug = row[1][:-1]
                st = csvslug.split('/')
                s = st[len(st)-1]
                category = Category.objects.all()
                for el in category:
                    if el.slug == s:#тут сравнение полей
                        try:
                            article = Article.objects.get(category=el)
                            #тут указать какие поля и на что меняются
                            article.buttonurlpopup = row[0]
                            article.buttonidpopup = 'someId'
                            article.save()
                            
                        except:
                            continue
    return redirect("/moscow/", permanent=True)

urls.py

from .views import category_view, redirect_to_city, atr_change

    url(r'moscow/s/', atr_change, name="atr_change"),