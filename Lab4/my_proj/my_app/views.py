from django.views import View
from django.shortcuts import render
from . import my_functions
from . import my_objects

class HomePageView(View):
    # This makes fix_name a static method, meaning it can be called without an instance of the class.
    @staticmethod
    def fix_name(name: str):
        return name.title()
    
    def get(self, request):
        orig_name = "sTONE"
        # Since fix_name is now a static method, it should be called on the class itself.
        name = HomePageView.fix_name(orig_name)

        names = ['LoUie','GabBy','MaRion']

        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.Car(make="Ford",year="2018",model='F-150',color="white",sound="beep beep beep")
        car2 = my_objects.Car(make="Subaru",year="2021",model='Outback',color="orange",sound="hoooooooonk honk")
        motorcycle1 = my_objects.Motorcycle(make="Yamaha",year="2014",model="201-IX",color="black",sound="vroom vroom")

        context = {
            'hi': 'hello world!',
            'name': name,
            'orig_name': orig_name,
            'names' : names,
            'fixed_names' : fixed_names,
            'car1' : car1,
            'car2' : car2,
            'motorcycle1' : motorcycle1
        }
        # Use the relative path from within the templates directory.
        # Ensure that 'my_app' is the name of your Django app and 'index.html' is located
        # at 'my_app/templates/my_app/index.html'.
        return render(request, 'my_app/index.html', context)
    