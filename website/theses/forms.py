from django import forms


class SimpleContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'What would you like to tell us?'})
    )


class InterestsForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Do you have anything else you would like to tell us?'})
    )

    course_and_university = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Course and University'})
    )

    deadline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'DD-MM-YYYY'}))

    find_out_website = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'How did you find out about this website?',
                                     'rows': 5})
    )

    thesis_title = forms.CharField(required=False)


class ProposalForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    organisation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Your organisation'})
    )
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Thesis title',
                                                                         'class': 'form-control'}))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Thesis description'})
    )

    why_important = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Why is it important?'})
    )

    sources = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Sources'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Is there anything else you '
                                                    'would like to inform us about?'})
    )


class CoachingForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name',
                                                                                'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Your email'}))
    university = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Course and University'})
    )

    requirements = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Any requirements we should be aware of? Do you have to use particular methodology? Do you have some budget available? Does your supervisor have some requirements (if you already have a supervisor)?',
                                     'rows': 5})
    )

    career = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Briefly describe your career plans (e.g. Do you '
                                                    'want to become top reseacher? Do you know the sector '
                                                    'or type of work that you would like to do after you graduate?)',
                                     'rows': 5})
    )

    preferences = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Do you have any strong interests and preferences regarding thesis topic?',
                                     'rows': 5})
    )

    read_above = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Please describe how knowledgeable are you in Effective Altruism and place yourself on a scale 0-5',
                                     'rows': 5})
    )

    deadline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'When is your deadline for having a topic chosen?'}))

    find_out_website = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'How did you find out about this website?',
                                     'rows': 5})
    )

    anything_else = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Anything else you would like to tell us?',
                                     'rows': 5})
    )


def get_discipline_choices():
    from theses.models import ThesisDiscipline
    discs = ThesisDiscipline.objects.all()
    return [(None, None)] + [(x.name, x.name) for x in discs]
