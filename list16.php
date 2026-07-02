public function getSpecialistsByService($serviceId)
{
    $service = Service::with('specialists')->findOrFail($serviceId);
    $specialists = $service->specialists;
    
    return response()->json([
        'specialists' => $specialists->map(function($specialist) {
            return [
                'id' => $specialist->id,
                'name' => $specialist->name,
                'specialization' => $specialist->specialization,
                'photo_url' => $specialist->photo_url,
                'experience_years' => $specialist->experience_years
            ];
        })
    ]);
}