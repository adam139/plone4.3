from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
#from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from my315ok.products import MessageFactory as _

image_size=[
('thumb','thumb image',_(u'thumb image')),
('mini','mini image',_(u'mini image')),
('preview','preview image',_(u'preview image')),
('large','large image',_(u'large image')),
('original','original',_(u'original image')),
  ]
image_size_terms = [
    SimpleTerm(value, token, title) for value, token, title in image_size
]


class ImageSizeVocabulary(object):
    """ Ad Unit sizes """

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary(image_size_terms)
    
ImageSizeVocabularyFactory = ImageSizeVocabulary()
