# Helper functions for encryption, hashing, and data I/O

import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes