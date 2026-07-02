public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'description' => 'nullable|string',
        'price' => 'required|numeric|min:0',
        'duration_minutes' => 'required|integer|min:5',
        'category' => 'nullable|string'
    ]);

    $service = Service::create($validated);

    return redirect()->route('admin.services')
        ->with('success', 'Услуга успешно создана!');
}