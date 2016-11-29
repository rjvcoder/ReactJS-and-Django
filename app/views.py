from django.shortcuts import render

# Create your views here.
def index(request):
    #try:
       # my_data_list = My_data.objects.all()[:10]

        #context = {
        #    'my_data_list' : my_data_list,
        #}
    #except:
        #raise Http404("ERROR!")
    #return render(request,'polls/index1.html', context)
    return render(request,'index.html')