public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'specialization' => 'required|string|max:255',
        'photo_url' => 'nullable|url',
        'experience_years' => 'required|integer|min:0',
        'bio' => 'nullable|string',
        'is_top' => 'boolean'
    ]);

    $specialist = Specialist::create($validated);

    return redirect()->route('admin.specialists')
        ->with('success', 'Мастер успешно добавлен!');
}