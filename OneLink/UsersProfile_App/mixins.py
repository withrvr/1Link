from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


class Custom_LoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.WARNING,
                'URL which you are trying to access, <b>Required Login</b>,<br>'
                'So Login and You will redirected to URL Which you are trying to access again'
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
