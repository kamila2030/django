public function update(Request $request, $id)
{
    $specialist = Specialist::findOrFail($id);
    
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'specialization' => 'required|string|max:255',
        'photo_url' => 'nullable|url',
        'experience_years' => 'required|integer|min:0',
        'bio' => 'nullable|string',
        'is_top' => 'boolean'
    ]);

    $specialist->update($validated);

    return redirect()->route('admin.specialists')
        ->with('success', 'Данные мастера обновлены!');
}