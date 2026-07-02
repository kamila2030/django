public function index()
{
    if (!auth()->user() || auth()->user()->role !== 'admin') {
        abort(403, 'Доступ запрещён. Требуются права администратора.');
    }
    
    $services = Service::all();
    return view('admin.services', compact('services'));
}