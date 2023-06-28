from django import forms
from django.forms import ValidationError


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})
    

def solo_numeros(value):
    if any(int.isint() for int in value):
        raise ValidationError('El telefono solo debe contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})  
    
class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre', 
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'})
        )
    apellido = forms.CharField(
        label='Apellido', 
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'})
        )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        error_messages={
                'required': 'Por favor completa el campo'
                },
        widget=forms.TextInput(attrs={'class':'form-control','type':'email'})
    )

    # telefono = forms.EmailField(
    #     abel='Tel/Cel',
    #     max_length=100,
    #     validators=(solo_numeros,),
    #     error_messages={
    #         'required': 'Por favor completa el campo'
    #         },
    #     widget=forms.TextInput(attrs={'class':'form-control','type':'Solo numeros'})
    # )
   
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)



  