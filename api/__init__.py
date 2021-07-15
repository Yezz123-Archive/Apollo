#!/usr/bin/python3
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
import bcrypt
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64