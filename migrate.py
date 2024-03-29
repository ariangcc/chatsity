#!/usr/bin/env python

"""
      migrate.py
      ----------
      This module contains declarations to handle database migrations.
"""

__author__ = "Arian Gallardo"

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db
from run import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()