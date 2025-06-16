# from django.core.management import execute_from_command_line
# import os
# import sys

# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
#     execute_from_command_line(sys.argv)

#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Online_library_project.settings')
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

