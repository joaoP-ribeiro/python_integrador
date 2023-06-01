
from selenium.webdriver.common.by import By
from selenium import webdriver
from excel import excel
import pandas as pd
from openpyxl.workbook import Workbook

class Scraping():
    def __init__(self, save, nome_arquivo):
        self.site = r"file:///C:/xampp/htdocs/site/produtos.html"
        self.map = {
            "nome": {
                "xpath": "/html/body/main/div/div/div[2]/div[$nome$]/p[1]"
            },
            "valor": {
                "xpath": "/html/body/main/div/div/div[2]/div[$valor$]/p[2]"
            },
        }
        self.save = save
        self.nome_arquivo = nome_arquivo
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)#options=options
        self.varrer_site()
        self.driver.close()
    

    def varrer_site(self):
        self.driver.get(self.site)
        nome_lista=[]
        fabricante_lista=[]
        valor_lista=[]
        i = 0
        while True:
            i += 1
            try:
                n = self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace("$nome$", f"{i}")).text
                nome = n.split("'")[0]
                fabricante = n.split("'")[1]
                v = self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace("$valor$", f"{i}")).text
                valor = v.split(" ")[1]
                nome_lista.append(nome)
                fabricante_lista.append(fabricante)
                valor_lista.append(valor) 
            except:
                break
        
        dados = excel(nome_lista, fabricante_lista, valor_lista)
        if self.save =="csv":
            dados.to_csv(f"{self.save}{self.nome_arquivo}.csv", sep=";", index = False)
        else:
            dados.to_excel(f"{self.save}{self.nome_arquivo}.xlsx", index = False)
            dados.to_csv(f"{self.save}{self.nome_arquivo}.csv", sep=";", index = False)
        nome_lista.clear()
        fabricante_lista.clear()
        valor_lista.clear() 




#/html/body/main/div/div/div[2]/div[1]/p[1]
#/html/body/main/div/div/div[2]/div[4]/p[1]

#/html/body/main/div/div/div[2]/div[1]/p[2]
#/html/body/main/div/div/div[2]/div[9]/p[2]