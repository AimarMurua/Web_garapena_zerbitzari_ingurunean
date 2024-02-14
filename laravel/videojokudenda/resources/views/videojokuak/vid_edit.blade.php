<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bid_edit</title>
</head>
<body>
    <h1>Bideojokua editatu</h1>
    <a href="/bideojokuak">back</a>
    <form action="/update/{{ $bideojokua->id }}" method="POST">
        @csrf
        <label for="bid_izena">izena</label>
        <input type="text" name="bid_izena" id="bid_izena" value="{{ $bideojokua->bid_izena }}">
        <br>
        <label for="bid_deskripzioa">deskripzioa</label><br>
        <textarea name="bid_deskripzioa" id="bid_deskripzioa" rows="4" cols="50">{{ $bideojokua->bid_deskripzioa }}</textarea>
        <br>
        <input type="submit" value="edit">
    </form>
</body>
</html>
