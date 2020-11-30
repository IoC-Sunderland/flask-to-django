from django.shortcuts import render, redirect
from django.http import HttpResponse
from signup.models import Users


def test(request):
    return HttpResponse("Hello, world. You're at the test route.")


def index(request):
    # Display all records in db
    all_users = Users.objects.all()
    return render(request, 'index.html', {
        'all_users': all_users,
    })


def sign_up(request):

    if request.method == "POST":

        details = {}

        details['username'] = request.POST.get('username','')
        details['email'] = request.POST.get('email','')
        details['password'] = request.POST.get('password','')

        print(details)

        missing = list()

        for k, v in details.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render(request, "sign_up.html", {
                'missing_fields': feedback,
            })

        new_user = Users(username=details['username'],
                         email=details['email'],
                        password=details['password'])

        print(new_user)

        new_user.save()

        return redirect('/')

    return render(request, "sign_up.html")