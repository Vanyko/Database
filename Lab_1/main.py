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
    try:
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
    except Exception:
        print "Error"
    if not key == 9:
        ui.wait()

ui.stop(companies, models)
