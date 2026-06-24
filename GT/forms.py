from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from GT.models import Usuario
from wtforms import TextAreaField


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[ DataRequired(), Email()])
    senha = PasswordField("Senha",validators=[ DataRequired(), Length(min=6, max=20)] )
    botao_confirmacao = SubmitField("Entrar")


class FormCriarConta(FlaskForm):
    username = StringField("Nome", validators=[ DataRequired(), Length(min=2, max=50) ] )
    email = StringField("E-mail", validators=[ DataRequired(), Email() ])
    senha = PasswordField("Senha", validators=[ DataRequired(),Length(min=6, max=20)] )
    cargo = SelectField("Cargo",choices=[("gerente", "Gerente"), ("funcionario", "Funcionário")],validators=[DataRequired()])
    confirmacao_senha = PasswordField("Confirmar Senha",validators=[ DataRequired(), EqualTo("senha") ])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()

        if usuario:
            raise ValidationError( "Este e-mail já está cadastrado. Use outro e-mail.")


class FormTarefa(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired()])
    descricao = TextAreaField("Descrição", validators=[DataRequired()])
    responsavel = SelectField("Responsável", coerce=int)
    botao_confirmacao = SubmitField("Criar Tarefa")


