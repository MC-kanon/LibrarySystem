from django.shortcuts import render,redirect
from bookapp import models
from django import forms
# Create your views here.
def book_list(request):
    '''书籍列表'''
    book_query = models.Book.objects.all()
    return render(request,'book_list.html',locals())

class MyForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Book
    # 添加bootstrap样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有插件，添加属性form-control
        for name, field in self.fields.items():
            # if name == "password":
            #     continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def book_add(request):
    '''增加书籍'''
    if request.method == 'GET':
        form = MyForm()
        return render(request,'book_add.html',locals())
    else:
        # 用form表单验证并且保存到数据库中
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/list/')
        else:
            return render(request,'book_add.html')

def book_delete(request):
    '''删除书籍'''
    nid = request.GET.get("nid")
    models.Book.objects.filter(pk=nid).delete()
    return redirect('/book/list/')

def book_search(request):
    '''查找书籍'''
    search_data = request.POST.get("search_data","")
    print(search_data)
    if search_data is None:
        return redirect('/book/list')
    else:
        book_query = models.Book.objects.filter(title__contains=search_data).all()
        return render(request,'book_list.html',locals())

def book_edit(request,nid):
    '''编辑书籍'''
    row_object = models.Book.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = MyForm(instance=row_object)
        return render(request,'book_edit.html',locals())
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/list/')
        else:
            return render(request,'book_edit.html')