<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bez_edit</title>
</head>
<body>
    <h1>Bezeroa editatu</h1>
    <a href="/bezeroak">back</a>
    <form action="/bez_update/{{ $bezeroa->id }}" method="POST">
        @csrf
        <label for="izena">izena:</label>
        <input type="text" name="izena" id="izena" value="{{ $bezeroa->izena }}">
        <br>
        <label for="abizena">abizena:</label>
        <input type="text" name="abizena" id="abizena" value="{{ $bezeroa->abizena }}">
        <br>
        <input type="submit" value="edit">
    </form>
</body>
</html>
