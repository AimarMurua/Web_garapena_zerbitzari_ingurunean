<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class bezeroa extends Model
{
    use HasFactory;
    protected $fillable = ['izena', 'abizena'];

    public function alkilerras() {
        return $this->hasMany(Alkilerra::class);
    }
}
