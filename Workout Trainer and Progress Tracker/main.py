from website import create_app

app = create_app()

if __name__ == '__main__': # only if we run this file are we going to execute the next line
  app.run(debug=True)