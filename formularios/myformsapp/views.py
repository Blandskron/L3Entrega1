from django.shortcuts import render, redirect
from .forms import MyForm

def nueva_pagina(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_pagina')
    else:
        form = MyForm()
    return render(request, 'myformsapp/nueva_pagina.html', {'form': form})
