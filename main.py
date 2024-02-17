if __name__ == ("__main__"):
    with open ("app.py", "r") as file:
        code=file.read()
    exec(code)