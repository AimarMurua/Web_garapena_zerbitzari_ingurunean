<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\BideojokuaController;
use App\Http\Controllers\BezeroaController;
use App\Http\Controllers\AlkilerraController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('home');
});

// VIDEOJUEGOS
    Route::get('/bideojokuak', [BideojokuaController::class, 'bid_index']);

    Route::get('/bid_gehitu', [BideojokuaController::class, 'bid_gehitu']);
    Route::post('/bid_gehituu', [BideojokuaController::class, 'store']);

    Route::get('/delete/{id}', [BideojokuaController::class, 'destroy']);

    Route::get('/edit/{id}', [BideojokuaController::class, 'edit']);
    Route::post('/update/{id}', [BideojokuaController::class, 'update']);

//BEZEROAK
    Route::get('/bezeroak', [BezeroaController::class, 'bez_index']);

    Route::get('/bez_gehitu', [BezeroaController::class, 'bez_gehitu']);
    Route::post('/bez_gehituu', [BezeroaController::class, 'bez_store']);

    Route::get('/bez_delete/{id}', [BezeroaController::class, 'bez_destroy']);

    Route::get('/bez_edit/{id}', [BezeroaController::class, 'bez_edit']);
    Route::post('/bez_update/{id}', [BezeroaController::class, 'bez_update']);

//ALKILERRAK
    Route::get('/alkilerrak', [AlkilerraController::class, 'alk_index']);

    Route::get('/alk_gehitu', [AlkilerraController::class, 'alk_gehitu']);
    Route::post('/alk_store', [AlkilerraController::class, 'alk_store']);

    Route::get('/alk_delete/{id}', [AlkilerraController::class, 'alk_destroy']);