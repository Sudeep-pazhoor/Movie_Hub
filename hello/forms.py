from django import forms

from hello.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("name", "image_url", "rating", "release_date", "youtube_trailer", "is_favorite")
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "rating": forms.NumberInput(attrs={"step": "0.1", "min": "0", "max": "10"}),
        }
