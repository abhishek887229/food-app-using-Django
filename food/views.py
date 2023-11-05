from django.shortcuts import render,redirect
from .models import Item
from django.http import HttpResponse
from .forms import ItemForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):

    
    return render(request, 'food/base.html') 

def index(request):
    x=Item.objects.all()
    return render(request,'food/index.html',{'val':x})

def detail(request,item_id,item_name):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/deailed.html',context)

@login_required
def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index_page')

    return render(request,'food/item_form.html',{'form':form})

class CreateItem(CreateView):
    model=Item;
    fields=['item_name','item_des','item_price','item_image']
    template_name='food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user

        return super().form_valid(form)
    
@login_required
def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index_page')

    return render(request,'food/item_form.html',{'form':form,'item':item,})

@login_required
def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index_page')

    return render(request,'food/delete_item.html',{'item':item,})

