<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Alkilerra;
use App\Models\Bezeroa;
use App\Models\Bideojokua;

class AlkilerraController extends Controller {
    
    public function alk_index() {
        $alkilerrak = Alkilerra::all();
        return view('alkilerrak.alk_index', ['alkilerra' => $alkilerrak]);
    }

    public function alk_gehitu() {
        $bezeroak = Bezeroa::all();
        $bideojokuak = Bideojokua::all();
        return view('alkilerrak.alk_gehitu', compact('bezeroak', 'bideojokuak'));
    }

    public function alk_store(Request $request) {
        $validatedData = $request->validate([
            'bezeroa_id' => 'required',
            'bideojokua_id' => 'required',
            'hasiera_data' => 'required',
            'amaiera_data' => 'required',
        ]);

        Alkilerra::create([
            'bezeroa_id' => $request->bezeroa_id,
            'bideojokua_id' => $request->bideojokua_id,
            'hasiera_data' => $request->hasiera_data,
            'amaiera_data' => $request->amaiera_data,
        ]);

        return redirect('/alkilerrak');
    }

    public function alk_destroy($id) {
        $alkilerra = Alkilerra::findOrFail($id);
        $alkilerra->delete();

        return redirect('/alkilerrak');
    }
}
