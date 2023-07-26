from django.contrib import admin
from core.models.firm_model import Firm
from core.models.assets_model import Assets
from core.models.funds_models import Funds


admin.site.register(Firm)
admin.site.register(Assets)
admin.site.register(Funds)
