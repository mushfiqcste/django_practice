from topics.models import Topics
from django.contrib import admin

'''class CustomFeatures(admin):
	def show_object_title(self):
		return self.content_object.title
	

	list_display = super(CustomFeatures, self).list_display
	list_display += (show_object_title,)
'''


admin.site.register(Topics)
