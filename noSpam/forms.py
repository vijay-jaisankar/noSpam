from django import forms

class PredictForm(forms.Form) :
    message = forms.CharField(
                                label='',
                                widget=forms.Textarea(
                                    attrs={
                                        "class" :"mx-auto",
                                        "id" : "textarea",
                                        "name" : "textarea", 
                                        "rows" : 10,
                                        "cols" : 50, 
                                        "placeholder" : "Enter your sms here", 

                                    }
                                )
    )
