@login_required
def profile(request):
    user_report, created = DatasetOtchet.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        if request.POST.get('familia'):
            user_report.familia = request.POST['familia']
        if request.POST.get('name'):
            user_report.name = request.POST['name']
        if request.POST.get('otchestvo'):
            user_report.otchestvo = request.POST['otchestvo']
        if request.POST.get('tip'):
            try:
                user_report.prac_type = PracType.objects.get(type_name=request.POST['tip'])
            except PracType.DoesNotExist:
                pass
        
        # Модуль - проверяем, выбран ли "other"
        if request.POST.get('module') == 'other':
            if request.POST.get('module_other'):
                user_report.module = request.POST['module_other']
            else:
                user_report.module = ''
        else:
            user_report.module = request.POST.get('module', '')
        
        # Специализация - проверяем, выбран ли "other"
        if request.POST.get('specialization') == 'other':
            if request.POST.get('specialization_other'):
                user_report.specialization = request.POST['specialization_other']
            else:
                user_report.specialization = ''
        else:
            user_report.specialization = request.POST.get('specialization', '')
        
        # Курс - проверяем, выбран ли "other"
        if request.POST.get('kurs') == 'other':
            if request.POST.get('kurs_other'):
                user_report.kurs = request.POST['kurs_other']
            else:
                user_report.kurs = ''
        else:
            user_report.kurs = request.POST.get('kurs', '')
        
        # Группа - проверяем, выбран ли "other"
        if request.POST.get('group') == 'other':
            if request.POST.get('group_other'):
                user_report.group = request.POST['group_other']
            else:
                user_report.group = ''
        else:
            user_report.group = request.POST.get('group', '')
        
        if request.POST.get('begin_date'):
            date_parts = request.POST['begin_date'].split('-')
            if len(date_parts) == 3:
                user_report.date_begin = f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
        if request.POST.get('finish_date'):
            date_parts = request.POST['finish_date'].split('-')
            if len(date_parts) == 3:
                user_report.date_finish = f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
        if request.POST.get('head1'):
            user_report.head1 = request.POST['head1']
        if request.POST.get('head2'):
            user_report.head2 = request.POST['head2']
        if request.POST.get('ruc_pract'):
            user_report.ruc_pract = request.POST['ruc_pract']
        if request.POST.get('year'):
            user_report.year = request.POST['year']
        
        user_report.save()
        messages.success(request, 'Данные успешно сохранены!')
        return redirect('/profile/')