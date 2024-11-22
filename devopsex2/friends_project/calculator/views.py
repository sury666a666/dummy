from django.shortcuts import render # type: ignore

def calculator(request):
    display = ""
    result = None

    if request.method == "POST":
        button = request.POST.get('button')
        display = request.POST.get('display', '')

        if button == "C":
            display = ""
        elif button == "=":
            try:
                result = eval(display)
                display = str(result)
            except Exception as e:
                display = "Error"
                result = None
        else:
            display += button

    return render(request, 'calculator/calculator.html', {'display': display, 'result': result})
