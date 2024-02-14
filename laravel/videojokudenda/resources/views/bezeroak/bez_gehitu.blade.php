<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bez_gehitu</title>
</head>
<body>
    <h1>bezeroa gehitu</h1>
    <form action="/bez_gehituu" method="POST">
        @csrf
        <label for="izena">izena: </label>
        <input type="text" name="izena" id="izena">
        <br>
        <label for="abizena">abizena: </label>
        <input name="abizena" id="bid_deskripzioa">
        <br>
        <input type="submit" value="gehitu">
    </form>
</body>
</html>