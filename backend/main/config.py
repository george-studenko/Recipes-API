class Config:
    DEBUG = False


class Development_Config(Config):
    database_name = 'recipesDB'
    database_host = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = 'postgres://{}/{}'.format(database_host, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class Test_Config(Config):
    database_name = 'recipesTestDB'
    database_host = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = 'postgres://{}/{}'.format(database_host, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True


environments = dict(
    dev=Development_Config,
    test=Test_Config
)



