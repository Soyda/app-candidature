from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd 
import json 
import plotly
import plotly.express as px





@app.route('/statistics', methods=['GET', 'POST'])
@login_required
def show_stats():
    user_candidacy = Candidacy.query.join(Users).with_entities(Users.first_name,
                                                           Users.address,
                                                           Users.last_name,
                                                           Users.email_address,
                                                           Users.telephone_number,
                                                           Candidacy.user_id,
                                                           Candidacy.id, 
                                                           Candidacy.company, 
                                                           Candidacy.contact_full_name,
                                                           Candidacy.contact_email,
                                                           Candidacy.date,
                                                           Candidacy.status,
                                                           Candidacy.job_type,
                                                           Candidacy.contact_mobilephone,
                                                           Candidacy.origin,
                                                           Candidacy.description,
                                                           Candidacy.comment,
                                                           
                                                           ).order_by(Candidacy.date.desc()).all()
    affichage = [{"user_id":c.user_id,
                "id":c.id,
                "first_name":c.first_name,
                "last_name":c.last_name,
                "address":c.address,
                "email_address":c.email_address, 
                "telephone_number":c.telephone_number,
                "company":c.company,
                "job_type":c.job_type,
                "contact_full_name":c.contact_full_name,
                "contact_email":c.contact_email,
                "contact_mobilephone":c.contact_mobilephone,
                "date":c.date,
                "status":c.status, 
                "origin":c.origin, 
                "description":c.description,
                "comment":c.comment 
                } for c in user_candidacy]   

    df = pd.DataFrame(affichage)
    fig1 = px.histogram(df, x='status', title = "Stats")
    fig1json = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    
    # Graph two
    
    count = df.groupby(["job_type", "first_name"]).count()
    fig2 = px.pie(count.reset_index(), values='id',names="job_type", title="Répartition des métiers")
    fig2json = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    
    count = df.groupby(["origin"]).count()
    fig3 = px.pie(count.reset_index(), values='first_name', names='origin', title="Répartition des plateformes")
    fig3json = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Graph three
    # df = px.data.gapminder().query("continent=='Oceania'")
    # fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    # graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template("statistiques.html",  fig1json=fig1json , fig2json=fig2json, fig3json=fig3json ) #,  graph2JSON=graph2JSON, graph3JSON=graph3JSON)