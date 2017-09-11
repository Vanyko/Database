#from company import Company
#from model import Model
#company = Company(1, "ZAZ", "Ukraine")
#print company
#model = Model(company, 1, "Forza", 100, 60, 1.6)
#print model
#from companies import Companies
#company2 = Company(2, "KIA", "Japan")
#print company2
#print "---"
#from models import Models
#models = Models()
#model2 = Model(company2, 2, "Sportage", 7.7, 200, 2)
#models.add(model)
#models.add(model2)
#print models
#print "----------"
#companies = Companies()
#companies.add(company)
#companies.add(company2)
#print companies
#print companies.exists(1)
#print companies.exists(2)
#print companies.exists(3)
#if companies.delete(1, models):
#    print "Success"
#else:
#    print "Cant delete: this company is using"
#print companies
#print "-----"
#print models
#print "00000000"
##models.delete(1)
##print models
##print "!!!!!!!!"
##models.delete(2)
#print models
#print "\n\n\n"
#import ui
#ui.print_menu()
#companies.showById(5)
#print companies.update(2,"id",5, models)
#print companies.update(1,"name","Shkoda", models)
#print companies.update(1,"country","Chech", models)
#companies.showById(5)
#print "\n\n\n"
#models.update(1, "consumption", 10)
#print models
#models.showByEvolume(1.6)
#
#print "----------------------"
#
#import cPickle as pickle
#ui.dump(companies, "data.pkl")
#obj = ui.load("data.pkl")
#print obj
#
#print ui.getKey("Input number, please: ")
#ui.clear()
#ui.showCompanies(companies)

import ui
from companies import Companies
from models import Models
companies = Companies()
models = Models()
companies = ui.load("companies.pkl")
models = ui.load("models.pkl")
if not companies:
    companies = Companies()
if not models:
    models = Models()
key = 0
while not key == 9:
    ui.clear()
    ui.print_menu()
    key = ui.getKey("Please, input the number you would like to choose: ")
    ui.clear()
    if key == 0:
        ui.showCompanies(companies)
    elif key == 1:
        ui.showModels(models)
    elif key == 2:
        if ui.addCompany(companies):
            print "Company successfully added"
    elif key == 3:
        if ui.addModel(companies, models):
            print "Model successfully added"
    elif key == 4:
        if ui.deleteCompany(companies, models):
            print "Company successfully deleted"
    elif key == 5:
        if ui.deleteModel(models):
            print "Model successfully deleted"
    elif key == 6:
        if ui.updateCompany(companies, models):
            print "Company successfully updated"
        else:
            print "Error"
    elif key == 7:
        if ui.updateModel(companies, models):
            print "Model successfully updated"
        else:
            print "Error"
    elif key == 8:
        ui.searchByEVolume(models)
    if not key == 9:
        ui.wait()

ui.stop(companies, models)













