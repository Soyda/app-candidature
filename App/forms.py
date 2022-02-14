from flask_wtf import FlaskForm
from numpy import integer
from wtforms import PasswordField,EmailField,SubmitField,StringField, IntegerField, FieldList, SelectField, TextAreaField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):
    """[Form to login]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")


class AddCandidacy(FlaskForm): #add_candidacy.html to modifyh
    """[Form to add candidacy]
    """
    company = StringField(label='Entreprise', validators=[DataRequired()])
    job_type = SelectField(label="Type d'emploi", choices=[('Data Scientist', 'Data Scientist'), ('Data Analyst', 'Data Analyst'), ('Data Engineer', 'Data Engineer'),('Developpeur Python','Developpeur Python'),('Data architect','Data architect'),('Autre','Autre')]) 
    description = StringField(label='Description de l\'offre')
    contact_full_name = StringField(label='Nom et prénom de votre contact', validators=[DataRequired()])
    contact_email = EmailField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Mobile du contact')
    status = SelectField(label='Statut de la candidature', choices=[('En cours', 'En Cours'), ('Accepté', 'Accepté'), ('Refusé', 'Refusé')])
    origin = SelectField(label='Origine de l\'offre', choices=[('LinkedIn','LinkedIn'), ('Indeed', 'Indeed'), ('Pole Emploi', 'Pole Emploi'),('Par un proche','Par un proche'),('Autre','Autre')])
    comment = TextAreaField(label='Commentaires')
    submit = SubmitField(label='Ajouter une candidature')

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
    """[form to modify candidacy]
    """
    job_type = SelectField(label="Type d'emploi", choices=[('Data Scientist', 'Data Scientist'), ('Data Analyst', 'Data Analyst'), ('Data Engineer', 'Data Engineer'),('Developpeur Python','Developpeur Python'),('Data architect','Data architect'),('Autre','Autre')]) 
    description = StringField(label='Description de l\'offre')
    contact_full_name = StringField(label='Contact', validators=[DataRequired()])
    contact_email = StringField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Mobile du contact')
    status = SelectField(label='Statut de la candidature', choices=[('En cours', 'En Cours'), ('Accepté', 'Accepté'), ('Refusé', 'Refusé')])
    origin = SelectField(label='Origine de l\'offre', choices=[('LinkedIn','LinkedIn'), ('Indeed', 'Indeed'), ('Pole Emploi', 'Pole Emploi'),('Par un proche','Par un proche'),('Autre','Autre')])
    comment = StringField(label='Commentaires')
    submit = SubmitField(label="Valider les modifications")

class Forgotten_pwd(FlaskForm):
    """[Form to forgotten password]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    submit = SubmitField(label="Send mail")

class Modify_pwd(FlaskForm):
    """[Form to modify password]
    """
    # email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    # current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Valider")