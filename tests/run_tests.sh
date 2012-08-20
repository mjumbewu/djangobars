#!/bin/sh

THIS_DIR=`dirname $0`
export PYTHONPATH=$THIS_DIR:$THIS_DIR/..:$PYTHONPATH

# Make sure things work with template-generic settings
django-admin.py test project --settings=project.settings $@

# Make sure things work with handlebars-specific settings
django-admin.py test project --settings=project.settings_handlebars $@

# Make sure default settings are reasonable
django-admin.py test project --settings=project.settings_defaults $@
