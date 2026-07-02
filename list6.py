def to_genitive_simple(full_name):
    """
    Преобразует ФИО в родительный падеж
    Усубалиева Камила Кенешбековна -> Усубалиевой Камилы Кенешбековны
    """
    if not full_name or len(full_name.strip()) == 0:
        return ""
    
    def transform_last_name(name):
        if not name:
            return name
        if name.endswith('ко'):
            return name
        if name.endswith(('о', 'е', 'и', 'у', 'ю', 'ы', 'э')):
            return name
        if name.endswith('а'):
            return name[:-1] + 'ы'
        if name.endswith('я'):
            return name[:-1] + 'и'
        if name.endswith('ий'):
            return name[:-2] + 'его'
        if name.endswith('ый'):
            return name[:-2] + 'ого'
        if name.endswith('ой'):
            return name[:-2] + 'ого'
        if name.endswith('ь'):
            return name[:-1] + 'я'
        if name.endswith(('ж', 'ч', 'ш', 'щ', 'ц')):
            return name + 'а'
        return name + 'а'

def normalize_prac_type_for_accusative(prac_type):
    """
    Преобразует тип практики в винительный падеж (кого? что?)
    "Производственная" -> "производственную"
    "Учебная" -> "учебную"
    """
    if not prac_type:
        return "производственную"
    
    prac_type_lower = prac_type.lower()
    
    if prac_type_lower == "производственная":
        return "производственную"
    elif prac_type_lower == "учебная":
        return "учебную"
    else:
        return prac_type_lower