from django import forms

from . models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')
        
        widgets ={
            'category':forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
             'category':forms.TextInput(attrs={
            'class': INPUT_CLASSES
             }),
              'category':forms.Textarea(attrs={
            'class': INPUT_CLASSES
              }),
               'category':forms.TextInput(attrs={
            'class': INPUT_CLASSES
               }),
                'category':forms.FileInput(attrs={
            'class': INPUT_CLASSES}),
                                     
            }