import sys
# Импортируем твои классы из пакета analytics
from analytics.file_manager import FileManager, ResultSaver
from analytics.data_loader import DataLoader
from analytics.analyser import CountryAnalyser

def main():
    # Путь к твоему файлу со студентами
    input_file = 'students.csv'
    output_file = 'output/result.json'
    
    # 1. Используем FileManager (из твоего 3-го ассаймента)
    fm = FileManager(input_file)
    if not fm.check_file():
        print(f"Ошибка: Файл {input_file} не найден. Программа остановлена.")
        sys.exit()
    
    # Создаем папку для результата
    fm.create_output_folder()

    # 2. Используем DataLoader
    dl = DataLoader(input_file)
    students_data = dl.load()
    
    if not students_data:
        print("Ошибка: Данные не загружены.")
        return

    # 3. Используем CountryAnalyser (Наследование из 4-го ассаймента)
    # Передаем загруженные данные в анализатор
    analyser = CountryAnalyser(students_data)
    analyser.analyse()
    
    # Выводим красивые результаты в консоль (как в 3-м ассайменте)
    analyser.print_results()

    # 4. Используем ResultSaver для сохранения в JSON
    saver = ResultSaver(analyser.result, output_file)
    saver.save_json()

if __name__ == "__main__":
    main()