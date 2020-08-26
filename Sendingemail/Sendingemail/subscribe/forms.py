from django import form

class Subscribe(forms.Form):
    Email = forms.EmailField()
    #first_name = forms.CharField(max_length=30)
    #last_name = forms.CharField(max_length=30)
    #subject = forms.CharField(max_length=30)
    #content = forms.TextField()

    def __str__(self):
        return self.Email