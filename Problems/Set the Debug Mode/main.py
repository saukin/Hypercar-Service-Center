IS_RELEASE_SERVER = input().lower()
if IS_RELEASE_SERVER == "false":
    IS_RELEASE_SERVER = False
else:
    IS_RELEASE_SERVER = True
DEBUG = not bool(IS_RELEASE_SERVER)

