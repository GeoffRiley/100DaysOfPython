import demiurge


###
# THIS DOES NOT WORK… Probably needs to run scripts on the imdb page before these elements
# get loaded.
###
class Itch(demiurge.Item):
    img = demiurge.AttributeValueField(selector='div.ninja_image img.pri_image', attr='src')
    celeb = demiurge.AttributeValueField(selector='div.ninja_image img.pri_image', attr='title')
    age = demiurge.TextField(selector='div.ninja_image div.widget_caption div.primary(2)')

    class Meta:
        selector = 'div.ab_borntoday div.widget_content'
        base_url = 'https://www.imdb.com/'


i = Itch.all()
