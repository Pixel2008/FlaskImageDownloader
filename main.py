#! python3
'''
Sample script for downloading all images from website
Pixel2008 All Rights Reserved ®
'''


from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
