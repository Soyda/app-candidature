from calendar import c
from App.models import Candidacy, Users
from App import db




#print(Candidacy.query.join(Users).with_entities(Candidacy.*, Users.first_name).first())

#print(Candidacy.query.join(Users).with_entities(Users.first_name,Candidacy.entreprise, Candidacy.contact_full_name, Candidacy.contact_email, Candidacy.contact_mobilephone,Candidacy.date,Candidacy.status).all())
mon_id = 23
u = Candidacy.query.filter(Candidacy.status == "En cours").all()

l = list(set([u[i].user_id for i in range(0,len(u))]))
print(Users.query.filter_by(id=l[0]).first().last_name)
print(l)




test = Candidacy.query.group_by("company").all()
#test2 = [comp.company for comp in test]
print(test)

comp = [{"company" : c.company} for c in Candidacy.query.group_by("company").all()]
print(comp[0]["company"])

user_candidacy=Candidacy.get_all_in_list_with_user_name()
u = Candidacy.query.order_by("date").all()
print(u[0]["date"])