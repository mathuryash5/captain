
import os
import unittest
import init_data

from flask.cli import FlaskGroup

from app import create_app, db   

app = create_app()

# creates a new FlaskGroup instance to extend the normal CLI with commands related to the Flask app
cli = FlaskGroup(create_app = create_app)

@cli.command()
def recreate_db():
	""" Initializes the database """
	db.drop_all()
	db.create_all()
	db.session.commit()

@cli.command()
def test():
	""" Runs the tests without code coverage"""
	tests = unittest.TestLoader().discover('tests')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

@cli.command()
def seed_db():
	"""Seeds the database."""
	init_data.coursebase_data()
	init_data.course_deliverable_data()
	init_data.course_resource_data()
	init_data.student_data()
	init_data.teacher_data()
	init_data.team_data()

	
if __name__ == '__main__':
	cli() 
