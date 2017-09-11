import cPickle as pickle
import os
from company import Company
from model import Model
from companies import Companies
from models import Models

def print_menu():
    print "--- Menu ---\n\n0: Show companies\n1: Show models\n2: Add company\n3: Add model\n4: Delete company\n5: Delete model\n6: Update company\n7: Update model\n8: Search by volume 2.0(l)\n9: Exit\n"

def dump(data, fname):
    output = open(fname, 'wb')
    pickle.dump(data, output)
    output.close()

def load(fname):
    try:
        input = open(fname, 'rb')
        data = pickle.load(input)
        input.close()
        return data
    except Exception:
        print "File is empty"
        return

def start(companies, models):
    print "Start"

def stop(companies, models):
    dump(companies, "companies.pkl")
    dump(models, "models.pkl")

def getKey(text = ""):
    try:
        data = input(text)
        return data
    except Exception:
        print "Input number, please"


def clear():
    os.system('clear')

def wait():
    raw_input("Push enter to back to the menu! ")
    return

def showCompanies(companies):
    print companies

def showModels(models):
    print models

def addCompany(companies):
    id = input("Please, input the company id: ")
    if companies.exists(id):
        print "This id already exists"
        return False
    name = raw_input("Please, input the company name: ")
    country = raw_input("Please, input the company country: ")
    new_company = Company(id, name, country)
    return companies.add(new_company)

def addModel(companies, models):
    companyId = input("Please, input the company id: ")
    if not companies.exists(companyId):
        print "There is no such company, please try again"
        return False
    company = companies.get(companyId)
    mid = input("Please, input the model id: ")
    if models.mexists(mid):
        print "This id already exists"
        return False
    name = raw_input("Please, input the model name: ")
    consumption = input("Please, input the model consumption: ")
    speed = input("Please, input the model speed: ")
    evolume = input("Please, input the model engine volume: ")
    new_model = Model(company, mid, name, consumption, speed, evolume)
    return models.add(new_model)

def deleteCompany(companies, models):
    id = input("Please, input the company id: ")
    return companies.delete(id, models)

def deleteModel(models):
    id = input("Please, input the model id: ")
    return models.delete(id)

def updateCompany(companies, models):
    id = input("Please, input the company id: ")
    name = raw_input("Please, input the attribute name: ")
    attr = raw_input("Please, input the attribute value: ")
    return companies.update(id, name, attr, models)

def updateModel(companies, models):
    id = input("Please, input the model id: ")
    if not models.mexists(id):
        print "There is no such model"
        return False
    name = raw_input("Please, input the attribute name: ")
    attr = raw_input("Please, input the attribute value: ")
    return models.update(id, name, attr, companies)

def searchByEVolume(models, value = 2.0):
    models.searchByEvolume(value)

