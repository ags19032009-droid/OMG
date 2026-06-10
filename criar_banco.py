from GT import database, app


with app.app_context():
    database.create_all()

print("Banco criado com sucesso!")

