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

auth0_config =  {
    'AUTH0_DOMAIN' : 'gnsd.eu.auth0.com',
    'ALGORITHMS' : ['RS256'],
    'API_AUDIENCE' : 'RecipesAPI'
}

bearer_tokens = {
    'cook': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA0NjQ2Nzc4MTc2NDQ4MzE3OTIyIiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4Mjc0ODUzNywiZXhwIjoxNTgyODM0OTM2LCJhenAiOiJPOXo0RkJ5U1dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2F0ZWdvcnkiLCJnZXQ6cmVjaXBlIl19.dMdwgRgicsbRepGSZnpL5bEkME2FJeU9elSBxcTAXUStyuQJHcWYVgP8A_3sonh9ywfiGRJnytE4dps_PQwqOMo8rlsBKRezrN4BzFmFtFpNGsIri_j3sCg6-0lvu58PCH45GgQjAyo3wLXDrQrvBALWENkEZhVnUM79tYSxMp-7Q5xlDFwXuga2E89vXE8cG8Rvnccf-5SRj-ttwLH7OwoGegVZAAhPrtz5p_jgrG__YyktofIfzh-BFOcV1qN13X6Po5QkXqQsDWQLc6T_7Za5he_qn2jwf-Vh0xqn8A0rmxpZwai8grp5Gq_CbbJjZsgvqFIq_sG0caKycycleQ",
    'chef': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzMjE4MDA0MjE0OTE4ODk1ODU3IiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4Mjc0Nzg3MiwiZXhwIjoxNTgyODM0MjcxLCJhenAiOiJPOXo0RkJ5U1dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cmVjaXBlIiwiZ2V0OmNhdGVnb3J5IiwiZ2V0OnJlY2lwZSIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6cmVjaXBlIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cmVjaXBlIl19.DG_Yv7jdG2hUL9QqtG6srwAAGOEL24eIgqN73yjCL1nsr7jaZe1RkxiSlT-G7ZuEFXPyzruO2urzpd-cEr44E834VxtwaVGYWk8styq8jo7QesKqaVoQcGouUX4TufS7tUlkRZ0x164ntabqQHfmWBSCDcQKidYiJviub7e8X6hFhm4l13yYeIUu4TPt0aWOcufsUcmJJ3dr5t_XCTDLBhrA0DRAQQAc9RbDmjIwBVbaanWRZYmEDF4ezAlQkvklsMOzvYsizFQIUrR45iZ1INvBV5aAtDiuiq5FzvE42AucCgBzowG7Ln6-QGVUdNrR2AP-B-E6cbYw15t7_ODeUg"
}

