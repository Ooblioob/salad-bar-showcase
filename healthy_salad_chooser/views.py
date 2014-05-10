from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from healthy_salad_chooser.models import Ingredient
from django.views import generic
from healthy_salad_chooser.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from braces import views

# Create your views here.
def index(request):
	ingredient_list = Ingredient.objects.order_by('-name')
	context = {'ingredient_list': ingredient_list}

	return render(request, 'healthy_salad_chooser/index.html', context)

def about(request):
	context = {}
	return render(request, 'healthy_salad_chooser/about.html', context)

def detail(request, id):
	ingredient = get_object_or_404(Ingredient, pk=id)
	price = '%.2f' % (float(ingredient.weight_in_oz) * (7.99/16.0))
	return render(request, 'healthy_salad_chooser/detail.html', {'ingredient': ingredient, 'price': price})

class LoginView(views.AnonymousRequiredMixin,
				views.FormValidMessageMixin,
				generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('index')
	template_name = 'healthy_salad_chooser/login.html'
	form_valid_message = 'You have logged in'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)

			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)

class LogoutView(views.LoginRequiredMixin,
				views.MessageMixin,
				generic.RedirectView):
	url = reverse_lazy('index')

	def get(self, request, *args, **kwargs):
		logout(request)
		self.messages.success("You have been logged out. Come back soon!")
		return super(LogoutView, self).get(request, *args, **kwargs)	

class SignUpView(generic.CreateView,
				views.AnonymousRequiredMixin,
				views.FormValidMessageMixin):
	form_class = RegistrationForm
	model = User
	template_name = 'healthy_salad_chooser/signup.html'
	success_url = reverse_lazy('login')

	form_valid_message = "Thanks for signing up!"

	#def get_success_url(self, request, user):
	#	return reverse_lazy('index')

class ProfileView(generic.TemplateView):
	model = User
	template_name = 'healthy_salad_chooser/profile.html'
