def total_import(request):
    total = 0
    
    if request.user.is_authenticated:
        for k, v in request.session["cart"].items():
            total = total + float(v["price"])
        
    return {"total_import": total}