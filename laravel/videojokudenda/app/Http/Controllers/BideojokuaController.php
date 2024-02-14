<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Bideojokua;

class BideojokuaController extends Controller {
    
    public function bid_index() {
        $bideojokuak = Bideojokua::all();
        return view('videojokuak.vid_index', ['bideojokua' => $bideojokuak]);
    }

    public function bid_gehitu() {
        return view('videojokuak.vid_gehitu');
    }

    public function store(Request $request) {
        $validatedData = $request->validate([
            'bid_izena' => 'required',
            'bid_deskripzioa' => 'required',
        ]);

        Bideojokua::create([
            'bid_izena' => $request->bid_izena,
            'bid_deskripzioa' => $request->bid_deskripzioa,
        ]);

        return redirect('/bideojokuak');
    }

    public function destroy($id) {
        $bideojokua = Bideojokua::findOrFail($id);
        $bideojokua->delete();

        return redirect('/bideojokuak');
    }

    public function edit($id) {
        $bideojokua = Bideojokua::findOrFail($id);
        return view('videojokuak.vid_edit', ['bideojokua' => $bideojokua]);
    }

    public function update(Request $request, $id) {
        $request->validate([
            'bid_izena' => 'required',
            'bid_deskripzioa' => 'required',
        ]);
        
        $bideojokua = Bideojokua::findOrFail($id);
        $bideojokua->update([
            'bid_izena' => $request->bid_izena,
            'bid_deskripzioa' => $request->bid_deskripzioa,
        ]);

        return redirect('/bideojokuak');
    }
}
