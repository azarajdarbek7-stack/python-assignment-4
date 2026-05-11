from analytics.analyser import CountryAnalyser

def main():
    # Тестовые данные (представь, что это из CSV)
    sample_data = [
        {"country": "USA"}, {"country": "India"},
        {"country": "USA"}, {"country": "Kazakhstan"}, {"country": "India"}
    ]

    analyser = CountryAnalyser(sample_data)
    print(analyser) # Выведет информацию о классе
    
    analyser.analyse()
    analyser.print_results() # Выведет таблицу с результатами

if __name__ == "__main__":
    main()