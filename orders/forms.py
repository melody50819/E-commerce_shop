from django import forms

from orders.models import Order


class ShopcarForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('products',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #有指定instance的情況
        if self.instance:
            #編輯:取得產品的product欄位 替換成 目前訂單有的所有產品
            self.fields['products'].queryset = self.instance.products.all() 