<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bez_gehitu</title>
</head>
<body>
<h1>alkilerra gehitu</h1>
    <form action="/alk_store" method="POST">
        @csrf
        <label for="bezeroa_id">Bezeroa:</label>
        <select name="bezeroa_id" id="bezeroa_id">
            @foreach ($bezeroak as $bezeroa)
                <option value="{{ $bezeroa->id }}">{{ $bezeroa->izena }}</option>
            @endforeach
        </select><br>
        <label for="bideojokua_id">Bideojokua:</label>
        <select name="bideojokua_id" id="bideojokua_id">
            @foreach ($bideojokuak as $bideojokua)
                <option value="{{ $bideojokua->id }}">{{ $bideojokua->bid_izena }}</option>
            @endforeach
        </select><br>
        <label for="hasiera_data">Hasiera Data:</label>
        <input type="date" name="hasiera_data"><br>
        <label for="amaiera_data">Amaiera Data:</label>
        <input type="date" name="amaiera_data"><br>

        <input type="submit" value="gehitu">
    </form>
</body>
</html>