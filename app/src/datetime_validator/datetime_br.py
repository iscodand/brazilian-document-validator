from datetime import datetime, timedelta


class DateTimeBR():
    def __init__(self):
        self.register_moment = datetime.now()

    def __str__(self):
        return self.format()

    def register_month(self):
        year_months = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        month = self.register_moment.month
        return year_months[month - 1]

    def register_weekday(self):
        week_days = [
            "Segunda", "Terça", "Quarta",
            "Quinta", "Sexta", "Sábado", "Domingo" 
        ]
        weekday = self.register_moment.weekday()
        return week_days[weekday]

    def format(self):
        formated_time = self.register_moment
        return formated_time.strftime("%d/%m/%Y - %H:%M")

    def register_time(self):
        total_time = (datetime.today() + timedelta(days=30))- self.register_moment
        return total_time
        