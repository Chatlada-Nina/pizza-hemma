from django.shortcuts import render


def handler404(request, exception):
    """
    Handle 404 Page Not Found errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: A rendered 404 error page with a 404 status code.
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Handle 500 Internal Server Error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered 500 error page with a 500 status code.
    """
    return render(request, "errors/500.html", status=500)
