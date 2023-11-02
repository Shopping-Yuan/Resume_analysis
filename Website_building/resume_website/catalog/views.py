from django.shortcuts import redirect, render

# Create your views here.
#from django.http import HttpResponse, HttpResponseRedirect
from .models import all_card,CardForm
def my_index(request):
    cards = all_card.objects.all()
    columns = {
        "content" : cards
 }
    return  render(request, 'index.html', context=columns)

def add_data(request):
    print(request.method)
    if request.method == 'POST':
        new_card = CardForm(request.POST)
        if new_card.is_valid():
            new_card.save()
        return redirect('index_url')
    content ={'form':CardForm()}
    return  render(request, 'add_data.html',content)
def renew_data(request):
    content = {}
    if request.method == 'POST':
        if request.POST.get("action") == "search":
            s_id = request.POST['search_id']
            try :
                renew_card = all_card.objects.get(card_ID=s_id)
                content["old_card"] = renew_card
            except:
                return redirect('renew_data_url')
        if request.POST.get("action") == "renew":
                print(request.method)
                new_card = all_card.objects.get(card_ID=request.POST.get("new_ID"))
                new_card.card_name = request.POST.get("new_name")
                new_card.card_type = request.POST.get("new_type")
                new_card.save()
                content['card'] = new_card
    return  render(request, 'renew_data.html',content)
def search(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)