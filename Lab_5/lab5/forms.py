from django import forms

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=20)
    review_area = forms.MultipleChoiceField(choices=[('food','Food'),('srvc','Service'),('amb','Ambiance'),('price','Price'),('wait','Wait')], widget=forms.CheckboxSelectMultiple)

    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        if "horrible" in my_message:
            raise forms.ValidationError(f"message must not contain 'a'the message was '{my_message}'")
        
        return my_message

