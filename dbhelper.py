import mysql.connector

class DB:
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='countryiq'
            )
            self.mycursor = self.conn.cursor()
            print("Connection established")
        except:
            print("Connection error")


    def show_country_map(self):
        
        country = []
        iq =[]
        self.mycursor.execute("SELECT Country, AverageIQ FROM countryiq.countryiq")        
        data = self.mycursor.fetchall()

        print(data)
        for item in data:
            country.append(item[0])
            iq.append(item[1])

        return country, iq    
    
    def show_schooling(self):
        
        schooling= []
        AverageIQ = []
        Country = []
        self.mycursor.execute("""
                              SELECT Mean_years_of_schooling_2021,
                            AverageIQ,Country FROM countryiq""")
        data = self.mycursor.fetchall()

        for item in data:
            schooling.append(item[0])
            AverageIQ.append(item[1])
            Country.append(item[2])

        return schooling, AverageIQ, Country    
    
    def show_literacy_rate(self):
        
        literacy_rate = []
        average_iq =[]
        country = []
        self.mycursor.execute("SELECT Literacy_Rate, AverageIQ, Country FROM countryiq")
        data = self.mycursor.fetchall()
        for item in data:
            literacy_rate.append(item[0])
            average_iq.append(item[1])
            country.append(item[2])

        return literacy_rate, average_iq, country

    def show_nobel_prices(self):
        
        country = []
        nobel_prices = []
        self.mycursor.execute("""
                              SELECT Country, Nobel_Prices FROM countryiq
                                ORDER BY Nobel_Prices DESC
                                LIMIT 5""")    
        data = self.mycursor.fetchall()
        for item in data:
            country.append(item[0])
            nobel_prices.append(item[1])
        return country, nobel_prices    