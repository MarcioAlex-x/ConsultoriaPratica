from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import RevistaAvon, RevistaCasaEstilo, RevistaConsultor, RevistaEspaco, Combo, Banner

def download_revista_consultoria(request, id):
    revista = get_object_or_404(RevistaConsultor, id=id)
    file_path = revista.revista.path
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{revista.revista.name}"'
        return response

def download_revista_espaco(request, id):
    revista = get_object_or_404(RevistaEspaco, id=id)
    file_path = revista.revista.path
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{revista.revista.name}"'
        return response

def download_revista_avon(request, id):
    revista = get_object_or_404(RevistaAvon, id=id)
    file_path = revista.revista.path
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{revista.revista.name}"'
        return response

def download_revista_estilo(request, id):
    revista = get_object_or_404(RevistaCasaEstilo, id=id)
    file_path = revista.revista.path
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{revista.revista.name}"'
        return response


def download_imagem_combo(request, id):
    combo = get_object_or_404(Combo, id=id)
    file_path = combo.imagemCombo.path
    with open(file_path, 'rb') as img_file:
        response = HttpResponse(img_file.read(), content_type='image/*')
        response['Content-Disposition'] = f'attachment; filename="{combo.imagemCombo.name}"'
        return response

def index(request):
    revistaConsultoria = RevistaConsultor.objects.all()
    revistaAvon = RevistaAvon.objects.all()
    revistaCasaEstilo = RevistaCasaEstilo.objects.all()
    revistaEspaco = RevistaEspaco.objects.all()
    combo = Combo.objects.all()
    banner = Banner.objects.all()

    return render(request, 'index.html',{'avon':revistaAvon,
                                        'estilo':revistaCasaEstilo,
                                        'consultoria':revistaConsultoria,
                                        'espaco':revistaEspaco,
                                        'combo':combo,
                                        'banner':banner})


