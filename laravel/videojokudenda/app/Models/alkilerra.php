<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Alkilerra extends Model {
    use HasFactory;

    protected $fillable = ['bezeroa_id', 'bideojokua_id', 'hasiera_data', 'amaiera_data'];

    public function bezeroa() {
        return $this->belongsTo(Bezeroa::class);
    }

    public function bideojokua() {
        return $this->belongsTo(Bideojokua::class);
    }
}
