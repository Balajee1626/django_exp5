from django.shortcuts import render
from django.http import HttpResponse

# View to display form and set session data
def set_session(request):
    if request.method == 'POST':
        # Get user input from form
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Check if form data is valid
        if username and email:
            # Store user input in session
            request.session['username'] = username
            request.session['email'] = email
            return render(request, 'set_session.html', {'message': 'Session data set successfully!'})
        else:
            return HttpResponse("Invalid input. Please fill in both fields.")
    
    # Render form for GET request
    return render(request, 'set_session_form.html')

# View to get and display session data
def get_session(request):
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not set
    email = request.session.get('email', 'No Email')  # Default to 'No Email' if not set

    return render(request, 'get_session.html', {'username': username, 'email': email})

# View to delete session data
def delete_session(request):
    request.session.flush()  # Clear session data
    return render(request, 'delete_session.html', {'message': 'Session data cleared!'})
