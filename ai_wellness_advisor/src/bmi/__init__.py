# This file makes 'bmi' a sub-package of 'src'.
from .bmi_calculate import calculate_bmi
from .bmi_categorize import categorize_bmi

__all__ = ['calculate_bmi', 'categorize_bmi']