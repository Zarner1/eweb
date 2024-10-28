from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.


def anasayfa(request):
    
    return render(request,'eweb/anasayfa.html')

@login_required(login_url="/login")
def urunadd(request):
    if request.method == "POST":
        urunid = request.POST.get("urunid")
        urunad = request.POST.get("urunad")
        uruntur = request.POST.get("uruntur")
        cinsiyet = request.POST.get("cinsiyet")
        
        urun = models.urun.objects.create(urunid=urunid, urunad=urunad,uruntur=uruntur,cinsiyet=cinsiyet)

        
        if 'images' in request.FILES:
            images = request.FILES.getlist("images")  # Birden fazla resim alındı
            for image in images:
                
                models.UrunImage.objects.create(urun=urun, image=image)  # UrunImage gibi ayrı bir model
       
        
    return render(request,'eweb/urunadd.html')

def urunlistt(request):
    all_urun = models.urun.objects.all()
    urun_dict = {"uruns":all_urun}
    return render(request,'eweb/urunler.html',context=urun_dict)   
    
@login_required
def urunsil(request,id):
    models.urun.objects.filter(id=id).delete()
    return redirect('eweb:urunlistt')

        
    

    


   













# Create your views here.
