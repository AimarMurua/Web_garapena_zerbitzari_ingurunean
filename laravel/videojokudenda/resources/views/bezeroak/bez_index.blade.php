<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bez_index</title>
</head>
<body>
    <div>
        <a href="/">home</a>
        <a href="/bez_gehitu">bezeroa gehitu</a>
    </div>
    <table border="1">
        <tr>
            <th>id</th>
            <th>bez_izena</th>
            <th>bez_abizena</th>
            <th>x</th>
            <th>=</th>
        </tr>
        @foreach ($bezeroa as $bezeroa)
            <tr>
                <td>{{ $bezeroa->id }}</td>
                <td>{{ $bezeroa->izena }}</td>
                <td>{{ $bezeroa->abizena }}</td>
                <td><a href="/bez_delete/{{ $bezeroa->id }}" style="color:red;">x</a></td>
                <td><a href="/bez_edit/{{ $bezeroa->id }}" style="color:orange;">=</a></td>
            </tr>
        @endforeach
    </table>
</body>
</html>