public function destroy($id)
{
    $service = Service::findOrFail($id);
    $service->delete();

    return redirect()->route('admin.services')
        ->with('success', 'Услуга успешно удалена!');
}