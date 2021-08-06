import os

import connexion

basedir = os.path.abspath(os.path.dirname(__file__))

app = connexion.App(__name__, specification_dir=basedir)
