public function store(Request $request)
{
    $validated = $request->validate([
        'service_id' => 'required|exists:services,id',
        'specialist_id' => 'required|exists:specialists,id',
        'client_name' => 'required|string|min:2|max:100',
        'client_phone' => 'required|string|min:10|max:20',
        'appointment_time' => 'required|date|after:now'
    ]);

    $appointment = Appointment::create($validated);

    return response()->json([
        'success' => true,
        'message' => 'Вы успешно записаны!'
    ]);
}