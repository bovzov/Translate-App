from django.shortcuts import render
from googletrans import Translator

def homeView(request):
    translator = Translator()
    if request.method == 'POST':
        text = request.POST.get('inputText', '')
        language = request.POST.get('target_language', 'en')
        
        if text.strip() == "":
            return render(request, 'home.html', {'translation': "Iltimos, tarjima qilish uchun matn kiriting."})

        try:
            translation = translator.translate(text, dest=language)
            # Qo'shimcha tekshiruv
            if translation:
                translated_text = translation.text
            else:
                translated_text = "Tarjima xizmati hozirda mavjud emas. Keyinroq qayta urinib ko‘ring."
        except AttributeError:
            translated_text = "Tarjima xizmati hozirda mavjud emas. Keyinroq qayta urinib ko‘ring."
        except Exception as e:
            translated_text = f"Xato yuz berdi: {str(e)}"

        return render(request, 'home.html', {'translation': translated_text})
    else:
        return render(request, 'home.html')
