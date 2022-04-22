from django import forms
# the class is going to inherit form from forms

class TodoListForm(forms.Form):
# adding a text input widget
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' :'Enter your Task e.g Transfer Money to Pratik', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))
