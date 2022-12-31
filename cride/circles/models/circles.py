"""Circle model"""

#Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Circle (CRideModel):
    """Circle model.
    A  circle is a private group where rides are offered and taken
     by its members.  To join a circle  a user must receive an unique
     invitation code from an existing circle member
    """

