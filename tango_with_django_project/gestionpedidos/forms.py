from django import forms
from gestionpedidos.models import Pedido, Cliente

class ClienteForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Introduzca el nombre del cliente")
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Cliente
        fields = ('name',)


class PedidoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Introduzca el nombre del producto")
    url = forms.URLField(max_length=200, help_text="Introduzca la URL del producto")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    fechaPedido = forms.CharField(max_length=128, help_text="Introduzca la fecha del pedido")
    precio = forms.CharField(max_length=128, help_text="Introduzca el precio del producto")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pedido

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the cliente field from the form,
        exclude = ('cliente',)
        #or specify the fields to include (i.e. not include the cliente field)
        #fields = ('title', 'url', 'views')

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')

    #     # If url is not empty and doesn't start with 'http://', prepend 'http://'.
    #     if url and not url.startswith('http://'):
    #         url = 'http://' + url
    #         cleaned_data['url'] = url

    #     return cleaned_data