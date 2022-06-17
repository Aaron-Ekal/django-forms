from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForm(forms.Form):
    #fields similar to forms
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #We use formhelper to specify certain attributes inside our form
        self.helper = FormHelper
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            'name', 
            'email', 
            'category', 
            'subject', 
            'body',
            Submit('submit', 'Submit', css_class='btn-primary')
        )
    
    
# class SnippetForm(forms.ModelForm):
    
#     class Meta:
#         model = Snippet
#         fields = ('name', 'body')