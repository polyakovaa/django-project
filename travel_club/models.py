from django.db import models

class User(models.Model):
    types = (
        ('admin', 'Администратор'),
        ('organizer', 'Организатор'),
        ('participant', 'Участник'),
    )
    first_name = models.CharField(max_length=120, verbose_name="Имя", blank=True,null=True)
    last_name = models.CharField(max_length=120,verbose_name="Фамилия",blank=True,null=True)
    user_type = models.CharField(max_length=20, choices=types, default='participant',verbose_name="Роль")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер")
    email = models.EmailField(blank=True, null=True, verbose_name="Почта")
    card = models.OneToOneField('ClubCard', on_delete=models.CASCADE,verbose_name="Клубная карта", blank=True, null=True)
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Event(models.Model):
    statuses = (
        ('completed', 'Проведено'),
        ('planned', 'Запланировано'),
        ('in_progress', 'В разработке'),
    )
    
    levels = (
        ('hard', 'Сложный'),
        ('medium', 'Средний'),
        ('easy', 'Для новичков'),
    )
    
    event_type = models.CharField(max_length=50, verbose_name="Тип мероприятия")
    name = models.CharField(max_length=200,verbose_name="Название")
    is_multi_day = models.BooleanField(default=False, verbose_name="Многодневный")
    planned_date = models.DateField(verbose_name="Запланированная дата")
    actual_date = models.DateField(blank=True, null=True, verbose_name="Фактическая дата")
    status = models.CharField(max_length=20, choices=statuses,verbose_name="Статус")
    difficulty = models.CharField(max_length=20, choices=levels, verbose_name="Сложность")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Стоимость")
    comment = models.TextField(blank=True, null=True,verbose_name="Описание")
    participants = models.ManyToManyField(User, through='EventParticipation', verbose_name="Участники мероприятия")
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.name
    
class RouteTrack(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name="Мероприятие")
    name = models.CharField(max_length=200, verbose_name="Название")
    distance = models.FloatField(blank=True, null=True,verbose_name="Дистаниця")

    class Meta:
        verbose_name = "Трек маршрута"
        verbose_name_plural = "Треки маршрута"

    def __str__(self):
        return f"{self.event.name} - {self.name}"

class EventParticipation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Имя")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    is_organizer = models.BooleanField(default=False, verbose_name="Организатор")
    
    class Meta:
        unique_together = ('user', 'event')
        verbose_name = "Участие в мероприятиях"
        verbose_name_plural = "Участие в мероприятиях"
    def __str__(self):
        return "Организатор" if self.is_organizer else "Участник"

class ClubCard(models.Model):
    card_states = (
        ('in_use', 'Используется'),
        ('not_in_use', 'Не используется'),
        ('hidden', 'Спрятана'),
    )
    
    number = models.CharField(max_length=50, unique=True,verbose_name="Номер")
    state = models.CharField(max_length=20, choices=card_states,verbose_name="Состояние")
    owner = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Стоимость")
    sale_date = models.DateField(blank=True, null=True,verbose_name="Дата продажи")
    hidden_location = models.CharField(blank=True, null=True,verbose_name="Место")
    
    class Meta:
        verbose_name = "Клубная карта"
        verbose_name_plural = "Клубные карты"

    def __str__(self):
        return f"Карта №{self.number}"