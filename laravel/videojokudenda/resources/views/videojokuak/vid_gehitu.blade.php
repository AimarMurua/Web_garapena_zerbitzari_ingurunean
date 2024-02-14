<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bid_gehitu</title>
</head>
<body>
    <h1>bideojokua gehitu</h1>
    <form action="/bid_gehituu" method="POST">
        @csrf
        <label for="bid_izena">izena: </label>
        <input type="text" name="bid_izena" id="bid_izena">
        <br>
        <label for="bid_deskripzioa">deskripzioa: </label><br>
        <textarea name="bid_deskripzioa" id="bid_deskripzioa" rows="4" cols="50"></textarea>
        <br>
        <input type="submit" value="gehitu">
    </form>
</body>
</html>