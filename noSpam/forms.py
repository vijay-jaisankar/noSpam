from django import forms

class PredictForm(forms.Form) :
    message = forms.CharField(
                                widget=forms.Textarea(
                                    attrs={
                                        "class" :"new-class-name two",
                                        "id" : "textarea",
                                        "name" : "textarea", 
                                        "rows" : 8,
                                        "cols" : 40, 
                                        "placeholder" : "Enter your sms here", 
                                    }
                                )
    )