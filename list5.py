@login_required
def generate_document(request, doc_type):
    """
    Генерация документа на основе шаблона
    doc_type: 'title', 'assignment', 'diary'
    """
    from datetime import datetime
    
    user_report = get_object_or_404(DatasetOtchet, user=request.user)
    
    try:
        template_obj = DocumentTemplate.objects.get(doc_type=doc_type)
    except DocumentTemplate.DoesNotExist:
        messages.error(request, f'Шаблон для {doc_type} не загружен. Обратитесь к администратору.')
        return redirect('/profile/')
    
    if not user_report.familia or not user_report.name:
        messages.error(request, 'Пожалуйста, заполните фамилию и имя в профиле перед генерацией документа.')
        return redirect('/profile/')
    
    def parse_date(date_string):
        if not date_string:
            return {'day': '', 'month': '', 'year': ''}
        try:
            if '.' in date_string:
                parts = date_string.split('.')
                if len(parts) == 3:
                    return {
                        'day': parts[0],
                        'month': parts[1],
                        'year': parts[2]
                    }
            elif '-' in date_string:
                parts = date_string.split('-')
                if len(parts) == 3:
                    return {
                        'day': parts[2],
                        'month': parts[1],
                        'year': parts[0]
                    }
        except:
            pass
        return {'day': '', 'month': '', 'year': ''}
    
    date_begin_parts = parse_date(user_report.date_begin)
    date_finish_parts = parse_date(user_report.date_finish)
    
    months = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
        '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
        '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    
    month_begin_text = months.get(date_begin_parts['month'], date_begin_parts['month'])
    month_finish_text = months.get(date_finish_parts['month'], date_finish_parts['month'])

    prac_type_name = user_report.prac_type.type_name if user_report.prac_type else 'Производственная'
    
    prac_type_for_title = normalize_prac_type_for_title(prac_type_name)
    prac_type_genitive = normalize_prac_type_for_sentence(prac_type_name, case='genitive')
    prac_type_dative = normalize_prac_type_for_sentence(prac_type_name, case='dative')
    prac_type_accusative = normalize_prac_type_for_accusative(prac_type_name)
    
    full_name = f"{user_report.familia} {user_report.name} {user_report.otchestvo}".strip()
    
    full_name_genitive = to_genitive_simple(full_name)
    full_name_dative = to_dative_simple(full_name)
    
    head1_short = shorten_fio(user_report.head1)
    head2_short = shorten_fio(user_report.head2)
    ruc_pract_short = shorten_fio(user_report.ruc_pract)
    
    date_begin_formatted = format_date_for_doc(user_report.date_begin)
    date_finish_formatted = format_date_for_doc(user_report.date_finish)
    
    begin_day = get_day_from_date(user_report.date_begin)
    begin_month = get_month_name_from_date(user_report.date_begin)
    begin_year = get_year_from_date(user_report.date_begin)
    
    finish_day = get_day_from_date(user_report.date_finish)
    finish_month = get_month_name_from_date(user_report.date_finish)
    finish_year = get_year_from_date(user_report.date_finish)
    
    context = {
        'fio': full_name,
        'familia': user_report.familia or '',
        'name': user_report.name or '',
        'otchestvo': user_report.otchestvo or '',
        'fio_genitive': full_name_genitive,
        'fio_dative': full_name_dative,
        'tip': prac_type_name,
        'tip_title': prac_type_for_title,
        'tip_genitive': prac_type_genitive,
        'tip_dative': prac_type_dative,
        'tip_accusative': prac_type_accusative,
        'head1': user_report.head1 or '_________________________',
        'head2': user_report.head2 or '_________________________',
        'ruc_pract': user_report.ruc_pract or '_________________________',
        'head1_short': head1_short or '_________________________',
        'head2_short': head2_short or '_________________________',
        'ruc_pract_short': ruc_pract_short or '_________________________',
        'module': user_report.module or '',
        'module_code': user_report.module or '',
        'specialization': user_report.specialization or '09.02.07 "Информационные системы и программирование"',
        'kurs': user_report.kurs or '2',
        'group': user_report.group or '',
        'date_begin': user_report.date_begin or '',
        'date_finish': user_report.date_finish or '',
        'day_begin': date_begin_parts['day'],
        'month_begin': month_begin_text,
        'year_begin': date_begin_parts['year'],
        'day_finish': date_finish_parts['day'],
        'month_finish': month_finish_text,
        'year_finish': date_finish_parts['year'],
        'date_begin_formatted': date_begin_formatted,
        'date_finish_formatted': date_finish_formatted,
        'begin_day': begin_day,
        'begin_month': begin_month,
        'begin_year': begin_year,
        'finish_day': finish_day,
        'finish_month': finish_month,
        'finish_year': finish_year,
        'year': user_report.year or datetime.now().year,
        'username': request.user.username,
        'name_org': 'ГБПОУ МО «Люберецкий техникум имени Героя Советского Союза, летчика-космонавта Ю.А.Гагарина»',
        'address_org': 'Московская область, г. Люберцы, __________________',
        'phone_org': '+7 (495) XXX-XX-XX',
        'email_org': 'info@lubertsy-teh.ru',
        'sphere': 'Профессиональное образование',
        'year_foundation': '19XX',
        'form_ownership': 'Государственное бюджетное учреждение',
        'history_org': '_________________________',
        'godovoy_otchet': '_________________________',
        'uslugi_org': 'Образовательные услуги по подготовке специалистов СПО',
        'achievments_org': '_________________________',
        'name_docher': '_________________________',
        'address_docher': '_________________________',
        'phone_docher': '_________________________',
        'email_docher': '_________________________',
        'name_podrazdel': 'Отдел информационных технологий',
        'head_podrazdel': '_________________________',
        'fio_head_practice': user_report.ruc_pract or '_________________________',
        'kurator_phone': '_________________________',
        'kurator_email': '_________________________',
        'struk_and_func': '_________________________',
        'goal_pract': f'{prac_type_genitive} практической подготовки',
        'prof_kompetentsii': '''
- ПК 11.1 Осуществлять сбор, обработку и анализ информации для проектирования баз данных
- ПК 11.2 Проектировать базу данных на основе анализа предметной области
- ПК 11.3 Разрабатывать объекты базы данных в соответствии с результатами анализа предметной области
- ПК 11.4 Реализовывать базу данных в конкретной системе управления базами данных
- ПК 11.5 Администрировать базы данных
- ПК 11.6 Защищать информацию в базе данных с использованием технологии защиты информации
        ''',
        'obsh_kompetentsii': '''
- ОК 01. Выбирать способы решения задач профессиональной деятельности применительно к различным контекстам
- ОК 02. Использовать современные средства поиска, анализа и интерпретации информации 
- ОК 03. Планировать и реализовывать собственное профессиональное и личностное развитие
- ОК 04. Эффективно взаимодействовать и работать в коллективе и команде
- ОК 05. Осуществлять устную и письменную коммуникацию на государственном языке
- ОК 06. Проявлять гражданско-патриотическую позицию, демонстрировать осознанное поведение
- ОК 07. Содействовать сохранению окружающей среды, ресурсосбережению
- ОК 08. Использовать средства физической культуры для сохранения и укрепления здоровья
- ОК 09. Пользоваться профессиональной документацией на государственном и иностранном языках
        ''',
    }
    
    template_path = template_obj.template_file.path
    
    try:
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        doc = DocxTemplate(template_path)
        
        try:
            variables = doc.get_undeclared_template_variables()
            print(f"Переменные в шаблоне: {variables}")
        except Exception as e:
            print(f"Не удалось получить переменные: {e}")
        
        doc.render(context)
        doc.save(tmp_path)
        
        doc_names = {
            'title': 'Титульный_лист',
            'assignment': 'Задание',
            'diary': 'Дневник'
        }
        
        file_name = f"{doc_names.get(doc_type, 'document')}_{user_report.familia}_{user_report.name}.docx"
        
        with open(tmp_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        
        os.unlink(tmp_path)
        
        return response