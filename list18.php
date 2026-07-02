public function update(Request $request, $id)
{
    $salonInfo = SalonInfo::findOrFail($id);
    
    $validated = $request->validate([
        'address' => 'required|string',
        'phone' => 'required|string',
        'email' => 'required|email',
        'work_hours' => 'required|string',
        'about' => 'required|string'
    ]);

    $salonInfo->update($validated);

    return redirect()->route('admin.salon')
        ->with('success', 'Информация о салоне обновлена!');
}