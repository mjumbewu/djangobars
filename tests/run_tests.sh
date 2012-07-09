#!/bin/sh

THIS_DIR=`dirname $0`
export PYTHONPATH=$THIS_DIR:$THIS_DIR/..:$PYTHONPATH

django-admin.py test project --settings=project.settings
