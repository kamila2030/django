Schema::table('salon_info', function (Blueprint $table) {
    $table->string('salon_photo')->nullable()->after('about');
});