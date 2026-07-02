class Appointment extends Model
{
    use HasFactory;
    
    protected $fillable = [
        'service_id', 
        'specialist_id', 
        'client_name', 
        'client_phone', 
        'appointment_time'
    ];
    
    public function service()
    {
        return $this->belongsTo(Service::class);
    }
    
    public function specialist()
    {
        return $this->belongsTo(Specialist::class);
    }
}