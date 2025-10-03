from django.shortcuts import render

# Create your views here.

def index(request):
    animes = [
        {"titulo": "Attack on Titan", "genero": "Acción, Fantasía Oscura", "calificacion": 9.1, "imagen_url": "https://media.revistagq.com/photos/6061de8b7e6648d674c91a59/master/pass/attack%20on%20titan.jpeg"},
        {"titulo": "Demon Slayer", "genero": "Acción, Aventura, Fantasía", "calificacion": 8.7, "imagen_url": "https://palomaynacho.com/wp-content/uploads/2024/06/Demon-Slayer-trilogia.jpg"},
        {"titulo": "Jujutsu Kaisen", "genero": "Acción, Sobrenatural, Oscuro", "calificacion": 8.7, "imagen_url": "https://p325k7wa.twic.pics/high/jujutsu-kaisen/jujutsu-kaisen-cursed-clash/00-page-setup/JJK-header-mobile2.jpg?twic=v1/resize=760/step=10/quality=80"}
    ]
    context = {
        'series': animes # Mantenemos el nombre 'series' en el contexto para no cambiar el HTML
    }
    return render(request, 'index.html', context)