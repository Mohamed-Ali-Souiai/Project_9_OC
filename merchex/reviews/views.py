from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


from reviews.models import Band, Listing
from reviews.forms import ContactForm, BandForm


def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
        #return HttpResponseRedirect(reverse('band-list'))

    return render(request, 'reviews/band_delete.html', {'band': band})


def band_update(request, id):
    band = Band.objects.get(id=id)
    form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
        else:
            form = BandForm(instance=band)
    return render(request,
                  'reviews/band_update.html',
                  {'form': form})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
            #return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm()
    return render(request,
                  'reviews/band_create.html',
                  {'form': form})


def contact(request):
    # ajoutez ces instructions d'impression
    # afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-sent')  # ajoutez cette instruction de retour

    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactForm()
    return render(request,
                  'reviews/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def band_list(request):
    field_name = Band.objects.all()
    return render(request,
                  'reviews/band_list.html',
                  {'field_name': field_name})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'reviews/band_detail.html',
                  {'band': band})

