from django import forms
from .models import Post,Comment

class PostEditForm(forms.ModelForm):

    title= forms.CharField(label="",widget= forms.TextInput(attrs={'id':'pe-title'}))
    description= forms.CharField(label="",widget= forms.TextInput(attrs={'id':'pe-description'}))
    post_image= forms.CharField(label="",widget= forms.ClearableFileInput(attrs={'id':'pe-img'}))
    content = forms.CharField(label="",widget = forms.Textarea(attrs={'id':'pe-content'}))
    class Meta:
        model = Post
        fields = ['title','description','post_image','content']

class  PostCreateForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'id':'pc-title','placeholder':' Enter an awesome title','size':'80',}))
    description = forms.CharField(label="",widget=forms.TextInput(attrs={'id':'pc-description','placeholder':' Short description of the post','size':'80'}))
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'id':'pc-content','placeholder':' Write something here....','size':'100','cols':100,'row':60}))
    post_image = forms.ImageField(label="Post an image",widget=forms.ClearableFileInput(attrs={'id':'pc-img'}))
    class Meta:
        model = Post
        fields = ['title','description','post_image','content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget = forms.TextInput(attrs={'class':'form-control','id':'comment-field','placeholder':'Comment here!!','rows':'3','cols':'40'}))
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['content'].label = ""
