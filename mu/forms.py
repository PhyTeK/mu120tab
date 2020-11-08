from django import forms,utils
import time,datetime
from .models import Student,Multi

class MuForm(forms.ModelForm):
    
    i=0;
    for f in Multi.test_120:
        i = i + 1
        fname = '{}: {}x{}'.format(i,f[0],f[1])                   
        #locals()[fname]= forms.IntegerField(label_suffix='=',required=False,widget=forms.TextInput)
        locals()[fname]= forms.CharField(label_suffix='=',required=False)
        locals()[fname].widget.attrs.update(size='5',max_length=3)

        del locals()[fname]
        
        
    class Meta:
        model = Multi
        fields = []
        i=0
        labels = {}
        widgets = {}
        for f in model.test_120:
            i = i+1
            fname = '{}: {}x{}'.format(i,f[0],f[1])                   
            fields.append(fname)
            labels[fname] = '{}x{}'.format(f[0],f[1])
            widgets[fname] = forms.TextInput(attrs={'style': 'width: 50px'})

            

        print(labels)
            


        
class StudForm(forms.Form):
    tid = time.localtime()
    name = forms.CharField(label_suffix='',required=True)
    time = forms.CharField(disabled=True,required=False,label_suffix='', initial='{}:{}'.format(tid.tm_hour+1,tid.tm_min))
    date = forms.DateField(initial=datetime.date.today,label_suffix='',disabled=True,required=False)

    studid = forms.IntegerField(label_suffix='',required=False)
    studid.widget.attrs.update(disabled=True,required=False)

    class Meta:
        model = Student
        fields = ['name','date','time']


        help_texts = {
            'name' : 'Skriv ditt namn här.',
            'time' : None,
            'date' : None
         }

class ResForm(forms.ModelForm):
    tid = time.localtime()
    name = forms.CharField(label_suffix='',required=False)
    time = forms.CharField(disabled=True,required=False,label_suffix='', initial='{}:{}'.format(tid.tm_hour+1,tid.tm_min))
    date = forms.DateField(initial=datetime.date.today,label_suffix='',disabled=True,required=False)

    
    
