from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Avg

from .models import Destination, TravelPlan, Review


# ================= HOME =================
def home(request):
    destinations = Destination.objects.filter(is_popular=True)[:6]
    return render(request, 'home.html', {'destinations': destinations})


def destination_list(request):
    query = request.GET.get('q')

    if query:
        destinations = Destination.objects.filter(name__icontains=query)
    else:
        destinations = Destination.objects.all()

    return render(request, 'destination_list.html', {'destinations': destinations})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})


# ================= AUTH =================
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ================= TRAVEL PLAN =================
def create_plan(request):
    if not request.user.is_authenticated:
        return redirect('login')

    destinations = Destination.objects.all()

    if request.method == "POST":
        travel_date = request.POST.get('date')
        selected = request.POST.getlist('destinations')

        plan = TravelPlan.objects.create(
            user=request.user,
            travel_date=travel_date
        )

        plan.destinations.set(selected)

        return redirect('plan_summary', pk=plan.id)

    return render(request, 'create_plan.html', {'destinations': destinations})


def plan_summary(request, pk):
    plan = get_object_or_404(TravelPlan, pk=pk)
    return render(request, 'plan_summary.html', {'plan': plan})


def my_plans(request):
    if not request.user.is_authenticated:
        return redirect('login')

    plans = TravelPlan.objects.filter(user=request.user)
    return render(request, 'my_plans.html', {'plans': plans})


# ================= REVIEW =================
def add_review(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    destination = get_object_or_404(Destination, pk=pk)

    if request.method == "POST":
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            destination=destination,
            rating=rating,
            comment=comment
        )

        return redirect('destination_detail', pk=pk)

    return render(request, 'add_review.html', {'destination': destination})


def top_destinations(request):
    destinations = Destination.objects.annotate(
        avg_rating=Avg('review__rating')
    ).order_by('-avg_rating')[:6]

    return render(request, 'top_destinations.html', {'destinations': destinations})