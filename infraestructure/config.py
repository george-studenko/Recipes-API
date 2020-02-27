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


environments = dict(
    dev=Development_Config,
    test=Test_Config
)

auth0_config = {
    'AUTH0_DOMAIN': 'gnsd.eu.auth0.com',
    'ALGORITHMS': ['RS256'],
    'API_AUDIENCE': 'RecipesAPI'
}

bearer_tokens = {
    'cook': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3pRemMyTX"
            "pORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZDUWtKRk1qRkVRZyJ9."
            "eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2"
            "dsZS1vYXV0aDJ8MTA0NjQ2"
            "Nzc4MTc2NDQ4MzE3OTIyIiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL"
            "2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdC"
            "I6MTU4Mjc0ODUzNywiZXhwIjoxNTgyODM0OTM2LCJhenAiOiJPOXo0RkJ5U1"
            "dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoi"
            "b3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2"
            "F0ZWdvcnkiLCJnZXQ6cmVjaXBlIl19.dMdwgRgicsbRepGSZ"
            "npL5bEkME2FJeU9elSBxcTAXUStyuQJHcWYVgP8A_3sonh9ywfiGRJnytE4dp"
            "s_PQwqOMo8rlsBKRezrN4BzFmFtFpNGsIri_j3sCg6-0l"
            "vu58PCH45GgQjAyo3wLXDrQrvBALWENkEZhVnUM79tYSxMp-7Q5xlDFwXug"
            "a2E89vXE8cG8Rvnccf-5SRj-ttwLH7OwoGegVZAAhPrtz5p"
            "_jgrG__YyktofIfzh-BFOcV1qN13X6Po5QkXqQsDWQLc6T_7Za5he_qn2j"
            "wf-Vh0xqn8A0rmxpZwai8grp5Gq_CbbJjZsgvqFIq_sG0caK"
            "ycycleQ",
    'chef': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3"
            "pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZE"
            "dSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZX"
            "UuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzMj"
            "E4MDA0MjE0OTE4ODk1ODU3IiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJo"
            "dHRwczovL2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sIml"
            "hdCI6MTU4Mjc1MjQzNCwiZXhwIjoxNTgyODM4ODMzLCJhenAiOiJPO"
            "Xo0RkJ5U1dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3Bl"
            "Ijoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6"
            "WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cmVjaXBlIiwiZ2V0O"
            "mNhdGVnb3J5IiwiZ2V0OnJlY2lwZSIsInBhdGNoOmNhdGVnb3J5Ii"
            "wicGF0Y2g6cmVjaXBlIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cmV"
            "jaXBlIiwicG9zdDp1c2VyIl19.z5GZXYJeF0h9b0bfQ7L4ZlnHiaW"
            "-CyfB328ou4LfyYr7egIIzCUsRU2jBcoqC7sdwnx-hEBSgwbCx1L"
            "40sgnvgS6VeonmaqfKbbxTU2YbHYs0_TPejpHag2N2CC0cy-tDgy"
            "mug4o2ips8bOBoWiInRzBHIwHUlBG78nMKBt-qMtSnSLyNBeqi9Zu"
            "6Kag_ha0uBCfDbpsyWzFid7uE_RP4AlgpkEdyJW-9o7OaB3RjcI0t"
            "InQMsier9gMur8WQt9QZ2Bk_rWJtITMte-WoFXhwOqC1ZN0oZS4Ui"
            "V3j5k5bzcmzYksttOMoqUOqa56RD_OoS3Hd1Br8_E6yL9Ufya60Q"
}
