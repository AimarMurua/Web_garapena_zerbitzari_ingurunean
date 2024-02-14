<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('alkilerras', function (Blueprint $table) {
            $table->id();
            $table->foreignId('bezeroa_id')->constrained()->onDelete('cascade');
            $table->foreignId('bideojokua_id')->constrained()->onDelete('cascade');
            $table->dateTime('hasiera_data');
            $table->dateTime('amaiera_data');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('alkilerras');
    }
};
