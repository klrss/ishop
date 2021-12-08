from django.views.generic import ListView, DetailView
from django.shortcuts import render #, get_object_or_404

# Create your views here.
from .models import Product, ProductCategory


#create a function to make a query of product
def product_list_view(request):
	qs = Product.objects.all()
	return render(request, 'list.html', {'object_list':qs})


def product_detail_view(request, slug):
	qs = Product.objects.get(slug=slug)
	return render(request,'detail.html', {'obj_detail':qs})



#class ProductDetailSlugView(DetailView):
#	qs = Product.objects.all()
#
#	def get_object(self,*args,**kwargs):
#		request =self.request
#		slug = self.kwargs.get('slug')
#		#instance = get_object_or_404(Product,slug=slug, active =True)
#		try:
#			instance = Product.objects.get(slug=slug, active=True)
#		except Product.DoesNotExist:
#			raise Http404('Not found')
#		except Product.MultipleObiectsReturned:
#			qs = Product.objects.filter(slug=slug, active=True)
#			instance = qs.first()
#		except:
#			raise Http404('Not found...')
#		return instance


