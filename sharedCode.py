
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ajouter l'utilisateur à un groupe par défaut
            group = Group.objects.get(name='agent')  # ou 'manager'
            user.groups.add(group)
            login(request, user)
            return redirect('dashboard')  # redirige vers une page protégée
    else:
        form = RegisterForm()
    return render(request, 'authcnss/register.html', {'form': form})
