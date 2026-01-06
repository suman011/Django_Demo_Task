#!/usr/bin/env python
"""
Generate a Django secret key for production deployment.
Run: python generate_secret_key.py
"""
from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("SECRET KEY GENERATED")
    print("="*60)
    print(f"\n{secret_key}\n")
    print("="*60)
    print("\nCopy this key and use it as SECRET_KEY environment variable")
    print("="*60 + "\n")

