from django import forms
from .models import Story, Category


class AddStoryAdminForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'body', 'story_image', 'author', 'category')


        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }


class AddStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'body', 'story_image', 'category')


        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }


