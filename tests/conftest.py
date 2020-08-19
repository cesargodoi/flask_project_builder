import pytest

from flask_project_builder.app import create_app


@pytest.fixture(scope='module')
def app():
    '''Instance of main flask app'''
    return create_app()