from datetime import datetime


class DateTimeBR():
    def __init__(self):
        self.register_moment = datetime.now()

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
