#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trydjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


<appSettings>
    <!-- Required settings -->
    <add key="WSGI_HANDLER" value="django.core.wsgi.get_wsgi_application()" />
    <!-- Your django path -->
    <add key="PYTHONPATH" value="C:\inetpub\wwwroot\demodjango" /> 
    <!-- Your djangoname.settings -->
    <add key="DJANGO_SETTINGS_MODULE" value="demodjango.settings" />
  </appSettings>
https://onedrive.live.com/view?id=19E5441D50B45978!3215&resid=19E5441D50B45978!3215&authkey=!Annt_9dp_hEBwZI&wd=target(Business%20Plan.one|ddbea5a7-cc37-2643-af32-0b65b23799ea/Phishing%20Pattern%20Immediate%20Action%20Required%20Update%20Your%20Account%20Information|c7f7b7c2-09f5-4612-87bf-9287033e4c65/)&wdorigin=NavigationUrl&wdo=2&cid=19e5441d50b45978
