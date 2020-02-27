import os


class Config:
    DEBUG = False


class Development_Config(Config):
    database_name = 'recipesDB'
    database_host = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = 'postgres://{}/{}'.format(
        database_host, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class Test_Config(Config):
    database_name = 'recipesTestDB'
    database_host = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = 'postgres://{}/{}'.format(
        database_host, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True


class Heroku_Config(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class Heroku_Test_Config(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_BRONZE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


environments = dict(
    dev=Development_Config,
    test=Test_Config,
    heroku=Heroku_Config,
    heroku_test=Heroku_Test_Config
)

auth0_config = {
    'AUTH0_DOMAIN': 'gnsd.eu.auth0.com',
    'ALGORITHMS': ['RS256'],
    'API_AUDIENCE': 'RecipesAPI'
}

bearer_tokens = {
    'cook': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1q"
            "Z3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZ"
            "DUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0a"
            "DAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA0NjQ2Nzc4MTc2"
            "NDQ4MzE3OTIyIiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL2d"
            "uc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4Mjg0Mj"
            "g3NCwiZXhwIjoxNTgyOTI5MjczLCJhenAiOiJPOXo0RkJ5U1dQNzJt"
            "dGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2"
            "ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2F0ZWdvcnk"
            "iLCJnZXQ6cmVjaXBlIl19.ChjQEG-vGHvkFd0NUayC2QhK7JkD0P"
            "EZOFacCsz3l0vCSLvmWvCi9NPPT32yqTAOK9ji0i4RxD8G6zG7dDg"
            "fP7vN10IB3U1Z9Cm3Lx4L2c0xOoxmQhKqEgkt2UfdHLNz3BwNOZVx"
            "KlrE-wvYiXW4vkIjUHFbwUggKwD79TM3lQ7J2Ixc6KYYdgh43qW"
            "rap2H6w2iiQ0HkcbRm1yZ61yZ8V_q68RPpVZQJovbD1-F9jugE0D"
            "YyiPzZ4aLuYqKvXvbdYXJSBEThi9CDxyVa-H1nZFM-gJ-yIhDUq"
            "CW4NiHIRQqVC7GeOgIePXf1aNDTxs-FNidYH3PfSImFCj_9TsnhA",

    'chef': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZC"
            "I6Ik1qZ3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTB"
            "Jek5EZEdSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczo"
            "vL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1"
            "vYXV0aDJ8MTEzMjE4MDA0MjE0OTE4ODk1ODU3IiwiYXVkIjp"
            "bIlJlY2lwZXNBUEkiLCJodHRwczovL2duc2QuZXUuYXV0aDAu"
            "Y29tL3VzZXJpbmZvIl0sImlhdCI6MTU4MjgzODQ3NywiZXhwIj"
            "oxNTgyOTI0ODc2LCJhenAiOiJPOXo0RkJ5U1dQNzJtdGNnejB"
            "mNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2Zp"
            "bGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0Z"
            "WdvcnkiLCJkZWxldGU6cmVjaXBlIiwiZ2V0OmNhdGVnb3J5Ii"
            "wiZ2V0OnJlY2lwZSIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g"
            "6cmVjaXBlIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cmVjaXBl"
            "IiwicG9zdDp1c2VyIl19.OVZy5z_0josOoIG-cDB1CSpSPpxC"
            "2An3KCvkouA99HzaUdi_C_EfK4H-mMCb2N5tnK1aGScWRlf5B"
            "xa2yDC34YbgfalwCs72H8t4VeThEMi7LILfJMUiVckiMIGYqY"
            "psIefZ_u1KY_2NuQVnewDlxMJceXL9z2Cx-UHr4OthCXpbSkR"
            "KbbgzLfhWQ_lZYcO45qQn3HDds3JN9rr_RBgyn-VYoSfC3PCI"
            "JgXfqH-STpBh-JI4U0zskAh4vJFcdYpCo-Cpr0jpSFHSevrRl"
            "WEVZrCNROSqgLekRc7lj1wW7rIOlUEEL6mI5ugOlrTgz96zFm"
            "S38-fOb1kqHw5oMiqCaw"
}
