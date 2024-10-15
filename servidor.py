# Arquivo destinado 100% para a renderização do template html das páginas

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import dotenv