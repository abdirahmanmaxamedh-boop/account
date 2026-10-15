from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

MODULES = [
    ("Dashboard", "core", "Stage 2"),
    ("Inventory", "inventory", "Stage 3"),
    ("Sales", "sales", "Stage 4"),
    ("Purchases", "purchases", "Stage 5"),
    ("Customers", "customers", "Stage 6"),
    ("Suppliers", "suppliers", "Stage 6"),
    ("Accounting & Expenses", "accounting", "Stage 7"),
    ("Users & Roles", "users", "Stage 2"),
]


def home(request):
    return render(request, "core/home.html", {"modules": MODULES})


def health(request):
    """Simple liveness check that also verifies the database connection."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return JsonResponse({"status": "ok", "database": connection.vendor})
    except Exception:
        return JsonResponse({"status": "error", "database": "unavailable"}, status=503)
