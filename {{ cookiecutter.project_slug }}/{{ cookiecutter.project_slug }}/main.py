from {{ cookiecutter.project_slug }}.app import App


def main():
    app = App()
    app.loop()


if __name__ == "__main__":
    main()
