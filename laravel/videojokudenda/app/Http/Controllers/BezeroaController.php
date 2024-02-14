<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Bezeroa;

class BezeroaController extends Controller {

    public function bez_index() {
        $bezeroak = Bezeroa::all();
        return view('bezeroak.bez_index', ['bezeroa' => $bezeroak]);
    }

    public function bez_gehitu() {
        return view('bezeroak.bez_gehitu');
    }

    public function bez_store(Request $request) {
        $validatedData = $request->validate([
            'izena' => 'required',
            'abizena' => 'required',
        ]);

        Bezeroa::create([
            'izena' => $request->izena,
            'abizena' => $request->abizena,
        ]);

        return redirect('/bezeroak');
    }

    public function bez_destroy($id) {
        $bezeroa = Bezeroa::findOrFail($id);
        $bezeroa->delete();

        return redirect('/bezeroak');
    }

    public function bez_edit($id) {
        $bezeroa = Bezeroa::findOrFail($id);
        return view('bezeroak.bez_edit', ['bezeroa' => $bezeroa]);
    }

    public function bez_update(Request $request, $id) {
        $request->validate([
            'izena' => 'required',
            'abizena' => 'required',
        ]);
        
        $bezeroa = Bezeroa::findOrFail($id);
        $bezeroa->update([
            'izena' => $request->izena,
            'abizena' => $request->abizena,
        ]);

        return redirect('/bezeroak');
    }
}
