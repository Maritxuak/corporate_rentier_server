from django.db import models


class DcsCatServices(models.Model):
    class Meta:
        verbose_name = 'Что входит в услугу?'
        verbose_name_plural = 'Что входит в услуги?'

    CATEGORY_FIELDS = [
        ('1', 'Что входит в услугу?'),
        ('2', 'Как это вам поможет?')
    ]

    category = models.CharField(verbose_name='Категория', choices=CATEGORY_FIELDS, max_length=1)
    name = models.CharField(verbose_name='Наименование', max_length=155)
    dsc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(verbose_name='Активный?')

    def __str__(self):
        return f'{self.category} - {self.name}'


class Services(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    CATEGORY_FIELDS = [
        ('1', 'Разработка систем с веб-интерфейсом'),
        ('2', 'Разработка дизайна'),
        ('3', 'Обслуживание IT-инфраструктуры'),
        ('4', 'Разработка мобильных приложений'),
        ('5', 'Разработка умных систем'),
        ('6', 'Интернет реклама')
    ]

    name = models.CharField(verbose_name='Наименование', max_length=155)
    category = models.CharField(verbose_name='Категория', choices=CATEGORY_FIELDS, max_length=1)
    dsc = models.TextField(verbose_name='Описание')
    included_in_the_service = models.ManyToManyField(DcsCatServices, verbose_name='Подробное описание')

    def __str__(self):
        return f'{self.category} - {self.name}'


class Dignities(models.Model):
    class Meta:
        verbose_name = 'За что нас ценят?'
        verbose_name_plural = 'За что нас ценят?'

    name = models.CharField(verbose_name='Заголовок', max_length=155)
    dsc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(verbose_name='Активный?', blank=True, null=True, default=True)

    def __str__(self):
        return f'{self.name}'


class Quotes(models.Model):
    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    CATEGORY_FIELDS = [
        ('1', 'Разработчик'),
        ('2', 'Клиент')
    ]

    category = models.CharField(verbose_name='От кого?', choices=CATEGORY_FIELDS, max_length=1)
    username = models.CharField(verbose_name='Имя Фамилия', max_length=50)
    post = models.CharField(verbose_name='Должность', max_length=20)
    quotes = models.TextField(verbose_name='Цитата')

    def __str__(self):
        return f'{self.category} - {self.username} {self.post}'


class Projects(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    category_services = models.ForeignKey(verbose_name='Категория услуги', to=Services, on_delete=models.PROTECT)
    bw_preview_photo = models.ImageField(verbose_name='Фотография превью чб',
                                         upload_to='photo/project/bw_preview/%Y/%m/%d/')
    c_preview_photo = models.ImageField(verbose_name='Фотография превью цветная'
                                        , upload_to='photo/project/c_preview/%Y/%m/%d/')
    title_photo = models.ImageField(verbose_name='Фотография заголовка',
                                         upload_to='photo/project/title/%Y/%m/%d/')
    dsc_project = models.TextField(verbose_name='О проекте')
    dsc_task = models.TextField(verbose_name='Задача')
    photo_task = models.ImageField(verbose_name='Фотография задачи',
                                         upload_to='photo/project/task/%Y/%m/%d/')
    dsc_realization = models.TextField(verbose_name='Реализация')
    photo_realization = models.ImageField(verbose_name='Фотография реализации',
                                         upload_to='photo/project/realization/%Y/%m/%d/')
    quotes = models.ManyToManyField(Quotes, verbose_name='Цитаты')
    is_display_main_page = models.BooleanField(verbose_name='Отображать на гл стр?', default=False)
    is_active = models.BooleanField(verbose_name='Активный?', blank=True, null=True, default=True)

    def __str__(self):
        return f'{self.name}'


class FeedBack(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    username = models.CharField(verbose_name='Имя пользователя', max_length=155)
    number_phone = models.CharField(verbose_name='Номер телефона', max_length=30)
    name_company = models.CharField(verbose_name='Компания', max_length=55)
    document = models.FileField(verbose_name='Техническое задание', upload_to='feedback/document/%Y/%m/%d/',
                                blank=True, null=True)
    dsc = models.TextField(verbose_name='Описание проекта', default='Не заполнено', null=True, blank=True)
    category = models.CharField(verbose_name='Категория услуги', blank=True, null=True, max_length=155)
    data = models.DateTimeField(verbose_name='Дата обращения', auto_created=True, auto_now=True)
    is_processed = models.BooleanField(verbose_name='Обработан', default=False)
    is_successfully = models.BooleanField(verbose_name='Успешно', default=False)

    def __str__(self):
        return f'{self.username}'




