<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class bideojokua extends Model
{
    use HasFactory;
    protected $fillable = ['bid_izena', 'bid_deskripzioa'];

    public function alkilerras() {
        return $this->hasMany(Alkilerra::class);
    }
}
