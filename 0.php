Gate::define('admin', function ($user) {
    return $user->is_admin === 1;
});