from django.shortcuts import render



def catalog(request):
    context = {
        'title': 'Каталог Товаров',
    }
        
    
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')