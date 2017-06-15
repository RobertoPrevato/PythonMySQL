#!/usr/bin/env bash

# To generate classes from existing db:
# 1. install sqlacodegen in Python environment;
# env/bin/pip install sqlacodegen

# 2. use following command (replacing parameters as appropriate)
env/bin/sqlacodegen mysql+pymysql://USERNAME:PASSWORD@IP_ADDRESS_OF_MYSQL_SERVER:3306/DATABASE_NAME > entities.py

# 3. for more information on sqlacodegen, see: https://pypi.python.org/pypi/sqlacodegen