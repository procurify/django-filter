import django.test

# Django 4.2 renamed assertQuerysetEqual to assertQuerySetEqual, and Django
# 5.1 removed the old alias. Tests use the new name; alias it on Django < 4.2
# so the full support matrix (3.2/4.2/5.2) runs the same test code.
if not hasattr(django.test.TransactionTestCase, "assertQuerySetEqual"):
    django.test.TransactionTestCase.assertQuerySetEqual = (
        django.test.TransactionTestCase.assertQuerysetEqual
    )
