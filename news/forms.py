from django import forms
from .models import Article


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label = 'First Name', max_length = 30)
    email = forms.EmailField(label = 'Email')
    
    
    
class NewArticleForm(forms.ModelForm):
    class Meta: # defines what model we are defining the form from
        model = Article
        exclude = ['editor', 'pub_date'] # define what fields we do not want to create from the model
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), # checkbox widget that allows a user to check which tags to add
        }