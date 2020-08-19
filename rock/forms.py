from django import forms
from django.core.files.storage import default_storage as storage
from .models import *

class Sport_Location_Form(forms.ModelForm):
    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    class Meta:
        model = Location
        fields = ["sport_location_img"]
        #exclude = ('rocker', 'location')

def save(self):
    user = super(UploadImageForm, self).save()
    x = self.cleaned_data.get('x')
    y = self.cleaned_data.get('y')
    w = self.cleaned_data.get('width')
    h = self.cleaned_data.get('height')

    image = Image.open(user.primaryphoto)
    cropped_image = image.crop((x, y, w + x, h + y))
    resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)

    filename = os.path.splitext(resized_image.name)[0]

    output = StringIO()
    resized_image.save(output, format='JPEG', quality=95)
    output.seek(0) #Change the stream position to the given byte offset.


    new_image = InMemoryUploadedFile(output,'ImageField',\
        "%s.jpg" % filename , 'image/jpeg', output.__sizeof__(), None)

    user.primaryphoto = new_image
    user.save()

    return user
