# from django.contrib.auth import get_user_model
#
# class CurrentUser:
#     def get_user(self, user_id):
#         try:
#             return get_user_model().objects.select_related('profile').prefetch_related('notices').get(pk=user_id)
#         except get_user_model().DoesNotExist:
#             return None