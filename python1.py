
from flask import Flask, session, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash

start1 = (__name__)
start1.secret_key = "hello152carbaro"

@start1.route("/", methods = ["GET", "POST"])
def first1():
    














