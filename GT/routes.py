from GT import app, bcrypt, database
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user
from GT.forms import FormLogin, FormCriarConta
from GT.models import Usuario



@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    return render_template('homepage.html', form=formlogin)


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(
            nome=formcriarconta.username.data,
            email=formcriarconta.email.data,
            senha=senha,
            cargo=formcriarconta.cargo.data
        )

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', usuario=usuario.nome))


    return render_template(
        'criarconta.html',form=formcriarconta)


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template(
        'perfil.html',
        usuario=usuario
    )